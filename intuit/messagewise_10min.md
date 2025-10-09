# MessageWise: 10-Minute Interview Presentation (Simple Language)

## Introduction: What I Do at Sur La Table (1 minute)

• **My Role**: I'm a Senior Software Developer at Sur La Table, a high-end kitchen utensils retailer with both online and offline presence. The company also runs cooking classes which is one of the largest of it's kind in the US.

• **The Problem I Found**: Our support team of 10 people got about 50 alerts every day. They had to ask developers for help 70% of the time—not because the problems were hard, but because the answers were buried in cloudwatch logs, runbooks, wikis, and tribal knowledge.

• **Why This Mattered**:  This pattern consumed 30% of developer time on repetitive questions that had been solved before, impeding feature development

• **My Idea**: Apply RAG (Retrieval-Augmented Generation) and LLMs through a chat bot to help support engineers find answers on their own, without always needing developers.

## The Problem: Information Was Everywhere and Nowhere (2 minutes)

• **Time Wasted**: Support engineers spent 50 minutes per problem, mostly just searching for information across different systems—Amazon logs, monitoring tools, error trackers, wikis, and old Slack messages.

• **Bad Cycle**: 70% of problems got sent to developers, who were too busy to write down solutions, so the same problems kept coming back.

• **Where to Start**: We looked at all our tickets and found that 60% were about email delivery related problems due to deliverability dips, bounces spike, or ISP throttles. Sur La Table sends 45 million emails every month (about 1.8 million per day, up to 3.8 million during sales). So, this was our highest-impact opportunity.

• **Money on the Line**: For example, when 5% of promotional emails don't get delivered, we lose about 2 million emails that month, which means about $120,000 in lost sales. Other than this, any emails not delivered to customers regarding order details, order tracking, and cooking class details will have an indirect eventual impact on the revenue due to bad customer experience. This made email problems the perfect place to start.

## The Solution: MessageWise AI Assistant (3 minutes)

• **What I Built**: An AI system using RAG and LLM that sits on top of all our data and documents, using chat bot style interface to answer questions along with citations.

• **Not Just for Email**: I built it so we could add any type of problem later—payment issues, inventory problems, server crashes—but we started with email to prove it worked as the initial proof of concept. 

• **How It Works**: 
  - Domain-agnostic pipeline: Sources -> Kinesis Firehose → S3, with Glue handling transformation, aggregation, PII redaction.
  - We turned documents to chunks for creating embedding via Bedrock Titan pre-trained model.
  - Hybrid retrieval: OpenSearch combining BM25 keyword matching + vector similarity to fetch relevant information for LLM to process.

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

## What's Next (1 minute)

• **Growing the System**: 
1. Adding new problem types every few months—payments, inventory to the flow.
2. Use something similar on our website to help customers find the product of their choice without going through a long list of products. 
3. There is also plans to make use of agentic AI to automatically look at the issues, go through the logs, and other documents, fetch the code from the repository, make fixes and create a PR for review.
