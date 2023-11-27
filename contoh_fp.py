# Immutability
def add_element(lst, element):
    # Membuat salinan list dan menambahkan elemen baru
    new_list = lst.copy()
    new_list.append(element)
    return new_list

original_list = [1, 2, 3]
new_list = add_element(original_list, 4)
print(original_list)  # Output: [1, 2, 3]
print(new_list)       # Output: [1, 2, 3, 4]

# First-Class dan Higher-Order Functions
def square(x):
    return x * x

def operate_on_list(numbers, operation):
    return [operation(num) for num in numbers]

numbers = [1, 2, 3, 4]
squared_numbers = operate_on_list(numbers, square)
print(squared_numbers)  # Output: [1, 4, 9, 16]

# Pure Functions
def pure_add(a, b):
    return a + b

result = pure_add(3, 4)
print(result)  # Output: 7

# Referential Transparency
def multiply_by_two(x):
    return x * 2

expression_result = multiply_by_two(5) + multiply_by_two(3)
reference_result = pure_add(multiply_by_two(5), multiply_by_two(3))
print(expression_result == reference_result)  # Output: True

# Recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Lazy Evaluation (Dengan menggunakan generator)
def generate_numbers():
    for i in range(5):
        yield i

# Hanya menghasilkan nilai saat diperlukan
lazy_numbers = generate_numbers()
print(next(lazy_numbers))  # Output: 0

# Declarative Programming (menggunakan filter dan map)
numbers = [1, 2, 3, 4, 5]
filtered_numbers = filter(lambda x: x % 2 == 0, numbers)
squared_numbers = map(lambda x: x * x, filtered_numbers)
print(list(squared_numbers))  # Output: [4, 16]

# Statelessnes
def add_numbers(a, b):
    return a + b

# Tidak menggunakan state yang dapat diubah
result1 = add_numbers(2, 3)
result2 = add_numbers(5, 7)
print(result1, result2)  # Output: 5 12
