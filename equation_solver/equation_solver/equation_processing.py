import re

bcd_representation = {
    '0': [1, 1, 1, 1, 1, 1, 0],
    '1': [0, 1, 1, 0, 0, 0, 0],
    '2': [1, 1, 0, 1, 1, 0, 1],
    '3': [1, 1, 1, 1, 0, 0, 1],
    '4': [0, 1, 1, 0, 0, 1, 1],
    '5': [1, 0, 1, 1, 0, 1, 1],
    '6': [1, 0, 1, 1, 1, 1, 1],
    '7': [1, 1, 1, 0, 0, 0, 0],
    '8': [1, 1, 1, 1, 1, 1, 1],
    '9': [1, 1, 1, 1, 0, 1, 1],
}

def is_valid_equation(equation):
    try:
        operands, result = equation.split('=')
        return eval(operands) == eval(result)
    except ZeroDivisionError:
        return False
    except Exception as e:
        print(f"Error evaluating equation: {equation}. {e}")
        return False

def generate_valid_rearrangements(digit):
    digit_representation = bcd_representation[digit]
    count_ones = digit_representation.count(1)

    # Check other digits for equality
    equal_digits = [key for key, value in bcd_representation.items() if value.count(1) == count_ones]

    # Generate possible outcomes by adding or removing a bit
    adding_bit = []
    removing_bit = []

    for i in range(len(digit_representation)):
        modified_representation = digit_representation.copy()

        # Try removing a bit
        if modified_representation[i] == 1:
            modified_representation[i] = 0
            removing_bit.extend([key for key, value in bcd_representation.items() if value == modified_representation])

        # Try adding a bit
        modified_representation[i] = 1
        adding_bit.extend([key for key, value in bcd_representation.items() if value == modified_representation])

    # Remove duplicates and the original digit
    adding_bit = list(set(adding_bit) - {digit})
    removing_bit = list(set(removing_bit) - {digit})

    return equal_digits, adding_bit, removing_bit

def generate_combinations(input_str):
    combinations = []
    input_str = input_str.replace(" ", "")

    # Check if '=' is present in the modified string
    if '=' not in input_str:
        print("Invalid input: '=' not found.")
        return "Invalid input: '=' not found."

    # Split the operands after removing spaces
    operands, result = map(str.strip, input_str.split('='))
    if '+' in input_str:
        operator = '+'
    elif '-' in input_str:
        operator = '-'
    else:
        print("Only arithmetic addition and subtraction is possible")
        return "Only arithmetic addition and subtraction is possible"
    # Check if there are enough operands after splitting
    operand1, operand2 = map(str.strip, re.split(r'\+|\-', operands))
    equal_digits1, adding_bit1, removing_bit1 = generate_valid_rearrangements(operand1)
    equal_digits2, adding_bit2, removing_bit2 = generate_valid_rearrangements(operand2)
    equal_digits3, adding_bit3, removing_bit3 = generate_valid_rearrangements(result)

    # Append valid combinations based on the rules
    for equal_digit1 in equal_digits1:
        equation = f"{equal_digit1} {operator} {operand2} = {result}"
        if is_valid_equation(equation):
            combinations.append(equation)
    for equal_digit2 in equal_digits2:
        equation = f"{operand1} {operator} {equal_digit2} = {result}"
        if is_valid_equation(equation):
            combinations.append(equation)
    for equal_digit3 in equal_digits3:
        equation = f"{operand1} {operator} {operand2} = {equal_digit3}"
        if is_valid_equation(equation):
            combinations.append(equation)
    
    if operator == "+":
        for add_result1 in adding_bit1:
            for remove_result2 in removing_bit2:
                equation = f"{add_result1} {operator} {remove_result2} = {result}"
                if is_valid_equation(equation):
                    combinations.append(equation)
            for remove_result3 in removing_bit3:
                equation = f"{add_result1} {operator} {operand2} = {remove_result3}"
                if is_valid_equation(equation):
                    combinations.append(equation)
            equation = f"{add_result1} - {operand2} = {result}"
            if is_valid_equation(equation):
                combinations.append(equation)
            
        for add_result2 in adding_bit2:
            for remove_result1 in removing_bit1:
                equation = f"{remove_result1} {operator} {add_result2} = {result}"
                if is_valid_equation(equation):
                    combinations.append(equation)
            for remove_result3 in removing_bit3:
                equation = f"{operand1} {operator} {add_result2} = {remove_result3}"
                if is_valid_equation(equation):
                    combinations.append(equation)
            equation = f"{operand1} - {add_result2} = {result}"
            if is_valid_equation(equation):
                combinations.append(equation)
            
        for add_result3 in adding_bit3:
            for remove_result1 in removing_bit1:
                equation = f"{remove_result1} {operator} {operand2} = {add_result3}"
                if is_valid_equation(equation):
                    combinations.append(equation)
            for remove_result2 in removing_bit2:
                equation = f"{operand1} {operator} {remove_result2} = {add_result3}"
                if is_valid_equation(equation):
                    combinations.append(equation)
            equation = f"{operand1} - {operand2} = {add_result3}"
            if is_valid_equation(equation):
                combinations.append(equation)
    
    elif operator == "-":
        for add_result1 in removing_bit1:
            for remove_result2 in adding_bit2:
                equation = f"{add_result1} {operator} {remove_result2} = {result}"
                if is_valid_equation(equation):
                    combinations.append(equation)
            for remove_result3 in adding_bit3:
                equation = f"{add_result1} {operator} {operand2} = {remove_result3}"
                if is_valid_equation(equation):
                    combinations.append(equation)
            equation = f"{add_result1} + {operand2} = {result}"
            if is_valid_equation(equation):
                combinations.append(equation)
            
        for add_result2 in removing_bit2:
            for remove_result1 in adding_bit1:
                equation = f"{remove_result1} {operator} {add_result2} = {result}"
                if is_valid_equation(equation):
                    combinations.append(equation)
            for remove_result3 in adding_bit3:
                equation = f"{operand1} {operator} {add_result2} = {remove_result3}"
                if is_valid_equation(equation):
                    combinations.append(equation)
            equation = f"{operand1} + {add_result2} = {result}"
            if is_valid_equation(equation):
                combinations.append(equation)
            
        for add_result3 in removing_bit3:
            for remove_result1 in adding_bit1:
                equation = f"{remove_result1} {operator} {operand2} = {add_result3}"
                if is_valid_equation(equation):
                    combinations.append(equation)
            for remove_result2 in adding_bit2:
                equation = f"{operand1} {operator} {remove_result2} = {add_result3}"
                if is_valid_equation(equation):
                    combinations.append(equation)
            equation = f"{operand1} + {operand2} = {add_result3}"
            if is_valid_equation(equation):
                combinations.append(equation)
    if len(combinations) == 0:
        print("No valid combinations found")
        return "No valid combinations found"
    return combinations
