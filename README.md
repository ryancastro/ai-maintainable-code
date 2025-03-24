**AI-Maintainable Code: ai-meta v0.1 Specification**

---

**📘 Overview**
  
AI-maintainable code is a pattern for designing scripts and codebases that can be easily understood, extended, and reasoned about by stateless LLMs — even across tools, sessions, or different models. It uses lightweight metadata to provide AI with just enough context to reduce re-explaining, improve response quality, and enable smoother pair programming.

---

**🎯 Core Goals**

• Enable AI to instantly understand the purpose, structure, and flow of a codebase

• Reduce wasted tokens on re-orienting or re-explaining

• Improve the quality and accuracy of AI-assisted edits, reviews, and suggestions

• Create a repeatable standard that scales across dev teams and tools

---

**🧩 Core Components of AI-Meta Pattern**

| **Element**               | **Required** | **Purpose**                                                                                                                                      |
| ------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ai_context.yml/.json      | ✅            | Machine-readable summary of project purpose, pipeline, tools, entrypoints, and key relationships.<br><br>.yml is preferred for token efficiency. |
| file header @aif: comments | ✅            | Relevant Project code files have one or more  @aif: comments in its file header describing files core purpose and function. Consumers stop processing after `\n`                            |
| inline @ai: comments      | ✅            | Inline metadata annotations describing intent or purpose of code sections<br>                                                                    |
| README.ai.md              | ⭕            | A conversational summary of the project written for LLM consumption (optional)                                                                   |
| breadcrumbs.ai            | ⭕            | Chronological changelog focused on “why” rather than “what” (optional)                                                                           |
| ai_bootstrap_prompt.txt   | ⭕            | Optional file containing the suggested initial system prompt for LLM tools                                                                       |

These annotations are LLM-agnostic, lightweight, and embeddable in RAG workflows.

---

**📁 ai_context.yml Structure (Recommended Fields)**

```
title: Wikipedia Narrator
purpose: Generate narrated videos from Wikipedia articles using LLM summarization
pipeline:
  - fetch_article
  - summarize_text
  - generate_voiceover
  - render_video
entrypoints:
  main: run.py
  voice: voice.py
  video: render.py
tools:
  - openai/gpt-4
  - macOS `say`
  - ffmpeg
```

  

---
**💬 @aif: File header comments**

One or more file header comments (similar to `#!/bin/bash`) describe the files purpose and function to AI. The purpose is for automated tools to scan one or more files, folders, or the entire project to gain system-wide context, without consuming every available token.

```
# @aif: Fetches core article data. Provides all relevant methods to wiki article access and parsing.
```

---

**💬 @ai: Inline Comments**

Inline comments use a simple tag for LLM context:

```
# @ai: purpose: summarize fetched article
# @ai: input: raw Wikipedia text
# @ai: output: condensed summary for narration
```

**Common Tags:**

• purpose: (highly recommended)

• input: / output:

• depends_on: / feeds_into:

• note: for oddities, gotchas, or rationale

---

**📄 README.ai.md (Optional)**

  
A plain-English explanation of the project and its flow, optimized for LLM readability. Write it like you’re explaining to a helpful but forgetful AI coworker. Include:

• What the project does

• Key steps in the pipeline

• Tooling decisions or caveats

• Known pain points

---

**📜 breadcrumbs.ai (Optional)**

  

A lightweight evolution log for LLM grounding. Prioritize _why_ over _what_.

```
2025-03-22: Replaced GPT-3.5 with GPT-4 after summary quality complaints
2025-03-23: Broke out voiceover into separate script for easier debugging
```

This encourages an LLM to understand your history, avoiding the reimplementation of bugs, architectures or patterns that you previously removed.  

---

**⚙️ Optional Tooling Plans**
  
Looking at a CLI tool and/or VSCode plugin that will:

	• Parse and surface @ai: metadata and ai_context.yml
	• Auto-suggest related files based on dependency flow
	• Help bootstrap LLM prompts with structured grounding
	• Provide AI-powered edit scoping

  

Example behavior:

> “You’re editing the video render step. This depends on summary.py and feeds into upload.py. Load those too?”

---

**🔁 Contribution Guidelines**


We welcome suggestions, forks, and improvements. Help us:

• Improve spec clarity and utility

• Expand real-world examples

• Build the tooling ecosystem

  

Open issues or PRs at: [https://github.com/ryancastro/ai-maintainable-code](https://github.com/ryancastro/ai-maintainable-code)

---

**🚀 Try It Yourself**

1. Add an @ai: comment to one file header

2. Create a minimal ai_context.yml

3. Ask your LLM for help — and observe the improvement

---

**📄 License**
  

This specification is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You’re free to share and adapt it with attribution.

Credit: Ryan Castro ([ryancastro.com](https://www.ryancastro.com))
