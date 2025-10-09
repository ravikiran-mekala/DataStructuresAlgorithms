# MessageWise: AI-Powered Email Deliverability Copilot

## 1) One-Line Hook
I built an AI copilot that cuts down email deliverability troubleshooting from 50 minutes to 20 minutes, handling 45M emails monthly at Sur La Table, and reduced developer escalations by 32 percentage points [??how was 32% derived?] while achieving 84% user satisfaction. [??How was 84% derived?]

---

## 2) Context & Role
**Org & domain:** Sur La Table, premium cookware retailer with extensive cooking class programs. Email is critical for Marketing, promotions, product launches, class registrations, order updates, and security notices. We send 1.8M emails daily (3.8M on promo days), totaling 45M messages monthly across marketing, lifecycle, transactional, and security streams.

**Your role:** Senior Software Developer responsible for builing data pipelines, API integrations, and system observability mainly for legacy products. I also lead technical implementation while mentoring a junior developer.

**Why this mattered now:** Of all the examples, for marketing or promotion days during Peak season pressure with significant revenue impact. A 5% inboxing drop on 40M monthly sends means ~2M fewer deliveries, translating to ~$120,000 lost revenue monthly. Similarly we also have other use cases like order updates, class registrations where anything bad will have a bad customer experience. Production Support team of 10 engineers receiving ~50 alerts daily, with 70% of support tickets email-related, causing excessive developer escalations and productivity drain.

---

## 3) Problem Discovery (How you identified it)
**Signal:** ~60% of all support tickets were email deliverability issues, with ~70% requiring developer escalation despite many having known resolutions.

**Pain points:** 
- Production Support spending 50+ minutes per incident navigating logs, runbooks, and wikis
- Developers constantly pulled from productive work for repetitive issues
- Information scattered across SES metrics, New Relic, Sentry, CloudWatch, Slack channels
- Difficult to search for existing resolutions even when documented
- Context switching between multiple tools and dashboards

**Evidence:**
- ~50 alerts daily, ~20 requiring Jira tickets (2-3 min resolution threshold)
- Average resolution time: 50 minutes for non-escalated tickets
- Developer escalation rate: 70% of messaging incidents


**Current workaround & its limits:** Amazon Managed Grafana dashboards, CloudWatch Alarms, manual Athena queries, tribal knowledge. Limits: requires deep expertise, slow context gathering, inconsistent documentation access, no pattern recognition.

---

## 4) Hypothesis & Success Criteria
**Hypothesis:** An LLM-powered chat copilot with RAG and integrated tools can explain email deliverability incidents in plain English with citations, reducing both resolution time and developer escalations while enabling Production Support self-service.

**Metrics to move:**
- Time-to-resolve (non-escalation tickets only): Target -30% reduction
- Developer escalation rate: Target <50% (from 78%)
- User helpfulness rating: Target ≥80%


**Guardrails:**
- PII protection through hashing and redaction
- IAM role-based access control
- Full audit trail and citation requirements
- KMS encryption for sensitive data
- Responsible AI practices with deterministic responses

**Go/No-Go thresholds:** [?? what are these metrics, explain a bit better.]
- p95 latency ≤ 5 seconds
- ≥80% helpful ratings
- -20% reduction in TTFA
- 99% responses include citations

---

## 5) POC (What actually happens in a POC)
**Scope:** Yahoo bounces for security campaigns, DKIM/DMARC alignment issues, single ISP throttling patterns

**Data sample:** 
- 8 weeks of SES events (~70M records)
- 200 incident resolutions with structured format
- 50 runbooks and wikis
- ISP-specific guidance documents

**Baseline:** 
- Current MTTR: 50 minutes
- Escalation rate: 78%

**Tech spikes:**
- OpenSearch hybrid retrieval (BM25 + vector search)
- Bedrock Titan embeddings generation
- JSON-mode outputs for structured responses
- Athena query tool integration
- DNS/DMARC checking tools [?? what is this for?]

**Prototype UX:** Lightweight React chat interface with SSO via Cognito (done by front end engineers)

**Evaluation plan:**
- Golden question set (100 real incidents) [?? what is this?]
- Groundedness checks on citations 
- Hallucination detection
- Response consistency testing 

**Risks tested:**
- PII redaction effectiveness (email hashing)
- Latency under load (concurrent queries)
- Cost projections at scale
- Failure recovery paths

**POC outcome:** Met all criteria. Adjustments: added response caching, token-aware batching, stricter temperature controls (0-0.2) [?? what does token-aware batching and temperature controls mean and where do you set it?]

---

## 6) Stakeholders & Teaming
**Partners:**
- Engineering Manager (sponsor, guidance)
- Product Manager (requirements, prioritization)
- Junior Developer (statistics, templating components)
- Data Science team (model selection, tuning)
- Production Support team leads (30 engineers as users)
- Security team (compliance review) [??what would I ask the security team for compliance related things? Is this realted to responsible AI?]

**Responsibilities split:**
- **You:** Overall architecture, data ingestion pipelines, ETL/redaction, RAG retrieval system, tool integrations, API orchestration, observability, mentoring junior developer
- **Junior Dev:** Statistics calculation, data templating of logs, wikis, component development.
- **Data Science:** Model selection/tuning, evaluation frameworks, feedback loop implementation
- **Product Manager:** User research, success metrics, rollout strategy

**Decision cadence:** Weekly sprint reviews, bi-weekly stakeholder demos, monthly metrics review [?? what are these reviews about? explain each of them]

---

## 7) MVP Scope (Post-POC)
**Must-haves:**
- Core incident Q&A with citations ("Why did Yahoo bounce?")
- Real-time metrics integration (bounce rates, complaints)
- DNS/DMARC/SPF verification tools
- Athena query integration
- Feedback system (helpful/unhelpful)
- Audit logging [??what is audit logging?]

**Non-goals (cut):** [?? explain these better]
- Autonomous remediation actions
- Predictive analytics
- Multi-language support
- Mobile app
- Voice interface

**SLOs:** 
- Latency: median 2s, p95 ≤ 5s
- Availability: 99.5%
- Citation rate: ≥99% [??what is citation rate?]
- Cost: <$0.10/query

**Security review:**
- KMS encryption at rest
- IAM roles per service
- Lake Formation policies
- CloudTrail audit logs
- PII scrubbing validation

---

## 8) Pilot Plan (Why not ship to everyone)
**Pilot cohorts:** 
- 15 Production Support engineers + engineering manager
- Focus on email deliverability issues only
- Specific incident types: bounces, throttling, reputation

**Enablement:**
- Updated runbook templates
- Quick reference guide
- Dedicated Slack channel (#messagewise-pilot)
- Weekly office hours

**Measurement window:** 8 weeks tracking:
- Query volume and patterns
- Resolution times
- Escalation rates
- User satisfaction
- Cost per query

**Feedback loop:**
- In-chat 👍/👎 voting
- Auto-generated Jira tickets for unhelpful responses
- Weekly feedback sessions
- Suggested documentation improvements

---

## 9) Architecture (High-Level)
**Data ingest & lake:**
- Kinesis Firehose → S3 raw (32-68M events/month)
- AWS Glue jobs for PII redaction and normalization
- S3 curated layer with Parquet format
- Athena for SQL analytics
- Lake Formation for governance [?? what is this and where is opensearch?]

**Knowledge base:**
- 1.2-1.8k documents → 35-55k chunks [??what is this?]
- Bedrock Titan embeddings
- OpenSearch Serverless (40-60k vectors, 1-2GB) [??what are these statistics]
- Hybrid search: BM25 + k-NN vectors

**Orchestration:**
- API Gateway → Lambda functions
- Parallel retrieval from Athena/OpenSearch/Tools
- Step Functions for scheduled analysis [??what is this]
- EventBridge for alert routing [??what is this]

**LLM:**
- Amazon Bedrock (Open ai models)
- JSON-mode outputs
- Temperature: 0-0.2, low top_p
- Strict schema validation [??what is this]
- Tool calling capabilities [??what is this]

**Guardrails:**
- Email hashing before storage [??what is this]
- KMS encryption [??what is this]
- IAM role separation
- Prompt scrubbing [??what is this]
- Response validation [??what is this]

**Observability:**
- CloudWatch metrics and logs
- OpenTelemetry distributed tracing
- Amazon Managed Grafana dashboards
- Cost tracking per query


---

## 10) What You Built (Developer POV)
**Pipelines & storage:**
- Kinesis Firehose configuration for SES event streaming
- S3 partitioning strategy (by date/ISP/campaign) [??what is this partitioning strategy]
- Glue ETL jobs for data transformation 
- Parquet optimization for Athena queries

**Retrieval & tools:**
- OpenSearch hybrid search implementation
- BM25 + vector similarity scoring
- Athena query generation and execution
- DNS/DMARC/SPF checking tools [??what is this]
- Rate limit analysis tools [??what and how is this done]

**RAG orchestration:**
- Dynamic prompt assembly with context
- Tool calling framework
- JSON schema validation
- Citation extraction and linking
- Response streaming

**Reliability & ops:**
- Structured logging with correlation IDs
- Distributed tracing across services
- Cost controls and quotas
- Exponential backoff with jitter
- Circuit breakers for external services
- Dead letter queues for failed processing

**Collaboration:**
- Worked with DS on evaluation metrics
- DS handled model fine-tuning and retraining
- Provided APIs for feedback collection

---

## 11) Results (Pilot → Broader Use)
**Operational:**
- TTFA: ↓37% (50 min → 20 min) - adjusted based on feedback
- Developer escalations: 78% → 46% (-32pp)

**Adoption:**
- 30 Production Support engineers actively using
- ~640 queries/week by week 6
- Median response time: 2.0s
- p95 latency: 5.1s with streaming

**Quality:**
- 84% helpful rating (n=730)
- 99% responses include citations
- Average 2.4 citations per answer
- 66% first-contact resolution [??what is this]

**Business:**
- Estimated $120K/month revenue protection for marketing and promotion emails.
- Post-mortem completion: 40% → 85% [??what is this]
- 19 runbooks updated, 12 merged [??what is runbooks]
- Stale documentation links: ↓70% [??what is this]

**Counter-metrics:**
- Cost per query: $0.08 (within budget)
- Error rate: <1%
- No increase in false positives

---

## 12) "Between Start and Finish" (What typically happens)
**Friction points:**
- Inconsistent documentation quality requiring templating
- Unstructured ticket resolutions needed schema enforcement
- Token limits requiring intelligent batching
- Rate limits from LLM providers

**Course corrections:**
- Implemented strict document templates (title, context, steps, owner, last-verified)
- Enforced ticket schema: Cause, Signal, Fix, Prevention
- Backfilled 200+ historical records
- Added response caching for common queries

**Security approvals:**
- PII handling review (3 weeks) [??what is this]
- KMS key policy alignment [??what is this]
- RBAC implementation [??what is this]
- Audit logging requirements [??what is this]

**Scope trade-offs:**
- Deferred autonomous actions for MVP [??what is this]
- Limited to English-only initially
- Focused on read-only operations [??what is this]

**User feedback shaping UX:**
- Added copy-to-clipboard for queries
- Implemented collapsible citations
- Added "explain more" follow-ups
- Safe action buttons (open Jira, view dashboard)

**Stability work:**
- Request timeouts (30s hard limit) 
- Retry logic with exponential backoff
- Circuit breakers for OpenSearch [??what is this and how is this implemented]
- DLQ for failed embeddings [??what is this and how is it implemented]

---

## 13) Lessons Learned
**Technical:**
- Hybrid retrieval (BM25 + vectors) outperforms vectors-only by 23%
- Deterministic responses (low temperature) crucial for operational trust
- Citations aren't optional—they build confidence
- Token-aware batching essential for cost control [??what is this and why is that the case?]
- Structured schemas prevent prompt drift

**Product:**
- Start narrow: one incident type, one ISP
- Golden question sets accelerate iteration
- Measure everything, especially counter-metrics
- Users need to see sources, not just answers
- Feedback loops must be immediate and actionable

**Team:**
- Pair with champion users in Production Support
- Keep Data Science involved in drift monitoring
- Junior developers can own meaningful components
- Weekly demos maintain stakeholder alignment

---

## 14) Future Improvements
**Immediate (Q1):**
- Expanded to remaining projects

**Near-term (Q2):**
- Safe one-click actions with creating JIRAs from chat bot.

**Long-term (Q3-Q4):**
- Agentic AI with code base access:
  - Auto-generate fix PRs for known issues
  - Suggest code changes based on patterns

---

## 15) Demo Script (2-3 minutes) [?? Can you give me more examples to talk about? Give me 5 examples in total]
1. **Ask:** "Why did Yahoo bounce our security campaign yesterday?"
2. **Show:** 
   - Retrieved SES events with spike visualization
   - ISP guidance on authentication requirements
   - Citations to 3 sources (Athena query, runbook, ISP doc)
   - Recommended action: "Update DKIM alignment for m.surlatable.com"
3. **Click:** "Create Jira with reproduction steps" (pre-filled)
4. **Highlight:**
   - 2.1s response time
   - 3 verifiable citations
   - No PII exposed
   - Actionable next steps

---

## 16) Metrics Cheat Sheet

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Time-to-First-Action | 50 min | 20 min | -60% |
| Developer Escalations | 78% | 46% | -32pp |
| User Satisfaction | N/A | 84% | — |
| p95 Latency | N/A | 5.1s | — |
| Cost per Query | N/A | $0.08 | — |

---

## 17) Risks & Mitigations
**Hallucinations:**
- Mitigation: Temperature 0-0.2, JSON mode, mandatory citations, retrieval-only answers

**PII leakage:**
- Mitigation: Email hashing, field-level encryption, IAM policies, prompt scrubbing, audit logs

**Latency spikes:**
- Mitigation: Response caching (24hr TTL), query batching, precomputed aggregates, CDN for static content 

**Cost creep:**
- Mitigation: Athena partitioning by date, OpenSearch index optimization, token limits, query deduplication

**Model drift:**
- Mitigation: Weekly quality reviews, golden question regression tests, feedback-driven retraining

---

## 18) Q&A Prep (Crisp Answers)

**Why RAG vs fine-tuning?**
RAG provides real-time access to changing data (logs, metrics) with verifiable citations. Fine-tuning would require constant retraining and can't cite sources. Our operational data changes daily—RAG keeps answers current.

**How do you prevent prompt injection from retrieved text?**
Strict prompt templates, JSON-mode outputs, schema validation, and sandboxed execution. Retrieved text is marked as data, not instructions. Temperature near zero prevents creative interpretation.

**What happens if retrieval finds nothing?**
Graceful degradation: "I couldn't find specific information about [query]. Here are related topics..." with suggestions to refine the search or escalate to a developer with context.

**How do you keep costs predictable?**
Token limits per query (4K in, 2K out), response caching (24hr), query deduplication, batching similar requests, and daily budget alerts. Current cost: $0.08/query, well within $0.10 target.

**How do you ensure responsible AI practices?**
Deterministic responses (low temperature), mandatory citations for verification, PII protection through hashing, audit trails for all queries, human-in-the-loop for actions, regular bias testing, and transparent limitations messaging.

**What's the timeline and team composition?**
6-month project: 2 months POC, 2 months MVP, 2 months pilot/iteration. Team: myself (lead), junior developer (components/stats), PM (requirements), Data Science (2 members for model work), with guidance from Engineering Manager. [??what is POC, MVP, pilot]