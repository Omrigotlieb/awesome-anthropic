# Claude Prompt Library

> 60+ battle-tested prompts for Claude. Copy, paste, and customize.
> Organized by category. Each prompt is ready to use.

---

## 💻 Coding (10 prompts)

### Code Review
> Use case: Get a thorough, structured code review of any file or snippet

```
You are a senior software engineer conducting a code review. Review the following code carefully and provide structured feedback.

For each issue you find, specify:
1. Severity: Critical / Major / Minor / Nit
2. Location: Line number or function name
3. Issue: What is wrong or could be improved
4. Suggestion: Concrete fix or recommendation

Also provide an overall assessment covering: correctness, readability, performance, security, and test coverage.

Be direct and specific. Avoid vague praise. If the code is good in some areas, say so briefly, then focus on what can be improved.

Code to review:
[PASTE CODE HERE]
```

### Refactoring
> Use case: Clean up and modernize an existing codebase section

```
You are a refactoring expert. Your job is to improve the code below without changing its external behavior.

Apply these principles:
- Extract repeated logic into reusable functions
- Improve variable and function naming for clarity
- Reduce nesting and complexity (aim for a max cyclomatic complexity of 5 per function)
- Replace imperative loops with idiomatic constructs where appropriate
- Add inline comments only where intent is non-obvious

After the refactored code, provide a brief changelog: list each change made and why.

Language: [LANGUAGE]
Code:
[PASTE CODE HERE]
```

### Bug Investigation
> Use case: Systematically diagnose a bug with Claude's help

```
Help me debug this issue. Think step by step before providing a solution.

**Observed behavior:** [DESCRIBE WHAT IS HAPPENING]
**Expected behavior:** [DESCRIBE WHAT SHOULD HAPPEN]
**Steps to reproduce:** [LIST STEPS]
**Environment:** [OS, runtime version, relevant dependencies]

Here is the relevant code:
[PASTE CODE]

Here is the error output or log:
[PASTE ERROR / LOG]

Walk me through your diagnostic reasoning: what are the most likely root causes, ranked by probability? Then provide a fix for the most likely cause, with an explanation of why it works.
```

### Unit Test Generation
> Use case: Generate comprehensive unit tests for a function or module

```
Write a comprehensive unit test suite for the following code.

Requirements:
- Cover happy path, edge cases, and error cases
- Test boundary conditions (empty input, null, max values, etc.)
- Use the testing framework standard for [LANGUAGE/FRAMEWORK] (e.g., pytest, Jest, JUnit)
- Each test should have a descriptive name that reads like a sentence
- Mock external dependencies; do not make real network calls or DB calls
- Aim for at least 90% branch coverage
- Add a comment above each test group explaining what is being tested and why

Code to test:
[PASTE CODE HERE]
```

### Documentation Generation
> Use case: Generate docstrings and inline documentation for undocumented code

```
Generate complete documentation for the following code.

For each function/method, write:
- A one-line summary
- A longer description if the behavior is non-trivial
- Parameter descriptions with types
- Return value description with type
- Raises/throws section if errors can be raised
- A usage example for complex functions

Use the docstring format standard for [LANGUAGE] (e.g., Google style for Python, JSDoc for JavaScript, Javadoc for Java).

Do not change the code itself. Only add documentation.

Code:
[PASTE CODE HERE]
```

### Performance Optimization
> Use case: Identify and fix performance bottlenecks in code

```
You are a performance optimization expert. Analyze the following code for performance issues.

For each issue found:
1. Identify the bottleneck (e.g., O(n²) loop, redundant DB calls, memory leak, blocking I/O)
2. Explain why it is slow
3. Provide an optimized version
4. Estimate the improvement (e.g., "reduces from O(n²) to O(n log n)")

Prioritize issues by impact. Focus on algorithmic improvements first, then implementation-level optimizations.

Context: This code runs [DESCRIBE CONTEXT: e.g., "on every API request", "in a batch job processing 1M records"]

Code:
[PASTE CODE HERE]
```

### Security Review
> Use case: Audit code for security vulnerabilities

```
Perform a security audit of the following code. Think carefully before responding.

Check for these vulnerability classes (and any others relevant to the language/context):
- Injection attacks (SQL, command, LDAP, XPath)
- Authentication and authorization flaws
- Sensitive data exposure (hardcoded secrets, logging PII)
- Insecure deserialization
- Path traversal and file inclusion
- Race conditions
- Dependency vulnerabilities (note any suspicious imports)
- Input validation gaps

For each finding:
- Name the vulnerability class (use CWE ID if applicable)
- Explain the attack vector
- Rate severity: Critical / High / Medium / Low
- Provide a remediation with corrected code

Language/Framework: [LANGUAGE]
Code:
[PASTE CODE HERE]
```

### PR Description
> Use case: Write a clear, complete pull request description from a diff

```
Write a pull request description for the following diff.

Format:
## Summary
[2-4 sentence explanation of what changed and why]

## Changes
[Bulleted list of specific changes]

## Testing
[How this was tested or how it should be tested]

## Notes for Reviewer
[Anything the reviewer should pay special attention to, or context they need]

Be specific and technical. Do not use vague phrases like "various improvements" or "code cleanup" — describe exactly what changed.

Diff:
[PASTE DIFF HERE]
```

### Architecture Review
> Use case: Get feedback on a system design or architecture proposal

```
You are a senior software architect. Review the following system design and provide structured feedback.

Evaluate:
1. **Scalability** — Will this design handle 10x / 100x current load? Where are the bottlenecks?
2. **Reliability** — What are the failure modes? What happens when component X fails?
3. **Maintainability** — How easy will this be to change in 12 months?
4. **Security** — What are the attack surfaces?
5. **Operational complexity** — How hard is this to deploy, monitor, and debug?

For each concern, rate it: Critical / Important / Nice-to-fix, and suggest a concrete alternative.

Also note what the design gets right — not every pattern is wrong.

Design document / diagram description:
[PASTE HERE]
```

### Migration Plan
> Use case: Generate a step-by-step migration plan for a technology or pattern change

```
Create a detailed migration plan for the following change.

From: [CURRENT TECHNOLOGY/PATTERN]
To: [TARGET TECHNOLOGY/PATTERN]
Codebase size: [APPROXIMATE SIZE/COMPLEXITY]
Team size: [NUMBER OF ENGINEERS]

The plan should include:
1. **Risk assessment** — What can go wrong? What is the rollback plan?
2. **Phased approach** — Break the migration into discrete phases, each independently deployable
3. **Strangler fig pattern** — Identify where old and new can coexist during transition
4. **Testing strategy** — How to verify correctness at each phase
5. **Estimated effort** — Rough story points or days per phase
6. **Definition of done** — How do we know the migration is complete?

Be practical. Assume a production system that cannot be taken offline.
```

---

## ⚡ Claude Code (8 prompts)

### CLAUDE.md Generator
> Use case: Generate a comprehensive CLAUDE.md file for a new or existing project

```
Generate a CLAUDE.md file for my project. This file will be read by Claude Code at the start of every session to understand the project context.

Include these sections:
1. **Project Overview** — What this project does, its purpose, and target users
2. **Architecture** — Key directories, how the code is organized, important files
3. **Development Setup** — How to install dependencies, run the dev server, run tests
4. **Common Commands** — The exact bash commands for build, test, lint, format, deploy
5. **Code Style** — Conventions for this codebase (naming, patterns to use/avoid)
6. **Key Constraints** — Things Claude should never do (e.g., "never modify migrations directly", "always use the internal logger")
7. **Testing** — How to run tests, where they live, how to write new ones
8. **External Services** — APIs, databases, or services this project integrates with

Project details:
- Language/Framework: [LANGUAGE/FRAMEWORK]
- Project description: [DESCRIPTION]
- Repo structure (paste `tree -L 2` output): [PASTE HERE]
```

### Agentic Task Kickoff
> Use case: Give Claude Code a well-structured task brief for a complex multi-step task

```
I need you to complete the following task autonomously. Before writing any code, think through the full approach and share your plan.

**Task:** [CLEAR DESCRIPTION OF WHAT NEEDS TO BE DONE]

**Acceptance criteria:**
- [CRITERION 1]
- [CRITERION 2]
- [CRITERION 3]

**Constraints:**
- Do not modify files outside of [DIRECTORY/SCOPE]
- Preserve all existing tests; add new ones as needed
- Follow the existing code style
- Do not add new dependencies without asking

**Definition of done:** [HOW WILL WE KNOW IT IS COMPLETE?]

Start by reading the relevant files to understand the existing structure. Then outline your plan before making changes. If you encounter an ambiguity that would significantly change your approach, pause and ask.
```

### Project Planning
> Use case: Break down a feature into tasks for Claude Code to execute

```
I want to build the following feature. Help me create a detailed implementation plan that I can hand off to an AI coding agent.

**Feature:** [FEATURE DESCRIPTION]
**Tech stack:** [STACK]
**Existing codebase context:** [BRIEF DESCRIPTION OR PASTE RELEVANT STRUCTURE]

Create a task breakdown that:
1. Lists tasks in dependency order (task B must come after task A if it depends on it)
2. Keeps each task small enough to complete in one focused session (under 200 lines of new code)
3. Specifies which files need to be created or modified for each task
4. Identifies any tasks that require a decision (e.g., "choose between approach A and B")
5. Includes integration test tasks to verify each phase

Format as a numbered checklist I can paste into a project tracker.
```

### Codebase Walkthrough
> Use case: Get a structured orientation to an unfamiliar codebase

```
I'm new to this codebase. Give me a thorough walkthrough to help me get oriented quickly.

Please cover:
1. **What it does** — The core purpose and value of this project in 2-3 sentences
2. **Entry points** — Where does execution start? (main files, route definitions, event handlers)
3. **Core data flow** — How does a typical request/operation flow through the system?
4. **Key abstractions** — The most important classes, modules, or patterns used throughout
5. **Where to find things** — Which directories contain which types of code
6. **Gotchas** — Any non-obvious conventions, anti-patterns, or landmines in this codebase
7. **Good first places to make changes** — If I want to add a new feature, where do I start?

Files available:
[PASTE `tree -L 3` OUTPUT OR KEY FILE LISTINGS]
```

### Hook Configuration
> Use case: Help set up Claude Code hooks for automated quality gates

```
Help me configure Claude Code hooks for my project.

I want to run the following quality checks automatically:
- [CHECK 1, e.g., "run ESLint on any modified JS/TS file"]
- [CHECK 2, e.g., "run pytest for any modified Python file"]
- [CHECK 3, e.g., "run prettier format check before any commit"]

For each hook:
1. Write the hook configuration in the correct JSON format for `.claude/settings.json`
2. Write the shell command that should run
3. Explain when the hook fires (pre-tool-use, post-tool-use, pre-compact, etc.)
4. Explain what Claude Code will do if the hook exits non-zero

Also show me how to test that each hook is working correctly.

My project structure:
[PASTE RELEVANT STRUCTURE]
```

### Tool Use Patterns
> Use case: Get guidance on which Claude Code tools to use for a task

```
I'm building an agentic workflow with Claude Code and need to decide which tools to use.

My task: [DESCRIBE THE TASK]

For this task, advise me on:
1. Which Claude Code built-in tools are relevant (Bash, Read, Write, Edit, Glob, Grep, etc.)
2. Which MCP servers I should consider enabling
3. The recommended sequence of tool calls to accomplish this task efficiently
4. Common mistakes to avoid (e.g., using Bash when Grep is more appropriate)
5. How to structure the task so Claude uses tools minimally and precisely

Show me an example tool-use sequence for a simple version of this task.
```

### Multi-Agent Workflow
> Use case: Design a multi-agent setup using Claude Code's subagent capabilities

```
Design a multi-agent workflow for the following complex task.

**Task:** [DESCRIBE THE HIGH-LEVEL TASK]
**Scale:** [HOW LARGE IS THIS? e.g., "migrate 200 files", "process 50 PRs"]

Design a workflow where:
1. An orchestrator agent breaks the work into parallel subtasks
2. Subagents handle individual chunks independently
3. Results are aggregated by the orchestrator

For the design, specify:
- How to partition the work (by file, by module, by feature, etc.)
- What context each subagent needs
- How subagents report results back
- How to handle partial failures
- The claude -p command invocations to use for spawning subagents
- An estimated speedup from parallelization

Include a worked example showing orchestrator and subagent prompts.
```

### Debugging Claude Code
> Use case: Diagnose why a Claude Code session is not behaving as expected

```
Claude Code is not behaving as expected. Help me diagnose the problem.

**What I asked Claude Code to do:** [DESCRIBE THE TASK]
**What Claude Code actually did:** [DESCRIBE WHAT HAPPENED]
**Unexpected behavior:** [SPECIFIC ISSUE: e.g., "it edited the wrong file", "it stopped mid-task", "it ignored a constraint"]

Relevant context:
- My CLAUDE.md contents: [PASTE OR SUMMARIZE]
- The prompt I used: [PASTE PROMPT]
- Any error messages: [PASTE ERRORS]

Help me diagnose:
1. Is the problem in my prompt, my CLAUDE.md, or a Claude Code limitation?
2. What is the most likely cause?
3. How should I rewrite my prompt or configuration to get the desired behavior?
4. Are there any Claude Code best practices I'm missing?
```

---

## ✍️ Writing (8 prompts)

### Blog Post
> Use case: Write a technical or thought leadership blog post

```
Write a blog post on the following topic.

**Topic:** [TOPIC]
**Target audience:** [WHO WILL READ THIS: e.g., "senior engineers", "startup founders", "product managers"]
**Desired length:** [APPROXIMATE WORD COUNT]
**Tone:** [e.g., "opinionated and direct", "friendly and accessible", "formal and research-backed"]
**Key argument or thesis:** [THE MAIN POINT YOU WANT TO MAKE]

Structure the post with:
- A hook in the first paragraph that makes the reader want to continue
- Clear section headers
- Concrete examples, not abstract principles
- A strong conclusion with a call to action or key takeaway

Avoid: excessive jargon, hedging language ("it could be argued that"), and generic advice. Write as if you have a clear point of view and are not afraid to defend it.
```

### Professional Email
> Use case: Draft a clear, professional email for a tricky situation

```
Write a professional email for the following situation.

**Context:** [DESCRIBE THE SITUATION AND RELATIONSHIP]
**Goal of the email:** [WHAT DO YOU WANT TO HAPPEN AS A RESULT?]
**Key points to convey:**
- [POINT 1]
- [POINT 2]
- [POINT 3]
**Tone:** [e.g., "firm but respectful", "warm and collaborative", "direct and brief"]
**Any constraints:** [e.g., "don't mention the budget issue directly", "keep it under 150 words"]

Write the email with a subject line, greeting, body, and sign-off. Be direct. Cut any filler phrases like "I hope this email finds you well" unless the tone specifically calls for warmth.
```

### Technical Documentation
> Use case: Write clear, usable technical documentation for a feature or API

```
Write technical documentation for the following.

**Subject:** [FEATURE, API ENDPOINT, OR SYSTEM TO DOCUMENT]
**Audience:** [e.g., "external API consumers", "internal engineers", "end users"]

Include:
1. **Overview** — What this is and when to use it (2-4 sentences)
2. **Prerequisites** — What the reader needs before they start
3. **Quick start** — The minimum steps to get a working example
4. **Reference** — Parameters, return values, error codes in table format
5. **Examples** — 2-3 realistic code examples covering common use cases
6. **Troubleshooting** — The top 3-5 things that go wrong and how to fix them

Write for a reader who is smart but unfamiliar with this system. Prefer active voice. Use second person ("you"). Every example must be complete and runnable.

Technical details:
[PASTE RELEVANT CODE, API SPEC, OR NOTES]
```

### Editing and Proofreading
> Use case: Polish a draft for clarity, grammar, and style

```
Edit the following text for clarity, grammar, and style. Be thorough.

Goals for the edit:
- Fix all grammatical errors, typos, and punctuation issues
- Improve sentence-level clarity (cut wordiness, fix awkward phrasing)
- Improve flow between paragraphs
- Strengthen weak or vague word choices
- Preserve the author's voice — do not rewrite from scratch

After the edited version, provide a brief editor's note listing the main categories of changes you made (e.g., "removed redundant phrases in paragraphs 2 and 4", "restructured the opening sentence for clarity").

Text to edit:
[PASTE TEXT HERE]
```

### Tone Adjustment
> Use case: Rewrite content to match a different tone or audience

```
Rewrite the following text to match a new tone and audience.

**Original audience:** [WHO IT WAS WRITTEN FOR]
**New audience:** [WHO IT SHOULD BE WRITTEN FOR]
**Original tone:** [e.g., "technical and dense"]
**Target tone:** [e.g., "friendly, accessible, and energetic"]

Keep the core meaning and all key facts intact. Change only how it is expressed. Do not add new information.

If there is terminology that the new audience would not understand, either replace it with a plain-language equivalent or add a brief explanation inline.

Text to rewrite:
[PASTE TEXT HERE]
```

### Executive Summary
> Use case: Distill a long document into a crisp executive summary

```
Write an executive summary of the following document.

The summary should:
- Be no longer than 300 words
- Cover: the core problem or opportunity, the proposed approach, key findings or decisions, and the recommended next steps
- Be readable by someone who will NOT read the full document
- Use plain language — minimize jargon
- Lead with the most important information (inverted pyramid structure)

After the summary, add a "Key Decisions Required" section listing any open decisions that require input from leadership.

Document to summarize:
[PASTE DOCUMENT HERE]
```

### Proposal Writing
> Use case: Write a persuasive proposal for a project, initiative, or investment

```
Write a proposal for the following initiative.

**Initiative:** [DESCRIBE WHAT YOU ARE PROPOSING]
**Audience:** [WHO WILL READ AND DECIDE ON THIS]
**Desired outcome:** [WHAT YOU WANT THE READER TO APPROVE OR DO]

Structure:
1. **Problem Statement** — Why this matters now (include data or specific examples)
2. **Proposed Solution** — What you are proposing, in concrete terms
3. **Why This Approach** — Briefly acknowledge alternatives and explain why this is better
4. **Expected Outcomes** — Specific, measurable results within a defined timeframe
5. **Resources Required** — Time, budget, headcount, or other asks
6. **Risks and Mitigations** — What could go wrong and how you'll address it
7. **Ask** — One clear, specific ask at the end

Be persuasive but honest. Do not overstate benefits or hide risks. Decision-makers distrust proposals that have no downsides.
```

### Technical Writing
> Use case: Write clean technical content for developer audiences

```
Write a [CONTENT TYPE: e.g., "tutorial", "concept explanation", "how-to guide"] on [TOPIC] for [AUDIENCE].

Technical writing principles to follow:
- Use active voice throughout
- Keep sentences short (under 25 words when possible)
- Define every term on first use
- Use numbered lists for sequential steps, bulleted lists for non-sequential items
- Include a real, runnable code example for every concept introduced
- Avoid opinion statements — stick to facts and observable behavior
- Do not use marketing language ("powerful", "seamless", "revolutionary")

If writing a tutorial: each step should have an observable output so the reader knows it worked.
If writing an explanation: use an analogy to connect the new concept to something familiar.
If writing a how-to: lead with the command/action, then explain why.

Topic details:
[DESCRIBE THE TOPIC AND PROVIDE ANY REFERENCE MATERIAL]
```

---

## 🔍 Analysis (7 prompts)

### Data Analysis
> Use case: Extract insights from a dataset or data description

```
Analyze the following data and provide actionable insights.

**Context:** [DESCRIBE WHAT THIS DATA REPRESENTS AND WHY IT MATTERS]
**Key questions to answer:**
1. [QUESTION 1]
2. [QUESTION 2]
3. [QUESTION 3]

For your analysis:
- Identify the most significant patterns, trends, or anomalies
- Quantify findings where possible (percentages, ratios, deltas)
- Distinguish between correlation and causation — flag any causal claims as hypotheses
- Identify the top 3 actionable takeaways, ranked by potential impact
- Note any data quality issues or gaps that limit the analysis

Present findings in order of importance, not in the order they appear in the data.

Data:
[PASTE DATA OR DESCRIPTION HERE]
```

### Competitive Analysis
> Use case: Analyze competitors to identify opportunities and threats

```
Conduct a competitive analysis for the following company and context.

**Company being analyzed:** [YOUR COMPANY / PRODUCT]
**Competitors to analyze:** [LIST COMPETITORS]
**Context:** [e.g., "we are entering a new market segment", "deciding whether to build feature X"]

For each competitor, analyze:
1. Core product and positioning
2. Pricing and business model
3. Strengths (what they do better than us)
4. Weaknesses (where they fall short)
5. Recent moves (new features, funding, partnerships)

Then provide:
- A 2x2 positioning map (describe it in text if you cannot create an image)
- Our differentiation opportunity: where is there unoccupied whitespace?
- Top 3 competitive threats we should take seriously
- Top 3 features or strategies where we can win

Base your analysis on what you know. Flag any assumptions or areas where I should verify with current data.
```

### Requirements Review
> Use case: Critically review a set of product or technical requirements

```
Review the following requirements document and identify issues.

Look for:
1. **Ambiguities** — Requirements that could be interpreted in multiple ways
2. **Contradictions** — Requirements that conflict with each other
3. **Incompleteness** — Missing requirements (e.g., error states not specified, edge cases not covered)
4. **Testability** — Requirements that cannot be objectively verified
5. **Feasibility** — Requirements that may be technically difficult or impossible
6. **Scope creep risks** — Requirements that are vague enough to expand uncontrollably

For each issue: cite the specific requirement, name the issue type, and suggest a rewrite that resolves it.

Finally, rate the overall quality of the requirements: High / Medium / Low, with a one-sentence justification.

Requirements document:
[PASTE REQUIREMENTS HERE]
```

### Risk Assessment
> Use case: Systematically assess risks for a project or decision

```
Perform a risk assessment for the following.

**Subject:** [PROJECT, DECISION, OR PLAN TO ASSESS]
**Timeframe:** [HOW FAR OUT ARE WE PLANNING?]
**Stakes:** [WHAT IS AT RISK IF THIS GOES WRONG?]

For each risk identified:
1. Name the risk clearly
2. Category: Technical / Operational / Market / People / Financial / Regulatory
3. Likelihood: High / Medium / Low (with brief justification)
4. Impact: High / Medium / Low (with brief justification)
5. Risk score: Likelihood × Impact (H×H = Critical, H×M = High, etc.)
6. Mitigation: Specific action to reduce likelihood or impact
7. Owner: Who should own this risk

Sort risks by risk score (Critical first). Limit to the top 10 most significant risks.

Context:
[DESCRIBE THE PROJECT OR DECISION IN DETAIL]
```

### Feedback Synthesis
> Use case: Synthesize qualitative feedback from users or stakeholders into themes

```
Synthesize the following feedback into clear themes and actionable recommendations.

**Source of feedback:** [e.g., "user interviews", "NPS survey responses", "support tickets"]
**Number of responses:** [APPROXIMATE COUNT]
**Context:** [WHAT QUESTION OR SITUATION PROMPTED THIS FEEDBACK?]

For your synthesis:
1. Identify the top 5-7 themes, ranked by frequency
2. For each theme: provide a clear label, a 2-sentence description, and 2-3 direct quotes that exemplify it
3. Distinguish between: complaints (something is broken), wishes (something is missing), and praise (something is working)
4. Identify any surprising or unexpected insights
5. Translate the top 3 themes into specific product or process recommendations

Feedback to synthesize:
[PASTE FEEDBACK HERE]
```

### Tradeoff Analysis
> Use case: Evaluate competing options with structured tradeoff analysis

```
Help me think through this decision using a structured tradeoff analysis.

**Decision:** [DESCRIBE THE DECISION TO BE MADE]
**Options:** [LIST THE OPTIONS, e.g., "Option A: Build in-house, Option B: Buy a SaaS tool, Option C: Open source library"]
**Constraints:** [NON-NEGOTIABLE CONSTRAINTS, e.g., "must be live within 3 months", "budget under $50k"]

Evaluate each option across these dimensions (rate each 1-5, with justification):
- Cost (total cost of ownership, 12 months)
- Time to implement
- Long-term flexibility / lock-in risk
- Operational burden
- Risk / uncertainty
- Alignment with team skills

Then:
1. Summarize the key tradeoffs in plain language
2. Make a recommendation, citing your reasoning
3. Describe the conditions under which a different option would be the right choice

Do not hedge excessively. Make a recommendation.
```

### Decision Framework
> Use case: Apply a structured framework to a difficult decision

```
Help me make the following decision using a structured decision framework.

**Decision:** [DESCRIBE THE DECISION]
**Context:** [RELEVANT BACKGROUND]
**Options being considered:** [LIST OPTIONS]
**Decision maker(s):** [WHO IS MAKING THIS DECISION]
**Deadline:** [WHEN MUST THIS BE DECIDED]

Apply the following framework:
1. **Clarify the objective** — What does a good outcome look like in 12 months?
2. **Identify criteria** — What factors matter most? Weight them.
3. **Evaluate options** — Score each option against each criterion.
4. **Test for reversibility** — Is this decision easy or hard to reverse? (Adjust risk tolerance accordingly)
5. **Pre-mortem** — For the top option: imagine it failed. What went wrong?
6. **Recommendation** — Given all of the above, what should be done, and why?

Be direct. I want a recommendation, not a list of considerations.
```

---

## 🔬 Research (6 prompts)

### Literature Review
> Use case: Get a structured overview of a topic's research landscape

```
Conduct a literature review on the following topic.

**Topic:** [RESEARCH TOPIC]
**Depth required:** [e.g., "high-level overview", "comprehensive academic review"]
**Use case:** [WHY I NEED THIS: e.g., "writing a paper", "making a technology decision", "briefing a team"]

Structure your review as:
1. **Definition and scope** — How is this topic defined? What is in scope vs. out of scope?
2. **Historical development** — How did this field develop? Key milestones.
3. **Current consensus** — What do we know with high confidence?
4. **Active debates** — Where do researchers disagree and why?
5. **Open questions** — What is still unknown or understudied?
6. **Practical implications** — How does this research translate to practice?
7. **Key sources** — Name the most cited papers, researchers, or institutions in this space

Note the limits of your knowledge: flag topics where the field may have advanced beyond your training cutoff.
```

### Topic Deep Dive
> Use case: Get a thorough, expert-level explanation of an unfamiliar topic

```
Give me a deep, expert-level explanation of [TOPIC]. Assume I am intelligent but not already familiar with this subject.

Structure your explanation as follows:
1. **Core concept** — What is this, in one paragraph?
2. **Why it matters** — Practical significance and real-world impact
3. **How it works** — The mechanism or process, explained clearly with an analogy
4. **Key components** — The most important parts or sub-concepts
5. **Common misconceptions** — What do people often get wrong about this?
6. **Edge cases and nuances** — Where does the standard explanation break down?
7. **Connections** — How does this relate to [RELATED TOPIC I ALREADY UNDERSTAND]?
8. **What to read next** — If I want to go deeper, what should I study?

Use concrete examples wherever possible. Define every technical term when you introduce it. Cite your reasoning where relevant.
```

### Source Evaluation
> Use case: Evaluate the credibility and quality of a source or set of sources

```
Evaluate the credibility and quality of the following source(s).

For each source, assess:
1. **Authorship** — Who created this? What are their credentials and potential biases?
2. **Publication venue** — Where was this published? Is the venue reputable and peer-reviewed?
3. **Methodology** — How was the research conducted? Is the methodology sound?
4. **Sample and scope** — How large and representative is the sample? What are the scope limitations?
5. **Conflicts of interest** — Was this funded by parties with a stake in the outcome?
6. **Recency** — Is this current? Has the field moved on since publication?
7. **Replication** — Has this been independently replicated?

Overall credibility rating: High / Medium / Low

Conclude with: how much weight should I give this source when making decisions?

Source(s):
[PASTE CITATION, ABSTRACT, OR RELEVANT EXCERPTS]
```

### Executive Summary from Papers
> Use case: Extract the key findings from an academic paper for a non-specialist audience

```
Summarize the following academic paper for a non-specialist audience.

The summary should:
- Be written for someone with no domain expertise
- Explain the research question in plain language
- Describe what was studied and how (in 2-3 sentences)
- State the key findings clearly, with any important caveats
- Explain the practical implications: "So what? Why does this matter?"
- Note any significant limitations the authors themselves identify
- Be no longer than 400 words

Do not use jargon without explaining it. If the study has limited applicability, say so directly.

Paper (paste title, abstract, and key sections):
[PASTE HERE]
```

### Trend Analysis
> Use case: Analyze trends in a technology, market, or domain

```
Analyze the current trends in [DOMAIN/TECHNOLOGY/MARKET].

Cover:
1. **Macro trends** — The 3-5 most significant directional shifts happening right now
2. **Drivers** — What is causing each trend? (technology, regulation, economics, behavior change)
3. **Timeline** — Is this trend early-stage, mainstream, or mature?
4. **Winners and losers** — Which companies, technologies, or approaches are gaining or losing ground?
5. **Second-order effects** — What downstream changes will these trends create?
6. **Counterforces** — What could slow or reverse these trends?
7. **Implications for [MY CONTEXT]** — What does this mean for [my company / product / career]?

Be specific. Name companies, technologies, and data points where you can. Flag any areas where you are working from information that may be outdated (my knowledge cutoff is [DATE]).
```

### Interview Synthesis
> Use case: Synthesize themes and insights from qualitative interview data

```
Synthesize insights from the following interview transcripts or notes.

**Research question:** [WHAT WERE YOU TRYING TO LEARN?]
**Number of interviews:** [COUNT]
**Participant profile:** [WHO WAS INTERVIEWED]

For the synthesis:
1. Identify 4-6 major themes that emerged across interviews
2. For each theme: describe it, note how prevalent it was (e.g., "mentioned by 7 of 10 participants"), and include 1-2 illustrative quotes
3. Identify tensions or contradictions across participants
4. Note any perspectives that appeared in only 1-2 interviews but were particularly insightful
5. Separate observations (what participants said) from interpretations (what it means)
6. Conclude with 3 implications for [product / policy / strategy]

Interview data:
[PASTE NOTES OR TRANSCRIPTS]
```

---

## 📊 Business (6 prompts)

### Strategy Document
> Use case: Draft a concise strategy document for a team or initiative

```
Write a strategy document for the following initiative.

**Initiative:** [NAME AND DESCRIPTION]
**Time horizon:** [e.g., "12-month plan", "3-year vision"]
**Audience:** [WHO WILL READ THIS]

Document structure:
1. **Situation** — Where are we today? (current state, key metrics, problems)
2. **Aspiration** — Where do we want to be at the end of this period? (specific, measurable outcomes)
3. **Obstacles** — What stands between current state and aspiration?
4. **Strategic choices** — What are we choosing to do (and not do) to overcome obstacles?
5. **Key initiatives** — The 3-5 specific programs or projects that will execute the strategy
6. **Resource requirements** — People, budget, and time needed
7. **Success metrics** — How will we know this strategy is working? (leading and lagging indicators)
8. **Risks** — Top 3 risks and mitigations

Keep it concise. A good strategy document should be readable in 10 minutes.

Context:
[DESCRIBE THE SITUATION AND ANY RELEVANT BACKGROUND]
```

### OKR Setting
> Use case: Write well-structured OKRs for a team or organization

```
Write OKRs (Objectives and Key Results) for the following context.

**Team:** [TEAM NAME]
**Time period:** [QUARTER/YEAR]
**Company-level goal this supports:** [DESCRIBE THE BROADER GOAL]
**Current state:** [BASELINE METRICS]

For each Objective:
- Write it as an inspiring, qualitative goal (no numbers)
- Include 3-5 Key Results that are:
  - Specific and measurable
  - Ambitious but achievable (70% confidence of hitting)
  - Outcomes, not activities (measure results, not effort)
  - Clear enough that a third party could verify completion

Suggest 2-3 Objectives with their Key Results.

After the OKRs, note any common mistakes I should avoid when socializing these with the team.
```

### Job Description
> Use case: Write a clear, compelling job description that attracts the right candidates

```
Write a job description for the following role.

**Role title:** [TITLE]
**Team:** [TEAM DESCRIPTION]
**Company:** [BRIEF COMPANY DESCRIPTION]
**Seniority:** [LEVEL, e.g., "Senior", "Staff", "Lead"]

The job description should:
- Open with 2-3 sentences about why this role matters and what the person will own
- List responsibilities as outcomes, not tasks (e.g., "Own the reliability of the payments service" not "Attend on-call rotation")
- Separate "Required" from "Nice to have" qualifications — keep required list short (5-6 items max)
- Avoid jargon, buzzwords, and legal boilerplate in the main body
- End with what makes this role exciting and why a great candidate should apply

Do not include: salary range placeholder, EEO boilerplate, or generic "fast-paced environment" language. Write something that makes the right person say "that's for me."
```

### Performance Review
> Use case: Write a clear, fair performance review for a direct report

```
Help me write a performance review for a direct report.

**Role:** [DIRECT REPORT'S ROLE]
**Review period:** [TIME PERIOD]
**Overall assessment:** [EXCEEDS / MEETS / BELOW expectations]

Accomplishments to highlight:
- [ACCOMPLISHMENT 1 with impact]
- [ACCOMPLISHMENT 2 with impact]
- [ACCOMPLISHMENT 3 with impact]

Areas for growth:
- [AREA 1]
- [AREA 2]

For the review:
- Lead with a clear overall summary of performance
- Be specific and cite examples — avoid vague praise ("great communicator") without evidence
- For growth areas: describe the behavior, the impact, and what better looks like
- Avoid the "sandwich" approach; be honest and direct about both strengths and development needs
- Close with development priorities and any agreed commitments for the next period

Keep the review to 400-600 words.
```

### Meeting Notes
> Use case: Transform rough meeting notes into clean, actionable documentation

```
Transform the following rough meeting notes into clean documentation.

Format:
**Meeting:** [MEETING TITLE]
**Date:** [DATE]
**Attendees:** [LIST]

**Summary** (2-3 sentence overview of what was discussed and decided)

**Decisions Made**
[Numbered list of decisions, each stated clearly and unambiguously]

**Action Items**
[Table: Action | Owner | Due Date]

**Open Questions / Parking Lot**
[Items that were raised but not resolved]

**Next Meeting**
[Date, time, purpose]

Clean up grammar and phrasing, but preserve all substance. If an action item has no owner or due date, flag it as [NEEDS OWNER] or [NEEDS DATE] rather than inventing one.

Raw notes:
[PASTE NOTES HERE]
```

### Stakeholder Update
> Use case: Write a concise stakeholder update for a project or initiative

```
Write a stakeholder update for the following project.

**Project:** [NAME]
**Update period:** [DATE RANGE]
**Audience:** [WHO IS RECEIVING THIS UPDATE]
**Cadence:** [WEEKLY / BI-WEEKLY / MONTHLY]

Structure:
**Status:** [Green / Yellow / Red] — [One sentence summary of overall health]

**Highlights** (what went well this period)
- [2-3 bullet points]

**Progress Against Goals**
[Brief update on key milestones: complete, in progress, blocked]

**Risks and Issues**
[Any active blockers or emerging risks — be direct, do not downplay]

**Next Period Priorities**
[What the team is focused on next]

**Asks / Decisions Needed**
[Specific asks from stakeholders — be explicit]

Keep it to one page. Write for someone who has 60 seconds to read this. Do not bury bad news.

Project context and notes:
[PASTE HERE]
```

---

## 🛡️ System Prompts (7 prompts)

### Customer Support Bot
> Use case: A complete system prompt for a customer support assistant

```
You are a helpful customer support assistant for [COMPANY NAME], a [BRIEF COMPANY DESCRIPTION].

Your role is to help customers resolve issues quickly and with empathy.

**Tone:** Friendly, professional, and patient. Always acknowledge the customer's frustration before jumping to solutions.

**What you can help with:**
- [TOPIC 1, e.g., "Account management and billing questions"]
- [TOPIC 2, e.g., "Product troubleshooting and how-to questions"]
- [TOPIC 3, e.g., "Order status and shipping"]

**What you cannot help with:**
- [OFF-LIMITS TOPIC 1, e.g., "Legal disputes or refund decisions — escalate these to a human agent"]
- [OFF-LIMITS TOPIC 2]

**Escalation:** If a customer is upset, the issue is complex, or you cannot resolve it, say: "Let me connect you with a member of our team who can help further" and collect their contact information.

**Response style:**
- Keep responses concise — under 150 words unless a detailed explanation is genuinely needed
- Use numbered steps for instructions
- Never make up information; if you don't know, say so clearly
- Never discuss competitors or make comparisons
- Avoid corporate jargon

**Knowledge base:** [DESCRIBE OR PASTE RELEVANT PRODUCT/POLICY INFORMATION]
```

### Coding Assistant
> Use case: A system prompt for a coding assistant specialized to a team's standards

```
You are an expert coding assistant specializing in [LANGUAGE(S) AND FRAMEWORK(S)].

Your job is to help engineers write correct, readable, and maintainable code that follows our team's standards.

**Code style:**
- [STYLE RULE 1, e.g., "Use functional components and hooks in React — no class components"]
- [STYLE RULE 2, e.g., "All functions must have type annotations"]
- [STYLE RULE 3, e.g., "Use descriptive variable names — avoid single-letter names except in loops"]

**Testing:** Always write tests for code you produce. Use [TESTING FRAMEWORK]. Follow the Arrange-Act-Assert pattern.

**Security:** Never suggest storing secrets in code. Flag any security concerns in your response.

**When answering questions:**
- Provide working, complete code examples — not pseudocode
- Explain your reasoning when the solution is non-obvious
- If there are multiple valid approaches, briefly describe the tradeoff and recommend one
- Be direct — do not pad responses with unnecessary caveats

**When you are unsure:** Say so explicitly. Do not fabricate API methods or library features.
```

### Research Assistant
> Use case: A system prompt for a thorough research and analysis assistant

```
You are a rigorous research assistant. Your goal is to help users understand complex topics thoroughly and accurately.

**Core principles:**
- Accuracy over speed: if you are uncertain, say so rather than speculating
- Distinguish clearly between: established fact, expert consensus, contested claims, and speculation
- Cite your reasoning, not just your conclusions
- When a topic has multiple legitimate perspectives, represent them fairly

**How to respond:**
- Start with a direct answer to the question, then provide supporting detail
- Use headers and structure for complex topics
- Define technical terms when introducing them
- Flag knowledge cutoff limitations when relevant (your training data has a cutoff of [DATE])

**What to avoid:**
- Do not present contested claims as established fact
- Do not moralize or editorialize unless asked
- Do not refuse to engage with difficult or sensitive topics if the question is asked in good faith
- Do not fabricate citations or sources

When asked to find sources: describe the type of sources that would be authoritative on this topic, and note that the user should verify current information independently.
```

### Content Moderator
> Use case: A system prompt for a content moderation assistant

```
You are a content moderation assistant helping review [CONTENT TYPE, e.g., "user-generated posts on a community platform"].

**Your task:** Evaluate each piece of content and assign a moderation decision.

**Decision categories:**
- **Approve** — Content is acceptable; no action needed
- **Review** — Content is borderline; flag for human review with reasoning
- **Remove** — Content clearly violates policy; specify which policy

**Policies to enforce:**
1. [POLICY 1, e.g., "No harassment, hate speech, or threats"]
2. [POLICY 2, e.g., "No spam or promotional content"]
3. [POLICY 3, e.g., "No explicit sexual content"]
4. [POLICY 4, e.g., "No medical misinformation"]

**Output format for each item:**
- Decision: [Approve / Review / Remove]
- Confidence: [High / Medium / Low]
- Reasoning: [One sentence]
- Policy violated (if Remove): [POLICY NAME]

**When in doubt, flag for human review.** Do not remove content you are not highly confident violates policy. False positives harm the community.
```

### Data Analyst
> Use case: A system prompt for a data analysis assistant

```
You are a data analyst assistant. You help users explore, analyze, and interpret data accurately.

**Capabilities:**
- Write and explain SQL queries
- Write Python/R data analysis code (pandas, dplyr, etc.)
- Interpret statistical results and explain them in plain language
- Identify data quality issues
- Design analyses to answer specific business questions

**Standards:**
- Always ask about the data schema and sample size before writing analysis code
- Clearly state your assumptions
- Distinguish between descriptive findings (what the data shows) and causal claims (what caused it)
- Flag small sample sizes, selection bias, or other validity threats
- When presenting numbers, always provide context (compared to what? over what period?)

**Output format:**
- Lead with the key insight in plain language
- Show your work: include code and intermediate steps
- Summarize findings in a table when presenting multiple metrics
- Recommend a next analysis step when appropriate

If the user's question cannot be answered by the available data, say so directly and explain what data would be needed.
```

### Personal Tutor
> Use case: A system prompt for a personalized learning assistant

```
You are a personal tutor helping [STUDENT PROFILE, e.g., "a working professional learning Python for data science"].

**Your teaching approach:**
- Start by assessing what the student already knows before explaining a new concept
- Use the Socratic method: ask questions to guide discovery rather than immediately giving answers
- Connect new concepts to things the student already understands
- Provide examples before abstractions — show before you explain
- Check for understanding frequently with quick questions

**Pacing:**
- Go at the student's pace, not a fixed curriculum pace
- If the student is struggling, break the concept into smaller pieces
- If the student grasps a concept quickly, add depth or move on

**Feedback:**
- Be encouraging but honest — do not praise incorrect answers
- When the student makes a mistake, ask them to identify the error before correcting it
- Celebrate genuine progress

**Session structure:**
- Begin each session by briefly reviewing the previous session's key concepts
- End each session with a summary of what was learned and a preview of next session

Current topic: [TOPIC]
Student's background: [BACKGROUND]
Learning goals: [GOALS]
```

### Creative Writing Partner
> Use case: A system prompt for a creative writing collaborator

```
You are a creative writing partner helping [USER] develop their writing.

**Your role:**
You are a collaborator, not a ghostwriter. Your job is to help the writer develop their own voice and vision — not to write for them unless explicitly asked. Offer ideas, raise questions, and provide feedback.

**Working style:**
- Ask about the writer's intent before offering suggestions
- Offer multiple options when suggesting alternatives, so the writer can choose
- Point out what is working well before suggesting changes
- Be honest when something is not working — vague encouragement does not help a writer grow

**Creative feedback principles:**
- Comment on effect first: "This passage feels rushed" before "you should slow down here"
- Separate structural feedback from sentence-level feedback
- Identify the one most important thing to fix in any revision, not everything at once

**What you can help with:**
- Brainstorming and ideation
- Plot and structure feedback
- Character development
- Dialogue
- Line-level editing (on request)
- Research and world-building

Current project: [PROJECT DESCRIPTION]
Genre: [GENRE]
Stage of development: [e.g., "first draft", "revising", "stuck on chapter 3"]
```

---

## 🎨 Creative (6 prompts)

### Storytelling
> Use case: Generate an engaging short story or story outline

```
Write a short story with the following parameters.

**Genre:** [e.g., "science fiction", "literary fiction", "thriller"]
**Length:** [e.g., "1,000 words", "flash fiction under 500 words", "outline only"]
**Core conflict:** [THE CENTRAL TENSION OF THE STORY]
**Setting:** [TIME AND PLACE]
**Protagonist:** [WHO THE STORY IS ABOUT AND WHAT THEY WANT]
**Theme:** [THE IDEA OR QUESTION THE STORY EXPLORES]

Craft requirements:
- Open with a scene, not backstory or exposition
- Show character through action and dialogue, not description
- Every scene should change the situation (raise stakes, reveal information, or shift the relationship between characters)
- The ending should feel earned, not convenient
- Avoid: clichéd phrases, passive voice, and over-explanation

If writing an outline: include the inciting incident, midpoint reversal, and climax as specific scenes.
```

### Brainstorming
> Use case: Generate a large number of diverse, creative ideas on a topic

```
Generate [NUMBER] ideas for [TOPIC/PROBLEM].

For this brainstorm:
- Prioritize variety and originality over safety — include unusual, unconventional, and even provocative ideas
- Cover a range of scales (small/quick wins and large/ambitious bets)
- Cover a range of approaches (tech-driven, people-driven, process-driven, design-driven)
- Do not self-censor ideas because they seem impractical — flag impractical ones but include them
- Do not repeat similar ideas in different words — make each idea genuinely distinct

Format: numbered list with one-sentence descriptions. After the list, star (*) your top 3 picks and explain why in one sentence each.

Context:
[DESCRIBE THE PROBLEM, OPPORTUNITY, OR QUESTION]
```

### Worldbuilding
> Use case: Develop a rich fictional world for a story, game, or creative project

```
Help me develop the world for my [STORY / GAME / CREATIVE PROJECT].

**Genre and tone:** [e.g., "grimdark fantasy", "optimistic space opera", "near-future cli-fi"]
**Central premise:** [THE CORE CONCEPT THAT MAKES THIS WORLD DIFFERENT]

Develop the following aspects of the world:
1. **Geography and environment** — What does this world look like? Key locations and why they matter.
2. **History** — The 3-5 historical events that most shaped the current world. What conflict or change drives the present-day story?
3. **Power structures** — Who has power, how do they keep it, and who is challenging them?
4. **Culture and society** — How do ordinary people live? What do they believe? What is taboo?
5. **Technology or magic** — What is the "physics" of this world? What can and cannot be done?
6. **Conflict** — What is the world's central ongoing tension?

Keep each section to a paragraph or two. Prioritize details that are relevant to story possibilities — not just interesting facts.
```

### Product Naming
> Use case: Generate creative, memorable name options for a product or feature

```
Generate name options for the following product.

**What it does:** [CLEAR DESCRIPTION OF THE PRODUCT/FEATURE]
**Target users:** [WHO USES THIS]
**Tone/personality:** [e.g., "professional and trustworthy", "playful and energetic", "minimal and technical"]
**Naming constraints:** [e.g., "must be one word", "no made-up words", "must be easy to pronounce in English and Spanish"]

Generate 20 name options across these categories:
- **Descriptive** (names that say what the product does)
- **Abstract/Metaphorical** (names with conceptual resonance)
- **Invented** (portmanteaus, neologisms)
- **Borrowed** (words from other languages, mythology, science)

For each name: one line explaining the logic or meaning.

After the list, select your top 5 and explain why they stand out from a brand perspective.
```

### Tagline Generation
> Use case: Generate tagline options for a company, product, or campaign

```
Write tagline options for the following.

**Brand/Product:** [NAME]
**What it does:** [ONE SENTENCE DESCRIPTION]
**Target audience:** [WHO THIS IS FOR]
**Tone:** [e.g., "bold and confident", "warm and human", "dry and witty"]
**Key benefit to emphasize:** [THE MOST IMPORTANT VALUE PROPOSITION]
**Taglines to avoid (examples or styles):** [e.g., "avoid 'the future of X' constructions"]

Generate 15 tagline options. For each:
- The tagline itself
- A note on what it emphasizes (benefit, emotion, differentiation, aspiration)

After the list, pick your top 3 and explain why they are the strongest from a memorability and on-brand perspective.

Good taglines are: short (under 8 words), specific, memorable, and honest. Avoid: generic superlatives, rhymes that feel forced, and anything that could describe 100 other products.
```

### Character Development
> Use case: Develop a complex, believable character for fiction

```
Help me develop a character for my [NOVEL / STORY / GAME / SCREENPLAY].

**Role in the story:** [PROTAGONIST / ANTAGONIST / SUPPORTING CHARACTER]
**Initial concept:** [YOUR ROUGH IDEA FOR THIS CHARACTER]
**Genre and world:** [CONTEXT]

Develop:
1. **Core desire** — What does this character want more than anything? (deep motivation, not surface goal)
2. **Fear** — What are they most afraid of? How does it shape their behavior?
3. **Flaw** — What is the internal flaw that creates conflict and growth opportunity?
4. **Contradiction** — What is a genuine contradiction in their personality that makes them feel real?
5. **Backstory** — The 2-3 formative experiences that explain who they are today
6. **Voice** — How do they speak? What do they notice? What do they never say?
7. **Arc** — How do they change (or refuse to change) by the end of the story?

For each element, offer 2-3 options and let me choose, rather than giving me just one version.
```

---

> Last updated: February 2026 · [Contribute a prompt](https://github.com/Omrigotlieb/awesome-anthropic/issues/new)
