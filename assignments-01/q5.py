import numpy as np

v1 = np.array([[np.sqrt(3)], [1]])
print("v1.shape:", v1.shape)
v2 = np.array([[1], [1]])
print("v2.shape:", v2.shape)
inner_result = np.vdot(v1, v2)
print("inner_result:", inner_result)
