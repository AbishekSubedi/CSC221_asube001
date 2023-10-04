import functions as func  # imports functions.py module as func for main.py

# Call the functions with appropriate arguments
book_title = func.favorite_book("Harry Potter")
print(book_title)

shirt_result = func.make_shirt(size="Small", message="Python Developer")
print(shirt_result)

car = func.cars("Toyota", "Camry", year=2023, color="Silver")
print(car)

result = func.sum_and_sort_numbers(7, 3.5)
print(result)

# help(func)
