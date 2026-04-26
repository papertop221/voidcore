import sys, re

# Shorthand IT
SHORTHAND = {
    "database": "db", "information": "info", "configuration": "cfg",
    "application": "app", "environment": "env", "function": "fn",
    "parameter": "prm", "variable": "var", "description": "dsc",
    "message": "msg", "error": "err", "source": "src",
    "synchronize": "sync", "development": "dev", "production": "prd",
    "repository": "repo", "instruction": "cmd", "documentation": "doc",
    "terminal": "trm", "directory": "dir", "system": "sys", "network": "net"
}

# Simbol
SYMBOLS = {"and": "&", "with": "w/", "to": ">", "for": "4", "about": "~", "at": "@"}

# Caveman: Buang kata sopan & ganti orang
CAVEMAN_FILTER = {
    "please", "help", "can", "could", "would", "i", "me", "my", "you", "your",
    "we", "us", "our", "want", "need", "should", "like", "tolong", "saya",
    "aku", "kamu", "kita", "bantu", "ingin", "mohon", "bisakah"
}

STOP = {"the", "a", "an", "is", "are", "of", "in", "on", "by", "yang", "di", "ke"}

def strip_vowels(word):
    if len(word) <= 3: return word
    return re.sub(r'[aeiou]', '', word)

def compress(text):
    parts = re.split(r'(```[\s\S]*?```)', text)
    out = []
    
    for p in parts:
        if p.startswith('```'):
            c = re.sub(r'#.*|//.*', '', p)
            c = re.sub(r'\s+', ' ', c).replace('```', '`')
            out.append(c)
        else:
            words = p.split()
            nw = []
            for w in words:
                cw = w.lower().strip(".,!?;:()")
                # 1. Caveman: Buang kata tak penting
                if cw in CAVEMAN_FILTER or cw in STOP: continue
                # 2. Shorthand/Symbol
                if cw in SYMBOLS: nw.append(SYMBOLS[cw]); continue
                if cw in SHORTHAND: nw.append(SHORTHAND[cw]); continue
                # 3. Vowel Strip
                nw.append(strip_vowels(cw))
            out.append(" ".join(nw))
            
    return " ".join(out).strip()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(compress(" ".join(sys.argv[1:])))
