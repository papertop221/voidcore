import sys, re, os, json, difflib

# --- VOIDCORE DICTIONARIES ---
SHORTHAND = {
    "database": "db", "information": "info", "configuration": "cfg",
    "application": "app", "environment": "env", "function": "fn",
    "parameter": "prm", "variable": "var", "description": "dsc",
    "message": "msg", "error": "err", "source": "src",
    "synchronize": "sync", "development": "dev", "production": "prd",
    "repository": "repo", "instruction": "cmd", "documentation": "doc",
    "terminal": "trm", "directory": "dir", "system": "sys", "network": "net",
    "python": "py", "javascript": "js", "typescript": "ts"
}

# 1-Token Unicode/BPE Forcing (Simulated)
SYMBOLS = {
    "and": "&", "with": "w/", "to": ">", "for": "4", "about": "~", "at": "@",
    "equals": "=", "plus": "+", "minus": "-", "multiply": "*", "divide": "/"
}

CAVEMAN_FILTER = {
    "please", "help", "can", "could", "would", "i", "me", "my", "you", "your",
    "we", "us", "our", "want", "need", "should", "like", "tolong", "saya",
    "aku", "kamu", "kita", "bantu", "ingin", "mohon", "bisakah", "coba", "tolonglah"
}

STOP = {"the", "a", "an", "is", "are", "of", "in", "on", "by", "yang", "di", "ke", "dari", "ini", "itu"}

# --- METHOD 1: VOWEL STRIPPING ---
def strip_vowels(word):
    if len(word) <= 3: return word
    return re.sub(r'[aeiou]', '', word)

# --- METHOD 2: TEXTRANK / DENSITY PRUNING ---
def density_pruning(text):
    """Drops sentences that have low keyword density if text is very long."""
    sentences = re.split(r'(?<=[.!?]) +', text)
    if len(sentences) < 3: return text # Don't prune short texts
    
    important_sentences = []
    for s in sentences:
        words = s.lower().split()
        if not words: continue
        # Score = (Keywords + Shorthands) / Total words
        score = sum(1 for w in words if w in SHORTHAND or w not in STOP and w not in CAVEMAN_FILTER) / len(words)
        if score > 0.3: # Keep if > 30% dense
            important_sentences.append(s)
            
    return " ".join(important_sentences) if important_sentences else text

# --- METHOD 3: DELTA / DIFF COMPRESSION ---
def diff_compression(current_input):
    """Compares with last history entry. If very similar, send only the diff."""
    history_file = os.path.expanduser("~/.ai_history.json")
    if not os.path.exists(history_file): return current_input
    
    try:
        with open(history_file, 'r') as f:
            history = json.load(f)
            if not history: return current_input
            last_u = history[-1].get("u", "")
            
            # Calculate similarity
            seq = difflib.SequenceMatcher(None, last_u.lower(), current_input.lower())
            if seq.ratio() > 0.7: # > 70% similar, send diff
                diffs = []
                for tag, i1, i2, j1, j2 in seq.get_opcodes():
                    if tag == 'replace':
                        diffs.append(f"{last_u[i1:i2]}->{current_input[j1:j2]}")
                    elif tag == 'insert':
                        diffs.append(f"+{current_input[j1:j2]}")
                if diffs:
                    return "[DIFF] " + " | ".join(diffs)
    except: pass
    
    return current_input

# --- MAIN VOID ENGINE ---
def compress(text):
    # 1. Delta/Diff Compression (Checks history first)
    diff_text = diff_compression(text)
    if diff_text.startswith("[DIFF]"): return diff_text
    
    # 2. Information Density Pruning
    dense_text = density_pruning(text)
    
    # 3. Code vs Prose Separation
    parts = re.split(r'(```[\s\S]*?```)', dense_text)
    out = []
    
    for p in parts:
        if p.startswith('```'):
            # Minify Code
            c = re.sub(r'#.*|//.*', '', p)
            c = re.sub(r'\n\s*\n', '\n', c).replace('```', '`')
            out.append(c.strip())
        else:
            # 4. Caveman + BPE + Vowels
            words = p.split()
            nw = []
            for w in words:
                cw = w.lower().strip(".,!?;:()")
                if cw in CAVEMAN_FILTER or cw in STOP: continue
                if cw in SYMBOLS: nw.append(SYMBOLS[cw]); continue
                if cw in SHORTHAND: nw.append(SHORTHAND[cw]); continue
                nw.append(strip_vowels(cw))
            if nw: out.append(" ".join(nw))
            
    return " ".join(out).strip()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(compress(" ".join(sys.argv[1:])))
