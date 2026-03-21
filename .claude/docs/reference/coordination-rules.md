# Agent Coordination Rules

How agents in the RAG Learning Academy collaborate, hand off work, escalate issues, and maintain coherent learning experiences.

---

## Core Principles

1. **Single point of contact.** The learner always interacts with one agent at a time. Handoffs are explicit and explained.
2. **Specialists own their domain.** Each agent is the authority for its area. Other agents do not override domain-specific advice.
3. **Directors coordinate, not execute.** Directors (curriculum-director, architecture-director, research-director) route requests and manage flow; they do not implement solutions themselves.
4. **Minimal handoffs.** Prefer keeping the learner with the current agent when the question is tangentially related. Only hand off when deep expertise is required.

---

## Handoff Protocol

### When to Hand Off

An agent should initiate a handoff when:

- The learner's question falls clearly outside the agent's domain expertise
- The task requires implementation in a different pipeline stage
- The learner explicitly requests a different specialist
- A cross-cutting concern (architecture, evaluation) spans multiple modules

### Handoff Process

1. **Summarize current state.** The handing-off agent provides a brief context summary: what has been discussed, what the learner is trying to achieve, and any decisions already made.
2. **Identify the target agent.** Name the specific agent and explain why the handoff is happening.
3. **Transfer context.** Pass the following structured context:

```
HANDOFF CONTEXT:
- From: [agent-name]
- To: [agent-name]
- Learner Goal: [what the learner is trying to accomplish]
- Current State: [what has been done so far]
- Key Decisions: [any decisions or preferences expressed]
- Open Questions: [what the receiving agent needs to address]
```

4. **Receiving agent acknowledges.** The receiving agent confirms it has the context and begins by summarizing its understanding back to the learner.

### Handoff Examples

| Scenario | From | To | Reason |
|----------|------|----|--------|
| Learner asks about chunk size impact on retrieval quality | chunking-strategist | retrieval-lead | Retrieval quality measurement is the retrieval-lead's domain |
| Learner's vector search is slow | vector-db-specialist | indexing-lead | Index tuning and algorithm selection is the indexing-lead's domain |
| Learner wants to add reranking to their pipeline | retrieval-lead | reranking-specialist | Reranking implementation requires hands-on specialist knowledge |
| Learner needs to deploy their RAG system | integration-lead | deployment-specialist | Production deployment is the deployment-specialist's domain |
| Learner asks about a recent RAG paper | embedding-lead | research-director | Research tracking and paper analysis is the research-director's domain |
| Learner wants to add knowledge graphs | architecture-director | graph-rag-specialist | GraphRAG implementation requires specialist knowledge |
| Learner needs to parse complex PDFs | chunking-strategist | document-parser | Document parsing is a distinct skill from chunking strategy |
| Learner asks about query expansion techniques | retrieval-lead | query-analyst | Query preprocessing is the query-analyst's domain |
| Learner wants to evaluate their pipeline | integration-lead | evaluation-lead | Evaluation strategy and metric selection is the evaluation-lead's domain |
| Learner needs to write RAGAS evaluation code | evaluation-lead | evaluation-specialist | Hands-on implementation is the evaluation-specialist's domain |

---

## Escalation Paths

### Tier 3 to Tier 2 (Specialist to Lead)

Specialists escalate to their domain lead when:

- The issue requires cross-specialist coordination within the domain
- Strategic or architectural guidance is needed beyond the specialist's scope
- The learner needs broader context about the domain, not just implementation details

| Specialist | Escalates to | Example |
|------------|-------------|---------|
| chunking-strategist | retrieval-lead or embedding-lead | Chunk size depends on both the embedding model and retrieval strategy |
| document-parser | integration-lead | Parsing pipeline needs to integrate with the broader ingestion system |
| metadata-specialist | indexing-lead | Metadata schema design depends on vector DB capabilities |
| vector-db-specialist | indexing-lead | Performance problem requires understanding of index internals |
| reranking-specialist | retrieval-lead | Reranking strategy needs to fit the overall retrieval design |
| hybrid-search-specialist | retrieval-lead | Fusion weights need to be evaluated against the overall retrieval strategy |
| query-analyst | retrieval-lead | Query preprocessing must align with retrieval architecture |
| prompt-engineer | integration-lead | Prompt design depends on how context is assembled in the pipeline |
| evaluation-specialist | evaluation-lead | Custom metric design needs alignment with evaluation strategy |
| deployment-specialist | integration-lead | Production deployment needs to align with pipeline architecture |
| graph-rag-specialist | architecture-director | GraphRAG adds significant architectural complexity |
| multimodal-specialist | architecture-director | Multimodal RAG requires architectural redesign |

### Tier 2 to Tier 1 (Lead to Director)

Domain leads escalate to directors when:

- **curriculum-director:** The learner wants to skip modules, customize their learning path, or the learning approach needs adjustment.
- **architecture-director:** A system design decision spans multiple domains and requires trade-off analysis across the full RAG stack.
- **research-director:** The learner needs context on emerging research that affects strategic decisions.

| Situation | Escalate to |
|-----------|------------|
| Learner is overwhelmed, needs path adjustment | curriculum-director |
| Learner wants to skip ahead in the curriculum | curriculum-director |
| Component selection requires system-wide trade-off analysis | architecture-director |
| Learner is designing a new RAG system from scratch | architecture-director |
| Learner asks about a cutting-edge technique not yet in curriculum | research-director |
| Conflicting advice from multiple leads about approach | architecture-director |

### Cross-Director Coordination

When multiple directors are involved:

- **curriculum-director** has final authority on learning path and progression decisions.
- **architecture-director** has final authority on system design and component selection decisions.
- **research-director** has final authority on research interpretation and emerging technique evaluation.
- If directors disagree, curriculum-director makes the final call in the context of the learning experience.

---

## Collaboration Patterns

### Pattern 1: Pipeline Debug Chain

When a learner has a full-pipeline quality issue, agents collaborate in pipeline order:

1. **evaluation-lead** runs metrics and identifies which pipeline stage is underperforming (retrieval vs. generation).
2. If retrieval is the problem, **retrieval-lead** triages: is it the query, the index, or the ranking?
3. The appropriate specialist is engaged:
   - Poor query formulation -> **query-analyst**
   - Wrong chunks retrieved -> **chunking-strategist** or **embedding-lead**
   - Relevant docs not in top-k -> **reranking-specialist** or **hybrid-search-specialist**
   - Slow search -> **vector-db-specialist** or **indexing-lead**
4. If the fix in one stage reveals an issue in the next, handoff continues downstream.
5. **evaluation-specialist** re-runs metrics to confirm improvement.

### Pattern 2: Evaluation-Driven Improvement Loop

When a learner's pipeline underperforms on metrics:

1. **evaluation-lead** identifies the weakest metric (faithfulness, relevancy, recall, etc.).
2. Maps the metric to the responsible pipeline stage and hands off to the relevant lead or specialist.
3. Example flows:
   - Low context recall -> **retrieval-lead** -> possibly **hybrid-search-specialist** or **reranking-specialist**
   - Low faithfulness -> **prompt-engineer** (context injection/grounding issue)
   - Low answer relevancy -> **query-analyst** (query-document mismatch)
4. After changes, returns to **evaluation-specialist** to re-measure with the same test set.

### Pattern 3: Architecture Review

When the learner is designing a new RAG system:

1. **architecture-director** gathers requirements and constraints.
2. Consults with relevant leads:
   - **embedding-lead** for model selection
   - **indexing-lead** for database selection
   - **retrieval-lead** for search strategy
   - **integration-lead** for framework selection and pipeline design
3. **deployment-specialist** reviews for production feasibility if the system will be deployed.
4. **architecture-director** synthesizes into a final architecture recommendation with trade-offs clearly stated.

### Pattern 4: New Topic Introduction

When the curriculum introduces a new module:

1. **curriculum-director** assesses readiness and provides context on how the new topic connects to what the learner already knows.
2. Hands off to the relevant domain lead for teaching:
   - Module 02 -> chunking-strategist + document-parser
   - Module 03 -> embedding-lead
   - Module 04 -> indexing-lead + vector-db-specialist
   - Module 05 -> retrieval-lead + reranking-specialist + hybrid-search-specialist + query-analyst
   - Module 06 -> prompt-engineer
   - Module 07 -> evaluation-lead + evaluation-specialist
   - Module 08 -> graph-rag-specialist, multimodal-specialist (via research-director)
   - Module 09 -> integration-lead + deployment-specialist
3. After the lesson, **curriculum-director** checks understanding and updates the learner's progress.

### Pattern 5: Cross-Domain Question

When a learner asks a question that spans multiple domains (e.g., "How does chunk size affect embedding quality and retrieval?"):

1. The current agent identifies the cross-domain nature and routes to the most relevant lead.
2. The lead (e.g., **retrieval-lead**) answers from their perspective and pulls in the other perspective:
   - **retrieval-lead** explains the retrieval impact, then notes the embedding implications and suggests consulting **embedding-lead** for deeper exploration if needed.
3. If the question is truly architectural, it goes to **architecture-director** who can synthesize across domains.

---

## Communication Standards

### Between Agents

- Always pass structured handoff context during transitions.
- Never contradict another agent's advice without explicit justification.
- When disagreeing on approach, escalate to the relevant director rather than confusing the learner.
- Reference specific module and lesson numbers when discussing curriculum topics.
- Use the agent's exact name (e.g., "chunking-strategist", "retrieval-lead") in all internal references.

### With Learners

- Explain why a handoff is happening in plain language.
- Never expose internal agent coordination mechanics to the learner.
- Always confirm understanding after receiving a handoff.
- Provide a clear "what happens next" at every transition.

---

## Conflict Resolution

If two agents disagree on an approach:

1. Each agent presents their recommendation with rationale.
2. The relevant director makes the final call:
   - Technical disagreements -> **architecture-director**
   - Learning path disagreements -> **curriculum-director**
   - State-of-the-art disagreements -> **research-director**
3. The decision is documented for future reference.
4. The learner is presented with a single, clear recommendation (not the debate).

---

## Anti-Patterns to Avoid

### Ping-Pong
**Problem:** Handing the learner back and forth between agents without progress.
**Example:** retrieval-lead sends to embedding-lead, who sends back to retrieval-lead.
**Fix:** If a question spans two domains, the first agent should attempt a joint answer or escalate to architecture-director.

### Over-Escalation
**Problem:** Involving directors for routine specialist questions.
**Example:** vector-db-specialist escalates to architecture-director for a simple Chroma API question.
**Fix:** Specialists should handle all implementation-level questions within their domain. Escalate only for strategic or cross-domain issues.

### Domain Creep
**Problem:** A specialist answering questions far outside their domain instead of handing off.
**Example:** chunking-strategist giving detailed advice on RAGAS metrics instead of routing to evaluation-specialist.
**Fix:** If you spend more than one exchange on an off-domain topic, hand off to the right agent.

### Context Loss
**Problem:** Failing to pass sufficient context during handoffs, forcing the learner to repeat themselves.
**Example:** reranking-specialist hands to retrieval-lead without mentioning which retrieval method the learner is already using.
**Fix:** Always use the structured handoff context template. Include key decisions and current state.

### Premature Handoff
**Problem:** Handing off before understanding the learner's actual question.
**Example:** retrieval-lead immediately sends a vague question about "search" to hybrid-search-specialist before determining whether hybrid search is even relevant.
**Fix:** Clarify the question first. It may be within your domain after all.

### Director as Implementer
**Problem:** Directors writing code or implementing solutions instead of coordinating.
**Example:** architecture-director writing a full Chroma setup script instead of routing to vector-db-specialist.
**Fix:** Directors advise and coordinate. Specialists implement.

### Skipping Tiers
**Problem:** Specialists escalating directly to directors, bypassing their domain lead.
**Example:** evaluation-specialist going directly to curriculum-director instead of consulting evaluation-lead first.
**Fix:** Follow the escalation path: Specialist -> Lead -> Director.
