import numpy as np
def estimate_pi(num_samples):
    points = np.random.rand(num_samples, 2)
    distances = points[:, 0]**2 + points[:, 1]**2
    inside = np.sum(distances <= 1)
    return 4 * inside / num_samples

np.random.seed(0)
print(estimate_pi(10))

np.random.seed(0)
print(estimate_pi(100000))
