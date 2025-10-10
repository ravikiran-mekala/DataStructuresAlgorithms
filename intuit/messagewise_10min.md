# MessageWise: 10-Minute Interview Presentation (Simple Language)

## Introduction: What I Do at Sur La Table (1 minute)

• **My Role**: I'm a Senior Software Developer at Sur La Table, a high-end kitchen utensils retailer with both online and offline presence. The company also runs cooking classes which is one of the largest of it's kind in the US.

• **About Project**: I built MessageWise, an AI-powered copilot that revolutionized how Sur La Table handles operational incidents—cutting resolution time by 60% (from 50 to 20 minutes), reducing developer escalations by 32 percentage points. We started with email delivery issues and then designed the system to expand to any operational domain.

## The Problem: Information Was Everywhere and Nowhere (2 minutes)

• **What I Discovered**: Our support team of 10 people get about 50 alerts every day, spending 50 minutes per problem searching across Amazon CloudWatch logs, monitoring tools, error trackers, wikis, and old Slack messages. They had to escalate to developers 40% of the time—not because problems were complex, but because answers were scattered and hard to find.

• **The Vicious Cycle**: Developers spent 30% of their time answering repetitive questions that had been solved before, but were too busy to document solutions properly, so the same problems kept returning. This pattern was killing our feature development velocity.

• **Finding Our Focus**: After analyzing all tickets, we found 60% were email delivery problems—deliverability dips, bounce spikes, ISP throttles. With Sur La Table sending 45 million emails monthly (1.8M daily, up to 3.8M during sales), a 5% delivery failure meant 2 million undelivered emails and $120,000 in lost revenue. This was our perfect starting point.

• **My Solution**: Build an AI assistant using RAG (Retrieval-Augmented Generation) and LLMs that could instantly search all our scattered knowledge and answer questions with citations, letting support engineers solve problems independently without constantly interrupting developers.

## The Solution: MessageWise AI Assistant (3 minutes)

• **What I Built**: An AI system using RAG and LLM that sits on top of all our data and documents, using chat bot style interface to answer questions along with citations.

• **Not Just for Email**: I built it so we could add any type of problem later—payment issues, inventory problems, server crashes—but we started with email to prove it worked as the initial proof of concept. 

• **How It Works**: 
  - Domain-agnostic pipeline: Sources (SES email events, cloudwatch logs, or any other resource) → Kinesis Firehose → S3, with Glue handling transformation, aggregation, PII redaction → S3 processed.
  - Athena table sits on top of S3 processed bucket.
  - We turned documents (S3 processed bucket data, internal wikis, runbooks, past incident information) to chunks for creating embedding via Bedrock Titan pre-trained model → OpenSearch Index.
  - Hybrid retrieval: OpenSearch combining BM25 keyword matching + vector similarity to fetch relevant information for LLM to process.
  - User query → Lambda → async Parallel Retrieval jobs (athena query, vector search semantics to OpenSearch, Keyword Search BM25 to OpenSearch) → LLM processing with temp - 0.2
  - Once the data is fed to Bedrock Claude Opus 4 LLM model over other models we get the json response where the response is formatted for the user interface.

• **What Happens When Someone Asks a Question**: If someone asks "Why did Yahoo reject our emails yesterday?", the system executes parallel operations—querying Athena for patterns, searching knowledge base for ISP guidelines, verifying DNS records, analyzing rate limits—all assembled by Lambda orchestrator and sent to Bedrock LLM with 0.2 temperature for consistent responses.

• **Proof Included**: Every answer shows where the information came from (averaging 2-3 sources), so engineers can double-check by clicking through to the actual data or document.

• **Built to Grow**: Each new problem area just plugs in without changing the main system. Email has its own tools for checking DNS and email settings. When we add individual project related data, we'll plug in project-specific tools.

## How We Built It (2 minutes)

• **Timeline**: 6 months total—2 months testing the idea with Yahoo email problems, 2 months building MVP, 2 months testing with support engineers.

• **Proof It Worked**: Our test showed answers in under 5 seconds, 80% of users found them helpful, and problems got solved 30% faster.

• **The Team**: I led the technical work, mentored a junior developer on building statistics and also in the initial stages of Data cleaning, worked with our product manager to pick what to build first, and partnered with data scientists who found that hybrid search outperformed only BM 25 by 23%.

• **Learning as We Went**: The customer feedback is stored in a postgres data base along with other information like prompt and the result and citations. This information is accessed and fed back in to the system to improve it. 

## Results: It Worked (2 minutes)

• **Big Win**: Developers now help with only 38% of problems instead of 70%—that's 32% fewer interruptions. The system handles 350 questions per week with 2-second average response time.

• **Email Problems Fixed Faster**: What took 50 minutes now takes 20 minutes. 66% of problems get solved without asking anyone else for help from the developers.

• **Happy Team**: Support engineers feel more confident solving problems on their own. We fixed 19 outdated guides, removed broken links, and now problems get proper write-ups as it is used as one of the sources for the LLM to get better.

## Responsible AI & Security: Building Trust (1 minute)

• **Responsible AI Practices**: (trust worthy, ethical with transparency and no bias, aligns with human values.)
  - Deterministic responses with citations: Temperature set to 0.2 to ensure consistent, factual answers rather than creative variations
  - Mandatory citations: 99% of responses include source links, allowing verification of every claim
  - No hallucinations: System only answers from retrieved data, admits when it doesn't know something
  - Bias prevention: Regular testing ensures no systematic bias in responses across different ISPs or problem types

• **Security First Approach**:
  - PII Protection: All email addresses hashed before storage using SHA-256, no customer data exposed in logs
  - Access Control: IAM roles ensure only authorized support engineers can query, with full audit trails
  - Prompt Security: Input sanitization prevents prompt injection attacks (avoid common injection patterns phrases, sanitizing file content for system prompts, adding prompt to warn llm to treat everything from user as data and not as command)

• **Compliance & Auditing**:
  - Every query logged with user, timestamp, and response for compliance tracking

## What's Next (1 minute)

• **Growing the System**: 
1. Adding new problem types every few months—payments, inventory to the flow.
2. Use something similar on our website to help customers find the product of their choice without going through a long list of products. 
3. There is also plans to make use of agentic AI to automatically look at the issues, go through the logs, and other documents, fetch the code from the repository, make fixes and create a PR for review.

## How did you make it domain agnostic?

• **Responsibility Seggregation**: Core Engine (RAG, LLM, UI/API layer), Domain Plugins (Data connectors, Validation rules, etc.)
• **Universal data pipelines**:  domain-agnostic pipeline where any data source—email events, payment webhooks, or inventory updates—flows through the same Kinesis→S3→Glue→Athena. Cares about structure and not content.
• **Yaml configs**:  list the domain-specific tools, point to relevant runbooks.
