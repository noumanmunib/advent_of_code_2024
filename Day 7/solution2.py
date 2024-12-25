from itertools import product

def evaluate_equation(numbers, operators):
    """
    Evaluate the equation formed by inserting the operators (+, *, ||) into the numbers list.
    Operators are evaluated left-to-right, ignoring mathematical precedence.
    """
    expression = str(numbers[0])  # Start with the first number as a string
    for i in range(len(operators)):
        if operators[i] == '+':
            expression = str(int(expression) + numbers[i + 1])
        elif operators[i] == '*':
            expression = str(int(expression) * numbers[i + 1])
        elif operators[i] == '||':
            expression += str(numbers[i + 1])  # Concatenate the numbers as strings
    return int(expression)  # Convert the final result back to an integer

def parse_input(file_path):
    """
    Parse the input file to extract test values and number lists.
    """
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            test_value, numbers = line.split(':')
            test_value = int(test_value.strip())
            numbers = list(map(int, numbers.strip().split()))
            equations.append((test_value, numbers))
    return equations

def find_solvable_equations(equations):
    """
    Determine which equations can be made true by inserting +, *, or || operators.
    """
    total_calibration = 0

    for test_value, numbers in equations:
        num_positions = len(numbers) - 1  # Number of operator positions
        found_solution = False

        # Generate all combinations of +, *, and || operators for the given positions
        for ops in product(['+', '*', '||'], repeat=num_positions):
            try:
                if evaluate_equation(numbers, ops) == test_value:
                    total_calibration += test_value
                    found_solution = True
                    break
            except Exception:
                continue  # Skip invalid evaluations

    return total_calibration

def main(file_path):
    equations = parse_input(file_path)
    result = find_solvable_equations(equations)
    print(f"Total Calibration Result: {result}")

if __name__ == "__main__":
    file_path = "E:/Advent of Code 2024/Day 7/input.txt"
    main(file_path)