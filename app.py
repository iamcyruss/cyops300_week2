"""_summary_

a. Generate Secure Password
b. Calculate and Format a Percentage
c. How many days from today until July 4, 2025?
d. Use the Law of Cosines to calculate the leg of a triangle.
e. Calculate the volume of a Right Circular Cylinder
f. Exit program
"""
import random


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

    def get_valid_number(self, prompt="Enter a number: ", error_message="Invalid input. Please enter a valid number."):
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
    
    def boolean_check(self, user_boolean_string="Enter a y/n value.\nyes (y) or no (n): ", error_message="Invalid input. Please enter a valid entry."):
        """
        Prompts the user to input a boolean value until a valid boolean is provided.

        Parameters:
            prompt (str): The input prompt message for the user.

        Returns:
            bool: A valid boolean entered by the user.
        """
        while True:
            user_input = input(user_boolean_string).strip().lower()
            if user_input in ["yes", "y"]:
                return True
            elif user_input in ["no", "n"]:
                return False
            else:
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

    def generate_secure_password_old(self):
        """
        Logic to generate a secure password.
        """
        list_of_options = []
        user_password_character_number = self.get_valid_number(prompt="Input the number of characters for the password? 10-20\n: ")
        use_of_upper_case = self.boolean_check(input("Use of Upper Case: "))
        use_of_lower_case = self.boolean_check(input("Use of Lower Case: "))
        use_of_numbers = self.boolean_check(input("Use of Numbers: "))
        use_of_special_characters = self.boolean_check(input("Use of special characters: "))
        list_of_options.extend([use_of_upper_case, use_of_lower_case, use_of_numbers, use_of_special_characters])

        print("Generating secure password...")
        for option in list_of_options:
            password_pool = ""
            if use_of_upper_case:
                password_pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if use_of_lower_case:
                password_pool += "abcdefghijklmnopqrstuvwxyz"
            if use_of_numbers:
                password_pool += "0123456789"
            if use_of_special_characters:
                password_pool += "!@#$%^&*()-_=+[]{}|;:,.<>/?"
        print("Password generated successfully!")

    def generate_secure_password(self):
        """
        Logic to generate a secure password based on user preferences.
        """
        print("\nGenerate Secure Password:")
        # Get password length with validation
        user_password_character_number = self.get_valid_number("Input the number of characters for the password (10-20): ")
        while not (10 <= user_password_character_number <= 20):
            print("Password length must be between 10 and 20.")
            user_password_character_number = self.get_valid_number("Input the number of characters for the password (10-20): ")
        
        # Get user preferences
        use_of_upper_case = self.boolean_check(user_boolean_string="Use of Upper Case?\n(y/n): ", error_message="Invalid input. Please enter yes (y) or no (n).")
        use_of_lower_case = self.boolean_check(user_boolean_string="Use of Lower Case?\n(y/n): ", error_message="Invalid input. Please enter yes (y) or no (n).")
        use_of_numbers = self.boolean_check(user_boolean_string="Use of Numbers?\n(y/n): ", error_message="Invalid input. Please enter yes (y) or no (n).")
        use_of_special_characters = self.boolean_check(user_boolean_string="Use of Special Characters?\n(y/n): ", error_message="Invalid input. Please enter yes (y) or no (n).")

        # Build the pool of characters
        password_pool = ""
        if use_of_upper_case:
            password_pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if use_of_lower_case:
            password_pool += "abcdefghijklmnopqrstuvwxyz"
        if use_of_numbers:
            password_pool += "0123456789"
        if use_of_special_characters:
            password_pool += "!@#$%^&*()-_=+[]\{\}|;:,.<>/?"
        
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
        numerator = self.get_valid_number("Input the numerator: ", "Please enter a valid number.")
        denominator = self.get_valid_number("Input the denominator: ", "Please enter a valid number.")
        try:
            percentage = (numerator / denominator) * 100
            print(f"The percentage is {percentage:.2f}%")
        except ZeroDivisionError:
            print("Error: Denominator cannot be zero.")

    def days_until_date(self, target_date):
        """
        Calculate the number of days from today to a specified target date.
        """
        print("Days until date calculation is not implemented yet.")

    def calculate_triangle_leg(self):
        """
        Use the Law of Cosines to calculate the length of a leg of a triangle.
        """
        print("Triangle leg calculation is not implemented yet.")

    def calculate_cylinder_volume(self):
        """
        Calculate the volume of a right circular cylinder.
        """
        print("Cylinder volume calculation is not implemented yet.")

    def exit_program(self):
        """
        Exit the program gracefully.
        """
        print("Exiting program. Goodbye!")

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
                self.days_until_date("2025-07-04")  # Placeholder argument
            elif choice == 'd':
                self.calculate_triangle_leg()
            elif choice == 'e':
                self.calculate_cylinder_volume()
            elif choice == 'f':
                self.exit_program()
                break
            else:
                print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    app = UtilityProgram()
    app.main()
