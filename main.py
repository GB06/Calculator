def main():
	def add(num1, num2):
		return num1 + num2

	def subtract(num1, num2):
		return num1 - num2

	def multiply(num1, num2):
		return num1 * num2

	def divide(num1, num2):
		return num1 / num2

	print("Select operation -\n"
	      "1) Add\n"
	      "2) Subtract\n"
	      "3) Multiply\n"
	      "4) Divide\n")

	select = int(input("Choose operation (1 - 4): "))
	number1 = int(input("Enter number 1: "))
	number2 = int(input("Enter number 2: "))

	if select == 1:
		print(f"{number1} + {number2} =", add(number1, number2))
	elif select == 2:
		print(f"{number1} - {number2} =", subtract(number1, number2))
	elif select == 3:
		print(f"{number1} * {number2} =", multiply(number1, number2))
	elif select == 4:
		print(f"{number1} / {number2} =", divide(number1, number2))
	else:
		print("Invalid input")

	repeat = input("Do you want to count again? (y/n): ").lower()
	if repeat == "y":
		main()
	else:
		print("Bye")
		exit()

main()