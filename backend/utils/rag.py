import os
from collections import Counter
import math

def load_guides(guides_path):
    docs = {}
    for file in os.listdir(guides_path):
        if file.endswith(".txt"):
            with open(os.path.join(guides_path, file), "r", encoding="utf-8") as f:
                docs[file.replace(".txt", "")] = f.read().lower()
    return docs

def cosine_similarity(a, b):
    common = set(a) & set(b)
    num = sum(a[x] * b[x] for x in common)
    den = math.sqrt(sum(v*v for v in a.values())) * math.sqrt(sum(v*v for v in b.values()))
    return num / den if den else 0

def rag_search(query, docs):
    query_vec = Counter(query.lower().split())
    scores = {}

    for place, text in docs.items():
        doc_vec = Counter(text.split())
        scores[place] = cosine_similarity(query_vec, doc_vec)

    return sorted(scores, key=scores.get, reverse=True)
