# README.ai.md

This repo defines a pattern for writing AI-maintainable code — scripts and projects designed to be easily understood and modified by stateless LLMs.

## Project Purpose

The goal is to reduce friction when using LLMs as coding partners. By including lightweight metadata, we help models make sense of what each part of the project is doing without needing long prompts.

## Pipeline Overview

1. Annotate key files with `@ai:` comments
2. Include a short `ai_context.yml` describing project flow
3. (Optional) Add breadcrumbs and bootstrap prompts

## Notes for AI Assistants

- Use `ai_context.yml` to understand the overall project and file relationships
- Look for `@ai:` comments to infer purpose and data flow
- Focus on improving context-aware code edits, not just syntax
