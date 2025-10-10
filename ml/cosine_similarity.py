import numpy as np

def cosine_similarity(vector1: list, vector2: list):
    vec1 = np.array(vector1)
    vec2 = np.array(vector2)
    ## Dot product of vector
    dot_prod = np.dot(vec1, vec2)
    ## magnitude of each vector
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    score = dot_prod / (norm1 * norm2)
    return score

if __name__ == "__main__":
    vec1 = [3, 4, 5]
    vec2 = [14, 17, 21]
    score = cosine_similarity(vec1, vec2)
    print("Cosine similarity score: ", score)


