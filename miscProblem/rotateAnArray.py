"""
Rotate an array:
    [1,2,3,4,5] -- [5,1,2,3,4]
Cyclic rotation which shifts array from one index right

###### Brute Force Approach ########
  Assign Last index value of array or List a variable Last_elem
  iterate over list from reverse order 
"""
val = [11,12,13,14,15]
val1 = []
for j in range(len(val)-1,-1, -1):
    if val[len(val)-1] == val[j]:
        print(val[j])
    else:
        val1 = [val[j]] + val1
val1 = [val[len(val)-1]] + val1
print(val1)