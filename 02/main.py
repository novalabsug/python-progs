# List comprehension
# write a for loop in a list

w = [i for i in range(20) if i % 2 == 0]
x = [i for i in range(10)]
y = [[] for i in range(10)]
z = [[j for j in range(5)] for i in range(10)]

print(w)
print(x)
print(y)
print(z)
