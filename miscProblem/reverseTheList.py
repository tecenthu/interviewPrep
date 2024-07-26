"""
Q-3 Reverse the list
Description: reverse a list without using any built-in method like:
    reverse() or [::-1]
Input: [4,7,8] 
Ouput: [8,7,4]
"""
input = [4,7,8,11,6]
output = []

# count = 0
# for j in input:
#     count +=1
# Approach-1
for k in range(len(input)-1, -1, -1):
    output.append(input[k])
print(output)

# Approach-2:
result = []
for j in input:
    result = [j] + result
print(result)
