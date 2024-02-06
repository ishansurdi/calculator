class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        result = self.a + self.b
        print(f"Addition of {self.a} and {self.b} is {result}")
    def substraction(self):
        result = self.a - self.b
        print(f"Substraction of {self.a} and {self.b} is {result}")
    def multiplication(self):
        result = self.a * self.b
        print(f"Multiplication of {self.a} and {self.b} is {result}")
    def division(self):
        if self.b == 0:
            print("Invalid!")

        elif self.b>0:
            result = self.a / self.b
            print(f"Division of {self.a} and {self.b} is {result}")


print("Welcome to Calcultor!")
run_calculator = False
print("******MENU*****")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
run_calculator = True

while run_calculator:
    user_choice = int(input("Enter your choice: "))

    if user_choice == 5:
        run_calculator = False
        print("Thank you for using me! See you soon!")
        continue  # Skip further processing and start the next iteration of the loop

    user_input_1 = int(input("Enter your first number: "))
    user_input_2 = int(input("Enter your second number: "))

    calc = calculator(user_input_1, user_input_2)

    if user_choice == 1:
        calc.addition()
    elif user_choice == 2:
        calc.subtraction()
    elif user_choice == 3:
        calc.multiplication()
    elif user_choice == 4:
        calc.division()
    else:
        print("Invalid choice. Please enter a valid choice.")