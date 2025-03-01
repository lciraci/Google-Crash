import random

# Generate 5 unique random numbers between 1 and 100 using random.sample
random_numbers = set(random.sample(range(1, 101), 5))
#print("Set of 5 random numbers:")
#print(random_numbers)

# Generate 5 unique random numbers between 1 and 100 using random.sample and convert to tuple
random_numbers = tuple(random.sample(range(1, 101), 5))

#print("Tuple of 5 random numbers:")
#print(random_numbers)

# Generate 5 unique random numbers between 1 and 100 using random.sample and convert to list
squares = list(map(lambda x: x**2, range(10)))
#print("List of 5 random numbers:")
#print(squares)
filter_squares = list(filter(lambda x: x % 2 == 0, squares))
#print("List of 5 random numbers:",filter_squares)

# Create a dictionary with 5 students and their grades
students_grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92,
    "Evan": 88
}
print("Students Grades:", students_grades)
students_above_90 = dict(filter(lambda item: item[1] > 90, students_grades.items()))
print("Students with grade > 90:", students_above_90)