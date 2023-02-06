print("Decimal to binary converter")

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

decimal = int(input("Enter a decimal number: "))
print(decimal_to_binary(decimal))