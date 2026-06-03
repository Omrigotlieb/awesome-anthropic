# Anthropic Changelog

> Auto-synced from [https://docs.anthropic.com/en/release-notes/overview](https://docs.anthropic.com/en/release-notes/overview). Updated 2026-06-03T06:01:18Z

---

## June 2, 2026 — The advisor tool now supports a max_tokens parameter to cap the advisor model's 

The advisor tool now supports a max_tokens parameter to cap the advisor model's output per call, reducing latency and output token cost for workloads that don't need full-length advisor responses. Set tools[].max_tokens on the advisor tool definition; see Capping advisor output . 
 On the Claude API, you are no longer billed for a request when it returns stop_reason: "refusal" without Claude having generated any output. See Streaming refusals for detecting and handling refusals.

---

## May 29, 2026 — Claude Managed Agents webhooks , multiagent orchestration , and self-hosted sand

Claude Managed Agents webhooks , multiagent orchestration , and self-hosted sandboxes are now available on Claude Platform on AWS . See IAM actions for Claude Platform on AWS for the new IAM actions and the AnthropicSelfHostedEnvironmentAccess managed policy.

---

## May 28, 2026 — We've launched Claude Opus 4.8 ( claude-opus-4-8 ), our most capable generally a

We've launched Claude Opus 4.8 ( claude-opus-4-8 ), our most capable generally available model. Claude Opus 4.8 supports a 1M token context window by default on the Claude API, Amazon Bedrock, and Vertex AI (200k on Microsoft Foundry), 128k max output tokens, and the same set of tools and platform features as Claude Opus 4.7. See What's new in Claude Opus 4.8 for capability improvements, new features, and migration guidance. 
 We've launched mid-conversation system messages . On Claude Opus 4.8, you can send role: "system" messages after a user turn (subject to placement rules ) in the messages array, preserving prompt cache hits when instructions change during a long-running session. No beta header is required. 
 The stop_details field on refusal responses is now publicly documented; it returns a category ( cyber , bio , or null ) and a human-readable explanation , so your application can route different classes of refusal to the right next step. No beta header is required. 
 On Claude Opus 4.8, the effort parameter defaults to high across all surfaces, including Claude Code and the Messages API. 
 On Claude Opus 4.8, the minimum cacheable prompt length for prompt caching is 1,024

---

## May 19, 2026 — MCP tunnels is now available as a Research Preview, so you can connect to MCP se

MCP tunnels is now available as a Research Preview, so you can connect to MCP servers in your private network. 
 Self-hosted sandboxes are now available for Claude Managed Agents, as an alternative to running tool execution in Anthropic's infrastructure. See Self-hosted sandboxes . 
 With Claude Managed Agents, you can now update the agent's MCP server and tool configurations associated with an active session. 
 With Claude Managed Agents, large outputs from agent_toolset and MCP tools exceeding 100K tokens are now automatically spilled to a file in the sandbox. The model receives a truncated preview with the file path and can read the full content from there.

---

## May 18, 2026 — The web search tool now returns richer SEC filing data, making it easier to grou

The web search tool now returns richer SEC filing data, making it easier to ground financial research agents, earnings analysis, and due-diligence workflows in primary sources with citations.

---

## May 13, 2026 — We've launched cache diagnostics in public beta. Pass diagnostics.previous_messa

We've launched cache diagnostics in public beta. Pass diagnostics.previous_message_id on a Messages request and the API reports a cache_miss_reason explaining where the prompt cache prefix diverged from the previous turn. Include the cache-diagnosis-2026-04-07 beta header in your requests.

---

## May 12, 2026 — Fast mode (research preview) now supports Claude Opus 4.7. Set speed: "fast" wit

Fast mode (research preview) now supports Claude Opus 4.7. Set speed: "fast" with model: "claude-opus-4-7" and the fast-mode-2026-02-01 beta header for significantly faster output token generation at premium pricing. Pricing, rate limits, and access are the same as for Opus 4.6 fast mode; interested customers should join the waitlist .

---

## May 11, 2026 — We've launched Claude Platform on AWS , bringing the Claude API to Anthropic-man

We've launched Claude Platform on AWS , bringing the Claude API to Anthropic-managed infrastructure accessible through AWS, with AWS billing and IAM authentication. Access the full Messages API, Files API, Message Batches API, Claude Managed Agents, Agent Skills, code execution, and tool use through native AWS endpoints. Learn more in Claude Platform on AWS .

---

## May 6, 2026 — Multiagent sessions and Outcomes are now in public beta under the standard manag

Multiagent sessions and Outcomes are now in public beta under the standard managed-agents-2026-04-01 beta header. 
 Claude Managed Agents vault credential background refresh is now supported for mcp_oauth credentials. See Authenticate with vaults . 
 Webhooks for Claude Managed Agents are now supported. Webhook event types include session and vault lifecycle events. See Subscribe to webhooks . 
 Additional filtering and sorting options are now supported for Claude Managed Agents. Sessions can be filtered by status, and events can be filtered by type. Events can now be filtered by creation time.

---

## April 30, 2026 — We've retired the 1M token context window beta ( context-1m-2025-08-07 ) for Cla

We've retired the 1M token context window beta ( context-1m-2025-08-07 ) for Claude Sonnet 4.5 and Claude Sonnet 4. The beta header now has no effect on these models, and requests exceeding the standard 200k-token context window return an error. To use the 1M context window, migrate to Claude Sonnet 4.6 or Claude Opus 4.6 , where it's generally available at standard pricing with no beta header required.

---

## April 24, 2026 — We've released the Rate Limits API , allowing administrators to programmatically

We've released the Rate Limits API , allowing administrators to programmatically query the rate limits configured for their organization and workspaces.

---

## April 23, 2026 — Memory for Claude Managed Agents is now in public beta under the standard manage

Memory for Claude Managed Agents is now in public beta under the standard managed-agents-2026-04-01 header. See Using agent memory for the full integration guide.

---

## April 20, 2026 — We've retired the Claude Haiku 3 model ( claude-3-haiku-20240307 ). All requests

We've retired the Claude Haiku 3 model ( claude-3-haiku-20240307 ). All requests to this model will now return an error. We recommend upgrading to Claude Haiku 4.5 .

---

## April 16, 2026 — We've launched Claude Opus 4.7 , our most capable generally available model for 

We've launched Claude Opus 4.7 , our most capable generally available model for complex reasoning and agentic coding, at the same $5 / $25 per MTok pricing as Opus 4.6. See What's new in Claude Opus 4.7 for capability improvements, new features, and the updated tokenizer. Opus 4.7 includes API breaking changes versus Opus 4.6; see Migrating to Claude Opus 4.7 before upgrading. 
 Claude in Amazon Bedrock is now open to all Amazon Bedrock customers. Claude Opus 4.7 and Claude Haiku 4.5 are available self-serve from the Bedrock console through the Messages API endpoint at /anthropic/v1/messages , in 27 AWS regions with global and regional endpoints.

---

## June 15, 2026 — . We recommend migrating to Claude Sonnet 4.6 and Claude Opus 4.8 respectively. 

. We recommend migrating to Claude Sonnet 4.6 and Claude Opus 4.8 respectively. Read more in model deprecations .

---

## April 9, 2026 — We've launched the advisor tool in public beta. Pair a faster executor model wit

We've launched the advisor tool in public beta. Pair a faster executor model with a higher-intelligence advisor model that provides strategic guidance mid-generation, so long-horizon agentic workloads get close to advisor-solo quality while the bulk of token generation happens at executor-model rates. Include the beta header advisor-tool-2026-03-01 in your requests.

---

## April 8, 2026 — We've launched Claude Managed Agents in public beta, a fully managed agent harne

We've launched Claude Managed Agents in public beta, a fully managed agent harness for running Claude as an autonomous agent with secure sandboxing, built-in tools, and server-sent event streaming. Create agents, configure containers, and run sessions through the API. All endpoints require the managed-agents-2026-04-01 beta header. Learn more in Claude Managed Agents overview . 
 We've launched the ant CLI , a command-line client for the Claude API that enables faster interaction with the Claude API, native integration with Claude Code, and versioning of API resources in YAML files. Learn more in the CLI reference .

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
