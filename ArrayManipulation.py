'''
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element 
between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Example

n = 10
queries = (1,5,3], [4, 8, 7), [6, 9, 1]

Queries are interpreted as follows:

abk
153
487
691

Add the values of k between the indices a and b inclusive:

index->  1 2 3 4 5 6 7 8 9 10
        [0,0,0, 0, 0,0,0,0,0, 0]
        [3,3,3, 3, 3,0,0,0,0, 0]
        (3.3,3,10.10.77,7,0, 0]
        [3,3,3,10,10,8,8,8,1, 0]

The largest value is 10 after all operations are performed.

Function Description
Complete the function arrayManipulation in the editor below. arrayManipulation has the following parameters:
• int n - the number of elements in the array
• int queries(q][3] - a two dimensional array of queries where each querieslil contains three integers, a, b, and k.
Returns
• int - the maximum value in the resultant array
Input Format
The first line contains two space-separated integers n and m, the size of the array and the number of operations.
Each of the next m lines contains three space-separated integers a, b and k, the left index, right index and summand.

Constraints
• 35n≤ 107
• 15m≤ 2*105
• 1≤a≤b≤n
• 0≤k≤ 10°
Sample Input
5 3
1 2 100
2 5 100
3 4 100
Sample Output
200
Explanation
After the first update the list is 100 100 0 0 0.
After the second update list is 100 200 100 100 100.
After the third update list is 100 200 200 200 100.
The maximum value is 200.
'''


#!/bin/python3
import math
import os
import random
import re
import sys


#. 
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

''' Instead of walkthroug method we used  Difference Array technique for Time Complexity O(1)'''
def arrayManipulation(n, queries):
    #Write your code here
    arr = [0]*(n+1)

    for a, b, k in queries:
        arr[a-1] +=k
        if b<n:
            arr[b] -=k

    #use prefix sum
    current_sum = 0
    max_value = 0

    for i in range(n):
        current_sum += arr[i]
        max_value = max(max_value, current_sum)

    return max_value


if __name__ == "main":
    fptr = open(os.environ['OUTPUT PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    queries = []

    for i in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)

    fptr.write(str(result) + "\n")
    fptr.close()
