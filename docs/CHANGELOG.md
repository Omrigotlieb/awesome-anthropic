# Anthropic Changelog

> Auto-synced from [https://docs.anthropic.com/en/release-notes/overview](https://docs.anthropic.com/en/release-notes/overview). Updated 2026-04-08T06:00:34Z

---

## April 7, 2026 — We announced Claude Mythos Preview is available as a gated research preview for 

We announced Claude Mythos Preview is available as a gated research preview for defensive cybersecurity work as part of Project Glasswing . Access is invitation-only. 
 The Messages API is now available on Amazon Bedrock as a research preview. The new Claude in Amazon Bedrock endpoint at /anthropic/v1/messages uses the same request shape as the first-party Claude API and runs on AWS-managed infrastructure with zero operator access. Available in us-east-1 ; contact your Anthropic account executive to request access. Learn more in Claude in Amazon Bedrock .

---

## March 30, 2026 — We've raised the max_tokens cap to 300k on the Message Batches API for Claude Op

We've raised the max_tokens cap to 300k on the Message Batches API for Claude Opus 4.6 and Sonnet 4.6. Include the output-300k-2026-03-24 beta header to generate longer single-turn outputs for long-form content, structured data, and large code generation tasks. 
 We're retiring the 1M token context window beta for Claude Sonnet 4.5 and Claude Sonnet 4 on

---

## April 30, 2026 — . After that date, the context-1m-2025-08-07 beta header will have no effect on 

. After that date, the context-1m-2025-08-07 beta header will have no effect on these models, and requests that exceed the standard 200k-token context window will return an error. To continue using 1M context windows, migrate to Claude Sonnet 4.6 or Claude Opus 4.6 , which support the full 1M token context window at standard pricing with no beta header required.

---

## March 18, 2026 — We've added model capability fields to the Models API . GET /v1/models and GET /

We've added model capability fields to the Models API . GET /v1/models and GET /v1/models/{model_id} now return max_input_tokens , max_tokens , and a capabilities object. Query the API to discover what each model supports.

---

## March 16, 2026 — We've launched the display field for extended thinking, letting you omit thinkin

We've launched the display field for extended thinking, letting you omit thinking content from responses for faster streaming. Set thinking.display: "omitted" to receive thinking blocks with an empty thinking field and the signature preserved for multi-turn continuity. Billing is unchanged. Learn more in Controlling thinking display .

---

## March 13, 2026 — The 1M token context window is now generally available for Claude Opus 4.6 and S

The 1M token context window is now generally available for Claude Opus 4.6 and Sonnet 4.6 at standard pricing. Requests over 200k tokens work automatically for these models with no beta header required. The 1M token context window remains in beta for Claude Sonnet 4.5 and Sonnet 4. 
 We've removed the dedicated 1M rate limits for all supported models. Your standard account limits now apply across every context length. 
 We've raised the media limit from 100 to 600 images or PDF pages per request when using the 1M token context window.

---

## February 19, 2026 — We've launched automatic caching for the Messages API. Add a single cache_contro

We've launched automatic caching for the Messages API. Add a single cache_control field to your request body and the system automatically caches the last cacheable block, moving the cache point forward as conversations grow. No manual breakpoint management required. Works alongside existing block-level cache control for fine-grained optimization. Available on the Claude API and Azure AI Foundry (preview). Learn more in Prompt caching . 
 We've retired the Claude Sonnet 3.7 model ( claude-3-7-sonnet-20250219 ) and the Claude Haiku 3.5 model ( claude-3-5-haiku-20241022 ). All requests to these models will now return an error. We recommend upgrading to Claude Sonnet 4.6 and Claude Haiku 4.5 respectively. Researchers can request ongoing access through the External Researcher Access Program . 
 We announced the deprecation of the Claude Haiku 3 model ( claude-3-haiku-20240307 ), with retirement scheduled for

---

## April 19, 2026 — . We recommend migrating to Claude Haiku 4.5 . Read more in model deprecations 

. We recommend migrating to Claude Haiku 4.5 . Read more in model deprecations .

---

## February 17, 2026 — We've launched Claude Sonnet 4.6 , our latest balanced model combining speed and

We've launched Claude Sonnet 4.6 , our latest balanced model combining speed and intelligence for everyday tasks. Sonnet 4.6 delivers improved agentic search performance while consuming fewer tokens. Sonnet 4.6 supports extended thinking and a 1M token context window (beta). See Models & Pricing for details. 
 API code execution is now free when used with web search or web fetch . Sandboxed code execution improves model capability and token efficiency. See the pricing details for standalone usage. 
 The web search tool and programmatic tool calling are now generally available (no beta header required). Web search and web fetch now support dynamic filtering , which uses code execution to filter results before they reach the context window for better performance and reduced token cost. 
 The code execution tool , web fetch tool , tool search tool , tool use examples , and memory tool are now generally available (no beta header required).

---

## February 7, 2026 — We've launched fast mode in research preview for Opus 4.6, providing significant

We've launched fast mode in research preview for Opus 4.6, providing significantly faster output token generation via the speed parameter. Fast mode is up to 2.5x as fast at premium pricing. Interested customers should join the waitlist .

---

## February 5, 2026 — We've launched Claude Opus 4.6 , our most intelligent model for complex agentic 

We've launched Claude Opus 4.6 , our most intelligent model for complex agentic tasks and long-horizon work. Opus 4.6 recommends adaptive thinking ( thinking: {type: "adaptive"} ); manual thinking ( type: "enabled" with budget_tokens ) is deprecated. Opus 4.6 does not support prefilling assistant messages. Learn more in What's new in Claude 4.6 . 
 The effort parameter is now generally available (no beta header required) and supports Claude Opus 4.6. Effort replaces budget_tokens for controlling thinking depth on new models. 
 We've launched the compaction API in beta, providing server-side context summarization for effectively infinite conversations. Available on Opus 4.6. 
 We've introduced data residency controls , allowing you to specify where model inference runs with the inference_geo parameter. US-only inference is available at 1.1x pricing for models released after

---

## February 1, 2026 — 

. 
 The 1M token context window is now available in beta for Claude Opus 4.6, in addition to Sonnet 4.5 and Sonnet 4. applies to requests exceeding 200k input tokens.

---

## January 29, 2026 — Structured outputs are now generally available on the Claude API for Claude Sonn

Structured outputs are now generally available on the Claude API for Claude Sonnet 4.5, Claude Opus 4.5, and Claude Haiku 4.5. GA includes expanded schema support, improved grammar compilation latency, and a simplified integration path with no beta header required. The output_format parameter has moved to output_config.format . Existing beta users can continue using the beta header during the transition period. Structured outputs remain in public beta on Amazon Bedrock and Microsoft Foundry.

---

## January 12, 2026 — console.anthropic.com now redirects to platform.claude.com . The Claude Console 

console.anthropic.com now redirects to platform.claude.com . The Claude Console has moved to its new home as part of our Claude brand consolidation. Existing bookmarks and links will continue working via automatic redirect. For more details, see the

---

## January 5, 2026 — We've retired the Claude Opus 3 model ( claude-3-opus-20240229 ). All requests t

We've retired the Claude Opus 3 model ( claude-3-opus-20240229 ). All requests to this model will now return an error. We recommend upgrading to Claude Opus 4.5 , which offers significantly improved intelligence at a third of the cost. Researchers can request ongoing access to Claude Opus 3 on the API through the External Researcher Access Program .

---

## December 19, 2025 — We announced the deprecation of the Claude Haiku 3.5 model. Read more in Model d

We announced the deprecation of the Claude Haiku 3.5 model. Read more in Model deprecations .

---

## November 24, 2025 — We've launched Claude Opus 4.5 , our most intelligent model combining maximum ca

We've launched Claude Opus 4.5 , our most intelligent model combining maximum capability with practical performance. Ideal for complex specialized tasks, professional software engineering, and advanced agents. Features step-change improvements in vision, coding, and computer use at a more accessible price point than previous Opus models. Learn more in Models overview . 
 We've launched programmatic tool calling in public beta, allowing Claude to call tools from within code execution to reduce latency and token usage in multi-tool workflows. 
 We've launched the tool search tool in public beta, enabling Claude to dynamically discover and load tools on-demand from large tool catalogs. 
 We've launched the effort parameter in public beta for Claude Opus 4.5, allowing you to control token usage by trading off between response thoroughness and efficiency. 
 We've added client-side compaction to our Python and TypeScript SDKs, automatically managing conversation context through summarization when using tool_runner .

---

## November 21, 2025 — Search result content blocks are now generally available on Amazon Bedrock. Lear

Search result content blocks are now generally available on Amazon Bedrock. Learn more in Search results .

---

## November 19, 2025 — We've launched a new documentation platform at platform.claude.com/docs . Our do

We've launched a new documentation platform at platform.claude.com/docs . Our documentation now lives side by side with the Claude Console, providing a unified developer experience. The previous docs site at docs.claude.com will redirect to the new location.

---

## November 18, 2025 — We've launched Claude in Microsoft Foundry , bringing Claude models to Azure cus

We've launched Claude in Microsoft Foundry , bringing Claude models to Azure customers with Azure billing and OAuth authentication. Access the full Messages API including extended thinking, prompt caching (5-minute and 1-hour), PDF support, Files API, Agent Skills, and tool use. Learn more in Claude in Microsoft Foundry .

---
