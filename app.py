"""_summary_

a. Generate Secure Password
b. Calculate and Format a Percentage
c. How many days from today until July 4, 2025?
d. Use the Law of Cosines to calculate the leg of a triangle.
e. Calculate the volume of a Right Circular Cylinder
f. Exit program
"""
import random
from datetime import date, datetime
import math
import sys


class UtilityProgram:
    """
    A class that provides a command-line interface (CLI) for performing various utility tasks.

    This program includes the following functionalities:
    - Generate a secure password.
    - Calculate and format a percentage.
    - Calculate the number of days between today and a specified target date.
    - Use the Law of Cosines to calculate the leg of a triangle.
    - Calculate the volume of a right circular cylinder.
    - Exit the program.
    """
    def __init__(self):
        """
        Initialize any required variables or settings.
        """
        self.today = datetime.today().date()
        self.date_to = date(2025, 7, 4)

    def get_valid_number(
            self, prompt="Enter a number: ",
            error_message="Invalid input. Please enter a valid number."
            ):
        """
        Prompts the user to input a number until a valid float is provided.

        Parameters:
            prompt (str): The input prompt message for the user.
            error_message (str): The error message to display when input is invalid.

        Returns:
            float: A valid float entered by the user.
        """
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print(error_message)

    def boolean_check(
            self, user_boolean_string="Enter a y/n value.\nyes (y) or no (n): ",
            error_message="Invalid input. Please enter a valid entry."
            ):
        """
        Prompts the user to input a boolean value until a valid boolean is provided.
        """
        while True:
            user_input = input(user_boolean_string).strip().lower()
            if user_input in ["yes", "y"]:
                return True
            if user_input in ["no", "n"]:
                return False
            print(error_message)

    def display_menu(self):
        """
        Display the options for the user.
        """
        print("\nMenu:")
        print("a. Generate Secure Password")
        print("b. Calculate and Format a Percentage")
        print("c. How many days from today until July 4, 2025?")
        print("d. Use the Law of Cosines to calculate the leg of a triangle.")
        print("e. Calculate the volume of a Right Circular Cylinder")
        print("f. Exit program")

    def generate_secure_password(self):
        """
        Logic to generate a secure password based on user preferences.
        """
        print("\nGenerate Secure Password:")
        # Get password length with validation
        user_password_character_number = self.get_valid_number(
            "Input the number of characters for the password (10-20): "
            )
        while not 10 <= user_password_character_number <= 20:
            print("Password length must be between 10 and 20.")
            user_password_character_number = self.get_valid_number(
                "Input the number of characters for the password (10-20): "
                )

        # Get user preferences
        use_of_upper_case = self.boolean_check(
            user_boolean_string="Use of Upper Case?\n(y/n): ",
            error_message="Invalid input. Please enter yes (y) or no (n)."
            )
        use_of_lower_case = self.boolean_check(
            user_boolean_string="Use of Lower Case?\n(y/n): ",
            error_message="Invalid input. Please enter yes (y) or no (n)."
            )
        use_of_numbers = self.boolean_check(
            user_boolean_string="Use of Numbers?\n(y/n): ",
            error_message="Invalid input. Please enter yes (y) or no (n)."
            )
        use_of_special_characters = self.boolean_check(
            user_boolean_string="Use of Special Characters?\n(y/n): ",
            error_message="Invalid input. Please enter yes (y) or no (n)."
            )

        # Build the pool of characters
        password_pool = ""
        if use_of_upper_case:
            password_pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if use_of_lower_case:
            password_pool += "abcdefghijklmnopqrstuvwxyz"
        if use_of_numbers:
            password_pool += "0123456789"
        if use_of_special_characters:
            password_pool += "!@#$%^&*()-_=+[]{}|;:,.<>/?"

        # Check if at least one option is selected
        if not password_pool:
            print("At least one option must be selected to generate a password.")
            return

        # Generate the password
        password = "".join(random.choices(password_pool, k=int(user_password_character_number)))
        print(f"Generated Secure Password: {password}")

    def calculate_and_format_percentage(self):
        """
        Calculate and format a percentage.
        """
        print("\nCalculate and Format a Percentage:")
        numerator = self.get_valid_number(
            "Input the numerator: ",
            "Please enter a valid number."
            )
        denominator = self.get_valid_number(
            "Input the denominator: ",
            "Please enter a valid number."
            )
        try:
            percentage = (numerator / denominator) * 100
            print(f"\nThe percentage is {percentage}%")
        except ZeroDivisionError:
            print("\nError: Denominator cannot be zero.")

    def days_until_date(self):
        """
        Calculate the number of days from today to a specified target date.
        """
        diff = self.date_to - self.today
        print(f"\nThere are {diff.days} days left till July 4, 2025.")

    def calculate_triangle_leg(self):
        """
        Use the Law of Cosines to calculate the length of a leg of a triangle.
        """
        a = self.get_valid_number("Input the length of side 'a'.\n: ")
        b = self.get_valid_number("Input the length of side 'b'.\n: ")
        angle_c_degrees = self.get_valid_number("Input the angle 'C' in degrees.\n: ")
        angle_c_radians = math.radians(angle_c_degrees)
        c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle_c_radians))
        print(f"\nThe length of side a is: {c}")

    def calculate_cylinder_volume(self):
        """
        Calculate the volume of a right circular cylinder.
        """
        radius = self.get_valid_number("Input the radius of the base.\n: ")
        height = self.get_valid_number("Input the height of the cylinder.\n: ")
        volume = math.pi * (radius ** 2) * height
        print(f"\nThe volume of the cylinder is: {volume} cubic units")

    def exit_program(self):
        """
        Exit the program gracefully.
        """
        print("\nExiting program. Goodbye!\n")
        sys.exit()

    def main(self):
        """
        Main loop for the program.
        """
        while True:
            self.display_menu()
            choice = input("Choose an option (a-f): ").lower()
            if choice == 'a':
                self.generate_secure_password()
            elif choice == 'b':
                self.calculate_and_format_percentage()
            elif choice == 'c':
                self.days_until_date()
            elif choice == 'd':
                self.calculate_triangle_leg()
            elif choice == 'e':
                self.calculate_cylinder_volume()
            elif choice == 'f':
                self.exit_program()
            else:
                print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    app = UtilityProgram()
    app.main()
