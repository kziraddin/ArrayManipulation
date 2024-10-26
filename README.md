# Array Manipulation

This Python script implements a solution to the Array Manipulation problem. It's designed to work with HackerRank's environment and includes the necessary boilerplate code for input/output handling.

## Problem Description

Given a 1-indexed array of zeros and a list of operations, perform each operation by adding a value to each array element between two given indices, inclusive. After all operations have been performed, return the maximum value in the array.

**Example:**
- Input: n = 5, queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
- Output: 200

## Function Description

The main logic is implemented in the `arrayManipulation` function:

```python
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for a, b, k in queries:
        arr[a-1] += k
        if b < n:
            arr[b] -= k
    
    current_sum = 0
    max_value = 0
    for i in range(n):
        current_sum += arr[i]
        max_value = max(max_value, current_sum)
    
    return max_value
```

This function takes two parameters:
- `n`: an integer representing the size of the array
- `queries`: a 2D array where each inner array contains three integers [a, b, k]

It returns the maximum value in the resultant array after all operations.

## Applications

The Array Manipulation problem and its solution technique have several practical applications:

1. **Range Updates**: Efficiently handling range updates in large arrays or databases.

2. **Data Analysis**: Analyzing cumulative effects of multiple operations on datasets.

3. **Financial Modeling**: Calculating the impact of multiple transactions on account balances over time.

4. **Traffic Analysis**: Modeling traffic flow changes due to multiple events or restrictions.

5. **Resource Allocation**: Managing resource distribution across different time periods or departments.

6. **Image Processing**: Applying multiple filters or transformations to specific regions of an image.

7. **Scheduling Systems**: Managing overlapping time slots or resource reservations.

## Input Format

1. The first line contains two space-separated integers `n` and `m`, the size of the array and the number of operations.
2. Each of the next `m` lines contains three space-separated integers `a`, `b`, and `k`, representing the left index, right index, and summand.

## Constraints

- 3 ≤ n ≤ 10^7
- 1 ≤ m ≤ 2 * 10^5
- 1 ≤ a ≤ b ≤ n
- 0 ≤ k ≤ 10^9

## Usage

This script is designed to run in HackerRank's environment. To use it locally:

1. Ensure you have Python 3 installed.
2. Modify the input method to accept user input or read from a file.
3. Change the output method to print to console or write to a file.

## Algorithm

The solution uses the Difference Array technique:

1. Initialize an array of size n+1 with zeros.
2. For each query [a, b, k]:
   - Add k to arr[a-1]
   - Subtract k from arr[b] (if b < n)
3. Calculate the prefix sum and keep track of the maximum value.

## Time and Space Complexity

- Time Complexity: O(n + m), where n is the array size and m is the number of queries
- Space Complexity: O(n)

