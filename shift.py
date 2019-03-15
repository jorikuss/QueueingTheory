import numpy as np

array = np.arange(12)
print("Original array : \n", array)

print("\nRolling with 1 shift : \n", np.roll(array, -1))
