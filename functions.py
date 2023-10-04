""" Name = Abishek Subedi
 Assignment 10
 Email = asube001@plattsburgh.edu
 CSC221A-Intro to Programming
"""

import math


def favorite_book(title):
    """Returns a message about a favorite book."""
    return f"One of my favorite books is {title}."


def make_shirt(size="Large", message="I love Python"):
    """Creates a shirt with the specified size and message."""
    return f"Shirt size: {size}, Message: {message}"


def cars(manufacturer, model, **kwargs):
    """Creates a dictionary containing information about a car."""
    car_info = {
        "Manufacturer": manufacturer,
        "Model name": model,
    }
    car_info.update(kwargs)
    return car_info


def sum_and_sort_number(num1, num2=math.pi):
    """Calculates the sum of two numbers and sorts them in ascending order."""
    # Calculate the sum of the two numbers
    total = num1 + num2

    # Create a list containing both numbers in sorted order
    sorted_numbers = sorted([num1, num2])

    # Return the sum and the sorted list
    return total, sorted_numbers


def sum_and_sort_numbers(num1, num2=math.pi, verbose=False):
    """Calculates the sum of two numbers and sorts them in ascending order and shows the numbers and total if verbose is True."""
    # Calculate the sum of the two numbers
    total = num1 + num2

    # Create a list containing both numbers in sorted order
    sorted_numbers = sorted([num1, num2])

    # If 'verbose' is True, print parameters and results
    if verbose:
        return f"num1: {num1}, \nnum2: {num2}, \ntotal: {total}, \nsorted_numbers: {sorted_numbers}"

    # Return the sum and the sorted list
    return total, sorted_numbers


if __name__ == "__main__":
    # Test the functions when functions.py is run directly
    print("Running test code in functions.py:")

    # Call the function with a book title
    book_title = favorite_book("Alice in the WonderLand")
    print(book_title)

    # Call the function using keyword arguments
    shirt_result = make_shirt(size="Medium", message="Python Lover")
    print(shirt_result)

    # Call the function with the required information and additional details
    car = cars("Subaru", "Outback", color="Blue", tow_package=True)
    print(car)

    # Example usage with sum_and_sort_numbers function:
    result1 = sum_and_sort_numbers(3, 1, verbose=True)
    print(result1)

    result2 = sum_and_sort_number(5)
    print(result2)

    result3 = sum_and_sort_numbers(12, verbose=True)
    print(result3)
