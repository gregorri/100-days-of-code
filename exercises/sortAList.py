#Sort a list
first_parameter = input("List of numbers: ")
second_parameter = str(input("Use 'asc' for ascending or 'desc' for descending or 'none' for no sorting: "))

if second_parameter == "asc":
    parameter = "ascending"
elif second_parameter == "desc":
    parameter = "descending"
elif second_parameter == "none":
    parameter = "none"

def sort_list(first_parameter, parameter):
    # Convert the string of numbers into a list of numbers
    first_parameter = [int(num) for num in first_parameter.split()]
    if parameter == "ascending":
        first_parameter.sort()
        return first_parameter
    elif parameter == "descending":
        first_parameter.sort(reverse=True)
        return first_parameter
    elif parameter == "none":
        return first_parameter
    
print(sort_list(first_parameter, parameter))