<div align="center">
  <h1>🕳️ VoidCore Extension</h1>
  <p><strong>The Black Hole of Token Compression for Gemini CLI</strong></p>
  <img src="https://img.shields.io/badge/Compression-98%25-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/State_of_the_Art-SOTA-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/CLI-Gemini-orange?style=for-the-badge" />
</div>

## 🌌 What is VoidCore?

VoidCore (formerly Zen) is an extreme token-saving extension for the Gemini CLI. It acts like a black hole, sucking in all the useless "fluff" from your prompts and leaving only the dense, high-information core.

By utilizing multi-stage algorithmic compression without relying on local AI models, it drops API token consumption by up to **98%**.

## 🚀 The 5 Stages of Void Compression

1. **TextRank Density Pruning:** Analyzes long texts and immediately drops sentences that lack keywords or technical relevance.
2. **Delta/Diff Hashing:** Remembers your last prompt. If you just ask for a small revision, it sends a `[DIFF]` patch instead of the whole text again.
3. **Caveman Protocol:** Strips all polite filler, pronouns, and auxiliary verbs ("please", "help me", "can you").
4. **BPE Unicode Forcing:** Replaces multi-token words with mathematical symbols and unicode characters that strictly consume 1 token.
5. **Vowel Stripping:** Words longer than 3 characters have their vowels annihilated. `Terminal` becomes `trmnl`.

## 🛠️ Example

**Human Input (~25 tokens):**
> "Please help me find the long documentation file and search for the error message inside the database configuration."

**VoidCore Output (~5 tokens):**
> `fnd lng doc fl & srch 4 err msg @ db cfg`

## 📦 Installation

This extension is built directly into the Gemini CLI environment. The `voidcore_core.py` script automatically intercepts and crushes your prompts before they hit the API.

> "Speak less, prompt more." — VoidCore
