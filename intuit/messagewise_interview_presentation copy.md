# MessageWise: 10-Minute Interview Presentation (Structured)

## Introduction: Company and My Role (1 minute)

• **Company Scale**: I'm Ravi Kiran, Senior Software Developer at Sur La Table, a premium cookware retailer operating one of the largest cooking class programs in the US. We send 45 million emails monthly—1.8M daily, spiking to 3.8M during promotions—powering everything from class registrations to order confirmations.

• **My Role**: I build and maintain data pipelines, API integrations, and also handle our legacy systems, while mentoring a junior developer and leading technical implementations.

• **Critical Context**: Email isn't just marketing for us—it's the backbone of customer engagement, directly tied to revenue through product launches, class bookings, and transactional communications.

## The Problem: Email at Scale (2 minutes)

• **Operational Bottleneck**: Our 10-person Production Support team received ~50 daily alerts. 60% of all support tickets were email-related, and 70% of those required developer escalation—pulling developers away from feature work for 30% of their time.

• **Root Cause**: Average resolution took 50 minutes not due to complexity, but because diagnosis required searching across Amazon SES logs, CloudWatch metrics, New Relic dashboards, Sentry errors, internal wikis, and tribal knowledge—information existed but wasn't accessible during incidents.

• **Business Impact**: A 5% deliverability drop means 2 million undelivered emails monthly. With our metrics (2.5% CTR, 2% conversion, $120 AOV), that's $120,000 in lost revenue per month, plus the hidden cost of developer productivity loss.

## The Solution: MessageWise AI Copilot (3 minutes)

• **Core Innovation**: MessageWise uses RAG (Retrieval-Augmented Generation) to combine LLM reasoning with our operational data. When someone asks "Why did Yahoo bounce our campaign?", it orchestrates parallel queries across data lakes, knowledge bases, DNS records, and rate limits—delivering comprehensive answers with citations in 2 seconds.

• **Technical Architecture**: We ingest 45M email events monthly through Kinesis Firehose into S3, with Glue jobs handling PII redaction. Our knowledge base processes 1,500 documents into 50,000 chunks, embedded via Bedrock Titan and indexed in OpenSearch for hybrid search (BM25 + vectors). Lambda functions orchestrate retrieval while Bedrock runs OpenAI models at 0.2 temperature for deterministic responses.

• **Trust Through Transparency**: 99% of responses include citations (averaging 2.4 sources), allowing users to verify claims via Athena queries, runbooks, or dashboards. Security includes KMS encryption, IAM controls, audit logging, and prompt scrubbing against injection attacks.

• **Feedback Loop**: Users vote thumbs up/down on responses, with negative feedback auto-generating Jira tickets containing the question, context, and suggested documentation improvements—creating continuous improvement.

## Implementation Journey (2 minutes)

• **Phased Approach**: 6-month timeline with 2-month POC (Yahoo bounces, DKIM/DMARC issues), 2-month MVP (production architecture, security controls), and 2-month pilot with 15 Production Support engineers. POC proved resolution time reduction from 50 min to 20 min with 80% customer satisfaction.

• **Team Composition**: I led as technical architect, mentoring a junior developer on data templating/statistics, collaborating with our PM on requirements, partnering with 2 data scientists on model tuning, and working with security on compliance reviews.

• **Key Discoveries**: Hybrid retrieval outperformed pure vector search by 23%, users strongly preferred multiple citations over speed, and weekly feedback reviews were critical for refining retrieval strategies and updating stale documentation.

## Results and Impact (2 minutes)

• **Operational Metrics**: Resolution time dropped 60% (50→20 minutes), developer escalations decreased 32 percentage points (70%→38%), system handles 640 queries/week at 2-second median response time, with 84% user satisfaction and 66% first-contact resolution.

• **Efficiency Gains**: Manual log analysis reduced 45%, post-mortem completion improved from 40% to 85%, documentation updates led to 70% fewer broken links, and false-positive alerts dropped 30%.

• **Business Value**: Protecting $120K monthly revenue through maintained deliverability, achieving $0.08 cost per query within budget, maintaining 99.5% system availability, and most importantly—restoring developer focus to feature delivery instead of repetitive troubleshooting.

## Future Vision and Lessons Learned (1 minute)

• **Expansion Plans**: Near-term adding safe one-click actions (pre-filled Jira tickets, campaign pausing), long-term building agentic AI that can analyze code and auto-generate PRs for known issues, plus exploring customer-facing version for product recommendations.

• **Key Lessons**: Start narrow and prove value incrementally (one ISP, one problem type), prioritize deterministic behavior over sophistication for operational tools, make citations mandatory for trust, and ensure close engineering-data science collaboration.

• **Core Philosophy**: The best AI augments rather than replaces human capability—our support engineers are now more effective problem-solvers, not obsolete. MessageWise transforms 50-minute expert investigations into 2-second conversations anyone can have, democratizing operational excellence.