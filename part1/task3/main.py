# define a decorator
def convert_to_lowercase(func):
    def wrapper(input_str):
        modified_str = input_str.lower()
        func(modified_str)
    return wrapper

# define a print method
@convert_to_lowercase
def print_lowercase(input_str):
    print("Result = " + input_str)

# use the print method
message = input("Enter your message = ")
print_lowercase(message)





