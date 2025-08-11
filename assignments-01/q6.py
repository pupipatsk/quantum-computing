import numpy as np

v1 = np.array([[1j], [1]])
v2 = np.array([[-1j], [1]])
inner_result = np.vdot(v1, v2)
print(inner_result)
