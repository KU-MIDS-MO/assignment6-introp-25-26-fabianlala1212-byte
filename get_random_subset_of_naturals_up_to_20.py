import numpy as np
def get_random_subset_of_naturals_up_to_20():
    r = np.random.randint(0, 2**20)
    mask = [(r >> i) & 1 for i in range(20)]
    subset = [i+1 for i in range(20) if mask[i] == 1]
    return np.array(subset)

subset = get_random_subset_of_naturals_up_to_20()
print(subset)
