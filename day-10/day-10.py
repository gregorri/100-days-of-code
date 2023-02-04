# def format_name(name):
#     name = input("What is your name? ")
#     name = name.lower()
#     name = name.title()
#     return name

# print(format_name(""))

# def leap_year(year):
#     """Returns True if a year is a leap year, False if not."""
#     if year % 4 == 0 and(year % 400 == 0 or year % 100 != 0):
#         return True
#     return False

# def days_in_month(year, month):
#     """Returns the number of days in a month in a given year."""
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if leap_year(year) and month == 2:
#         return 29
#     if month > 12 or month < 1:
#         return "Invalid month"
#     return month_days[month - 1]

# year = int(input("Which year do you want to check? "))
# month = int(input("Which month do you want to check? "))
# days = days_in_month(year, month)
# print(days)


from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or 'c' to exit ") == "y":
            num1 = answer
    
        else:
            should_continue = False
            calculator()


calculator()


