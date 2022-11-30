from collections import OrderedDict

data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]

order_client_ages = OrderedDict(sorted(data, key=lambda x: x[1]))
print(order_client_ages)

import numpy as np
np.iinfo(np.int64)
print(np.iinfo)

arr = np.array([345234, 876362.12, 0, -1000, 99999999], dtype=np.int32)
print(arr)

arr = np.linspace(-5, 22, 60, endpoint=True, retstep=True)
print(arr)

print(mystery.ndim)