🔹 Definition of Lambda Function

👉 Lambda function is an anonymous (no name) one-line function used for small operations.

Syntax
lambda arguments : expression

🔹 Where we use Lambda Functions

We use lambda when:

The logic is small and single-line

The function is used only once

Inside built-in functions like:

sorted()

map()

filter()

🔹 Lambda with Input & Output Examples
1️⃣ Lambda with sorted()

Code

items = [[1, 3], [2, 1], [4, 2]]
result = sorted(items, key=lambda x: x[1])
print(result)


Input

[[1,3], [2,1], [4,2]]


Output

[[2,1], [4,2], [1,3]]

2️⃣ Lambda with map()

Code

nums = [1, 2, 3]
squares = list(map(lambda x: x*x, nums))
print(squares)


Input

[1, 2, 3]


Output

[1, 4, 9]

3️⃣ Lambda with filter()

Code

nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)


Input

[1, 2, 3, 4]


Output

[2, 4]

4️⃣ Simple Lambda (Normal Use)

Code

add = lambda a, b: a + b
print(add(3, 5))


Input

3, 5


Output

8

🔹 When NOT to use Lambda ❌

Multi-line logic

Complex programs

Repeated use

Use def instead.
