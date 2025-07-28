from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_sections(sections, persona, job):
    query = f"{persona}. {job}"
    documents = [s["full_text"] for s in sections]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([query] + documents)
    
    query_vec = tfidf_matrix[0]
    doc_vecs = tfidf_matrix[1:]

    similarities = cosine_similarity(query_vec, doc_vecs)[0]

    ranked_sections = []
    for i, score in enumerate(similarities):
        ranked = sections[i].copy()
        ranked["importance_rank"] = float(score)
        ranked_sections.append(ranked)

    ranked_sections.sort(key=lambda x: x["importance_rank"], reverse=True)
    return ranked_sections
