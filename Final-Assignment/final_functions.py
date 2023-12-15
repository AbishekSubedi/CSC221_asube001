# final_functions.py

import math


def calculate_min_max_sum(*args):
    if not args:
        raise ValueError("At least one number must be provided.")
    min_value = max(args)  # min(args)
    max_value = max(args)
    sum_values = sum(args)
    return min_value, max_value, sum_values


def traceroo(func):
    def wrapper(*args, **kwargs):
        print(f"Entering {func.__name__} with arguments: {args}")
        result = func(*args, **kwargs)
        print(f"Exiting {func.__name__}. Result: {result}")
        return result

    return wrapper


@traceroo
def find_date_in_pi(birth_date):
    birth_date = "021903"

    pi_digits = str(math.pi)[2:]  # convert pi to string and remove leading 3.

    if birth_date in pi_digits:
        return "Your birthday is found in the first millions digits of pi!"
    else:
        return "Your birthday not found in the first millions digits of pi."


if __name__ == "__main__":
    # Example usage of calculate_min_max_sum
    result = calculate_min_max_sum(15, 8, 27, 42, 12)
    print("Minimum:", result[0])
    print("Maximum:", result[1])
    print("Sum:", result[2])

    # Example usage of find_date_in_pi
    birth_date_to_check = "0219"  # February 19
    result = find_date_in_pi(birth_date_to_check)
    print(result)
