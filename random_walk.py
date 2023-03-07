import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""
x = 10

if (x<=10):
    print("E") 

x = 15

while x>10:
    print("W")
    x -= 1

x = [1,2,3,4]

for val in x:
    print(val)

"""

np.random.seed(123)

random_walk = [0]

for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1,7)
    if dice <= 2:
       step = max(0,step-1)
    elif dice <=5:  
        step += 1
    else:
        step += np.random.randint(1,7)
    random_walk.append(step)

print(random_walk)   

plt.plot(random_walk)
plt.show()
