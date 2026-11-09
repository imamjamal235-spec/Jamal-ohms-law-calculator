# ==========================================
# OHM'S LAW AND POWER CALCULATOR
# ND1 Mechatronics Engineering Project
#Author: Imam Jamal Adewale 
# ==========================================

# This list stores previous calculations.
calculation_history = []


# Function to collect and validate numerical input
def get_number(message, allow_zero=True):
    while True:
        try:
            number = float(input(message))

            if number < 0:
                print("Please enter a positive number.")
            elif not allow_zero and number == 0:
                print("Value cannot be zero.")
            else:
                return number

        except ValueError:
            print("Invalid input! Please enter a number.")


# Function to calculate voltage
def calculate_voltage():
    current = get_number("Enter current (A): ")
    resistance = get_number("Enter resistance (Ohms): ", False)

    voltage = current * resistance

    print(f"Voltage = {voltage:.2f} V")
    calculation_history.append(f"Voltage = {voltage:.2f} V")


# Function to calculate current
def calculate_current():
    voltage = get_number("Enter voltage (V): ")
    resistance = get_number("Enter resistance (Ohms): ", False)

    current = voltage / resistance

    print(f"Current = {current:.2f} A")
    calculation_history.append(f"Current = {current:.2f} A")


# Function to calculate resistance
def calculate_resistance():
    voltage = get_number("Enter voltage (V): ")
    current = get_number("Enter current (A): ", False)

    resistance = voltage / current

    print(f"Resistance = {resistance:.2f} Ohms")
    calculation_history.append(f"Resistance = {resistance:.2f} Ohms")


# Function to calculate electrical power
def calculate_power():
    voltage = get_number("Enter voltage (V): ")
    current = get_number("Enter current (A): ")

    power = voltage * current

    print(f"Power = {power:.2f} Watts")
    calculation_history.append(f"Power = {power:.2f} Watts")


# Main program
print("========================================")
print("     OHM'S LAW AND POWER CALCULATOR")
print("========================================")

# Loop keeps the calculator running
while True:

    print("\nWhat would you like to calculate?")
    print("1. Voltage")
    print("2. Current")
    print("3. Resistance")
    print("4. Power")
    print("5. View Calculation History")
    print("6. Exit")

    try:
        choice = int(input("\nEnter your choice (1-6): "))

        if choice == 1:
            calculate_voltage()

        elif choice == 2:
            calculate_current()

        elif choice == 3:
            calculate_resistance()

        elif choice == 4:
            calculate_power()

        elif choice == 5:
            print("\n===== CALCULATION HISTORY =====")

            if calculation_history:
                for record in calculation_history:
                    print(record)
            else:
                print("No calculations have been performed yet.")

        elif choice == 6:
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid choice! Please select between 1 and 6.")

    except ValueError:
        print("Invalid input! Please enter a number.")

