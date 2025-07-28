# ranker.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_chunks_tfidf(chunks, query, top_k=3):
    """
    Rank chunks by TF-IDF similarity to the query string.
    Returns top_k chunks sorted by relevance score descending.
    """
    vectorizer = TfidfVectorizer().fit(chunks + [query])
    chunk_vecs = vectorizer.transform(chunks)
    query_vec = vectorizer.transform([query])
    
    scores = cosine_similarity(chunk_vecs, query_vec).flatten()
    ranked_indices = scores.argsort()[::-1][:top_k]
    ranked_chunks = [chunks[i] for i in ranked_indices]
    
    return ranked_chunks

def rank_chunks_keyword(chunks, keywords, top_k=3):
    """
    Rank chunks by number of keyword matches.
    `keywords` is a list of words/phrases.
    Returns top_k chunks with highest match count.
    """
    keyword_set = set(k.lower() for k in keywords)
    
    def keyword_match_count(text):
        tokens = text.lower().split()
        return sum(1 for w in tokens if w in keyword_set)
    
    scored = [(chunk, keyword_match_count(chunk)) for chunk in chunks]
    scored = sorted(scored, key=lambda x: x[1], reverse=True)
    
    ranked_chunks = [chunk for chunk, score in scored[:top_k]]
    return ranked_chunks
