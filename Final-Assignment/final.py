# final.py

from final_functions import calculate_min_max_sum, traceroo, find_date_in_pi

# Exercise 1: Use calculate_min_max_sum with various sets of numbers
numbers_set1 = [10, 5, 8, 15, 20]
numbers_set2 = [100, 75, 120, 50]
numbers_set3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result_set1 = calculate_min_max_sum(*numbers_set1)
result_set2 = calculate_min_max_sum(*numbers_set2)
result_set3 = calculate_min_max_sum(*numbers_set3)

print("Exercise 1:")
print("Set 1 - Minimum:", result_set1[0], "Maximum:", result_set1[1], "Sum:", result_set1[2])
print("Set 2 - Minimum:", result_set2[0], "Maximum:", result_set2[1], "Sum:", result_set2[2])
print("Set 3 - Minimum:", result_set3[0], "Maximum:", result_set3[1], "Sum:", result_set3[2])

# Exercise 2: Use find_date_in_pi with different birth dates
@traceroo
def exercise_find_date_in_pi(birth_date):
    result = find_date_in_pi(birth_date)
    print(result)

print("\nExercise 2:")
exercise_find_date_in_pi("0401")  # April 1
exercise_find_date_in_pi("0723")  # July 23
exercise_find_date_in_pi("1111")  # November 11
exercise_find_date_in_pi("0915")  # September 15

# Exercise 3: Use find_date_in_pi with invalid birth date (empty string)
@traceroo
def exercise_invalid_date_in_pi():
    result = find_date_in_pi("")
    print(result)

print("\nExercise 3:")
exercise_invalid_date_in_pi()
