from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_matches(student_profile, internships):
    """
    Calculates match scores between a student's skills and a list of internships using TF-IDF and cosine similarity.
    Args:
        student_profile (dict): {'skills': [str, ...]}
        internships (list): [{'required_skills': [str, ...], ...}, ...]
    Returns:
        list: internships with added 'match_score' key, sorted by match_score descending.
    """
    # Prepare documents
    student_doc = " ".join(student_profile.get("skills", []))
    internship_docs = [" ".join(i.get("required_skills", [])) for i in internships]
    all_docs = internship_docs + [student_doc]

    # Vectorize
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_docs)
    student_vec = tfidf_matrix[-1]
    internship_vecs = tfidf_matrix[:-1]

    # Compute cosine similarity
    similarities = cosine_similarity(student_vec, internship_vecs)[0]

    # Add match_score to each internship
    for i, score in enumerate(similarities):
        internships[i]["match_score"] = round(score * 100, 1)

    # Sort by match_score descending
    return sorted(internships, key=lambda x: x["match_score"], reverse=True)

# Example usage
if __name__ == "__main__":
    student = {"skills": ["Python", "Machine Learning", "Data Analysis"]}
    internships = [
        {"title": "Data Science Intern", "required_skills": ["Python", "Data Analysis", "Machine Learning"]},
        {"title": "Frontend Developer Intern", "required_skills": ["React", "JavaScript", "UI/UX"]},
        {"title": "AI Research Intern", "required_skills": ["Python", "Deep Learning", "Research"]},
        {"title": "Project Management Intern", "required_skills": ["Project Management", "Communication", "Excel"]},
    ]
    results = calculate_matches(student, internships)
    for r in results:
        print(f"{r['title']}: {r['match_score']}% match")
