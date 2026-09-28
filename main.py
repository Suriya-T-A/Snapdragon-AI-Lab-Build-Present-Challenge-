"""SnapStudy AI starter prototype: local extractive summary + revision prompts.
No network calls or external AI model are used in this baseline.
"""
import re
from collections import Counter

STOP = set("""a an the and or but if then than to of in on for with by from is are was were be been
being this that these those it its as at into about your you we they he she i""".split())

def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\\s+", text.strip()) if s.strip()]

def summarize(text, max_sentences=3):
    parts = sentences(text)
    if len(parts) <= max_sentences:
        return " ".join(parts)
    words = re.findall(r"[a-zA-Z]{3,}", text.lower())
    freq = Counter(w for w in words if w not in STOP)
    scored = []
    for i, s in enumerate(parts):
        terms = re.findall(r"[a-zA-Z]{3,}", s.lower())
        score = sum(freq[w] for w in terms if w not in STOP) / max(1, len(terms))
        scored.append((score, i, s))
    chosen = sorted(sorted(scored, reverse=True)[:max_sentences], key=lambda x:x[1])
    return " ".join(s for _, _, s in chosen)

def make_questions(text, limit=5):
    parts = sentences(text)
    questions = []
    for s in parts:
        words = re.findall(r"\\b[A-Za-z]{5,}\\b", s)
        if len(words) >= 2:
            key = max(words, key=len)
            question = re.sub(re.escape(key), "________", s, count=1, flags=re.I)
            questions.append("Complete the statement: " + question)
        if len(questions) >= limit:
            break
    return questions or ["Add a few complete sentences to your notes to create revision prompts."]

def main():
    print("SnapStudy AI — local study-notes prototype")
    print("Paste notes below. Finish input with a line containing END.")
    lines=[]
    while True:
        try: line=input()
        except EOFError: break
        if line.strip()=="END": break
        lines.append(line)
    notes="\\n".join(lines).strip()
    if not notes:
        print("No notes provided."); return
    print("\\nSUMMARY\\n-------")
    print(summarize(notes))
    print("\\nREVISION PROMPTS\\n-----------------")
    for i,q in enumerate(make_questions(notes),1): print(f"{i}. {q}")
    print("\\nBaseline uses local text processing only; no generative model is included.")

if __name__=="__main__": main()
