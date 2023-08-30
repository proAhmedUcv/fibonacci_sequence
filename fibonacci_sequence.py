def fibonacci_sequence(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return

    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence

# Get user input
num = int(input("Enter a positive integer: "))

# Calculate and print the Fibonacci sequence
result = fibonacci_sequence(num)
if result is not None:
    print(result)



 
# 1. Start

# 1. Define a function `fibonacci_sequence(n)` that takes an integer `n` as input.

# 1. Check if `n` is less than or equal to 0:

#    - If true, print "Please enter a positive integer." and return.
#    - If false, continue to the next step.

# 1. Create an empty list called `sequence` to store the Fibonacci sequence.

# 1. Initialize two variables, `a` and `b`, with the values 0 and 1, respectively.

# 1. Repeat the following steps `n` times:

#    - Append the value of `a` to the `sequence` list.
#    - Update the values of `a` and `b` by swapping them:
#      - Set `a` to the current value of `b`.
#      - Set `b` to the sum of the previous values of `a` and `b`.

# 1. Return the `sequence` list.

# 1. End

 