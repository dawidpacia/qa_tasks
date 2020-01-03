def read_file(filename: str) -> list:
    mass_values = []
    with open(filename) as file:
        for value in file.readlines():
            mass_values.append(int(value))
    return mass_values


def calculate_fuel(mass: int) -> int:
    # 2.x --> 1/2 = 0
    # 3.x --> 1/2 = 0.5

    fuel = mass//3 - 2
    return fuel


def sum_fuels(mass_list: list) -> int:
    sum = 0
    for value in mass_list:
        sum += calculate_fuel(value)
    return sum


mass_values = read_file("input.txt")
total_fuel = sum_fuels(mass_values)

print(total_fuel)
