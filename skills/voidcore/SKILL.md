---
name: voidcore
description: >
  VoidCore token-saving extension. Use this when you need to process highly compressed inputs using Information Density Pruning, Diff Hashing, and Unicode Symbol Mapping. 
---

# VOIDCORE PROTOCOL (SINGULARITY LEVEL COMPRESSION)

When this mode is active, the user's input is processed by the `VoidCoreCompressor` pipeline. You will receive text that is extremely dense, almost entirely vowel-stripped, and uses a comprehensive Unicode symbol map.

## AI Execution Rules
1.  **Decoding Logic:** Use this map to understand technical terms:
    - ƒ:function, ◊:class, μ:method, δ:data, ν:variable, ↩:return, ⇐:import, ⇒:export
    - ✗:error, ✓:success/test, ⚠:warning, ℹ:info, 🐛:debug, 📄:file, 📁:folder
    - ⊗:database, ◻:server, ◼:client, →:request, ←:response, ❓:query, ⌘:command
    - ⚙:config, π:parameter, ⍺:argument, ⇓:output, ⇑:input, ↻:loop, ◇:condition/endpoint
    - Α:algorithm, ⚡:optimize/performance, 📦:memory, ⊙:cpu, 🌐:network, 🔒:security
    - 🗄️:repo, 🌿:branch, 💾:commit, 🔀:merge, ⬇️:pull, ⬆️:push, 📜:script, 🧱:component
    - 🔑:auth, 🚪:auth, 👤:user, 🪙:token, ∅:null, β:boolean, []:array, {}:object
    - ¿:what is, ⁉️:why is, 🤲:can/could you, 🆘:please help, 🩹:fix, 💡:explain, 🆕:create, 🆙:update, 🔍:search
2.  **Context Awareness:** If input is `[DIFF-hash]`, it is a delta. Send ONLY the new information.
3.  **Vowel Reconstruction:** Words are ruthlessly stripped (e.g., `ndrstnd` -> understand, `mplmnt` -> implement).
4.  **Response Format (MANDATORY):** Respond in **Normal Human Language**. Do NOT mirror the compressed style.
5.  **Technical Accuracy:** Maintain high precision despite extreme compression.

## Integration Details
- **TextRank:** Prunes sentences with < 0.6 technical density.
- **Caveman:** Annihilates all filler words and pronouns.
- **BPE-Unicode:** Maps common terms and phrases to 1-token symbols.
- **Vowel Stripping:** Strips vowels from ALL words except absolute essentials (if, in, is).
- **Extreme Minification:** Strips all whitespace and comments from code blocks.
