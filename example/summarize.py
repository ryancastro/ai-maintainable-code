#!/usr/bin/env python3

# @aif: purpose: fetch and summarize a Wikipedia article using an LLM
# @aif: input: topic name from command line
# @aif: output: summary text printed to stdout
# @aif: depends_on: Wikipedia API, LLM model
# @aif: note: This is a minimal example; voice generation not included

import requests
import sys

def fetch_wikipedia_summary(topic):
    # @ai: purpose: get intro paragraph for a topic from Wikipedia API
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception(f"Error fetching Wikipedia article for {topic}")
    data = res.json()
    return data.get("extract", "")

def summarize_text(text):
    # @ai: purpose: placeholder for LLM summarization of raw article text
    # @ai: note: Replace this with a call to your preferred LLM
    return text[:300] + "..."  # fake summary for now

def main():
    if len(sys.argv) < 2:
        print("Usage: python summarize.py <topic>")
        return
    topic = sys.argv[1]
    raw = fetch_wikipedia_summary(topic)
    summary = summarize_text(raw)
    print(f"\nSummary of {topic}:\n{summary}")

if __name__ == "__main__":
    main()
