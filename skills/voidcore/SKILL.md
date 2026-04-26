---
name: voidcore
description: >
  VoidCore token-saving extension. Use this when you need to process highly compressed inputs using Information Density Pruning, Diff Hashing, and Unicode Symbol Mapping. 
---

# VOIDCORE PROTOCOL (Singularity Efficiency)

When this mode is active, the user's input is intercepted and processed by the `VoidCoreCompressor` pipeline. You will receive text that is dense, lacks most vowels in non-critical words, and uses specific Unicode symbols for technical terms.

## AI Execution Rules
1.  **Decoding Logic:** Refer to the decoding map in `GEMINI.md` to translate symbols (e.g., `ƒ` -> function, `ν` -> variable).
2.  **Context Awareness:** If the input looks like `[DIFF-hash]`, it is a delta from a previous prompt. Focus on the `@index:new_word` or `+added_word` markers.
3.  **Vowel Reconstruction:** Mentally reconstruct vowel-stripped words based on context (e.g., `cmprss` -> compress, `implmnt` -> implement).
4.  **Response Format (MANDATORY):** Respond in **Normal Human Language**. Do NOT mirror the compressed style in your output.
5.  **Technical Accuracy:** Maintain high precision. Despite the compression, the technical substance is preserved.

## Integration Details
- **TextRank:** Removes sentences with low technical density.
- **Caveman:** Strips filler words and politeness.
- **BPE-Unicode:** Maps common dev terms to single-token symbols.
- **Vowel Stripping:** Removes vowels from non-essential words > 3 chars.
