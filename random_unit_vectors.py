import numpy as np
def random_unit_vectors(num_vectors, dim):
    M = np.random.randn(num_vectors, dim)
    norms = np.linalg.norm(M, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    M_unit = M / norms
    return M_unit

np.random.seed(1)
print(random_unit_vectors(5, 3))
