from random import shuffle
 
arr = [*range(1, 49)]
shuffle(arr)
print(sorted(arr[:6]))