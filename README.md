# 🕳️ VoidCore (v2.0)

**The Singularity Level Token Compressor for Gemini CLI.**

VoidCore is an ultra-aggressive token-saving extension that intercepts your prompts and compresses them using 7 stages of surgical precision before they hit the API. It "sucks in" tokens like a black hole, allowing you to send massive amounts of context for a fraction of the cost.

## 📊 Performance Statistics

| Mode | Token Savings | Use Case |
| :--- | :--- | :--- |
| **Balanced** | **50% - 70%** | Daily coding and queries. |
| **Aggressive** | **70% - 90%** | Complex tasks with large context. |
| **Singularity** | **Up to 99.9%** | Massive repetitive prompts via Delta Hashing. |

## 🚀 Key Features (The 7 Stages)

1.  **TextRank Density Pruning**: Removes low-signal sentences and fluff.
2.  **Delta/Diff Hashing**: Only sends the *changes* from your previous prompt.
3.  **Caveman Protocol**: Strips politeness, pronouns, and auxiliary verbs.
4.  **BPE Unicode Forcing**: Replaces common technical terms (e.g., `function`) with 1-token symbols (e.g., `ƒ`).
5.  **Vowel Stripping**: Removes vowels from non-critical words (e.g., `compress` -> `cmprss`).
6.  **Context Variable Mapping**: Replaces repeated phrases with short variables.
7.  **Semantic Code Compression**: Minifies code blocks while keeping logic intact.

## 🛠️ Installation

1. Clone to your Gemini CLI extensions folder:
   ```bash
   git clone https://github.com/papertop221/voidcore.git ~/.gemini/extensions/voidcore
   ```
2. Reload skills in Gemini CLI:
   ```bash
   /skills reload
   ```

## 📖 How It Works

VoidCore works on the **Input Level**. It compresses what you send. Gemini is instructed via `GEMINI.md` on how to decode these signals. 

**CRITICAL:** The AI will always respond in **Normal Human Language**. The compression is invisible to the output, saving you tokens only where it matters: the input overhead.

## 📜 Decoding Map (Internal)

If you see these symbols in your logs, here is what they mean:
- `ƒ` : function
- `δ` : data
- `⚡` : optimize
- `✗` : error
- `[DIFF-xxxx]` : Delta update from previous message.

---
*Created by [papertop221](https://github.com/papertop221)*
