"Module 2 lab 2 assignment"

# Create a tuple with numbers and print one item
t = (1, 2, 3, 4, 5)
print(f"Item at index 2: {t[2]}")
# Remove an item from a tuple.
t = (1, 2, 3, 4, 5)
t = list(t)
t.pop(0)
t = tuple(t)
print(f"After removing an item: {t}")
# Unpack a tuple in several variables.
a, b, c, d = t
print(f"Unpacked tuple: {a}, {b}, {c}, {d}")
# Convert a tuple to a string.
conver_t_to_string = str(t)
print(f"Tuple converted to string: {conver_t_to_string}")
# Find the repeated items of a tuple.
t = (1, 2, 3, 4, 5, 1, 2, 3)
repeated_items = []
for item in t:
    if t.count(item) > 1:
        if item not in repeated_items:
            repeated_items.append(item)
print(f"Repeated items: {repeated_items}")

# Reverse a tuple.
t = (1, 2, 3, 4, 5)
t = list(t)
t.reverse()
t = tuple(t)
print(f"Reversed tuple: {t}")
# Sum all the items in a list
l = [1, 2, 3, 4, 5]

sum = 0
for item in l:
    if isinstance(item, int):
        sum += item
print(f"Sum of all items in the list: {sum}")
# Remove duplicates from a list.
l = [1, 2, 3, 4, 5, 1, 2, 3]
l = list(set(l))
print(f"List with duplicates removed: {l}")
# Clone or copy a list
l = [1, 2, 3, 4, 5]
l_copy = l.copy()
print(
    f"Cloned list: {l_copy}, original list reference: {id(l)}, cloned list reference: {id(l_copy)}"
)
# Append a list to the second list.
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l1.extend(l2)
print(f"List after appending: {l1}")
# Get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_l = sorted(l, key=lambda x: x[-1])
print(f"Sorted list: {sorted_l}")
# Create a list of 10 persons. After doing so, use the slicing technique to get the first four.
persons = [
    "Ahmed",
    "Corey",
    "John",
    "Jane",
    "Sara",
    "Ali",
    "Mike",
    "Tom",
    "Jerry",
    "Mona",
]
first_four_persons = persons[:4]
print(f"First four persons: {first_four_persons}")
# Create a set.
s = {1, 2, 3, 4, 5}
print(f"Set: {s}")
# Create an intersection of sets.
s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8}
intersection = s1.intersection(s2)
print(f"Intersection of sets: {intersection}")
# Create a union of sets.
union_of_sets = s1.union(s2)
print(f"Union of sets: {union_of_sets}")


# Write a Python function to multiply all the numbers in a list.
def multiply_all_numbers(l):
    result = 1
    for item in l:
        if isinstance(item, int):
            result *= item
    return result
print(f"Multiplication of all numbers in the list: {multiply_all_numbers([1, 2, 3, 4, 5])}")
