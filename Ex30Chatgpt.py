def parse_input(input_str):
    """
    Parse the input string to extract employee names and salaries.
    """
    try:
        data = input_str.strip().split(',')
        names = [data[i].strip() for i in range(0, len(data), 2)]
        salaries = [float(data[i + 1].strip()) for i in range(0, len(data), 2)]
        return names, salaries
    except (IndexError, ValueError):
        print("Invalid input format. Please enter names and salaries separated by commas.")
        return [], []


def find_top_paid(names, salaries):

    if not names or not salaries:
        return []

    max_salary = max(salaries)
    top_paid = [(name, salary) for name, salary in zip(names, salaries) if salary == max_salary]
    return top_paid


def main():
    input_data = input("Please enter employee names and salaries separated by commas (e.g., 'Mary, 2343, John, 2134'): ")
    employee_names, employee_salaries = parse_input(input_data)

    if not employee_names or not employee_salaries:
        return  # Exit if input parsing failed

    top_paid_employees = find_top_paid(employee_names, employee_salaries)
    print(top_paid_employees)
    print("Employees with the maximum salary:")
    for name, salary in top_paid_employees:
        print(f"{name} - {salary}")

    exit_command = input("Type 'exit' to close the program: ")
    if exit_command.lower() == "exit":
        quit()


main()