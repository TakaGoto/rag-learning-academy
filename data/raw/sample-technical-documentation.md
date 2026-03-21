---
last_reviewed: 2026-03-21
review_cycle: semi-annually
staleness_risk: low
---

# DataFlow API Documentation

**Version:** 2.4.0
**Last Updated:** 2026-03-15
**Status:** Stable

DataFlow is a high-performance data processing pipeline framework for building, orchestrating, and monitoring ETL and streaming data workflows. This document covers the complete API surface, configuration options, and operational guidance.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Core Concepts](#core-concepts)
3. [Pipeline Configuration](#pipeline-configuration)
4. [Source Connectors](#source-connectors)
5. [Transform Operations](#transform-operations)
6. [Sink Connectors](#sink-connectors)
7. [Error Handling](#error-handling)
8. [Monitoring and Observability](#monitoring-and-observability)
9. [Authentication and Security](#authentication-and-security)
10. [Performance Tuning](#performance-tuning)
11. [Migration Guide](#migration-guide)
12. [API Reference](#api-reference)
13. [FAQ](#faq)

---

## Getting Started

### Installation

Install DataFlow using pip:

```bash
pip install dataflow-sdk>=2.4.0
```

For optional dependencies (Kafka, S3, PostgreSQL connectors):

```bash
pip install dataflow-sdk[kafka,s3,postgres]
```

### Minimum Requirements

| Requirement | Version |
|---|---|
| Python | 3.10+ |
| Memory | 512 MB minimum, 2 GB recommended |
| Disk | 100 MB for SDK, additional for local state |
| OS | Linux, macOS, Windows (WSL2 recommended) |

### Quick Start

Create your first pipeline in under 10 lines:

```python
from dataflow import Pipeline, CSVSource, JsonSink, transforms

pipeline = Pipeline(name="my-first-pipeline")

pipeline.source(CSVSource("input/sales_data.csv"))
pipeline.transform(transforms.rename_columns({"old_name": "new_name"}))
pipeline.transform(transforms.filter_rows(lambda row: row["amount"] > 0))
pipeline.sink(JsonSink("output/cleaned_sales.json"))

result = pipeline.run()
print(f"Processed {result.rows_processed} rows in {result.duration_ms}ms")
```

### Project Structure

A typical DataFlow project follows this layout:

```
my-project/
├── pipelines/
│   ├── ingest.py
│   ├── transform.py
│   └── export.py
├── config/
│   ├── dev.yaml
│   ├── staging.yaml
│   └── prod.yaml
├── tests/
│   └── test_pipelines.py
├── dataflow.yaml          # Global configuration
└── requirements.txt
```

---

## Core Concepts

DataFlow is built around five core abstractions. Understanding these is essential before building pipelines.

### Pipeline

A `Pipeline` is the top-level container for a data workflow. It connects one or more sources to transforms and sinks, and manages execution lifecycle, error handling, and metrics collection.

Pipelines can run in two modes:

- **Batch mode:** Processes a fixed dataset from start to finish, then exits. Suitable for ETL jobs, nightly data loads, and report generation.
- **Streaming mode:** Continuously processes incoming records as they arrive. Suitable for real-time dashboards, event processing, and CDC (Change Data Capture) workflows.

```python
# Batch pipeline
batch = Pipeline(name="nightly-etl", mode="batch")

# Streaming pipeline
stream = Pipeline(name="event-processor", mode="streaming", checkpoint_interval_s=30)
```

### Record

A `Record` is the fundamental unit of data in DataFlow. Every record contains:

- `data`: A dictionary of field names to values
- `metadata`: System-assigned properties (timestamp, source, partition key)
- `headers`: Optional key-value pairs for routing and filtering

Records are immutable after creation. Transform operations produce new records rather than modifying existing ones.

```python
from dataflow import Record

record = Record(
    data={"user_id": "u_123", "event": "purchase", "amount": 49.99},
    metadata={"source": "kafka://events", "timestamp": 1711036800},
    headers={"region": "us-east-1"}
)
```

### Transform

A `Transform` is a function that takes one or more records and produces zero or more records. Transforms can filter, map, aggregate, join, or reshape data. They are the building blocks of pipeline logic.

DataFlow provides built-in transforms for common operations and supports custom transforms via Python functions or classes.

### Source

A `Source` reads data from an external system and produces records. DataFlow ships with connectors for CSV, JSON, Parquet, PostgreSQL, MySQL, Kafka, S3, GCS, and HTTP APIs. Custom sources can be built by implementing the `BaseSource` interface.

### Sink

A `Sink` writes records to an external system. Like sources, DataFlow includes built-in sinks for common destinations. Sinks handle batching, retries, and acknowledgment.

---

## Pipeline Configuration

### YAML Configuration

Pipelines can be configured via YAML files. This is the recommended approach for production deployments because it separates logic from configuration.

```yaml
# config/prod.yaml
pipeline:
  name: customer-data-sync
  mode: batch
  max_workers: 8
  retry_policy:
    max_retries: 3
    backoff_base_s: 2.0
    backoff_max_s: 60.0
  timeout_s: 3600

source:
  type: postgres
  connection_string: ${POSTGRES_URL}
  query: "SELECT * FROM customers WHERE updated_at > :last_sync"
  batch_size: 5000

transforms:
  - type: rename_columns
    mapping:
      cust_id: customer_id
      fname: first_name
      lname: last_name
  - type: filter_rows
    condition: "status != 'deleted'"
  - type: add_column
    name: full_name
    expression: "first_name + ' ' + last_name"

sink:
  type: s3
  bucket: data-warehouse-raw
  prefix: customers/
  format: parquet
  partition_by: [region, year]
```

### Environment Variables

Configuration values prefixed with `${}` are resolved from environment variables at runtime. This is the recommended way to handle secrets and environment-specific settings.

```yaml
source:
  connection_string: ${DATABASE_URL}        # Required
  api_key: ${API_KEY:-default_key}          # With default
  debug: ${DEBUG_MODE:-false}               # Boolean with default
```

### Programmatic Configuration

For dynamic pipelines, use the Python API:

```python
from dataflow import Pipeline, PipelineConfig

config = PipelineConfig(
    name="dynamic-pipeline",
    mode="batch",
    max_workers=4,
    retry_policy={"max_retries": 3, "backoff_base_s": 1.0},
)

pipeline = Pipeline(config=config)
```

### Configuration Precedence

When the same setting appears in multiple places, DataFlow resolves it in this order (highest priority first):

1. Programmatic arguments passed directly to constructors
2. Environment variables
3. Pipeline-specific YAML config
4. Global `dataflow.yaml` config
5. Built-in defaults

---

## Source Connectors

### CSV Source

Reads data from CSV files with automatic type inference.

```python
from dataflow.sources import CSVSource

source = CSVSource(
    path="data/input/*.csv",          # Supports glob patterns
    delimiter=",",
    encoding="utf-8",
    has_header=True,
    skip_rows=0,
    null_values=["", "NULL", "N/A"],
    dtypes={"amount": float, "date": "datetime"},
)
```

**Options:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `path` | `str` | Required | File path or glob pattern |
| `delimiter` | `str` | `","` | Column separator |
| `encoding` | `str` | `"utf-8"` | File encoding |
| `has_header` | `bool` | `True` | Whether the first row is a header |
| `skip_rows` | `int` | `0` | Number of rows to skip at the start |
| `null_values` | `list[str]` | `[""]` | Strings to interpret as null |
| `dtypes` | `dict` | `None` | Explicit column type overrides |
| `batch_size` | `int` | `10000` | Rows per batch for memory control |

### PostgreSQL Source

Reads from PostgreSQL databases with connection pooling and incremental query support.

```python
from dataflow.sources import PostgresSource

source = PostgresSource(
    connection_string="postgresql://user:pass@host:5432/dbname",
    query="SELECT * FROM orders WHERE created_at > :checkpoint",
    params={"checkpoint": "2026-01-01"},
    batch_size=5000,
    pool_size=3,
)
```

The PostgreSQL source supports parameterized queries with `:param_name` syntax. Parameters are safely escaped to prevent SQL injection.

### Kafka Source

Consumes records from Apache Kafka topics with exactly-once semantics.

```python
from dataflow.sources import KafkaSource

source = KafkaSource(
    bootstrap_servers="kafka-1:9092,kafka-2:9092",
    topic="user-events",
    group_id="dataflow-consumer-group",
    auto_offset_reset="earliest",
    value_deserializer="json",
    max_poll_records=500,
    session_timeout_ms=30000,
)
```

**Important:** When using Kafka in streaming mode, ensure your consumer group ID is unique per pipeline to avoid message duplication. See [Error Handling](#error-handling) for details on exactly-once delivery guarantees.

### S3 Source

Reads files from Amazon S3 with support for various formats.

```python
from dataflow.sources import S3Source

source = S3Source(
    bucket="my-data-lake",
    prefix="raw/events/2026/",
    file_format="parquet",
    aws_region="us-east-1",
    assume_role_arn="arn:aws:iam::123456789:role/DataFlowReader",
)
```

### HTTP API Source

Fetches data from REST APIs with pagination support.

```python
from dataflow.sources import HTTPSource

source = HTTPSource(
    url="https://api.example.com/v2/records",
    method="GET",
    headers={"Authorization": "Bearer ${API_TOKEN}"},
    pagination={
        "type": "cursor",
        "cursor_field": "next_cursor",
        "results_field": "data",
    },
    rate_limit_rps=10,
    timeout_s=30,
)
```

### Building a Custom Source

Implement the `BaseSource` interface for unsupported data systems:

```python
from dataflow.sources import BaseSource
from dataflow import Record

class MongoSource(BaseSource):
    def __init__(self, connection_string: str, collection: str, filter: dict = None):
        self.connection_string = connection_string
        self.collection = collection
        self.filter = filter or {}

    def setup(self) -> None:
        """Called once before reading begins. Initialize connections here."""
        from pymongo import MongoClient
        self.client = MongoClient(self.connection_string)
        self.col = self.client.get_default_database()[self.collection]

    def read(self):
        """Yield records from the source. Must be a generator."""
        for doc in self.col.find(self.filter):
            doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
            yield Record(data=doc, metadata={"source": f"mongo://{self.collection}"})

    def teardown(self) -> None:
        """Called after reading completes. Clean up resources."""
        self.client.close()

    def get_schema(self) -> dict:
        """Optional: return the expected schema for validation."""
        return {"type": "object", "properties": {"_id": {"type": "string"}}}
```

---

## Transform Operations

### Built-in Transforms

DataFlow includes a library of common transforms. These cover 90% of typical data processing needs.

#### Column Operations

```python
from dataflow import transforms

# Rename columns
transforms.rename_columns({"old_name": "new_name", "col_a": "column_alpha"})

# Select specific columns (drop all others)
transforms.select_columns(["id", "name", "email", "created_at"])

# Drop specific columns
transforms.drop_columns(["internal_id", "debug_flag", "temp_score"])

# Add a computed column
transforms.add_column("full_name", expression="first_name + ' ' + last_name")

# Cast column types
transforms.cast_columns({"amount": float, "created_at": "datetime", "is_active": bool})
```

#### Row Operations

```python
# Filter rows by condition
transforms.filter_rows(lambda row: row["status"] == "active")

# Deduplicate by key columns
transforms.deduplicate(keys=["user_id", "event_type"], keep="last")

# Sort rows
transforms.sort_by("created_at", ascending=False)

# Limit number of rows
transforms.limit(1000)

# Sample random rows
transforms.sample(fraction=0.1, seed=42)
```

#### Aggregation

```python
# Group by and aggregate
transforms.group_by(
    keys=["region", "product_category"],
    aggregations={
        "total_revenue": ("amount", "sum"),
        "order_count": ("order_id", "count"),
        "avg_order_value": ("amount", "mean"),
        "max_order_value": ("amount", "max"),
    }
)
```

#### String Operations

```python
# Normalize text
transforms.normalize_text("description", lowercase=True, strip=True, remove_extra_spaces=True)

# Regex extraction
transforms.regex_extract("raw_log", r"user=(\w+)", output_column="user_id")

# Split column into multiple columns
transforms.split_column("full_address", delimiter=",", output_columns=["street", "city", "state", "zip"])
```

#### Data Quality

```python
# Fill missing values
transforms.fill_null({"amount": 0.0, "status": "unknown", "region": "unspecified"})

# Validate against schema
transforms.validate_schema({
    "user_id": {"type": "string", "required": True},
    "email": {"type": "string", "pattern": r"^[\w.-]+@[\w.-]+\.\w+$"},
    "age": {"type": "integer", "min": 0, "max": 150},
})

# Flag anomalies (statistical outlier detection)
transforms.flag_anomalies(
    column="transaction_amount",
    method="zscore",       # or "iqr", "isolation_forest"
    threshold=3.0,
    output_column="is_anomaly",
)
```

### Custom Transforms

For logic not covered by built-ins, write a custom transform function:

```python
from dataflow import Record, Transform

class EnrichWithGeodata(Transform):
    """Adds geographic data based on IP address."""

    def __init__(self, geoip_db_path: str):
        self.db_path = geoip_db_path
        self.reader = None

    def setup(self) -> None:
        import geoip2.database
        self.reader = geoip2.database.Reader(self.db_path)

    def process(self, record: Record) -> list[Record]:
        ip = record.data.get("ip_address")
        if not ip:
            return [record]  # Pass through unchanged

        try:
            response = self.reader.city(ip)
            enriched_data = {
                **record.data,
                "country": response.country.name,
                "city": response.city.name,
                "latitude": response.location.latitude,
                "longitude": response.location.longitude,
            }
            return [Record(data=enriched_data, metadata=record.metadata)]
        except Exception:
            return [record]  # Pass through on error

    def teardown(self) -> None:
        if self.reader:
            self.reader.close()
```

### Transform Chaining

Transforms are applied in the order they are added. Each transform receives the output of the previous one.

```python
pipeline = Pipeline(name="chained-transforms")
pipeline.source(CSVSource("input.csv"))

# These run in sequence
pipeline.transform(transforms.filter_rows(lambda r: r["country"] == "US"))
pipeline.transform(transforms.rename_columns({"zip": "zip_code"}))
pipeline.transform(transforms.cast_columns({"zip_code": str}))
pipeline.transform(transforms.add_column("processed_at", expression="NOW()"))

pipeline.sink(JsonSink("output.json"))
```

---

## Sink Connectors

### JSON Sink

Writes records as JSON (one object per line or as an array).

```python
from dataflow.sinks import JsonSink

sink = JsonSink(
    path="output/results.jsonl",
    mode="lines",           # "lines" for JSONL, "array" for JSON array
    encoding="utf-8",
    pretty=False,
)
```

### PostgreSQL Sink

Writes records to PostgreSQL with upsert support.

```python
from dataflow.sinks import PostgresSink

sink = PostgresSink(
    connection_string="postgresql://user:pass@host:5432/dbname",
    table="processed_orders",
    write_mode="upsert",           # "insert", "upsert", "replace"
    conflict_columns=["order_id"],  # For upsert: which columns determine uniqueness
    batch_size=1000,
)
```

### Kafka Sink

Produces records to Kafka topics.

```python
from dataflow.sinks import KafkaSink

sink = KafkaSink(
    bootstrap_servers="kafka-1:9092",
    topic="processed-events",
    key_field="user_id",            # Record field to use as Kafka key
    value_serializer="json",
    compression="snappy",
    acks="all",                     # "all" for strongest durability guarantee
)
```

### S3 Sink

Writes files to Amazon S3 with partitioning support.

```python
from dataflow.sinks import S3Sink

sink = S3Sink(
    bucket="data-warehouse",
    prefix="processed/orders/",
    file_format="parquet",
    partition_by=["year", "month"],
    max_file_size_mb=128,
    compression="snappy",
)
```

### Multi-Sink

Write to multiple destinations simultaneously:

```python
from dataflow.sinks import MultiSink

sink = MultiSink([
    JsonSink("output/backup.jsonl"),
    PostgresSink(connection_string=DB_URL, table="orders"),
    KafkaSink(bootstrap_servers=KAFKA_URL, topic="order-events"),
])
```

---

## Error Handling

DataFlow provides a layered error handling system designed for production reliability.

### Retry Policies

Configure automatic retries for transient failures:

```python
from dataflow import Pipeline, RetryPolicy

policy = RetryPolicy(
    max_retries=5,
    backoff_base_s=1.0,          # First retry after 1 second
    backoff_max_s=120.0,         # Cap backoff at 2 minutes
    retryable_exceptions=[
        ConnectionError,
        TimeoutError,
        "kafka.errors.KafkaTimeoutError",
    ],
)

pipeline = Pipeline(name="resilient-pipeline", retry_policy=policy)
```

### Dead Letter Queues

Records that fail after all retries are routed to a dead letter queue (DLQ) for manual inspection:

```python
from dataflow import Pipeline, DeadLetterQueue

dlq = DeadLetterQueue(
    sink=JsonSink("errors/failed_records.jsonl"),
    include_error=True,          # Attach the error message to each record
    include_stack_trace=True,    # Attach the full Python stack trace
    max_records=10000,           # Safety limit
)

pipeline = Pipeline(name="safe-pipeline", dead_letter_queue=dlq)
```

### Circuit Breaker

Prevent cascading failures when a downstream system is unhealthy:

```python
from dataflow import CircuitBreaker

breaker = CircuitBreaker(
    failure_threshold=5,           # Open circuit after 5 consecutive failures
    recovery_timeout_s=60,         # Wait 60 seconds before trying again
    half_open_max_calls=3,         # Allow 3 test calls in half-open state
)

pipeline = Pipeline(name="protected-pipeline", circuit_breaker=breaker)
```

The circuit breaker has three states:

- **Closed:** Normal operation. Failures increment a counter.
- **Open:** All calls fail immediately without executing. The pipeline waits for `recovery_timeout_s`.
- **Half-Open:** A limited number of calls are allowed through. If they succeed, the circuit closes. If they fail, it opens again.

### Error Callbacks

Register custom handlers for specific error types:

```python
def on_schema_error(record, error):
    """Handle records that fail schema validation."""
    logger.warning("Schema violation: %s in record %s", error, record.data.get("id"))
    # Return the record to continue processing, or None to drop it
    return None

pipeline.on_error("SchemaValidationError", on_schema_error)
```

---

## Monitoring and Observability

### Built-in Metrics

Every pipeline automatically collects these metrics:

| Metric | Type | Description |
|---|---|---|
| `dataflow_records_processed_total` | Counter | Total records processed |
| `dataflow_records_failed_total` | Counter | Total records that failed processing |
| `dataflow_processing_duration_seconds` | Histogram | Time to process each record |
| `dataflow_batch_size` | Gauge | Current batch size |
| `dataflow_pipeline_status` | Gauge | Pipeline status (0=stopped, 1=running, 2=error) |
| `dataflow_source_lag` | Gauge | Records pending in source (Kafka only) |
| `dataflow_memory_usage_bytes` | Gauge | Current memory usage |
| `dataflow_checkpoint_age_seconds` | Gauge | Time since last checkpoint |

### Prometheus Integration

Export metrics to Prometheus:

```python
from dataflow.monitoring import PrometheusExporter

exporter = PrometheusExporter(port=9090, path="/metrics")
pipeline = Pipeline(name="monitored", metrics_exporter=exporter)
```

### Structured Logging

DataFlow uses structured JSON logging by default:

```python
from dataflow.logging import configure_logging

configure_logging(
    level="INFO",
    format="json",                # "json" or "text"
    output="stdout",              # "stdout", "stderr", or a file path
    include_fields=["pipeline", "stage", "record_count", "duration_ms"],
)
```

Example log output:

```json
{
  "timestamp": "2026-03-15T10:30:00Z",
  "level": "INFO",
  "pipeline": "customer-sync",
  "stage": "transform",
  "message": "Batch processed",
  "record_count": 5000,
  "duration_ms": 342,
  "memory_mb": 256
}
```

### Health Check Endpoint

Enable a health check HTTP endpoint for orchestration systems:

```python
pipeline = Pipeline(
    name="production-pipeline",
    health_check_port=8080,     # GET /health returns pipeline status
)
```

The health check returns:

```json
{
  "status": "healthy",
  "pipeline": "production-pipeline",
  "uptime_s": 3600,
  "records_processed": 150000,
  "last_error": null,
  "source_lag": 0
}
```

---

## Authentication and Security

### Credential Management

DataFlow supports multiple credential providers. Never hardcode credentials in pipeline code or configuration files.

```python
from dataflow.auth import AWSSecretsProvider, EnvVarProvider, VaultProvider

# AWS Secrets Manager
provider = AWSSecretsProvider(secret_name="dataflow/prod/credentials")

# Environment variables (default)
provider = EnvVarProvider()

# HashiCorp Vault
provider = VaultProvider(
    vault_url="https://vault.internal:8200",
    auth_method="kubernetes",
    secret_path="secret/data/dataflow",
)

pipeline = Pipeline(name="secure-pipeline", credential_provider=provider)
```

### Data Encryption

Encrypt sensitive fields in transit and at rest:

```python
from dataflow.security import FieldEncryptor

encryptor = FieldEncryptor(
    fields=["ssn", "credit_card", "email"],
    algorithm="AES-256-GCM",
    key_provider=AWSSecretsProvider(secret_name="dataflow/encryption-key"),
)

pipeline.transform(encryptor)
```

### Audit Logging

Track who accessed what data and when:

```python
from dataflow.security import AuditLogger

audit = AuditLogger(
    sink=PostgresSink(connection_string=AUDIT_DB_URL, table="audit_log"),
    log_events=["pipeline_start", "pipeline_end", "schema_change", "error"],
    include_record_counts=True,
    include_user_context=True,
)

pipeline = Pipeline(name="audited-pipeline", audit_logger=audit)
```

---

## Performance Tuning

### Parallelism

Control how many records are processed concurrently:

```python
pipeline = Pipeline(
    name="parallel-pipeline",
    max_workers=8,                 # Parallel processing threads
    batch_size=5000,               # Records per batch
    prefetch_batches=2,            # Batches to read ahead
)
```

**Guidelines for setting `max_workers`:**

- CPU-bound transforms: set to number of CPU cores
- I/O-bound transforms (API calls, DB lookups): set to 2-4x CPU cores
- Memory-intensive transforms: reduce workers, increase batch size

### Memory Management

For large datasets that do not fit in memory, use streaming mode with bounded buffers:

```python
pipeline = Pipeline(
    name="low-memory",
    mode="streaming",
    buffer_size=10000,             # Maximum records in memory
    spill_to_disk=True,            # Write overflow to disk
    spill_directory="/tmp/dataflow-spill",
)
```

### Checkpointing

Enable checkpoints to resume from the last successful position after a failure:

```python
pipeline = Pipeline(
    name="checkpointed",
    checkpoint_store="sqlite:///checkpoints.db",  # or "s3://bucket/checkpoints/"
    checkpoint_interval_s=30,                      # Save progress every 30 seconds
    checkpoint_interval_records=10000,             # Or every 10,000 records
)
```

When a pipeline restarts, it automatically resumes from the last checkpoint. This is especially important for long-running batch jobs and streaming pipelines.

### Benchmarking

Measure pipeline performance before deploying to production:

```python
from dataflow.testing import PipelineBenchmark

benchmark = PipelineBenchmark(pipeline)
results = benchmark.run(
    num_records=100000,
    warmup_records=1000,
    measure_memory=True,
)

print(results)
# PipelineBenchmarkResult(
#   throughput_rps=12500,
#   p50_latency_ms=0.8,
#   p95_latency_ms=2.1,
#   p99_latency_ms=5.3,
#   peak_memory_mb=384,
#   total_duration_s=8.0,
# )
```

---

## Migration Guide

### Migrating from v1.x to v2.x

Version 2.0 introduced breaking changes. Follow these steps to migrate.

#### Step 1: Update Import Paths

```python
# v1.x (old)
from dataflow.pipeline import DataPipeline
from dataflow.connectors.csv_reader import CSVReader

# v2.x (new)
from dataflow import Pipeline
from dataflow.sources import CSVSource
```

#### Step 2: Update Configuration Format

The configuration format changed from flat dictionaries to nested YAML:

```yaml
# v1.x (old)
pipeline_name: my-pipeline
source_type: csv
source_path: data.csv
sink_type: json
sink_path: output.json

# v2.x (new)
pipeline:
  name: my-pipeline
source:
  type: csv
  path: data.csv
sink:
  type: json
  path: output.json
```

#### Step 3: Update Error Handling

```python
# v1.x (old)
pipeline.set_error_handler(lambda e: print(e))

# v2.x (new)
from dataflow import RetryPolicy, DeadLetterQueue
pipeline = Pipeline(
    name="my-pipeline",
    retry_policy=RetryPolicy(max_retries=3),
    dead_letter_queue=DeadLetterQueue(sink=JsonSink("errors.jsonl")),
)
```

#### Step 4: Update Transform Syntax

```python
# v1.x (old)
pipeline.add_step("rename", {"old_col": "new_col"})
pipeline.add_step("filter", "status == 'active'")

# v2.x (new)
pipeline.transform(transforms.rename_columns({"old_col": "new_col"}))
pipeline.transform(transforms.filter_rows(lambda r: r["status"] == "active"))
```

### Migrating from v2.3 to v2.4

Version 2.4 is backward compatible with 2.3. New features include:

- **Multi-sink support:** Write to multiple destinations (see [Multi-Sink](#multi-sink))
- **Circuit breaker:** Automatic failure protection (see [Circuit Breaker](#circuit-breaker))
- **Anomaly detection transform:** Statistical outlier flagging (see [Data Quality](#data-quality))
- **Improved checkpointing:** S3-backed checkpoint store for distributed pipelines

No code changes are required. Optional: update your `dataflow.yaml` to use new defaults:

```yaml
# dataflow.yaml — recommended v2.4 defaults
defaults:
  checkpoint_interval_s: 30
  retry_policy:
    max_retries: 3
    backoff_base_s: 1.0
  circuit_breaker:
    failure_threshold: 5
    recovery_timeout_s: 60
```

---

## API Reference

### Pipeline

```python
class Pipeline:
    def __init__(
        self,
        name: str,
        mode: str = "batch",                          # "batch" or "streaming"
        config: PipelineConfig = None,
        max_workers: int = 4,
        retry_policy: RetryPolicy = None,
        dead_letter_queue: DeadLetterQueue = None,
        circuit_breaker: CircuitBreaker = None,
        checkpoint_store: str = None,
        checkpoint_interval_s: int = 30,
        metrics_exporter: MetricsExporter = None,
        health_check_port: int = None,
        credential_provider: CredentialProvider = None,
        audit_logger: AuditLogger = None,
    ) -> None: ...

    def source(self, source: BaseSource) -> "Pipeline": ...
    def transform(self, transform: Transform) -> "Pipeline": ...
    def sink(self, sink: BaseSink) -> "Pipeline": ...
    def run(self) -> PipelineResult: ...
    def stop(self) -> None: ...
    def status(self) -> PipelineStatus: ...
    def on_error(self, error_type: str, callback: Callable) -> None: ...
```

### PipelineResult

```python
@dataclass
class PipelineResult:
    pipeline_name: str
    status: str                      # "success", "partial_failure", "failure"
    rows_processed: int
    rows_failed: int
    duration_ms: int
    started_at: datetime
    completed_at: datetime
    metrics: dict                    # Stage-level metrics
    errors: list[PipelineError]      # Errors encountered during execution
```

### PipelineError

```python
@dataclass
class PipelineError:
    stage: str                       # "source", "transform", "sink"
    error_type: str
    message: str
    record_id: str | None
    timestamp: datetime
    stack_trace: str | None
    is_retryable: bool
```

### RetryPolicy

```python
@dataclass
class RetryPolicy:
    max_retries: int = 3
    backoff_base_s: float = 1.0
    backoff_max_s: float = 60.0
    retryable_exceptions: list[str | type] = field(default_factory=list)
```

### DeadLetterQueue

```python
@dataclass
class DeadLetterQueue:
    sink: BaseSink
    include_error: bool = True
    include_stack_trace: bool = False
    max_records: int = 100000
```

### Record

```python
@dataclass(frozen=True)
class Record:
    data: dict
    metadata: dict = field(default_factory=dict)
    headers: dict = field(default_factory=dict)

    def get(self, key: str, default=None): ...
    def with_data(self, **updates) -> "Record": ...
    def with_metadata(self, **updates) -> "Record": ...
```

---

## FAQ

**Q: How do I handle schema changes in my source data?**

A: Use the `validate_schema` transform to catch unexpected changes. Records that fail validation can be routed to a dead letter queue for manual review. For expected schema evolution, use the `schema_migration` transform to map old field names to new ones.

**Q: Can I run multiple pipelines in the same process?**

A: Yes. Create multiple `Pipeline` instances and call `run()` on each. For parallel execution, use `PipelineGroup`:

```python
from dataflow import PipelineGroup

group = PipelineGroup([pipeline_a, pipeline_b, pipeline_c])
results = group.run_parallel(max_concurrent=2)
```

**Q: How do I test my pipelines locally?**

A: DataFlow includes a test harness that mocks external sources and sinks:

```python
from dataflow.testing import MockSource, MockSink, PipelineTestHarness

harness = PipelineTestHarness(pipeline)
harness.set_source(MockSource([
    {"id": 1, "name": "Alice", "status": "active"},
    {"id": 2, "name": "Bob", "status": "deleted"},
]))
harness.set_sink(MockSink())

result = harness.run()
assert result.rows_processed == 1  # Only Alice passes the filter
assert harness.sink.records[0]["name"] == "Alice"
```

**Q: What happens if my pipeline crashes mid-execution?**

A: If checkpointing is enabled, the pipeline resumes from the last checkpoint on restart. Without checkpointing, the entire pipeline re-runs from the beginning. For streaming pipelines with Kafka sources, Kafka consumer offsets provide built-in resumability.

**Q: How do I optimize a slow pipeline?**

A: Follow this diagnostic checklist:

1. Check `dataflow_processing_duration_seconds` histogram to identify the slowest stage
2. If source is slow: increase `batch_size`, add `prefetch_batches`
3. If transform is slow: increase `max_workers`, check for blocking I/O calls
4. If sink is slow: increase `batch_size`, enable compression, check network latency
5. Use `PipelineBenchmark` to measure throughput before and after changes

**Q: Does DataFlow support exactly-once processing?**

A: Yes, with caveats. Exactly-once semantics are supported for Kafka-to-Kafka pipelines using transactional producers. For other source/sink combinations, DataFlow provides at-least-once delivery with idempotent sinks (using upsert with conflict resolution).

**Q: How do I handle large files that do not fit in memory?**

A: Use streaming mode with bounded buffers. Set `buffer_size` to control the maximum number of records held in memory, and enable `spill_to_disk` for overflow. For Parquet and CSV files, DataFlow automatically reads in chunks based on `batch_size`.

**Q: Can I use DataFlow with Apache Airflow or other orchestrators?**

A: Yes. DataFlow pipelines can be wrapped in Airflow operators:

```python
from airflow.operators.python import PythonOperator

def run_dataflow_pipeline():
    from dataflow import Pipeline
    pipeline = Pipeline.from_config("config/prod.yaml")
    result = pipeline.run()
    if result.status != "success":
        raise RuntimeError(f"Pipeline failed: {result.errors}")

task = PythonOperator(
    task_id="run_etl",
    python_callable=run_dataflow_pipeline,
    dag=dag,
)
```

**Q: What is the maximum number of records DataFlow can handle?**

A: There is no hard limit. DataFlow has been tested with datasets exceeding 1 billion records. Performance depends on your hardware, source/sink throughput, and transform complexity. For very large datasets, use streaming mode with checkpointing enabled.

**Q: How do I add custom metrics to my pipeline?**

A: Use the metrics API to register custom counters, gauges, and histograms:

```python
from dataflow.monitoring import metrics

orders_counter = metrics.counter("custom_orders_processed", "Orders processed by region")
amount_histogram = metrics.histogram("custom_order_amount", "Order amount distribution")

class ProcessOrder(Transform):
    def process(self, record: Record) -> list[Record]:
        orders_counter.inc(labels={"region": record.data["region"]})
        amount_histogram.observe(record.data["amount"])
        return [record]
```

**Q: How do I contribute to DataFlow?**

A: See the `CONTRIBUTING.md` file in the DataFlow repository. We accept bug reports, feature requests, and pull requests. All contributions must include tests and documentation updates.

---

## Appendix: Supported File Formats

| Format | Source | Sink | Notes |
|---|---|---|---|
| CSV | Yes | Yes | Configurable delimiter, quoting, encoding |
| JSON | Yes | Yes | Object-per-line (JSONL) or array format |
| Parquet | Yes | Yes | Columnar, compressed, schema-aware |
| Avro | Yes | Yes | Schema evolution support |
| ORC | Yes | No | Read-only support |
| XML | Yes | No | Requires `dataflow-sdk[xml]` extra |
| Excel (.xlsx) | Yes | Yes | Requires `dataflow-sdk[excel]` extra |
| Protocol Buffers | Yes | Yes | Requires compiled `.proto` definitions |

## Appendix: Environment Variable Reference

| Variable | Description | Default |
|---|---|---|
| `DATAFLOW_LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) | `INFO` |
| `DATAFLOW_LOG_FORMAT` | Log format (`json` or `text`) | `json` |
| `DATAFLOW_MAX_WORKERS` | Default worker thread count | `4` |
| `DATAFLOW_CHECKPOINT_DIR` | Directory for checkpoint files | `/tmp/dataflow` |
| `DATAFLOW_METRICS_PORT` | Port for Prometheus metrics endpoint | `9090` |
| `DATAFLOW_HEALTH_PORT` | Port for health check endpoint | `8080` |
| `DATAFLOW_SPILL_DIR` | Directory for memory spill files | `/tmp/dataflow-spill` |
| `DATAFLOW_BATCH_SIZE` | Default batch size for sources and sinks | `10000` |

---

*This documentation is for DataFlow SDK version 2.4.0. For older versions, see the version-specific documentation at docs.dataflow.example.com/archive.*
