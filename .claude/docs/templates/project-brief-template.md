# RAG Project Brief

> Use this template to define the scope, requirements, and success criteria for a RAG project before beginning implementation.

---

## Project Overview

### Project Name
_[Your project name]_

### Date
_[YYYY-MM-DD]_

### Author
_[Your name]_

### Status
_[Draft | In Review | Approved | In Progress | Complete]_

### One-Line Summary
_Describe the project in a single sentence._

_[e.g., "Build a RAG-powered customer support chatbot that answers questions about our product documentation."]_

---

## 1. Goal

### Business Goal
_What business outcome does this project achieve?_



### Technical Goal
_What technical capability does this project deliver?_



### Non-Goals
_What is explicitly out of scope?_

1.
2.
3.

---

## 2. Data Sources

### Primary Sources

| Source | Format | Size | Location | Owner | Update Cadence |
|---|---|---|---|---|---|
| _[e.g., Product docs]_ | _Markdown_ | _500 files_ | _[URL/path]_ | _[Team]_ | _Weekly_ |
| | | | | | |
| | | | | | |

### Data Characteristics

- **Total volume:** _[e.g., 10,000 documents, ~50MB of text]_
- **Languages:** _[e.g., English, Japanese]_
- **Content types:** _[e.g., text-only, text + tables, text + images]_
- **Sensitivity:** _[e.g., Public, Internal, Confidential — affects deployment model]_
- **Quality:** _[e.g., Well-structured, noisy, mixed quality]_

### Data Access

- **Authentication:** _[e.g., API key, OAuth, public]_
- **Rate limits:** _[e.g., 100 requests/minute]_
- **Data pipeline:** _[e.g., Batch download, real-time API, webhook]_

---

## 3. Requirements

### Functional Requirements

| # | Requirement | Priority | Notes |
|---|---|---|---|
| FR-1 | _[e.g., Answer natural language questions about product features]_ | Must | |
| FR-2 | _[e.g., Cite source documents in every answer]_ | Must | |
| FR-3 | _[e.g., Say "I don't know" when information is not available]_ | Must | |
| FR-4 | _[e.g., Support follow-up questions in a conversation]_ | Should | |
| FR-5 | _[e.g., Filter results by product version]_ | Should | |
| FR-6 | _[e.g., Support image-based queries]_ | Could | |

### Non-Functional Requirements

| # | Requirement | Target | Notes |
|---|---|---|---|
| NFR-1 | Response latency (P95) | _<3 seconds_ | |
| NFR-2 | Availability | _99.5%_ | |
| NFR-3 | Cost per query | _<$0.03_ | |
| NFR-4 | Concurrent users | _50_ | |
| NFR-5 | Data freshness | _<24 hours_ | _Time from doc update to searchable_ |

### User Interface

_How will users interact with this system?_

- [ ] Chat interface (web)
- [ ] Chat interface (Slack/Teams)
- [ ] API endpoint
- [ ] CLI tool
- [ ] Embedded in existing application
- [ ] Other: ___

---

## 4. Constraints

### Technical Constraints

| Constraint | Impact |
|---|---|
| _[e.g., Must use company's existing PostgreSQL instance]_ | _Limits vector DB to pgvector_ |
| _[e.g., No data can leave the VPC]_ | _Must self-host embedding model_ |
| _[e.g., Maximum budget: $500/month]_ | _Limits model and infrastructure choices_ |
| | |

### Timeline Constraints

| Milestone | Target Date |
|---|---|
| Proof of concept | _[YYYY-MM-DD]_ |
| Internal beta | _[YYYY-MM-DD]_ |
| Production launch | _[YYYY-MM-DD]_ |

### Team Constraints

| Role | Available? | Notes |
|---|---|---|
| ML Engineer | _Yes/No_ | _[Hours per week]_ |
| Backend Engineer | _Yes/No_ | _[Hours per week]_ |
| DevOps/SRE | _Yes/No_ | _[Hours per week]_ |
| Domain Expert (for evaluation) | _Yes/No_ | _[Hours per week]_ |

---

## 5. Success Criteria

### Quality Metrics

_Define measurable quality targets. These will drive your evaluation strategy._

| Metric | Target | Measurement Method |
|---|---|---|
| Answer correctness | _>85%_ | _Human evaluation on 100 test questions_ |
| Faithfulness (no hallucination) | _>90%_ | _RAGAS faithfulness score_ |
| Retrieval recall@5 | _>80%_ | _RAGAS context recall_ |
| User satisfaction | _>4.0/5.0_ | _In-app feedback widget_ |

### Operational Metrics

| Metric | Target | Measurement Method |
|---|---|---|
| P95 latency | _<3s_ | _Application monitoring_ |
| Error rate | _<1%_ | _Application monitoring_ |
| Monthly cost | _<$500_ | _Cloud billing_ |

### Definition of Done

_What must be true for this project to be considered complete?_

- [ ] All functional requirements marked "Must" are implemented
- [ ] Quality metrics meet targets on the evaluation dataset
- [ ] System is deployed and accessible to target users
- [ ] Monitoring and alerting are configured
- [ ] Documentation is complete (architecture doc, runbook)
- [ ] Evaluation dataset exists for ongoing quality monitoring

---

## 6. Risks and Mitigations

| # | Risk | Probability | Impact | Mitigation |
|---|---|---|---|---|
| 1 | _[e.g., Document quality is too low for good retrieval]_ | _Medium_ | _High_ | _[e.g., Invest in preprocessing; fall back to manual curation]_ |
| 2 | _[e.g., LLM costs exceed budget at scale]_ | _Medium_ | _Medium_ | _[e.g., Implement semantic caching; use smaller model for simple queries]_ |
| 3 | _[e.g., Users ask questions outside the document scope]_ | _High_ | _Low_ | _[e.g., Implement graceful abstention with redirect]_ |
| 4 | | | | |
| 5 | | | | |

---

## 7. Proposed Approach

_High-level technical approach. This will be detailed in the Architecture Decision Document._

### Architecture Sketch
_Describe the planned architecture in 3-5 sentences._



### Key Technology Choices

| Component | Proposed Choice | Confidence | Alternative |
|---|---|---|---|
| Embedding model | _[e.g., text-embedding-3-small]_ | _High/Medium/Low_ | _[e.g., BGE-base]_ |
| Vector database | _[e.g., pgvector]_ | _High/Medium/Low_ | _[e.g., ChromaDB]_ |
| LLM | _[e.g., Claude 3.5 Sonnet]_ | _High/Medium/Low_ | _[e.g., GPT-4o]_ |
| Framework | _[e.g., None (custom)]_ | _High/Medium/Low_ | _[e.g., LangChain]_ |

### Proof-of-Concept Plan
_What will you build first to validate the approach? (Should take <1 week)_

1.
2.
3.

---

## 8. Open Questions

_Questions that need answers before or during implementation._

| # | Question | Who Can Answer | Deadline |
|---|---|---|---|
| 1 | _[e.g., Can we access the documentation API from the production VPC?]_ | _[DevOps team]_ | _[Date]_ |
| 2 | | | |
| 3 | | | |

---

## Approval

| Role | Name | Date | Decision |
|---|---|---|---|
| Project Sponsor | | | _Approved / Rejected_ |
| Technical Lead | | | _Approved / Rejected_ |
| Domain Expert | | | _Approved / Rejected_ |
