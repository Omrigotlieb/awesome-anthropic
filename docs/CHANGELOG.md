# Anthropic Changelog Mirror

### 2026-02-19: We've launched automatic caching for the Messages API. Add a single cache_contro...

We've launched automatic caching for the Messages API. Add a single cache_control field to your request body and the system automatically caches the last cacheable block, moving the cache point forward as conversations grow. No manual breakpoint management required. Works alongside existing block-level cache control for fine-grained optimization. Available on the Claude API and Azure AI Foundry (preview). Learn more in our prompt caching documentation . 
 We've retired the Claude Sonnet 3.7 model ( claude-3-7-sonnet-20250219 ) and the Claude Haiku 3.5 model ( claude-3-5-haiku-20241022 ). All requests to these models will now return an error. We recommend upgrading to Claude Sonnet 4.6 and Claude Haiku 4.5 respectively. Researchers can request ongoing access through the External Researcher Access Program . 
 We announced the deprecation of the Claude Haiku 3 model ( claude-3-haiku-20240307 ), with retirement scheduled for

### 2026-04-19: . We recommend migrating to Claude Haiku 4.5 . Read more in model deprecations .

. We recommend migrating to Claude Haiku 4.5 . Read more in model deprecations .

### 2026-02-17: We've launched Claude Sonnet 4.6 , our latest balanced model combining speed and...

We've launched Claude Sonnet 4.6 , our latest balanced model combining speed and intelligence for everyday tasks. Sonnet 4.6 delivers improved agentic search performance while consuming fewer tokens. Sonnet 4.6 supports extended thinking and a 1M token context window (beta). See Models & Pricing for details. 
 API code execution is now free when used with web search or web fetch . Sandboxed code execution improves model capability and token efficiency. See the pricing details for standalone usage. 
 The web search tool and programmatic tool calling are now generally available (no beta header required). Web search and web fetch now support dynamic filtering , which uses code execution to filter results before they reach the context window for better performance and reduced token cost. 
 The code execution tool , web fetch tool , tool search tool , tool use examples , and memory tool are now generally available (no beta header required).

### 2026-02-07: We've launched fast mode in research preview for Opus 4.6, providing significant...

We've launched fast mode in research preview for Opus 4.6, providing significantly faster output token generation via the speed parameter. Fast mode is up to 2.5x as fast at premium pricing. Interested customers should join the waitlist .

### 2026-02-05: We've launched Claude Opus 4.6 , our most intelligent model for complex agentic ...

We've launched Claude Opus 4.6 , our most intelligent model for complex agentic tasks and long-horizon work. Opus 4.6 recommends adaptive thinking ( thinking: {type: "adaptive"} ); manual thinking ( type: "enabled" with budget_tokens ) is deprecated. Opus 4.6 does not support prefilling assistant messages. Learn more in What's new in Claude 4.6 . 
 The effort parameter is now generally available (no beta header required) and supports Claude Opus 4.6. Effort replaces budget_tokens for controlling thinking depth on new models. 
 We've launched the compaction API in beta, providing server-side context summarization for effectively infinite conversations. Available on Opus 4.6. 
 We've introduced data residency controls , allowing you to specify where model inference runs with the inference_geo parameter. US-only inference is available at 1.1x pricing for models released after

### 2026-02-01: .

. 
 The 1M token context window is now available in beta for Claude Opus 4.6, in addition to Sonnet 4.5 and Sonnet 4. Long context pricing applies to requests exceeding 200K input tokens. 
 Fine-grained tool streaming is now generally available on all models and platforms (no beta header required). The output_format parameter for structured outputs has been moved to output_config.format .

### 2026-01-29: Structured outputs are now generally available on the Claude API for Claude Sonn...

Structured outputs are now generally available on the Claude API for Claude Sonnet 4.5, Claude Opus 4.5, and Claude Haiku 4.5. GA includes expanded schema support, improved grammar compilation latency, and a simplified integration path with no beta header required. The output_format parameter has moved to output_config.format . Existing beta users can continue using the beta header during the transition period. Structured outputs remain in public beta on Amazon Bedrock and Microsoft Foundry.

### 2026-01-12: console.anthropic.com now redirects to platform.claude.com . The Claude Console ...

console.anthropic.com now redirects to platform.claude.com . The Claude Console has moved to its new home as part of our Claude brand consolidation. Existing bookmarks and links will continue working via automatic redirect. For more details, see the

### 2026-01-05: We've retired the Claude Opus 3 model ( claude-3-opus-20240229 ). All requests t...

We've retired the Claude Opus 3 model ( claude-3-opus-20240229 ). All requests to this model will now return an error. We recommend upgrading to Claude Opus 4.5 , which offers significantly improved intelligence at a third of the cost. Researchers can request ongoing access to Claude Opus 3 on the API through the External Researcher Access Program .

### 2025-12-19: We announced the deprecation of the Claude Haiku 3.5 model. Read more in our doc...

We announced the deprecation of the Claude Haiku 3.5 model. Read more in our documentation .

### 2025-11-24: We've launched Claude Opus 4.5 , our most intelligent model combining maximum ca...

We've launched Claude Opus 4.5 , our most intelligent model combining maximum capability with practical performance. Ideal for complex specialized tasks, professional software engineering, and advanced agents. Features step-change improvements in vision, coding, and computer use at a more accessible price point than previous Opus models. Learn more in our Models & Pricing documentation . 
 We've launched programmatic tool calling in public beta, allowing Claude to call tools from within code execution to reduce latency and token usage in multi-tool workflows. 
 We've launched the tool search tool in public beta, enabling Claude to dynamically discover and load tools on-demand from large tool catalogs. 
 We've launched the effort parameter in public beta for Claude Opus 4.5, allowing you to control token usage by trading off between response thoroughness and efficiency. 
 We've added client-side compaction to our Python and TypeScript SDKs, automatically managing conversation context through summarization when using tool_runner .

### 2025-11-21: Search result content blocks are now generally available on Amazon Bedrock. Lear...

Search result content blocks are now generally available on Amazon Bedrock. Learn more in our search results documentation .

### 2025-11-19: We've launched a new documentation platform at platform.claude.com/docs . Our do...

We've launched a new documentation platform at platform.claude.com/docs . Our documentation now lives side by side with the Claude Console, providing a unified developer experience. The previous docs site at docs.claude.com will redirect to the new location.

### 2025-11-18: We've launched Claude in Microsoft Foundry , bringing Claude models to Azure cus...

We've launched Claude in Microsoft Foundry , bringing Claude models to Azure customers with Azure billing and OAuth authentication. Access the full Messages API including extended thinking, prompt caching (5-minute and 1-hour), PDF support, Files API, Agent Skills, and tool use. Learn more in our Microsoft Foundry documentation .

### 2025-11-14: We've launched structured outputs in public beta, providing guaranteed schema co...

We've launched structured outputs in public beta, providing guaranteed schema conformance for Claude's responses. Use JSON outputs for structured data responses or strict tool use for validated tool inputs. Available for Claude Sonnet 4.5 and Claude Opus 4.1. To enable, use the beta header structured-outputs-2025-11-13 .

### 2025-10-28: We announced the deprecation of the Claude Sonnet 3.7 model. Read more in our do...

We announced the deprecation of the Claude Sonnet 3.7 model. Read more in our documentation . 
 We've retired the Claude Sonnet 3.5 models. All requests to these models will now return an error. 
 We've expanded context editing with thinking block clearing ( clear_thinking_20251015 ), enabling automatic management of thinking blocks. Learn more in our context editing documentation .

### 2025-10-16: We've launched Agent Skills ( skills-2025-10-02 beta), a new way to extend Claud...

We've launched Agent Skills ( skills-2025-10-02 beta), a new way to extend Claude's capabilities. Skills are organized folders of instructions, scripts, and resources that Claude loads dynamically to perform specialized tasks. The initial release includes: 
 
 Anthropic-managed Skills : Pre-built Skills for working with PowerPoint (.pptx), Excel (.xlsx), Word (.docx), and PDF files 
 Custom Skills : Upload your own Skills via the Skills API ( /v1/skills endpoints) to package domain expertise and organizational workflows 
 Skills require the code execution tool to be enabled 
 Learn more in our Agent Skills documentation and API reference

### 2025-10-15: We've launched Claude Haiku 4.5 , our fastest and most intelligent Haiku model w...

We've launched Claude Haiku 4.5 , our fastest and most intelligent Haiku model with near-frontier performance. Ideal for real-time applications, high-volume processing, and cost-sensitive deployments requiring strong reasoning. Learn more in our Models & Pricing documentation .

### 2025-09-29: We've launched Claude Sonnet 4.5 , our best model for complex agents and coding,...

We've launched Claude Sonnet 4.5 , our best model for complex agents and coding, with the highest intelligence across most tasks. Learn more in the models overview . 
 We've introduced global endpoint pricing for AWS Bedrock and Google Vertex AI. The Claude API (1P) pricing is unaffected. 
 We've introduced a new stop reason model_context_window_exceeded that allows you to request the maximum possible tokens without calculating input size. Learn more in our handling stop reasons documentation . 
 We've launched the memory tool in beta, enabling Claude to store and consult information across conversations. Learn more in our memory tool documentation . 
 We've launched context editing in beta, providing strategies to automatically manage conversation context. The initial release supports clearing older tool results and calls when approaching token limits. Learn more in our context editing documentation .

### 2025-09-16: We've unified our developer offerings under the Claude brand. You should see upd...

We've unified our developer offerings under the Claude brand. You should see updated naming and URLs across our platform and documentation, but our developer interfaces will remain the same . Here are some notable changes: 
 
 Claude Console ( console.anthropic.com ) → Claude Console ( platform.claude.com ). The console will be available at both URLs until

---

### 2026-02-19: We've launched

We've launched 
automatic caching
 for the Messages API. Add a single 
cache_control
 field to your request body and the system automatically caches the last cacheable block, moving the cache point forward as conversations grow. No manual breakpoint management required. Works alongside existing block-level cache control for fine-grained optimization. Available on the Claude API and Azure AI Foundry (preview). Learn more in our 
prompt caching documentation
.


We've retired the Claude Sonnet 3.7 model (
claude-3-7-sonnet-20250219
) and the Claude Haiku 3.5 model (
claude-3-5-haiku-20241022
). All requests to these models will now return an error. We recommend upgrading to 
Claude Sonnet 4.6
 and 
Claude Haiku 4.5
 respectively. Researchers can request ongoing access through the 
External Researcher Access Program
.


We announced the deprecation of the Claude Haiku 3 model (
claude-3-haiku-20240307
), with retirement scheduled for

### 2026-04-19: . We recommend migrating to

. We recommend migrating to 
Claude Haiku 4.5
. Read more in 
model deprecations
.

### 2026-02-17: We've launched

We've launched 
Claude Sonnet 4.6
, our latest balanced model combining speed and intelligence for everyday tasks. Sonnet 4.6 delivers improved agentic search performance while consuming fewer tokens. Sonnet 4.6 supports 
extended thinking
 and a 
1M token context window
 (beta). See 
Models & Pricing
 for details.


API 
code execution
 is now 
free when used with web search or web fetch
. Sandboxed code execution improves model capability and token efficiency. See the 
pricing details
 for standalone usage.


The 
web search tool
 and 
programmatic tool calling
 are now generally available (no beta header required). Web search and web fetch now support 
dynamic filtering
, which uses code execution to filter results before they reach the context window for better performance and reduced token cost.


The 
code execution tool
, 
web fetch tool
, 
tool search tool
, 
tool use examples
, and 
memory tool
 are now generally available (no beta header required).

### 2026-02-07: We've launched

We've launched 
fast mode
 in research preview for Opus 4.6, providing significantly faster output token generation via the 
speed
 parameter. Fast mode is up to 2.5x as fast at premium pricing. Interested customers should join the 
waitlist
.

### 2026-02-05: We've launched

We've launched 
Claude Opus 4.6
, our most intelligent model for complex agentic tasks and long-horizon work. Opus 4.6 recommends 
adaptive thinking
 (
thinking: {type: "adaptive"}
); manual thinking (
type: "enabled"
 with 
budget_tokens
) is deprecated. Opus 4.6 does not support prefilling assistant messages. Learn more in 
What's new in Claude 4.6
.


The 
effort parameter
 is now generally available (no beta header required) and supports Claude Opus 4.6. Effort replaces 
budget_tokens
 for controlling thinking depth on new models.


We've launched the 
compaction API
 in beta, providing server-side context summarization for effectively infinite conversations. Available on Opus 4.6.


We've introduced 
data residency controls
, allowing you to specify where model inference runs with the 
inference_geo
 parameter. US-only inference is available at 1.1x pricing for models released after

### 2026-02-01: .

.


The 
1M token context window
 is now available in beta for Claude Opus 4.6, in addition to Sonnet 4.5 and Sonnet 4. 
Long context pricing
 applies to requests exceeding 200K input tokens.


Fine-grained tool streaming
 is now generally available on all models and platforms (no beta header required). The 
output_format
 parameter for 
structured outputs
 has been moved to 
output_config.format
.

### 2026-01-29: Structured outputs

Structured outputs
 are now generally available on the Claude API for Claude Sonnet 4.5, Claude Opus 4.5, and Claude Haiku 4.5. GA includes expanded schema support, improved grammar compilation latency, and a simplified integration path with no beta header required. The 
output_format
 parameter has moved to 
output_config.format
. Existing beta users can continue using the beta header during the transition period. Structured outputs remain in public beta on Amazon Bedrock and Microsoft Foundry.

### 2026-01-12: console.anthropic.com

console.anthropic.com
 now redirects to 
platform.claude.com
. The Claude Console has moved to its new home as part of our Claude brand consolidation. Existing bookmarks and links will continue working via automatic redirect. For more details, see the

### 2026-01-05: We've retired the Claude Opus 3 model (

We've retired the Claude Opus 3 model (
claude-3-opus-20240229
). All requests to this model will now return an error. We recommend upgrading to 
Claude Opus 4.5
, which offers significantly improved intelligence at a third of the cost. Researchers can request ongoing access to Claude Opus 3 on the API through the 
External Researcher Access Program
.

### 2025-12-19: We announced the deprecation of the Claude Haiku 3.5 model. Read more in

We announced the deprecation of the Claude Haiku 3.5 model. Read more in 
our documentation
.

### 2025-12-04: Structured outputs

Structured outputs
 now supports Claude Haiku 4.5.

### 2025-11-24: We've launched

We've launched 
Claude Opus 4.5
, our most intelligent model combining maximum capability with practical performance. Ideal for complex specialized tasks, professional software engineering, and advanced agents. Features step-change improvements in vision, coding, and computer use at a more accessible price point than previous Opus models. Learn more in our 
Models & Pricing documentation
.


We've launched 
programmatic tool calling
 in public beta, allowing Claude to call tools from within code execution to reduce latency and token usage in multi-tool workflows.


We've launched the 
tool search tool
 in public beta, enabling Claude to dynamically discover and load tools on-demand from large tool catalogs.


We've launched the 
effort parameter
 in public beta for Claude Opus 4.5, allowing you to control token usage by trading off between response thoroughness and efficiency.


We've added 
client-side compaction
 to our Python and TypeScript SDKs, automatically managing conversation context through summarization when using 
tool_runner
.

### 2025-11-21: Search result content blocks are now generally available on Amazon Bedrock. Lear...

Search result content blocks are now generally available on Amazon Bedrock. Learn more in our 
search results documentation
.

### 2025-11-19: We've launched a

We've launched a 
new documentation platform
 at 
platform.claude.com/docs
. Our documentation now lives side by side with the Claude Console, providing a unified developer experience. The previous docs site at docs.claude.com will redirect to the new location.

### 2025-11-18: We've launched

We've launched 
Claude in Microsoft Foundry
, bringing Claude models to Azure customers with Azure billing and OAuth authentication. Access the full Messages API including extended thinking, prompt caching (5-minute and 1-hour), PDF support, Files API, Agent Skills, and tool use. Learn more in our 
Microsoft Foundry documentation
.

### 2025-11-14: We've launched

We've launched 
structured outputs
 in public beta, providing guaranteed schema conformance for Claude's responses. Use JSON outputs for structured data responses or strict tool use for validated tool inputs. Available for Claude Sonnet 4.5 and Claude Opus 4.1. To enable, use the beta header 
structured-outputs-2025-11-13
.

### 2025-10-28: We announced the deprecation of the Claude Sonnet 3.7 model. Read more in

We announced the deprecation of the Claude Sonnet 3.7 model. Read more in 
our documentation
.


We've retired the Claude Sonnet 3.5 models. All requests to these models will now return an error.


We've expanded context editing with thinking block clearing (
clear_thinking_20251015
), enabling automatic management of thinking blocks. Learn more in our 
context editing documentation
.

### 2025-10-16: We've launched

We've launched 
Agent Skills
 (
skills-2025-10-02
 beta), a new way to extend Claude's capabilities. Skills are organized folders of instructions, scripts, and resources that Claude loads dynamically to perform specialized tasks. The initial release includes:




Anthropic-managed Skills
: Pre-built Skills for working with PowerPoint (.pptx), Excel (.xlsx), Word (.docx), and PDF files


Custom Skills
: Upload your own Skills via the Skills API (
/v1/skills
 endpoints) to package domain expertise and organizational workflows


Skills require the 
code execution tool
 to be enabled


Learn more in our 
Agent Skills documentation
 and 
API reference

### 2025-10-15: We've launched

We've launched 
Claude Haiku 4.5
, our fastest and most intelligent Haiku model with near-frontier performance. Ideal for real-time applications, high-volume processing, and cost-sensitive deployments requiring strong reasoning. Learn more in our 
Models & Pricing documentation
.

### 2025-09-29: We've launched

We've launched 
Claude Sonnet 4.5
, our best model for complex agents and coding, with the highest intelligence across most tasks. Learn more in the 
models overview
.


We've introduced 
global endpoint pricing
 for AWS Bedrock and Google Vertex AI. The Claude API (1P) pricing is unaffected.


We've introduced a new stop reason 
model_context_window_exceeded
 that allows you to request the maximum possible tokens without calculating input size. Learn more in our 
handling stop reasons documentation
.


We've launched the memory tool in beta, enabling Claude to store and consult information across conversations. Learn more in our 
memory tool documentation
.


We've launched context editing in beta, providing strategies to automatically manage conversation context. The initial release supports clearing older tool results and calls when approaching token limits. Learn more in our 
context editing documentation
.

---

### 2026-02-26: Solutions

AI agents
Code modernization
Coding
Customer support
Education
Financial services
Government
Life sciences

### 2026-02-26: Partners

Amazon Bedrock
Google Cloud's Vertex AI

### 2026-02-26: Learn

Blog
Catalog
Courses
Use cases
Connectors
Customer stories
Engineering at Anthropic
Events
Powered by Claude
Service partners
Startups program

### 2026-02-26: Company

Anthropic
Careers
Economic Futures
Research
News
Responsible Scaling Policy
Security and compliance
Transparency

### 2026-02-26: Learn

Blog
Catalog
Courses
Use cases
Connectors
Customer stories
Engineering at Anthropic
Events
Powered by Claude
Service partners
Startups program

### 2026-02-26: Help and security

Availability
Status
Support
Discord

### 2026-02-26: Terms and policies

Privacy policy
Responsible disclosure policy
Terms of service: Commercial
Terms of service: Consumer
Usage policy

---

> Auto-synced from [docs.anthropic.com/en/release-notes](https://docs.anthropic.com/en/release-notes/overview)
> Last sync: _pending first run_

This file is automatically updated every 6 hours by the [changelog-check workflow](../.github/workflows/changelog-check.yml).

To manually trigger a sync:

```bash
python scripts/check_changelog.py
```
