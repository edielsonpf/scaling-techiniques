# Scaling techniques

## OVerview

This implementation brings some exaples in how to apply scaling techiniques to optimization problems.

## QUick start

```Python
import numpy as np
from LinearOptimization.ScalingTechniques import Scaling

max_iterations = 5
A=np.matrix([(0.1,2.9,3000),(3,99999,5.25),(13.3,10.5,5.25),(214,8,124.35)])
print(A)

print('Geometric Mean')
MyScaling = Scaling(max_iterations)
X = MyScaling.GeometricMean(A)
print(X)

print('Equilibration')
print(A)
X = MyScaling.Equilibration(X)
print(X)

print('Arithmetic Mean')
print(A)
X = MyScaling.ArithmeticMean(A)
print(X)
```
