"Module 2 lab 2 assignment"

import random

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

sum_list = 0
for item in l:
    if isinstance(item, int):
        sum_list += item
print(f"Sum_list of all items in the list: {sum_list}")
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
    """
    Multiply all the numbers in a list.
    Args:
        l (list): List of numbers.
    Returns:
        int: Multiplication of all numbers in the list.
    """
    result = 1
    for item in l:
        if isinstance(item, int):
            result *= item
    return result


print(
    f"Multiplication of all numbers in the list: {multiply_all_numbers([1, 2, 3, 4, 5])}"
)
# Generate a list of scores. After doing so, write a function that finds the min, max, and average.
scores = [random.randint(0, 100) for _ in range(10)]


def find_min_max_avg(scores: list):
    """
    Find the minimum, maximum, and average of a list of scores.
    Args:
        scores (list): List of scores.
    Returns:
        tuple: Minimum, maximum, and average of the scores.
    """
    min_score = min(scores)
    max_score = max(scores)
    avg_score = sum(scores) / len(scores)
    return min_score, max_score, avg_score


print(f"Scores: {scores}")
min_score, max_score, avg_score = find_min_max_avg(scores)
print(f"Min: {min_score}, Max: {max_score}, Avg: {avg_score}")


# Write a Python function to check whether a number is in a given range.
def is_in_range(num: int, start: int, end: int):
    """
    Check whether a number is in a given range.
    Args:
        num (int): Number to check.
        start (int): Start of the range.
        end (int): End of the range.
    Returns:
        bool: True if the number is in the range, False otherwise.
    """
    if isinstance(num, int) and isinstance(start, int) and isinstance(end, int):
        return start <= num <= end
    return False


print(f"Is 5 in the range 1-10: {is_in_range(5, 1, 10)}")
print(f"Is 15 in the range 1-10: {is_in_range(15, 1, 10)}")
# Generate a nested list with dog breed and max running speed. After doing so, write a function that finds the maximum and minimum speed based on dog breed.
dog_speeds = [
    ["Greyhound", 45],
    ["Saluki", 42],
    ["Vizsla", 40],
    ["Jack Russell Terrier", 38],
    ["Dalmatian", 37],
    ["Borzoi", 36],
    ["Whippet", 35],
    ["Doberman Pinscher", 32],
    ["Border Collie", 30],
    ["Golden Retriever", 25],
]


def find_max_min_speed(dog_list):
    """
    Finds the dog breeds with the maximum and minimum running speeds.

    Parameters:
    dog_list (list): A list of lists where each sublist contains a dog breed and its maximum speed.

    Returns:
    tuple: A tuple containing two lists - the fastest and slowest dog breed with their respective speeds.
    """
    max_speed_dog = max(dog_list, key=lambda x: x[1])
    min_speed_dog = min(dog_list, key=lambda x: x[1])

    return max_speed_dog, min_speed_dog


# unpack the function output tuple
max_dog, min_dog = find_max_min_speed(dog_speeds)
# print the fastest and slowest dog breed with their respective speeds
print(f"Fastest dog: {max_dog[0]} with a speed of {max_dog[1]} mph")
print(f"Slowest dog: {min_dog[0]} with a speed of {min_dog[1]} mph")
