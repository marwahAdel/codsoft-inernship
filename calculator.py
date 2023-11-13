def math_add(num1,num2):
    return print("result = ",num1+num2)
def math_sub(num1,num2):
    return print("result = ",num1-num2)
def math_multi(num1,num2):
    return print("result = ",num1*num2)
def math_divid(num1,num2):
    if num2 == 0 :
        return "Cannot divide by zero"
    return print("result = ",num1/num2)
def main():
    while True:
        print("CALCULATOR:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")


        choice = input("Enter your choice: ")
        num1 = float(input(" please enter first number: "))
        num2 = float(input(" please enter second number: "))

        if choice == "1":
            print("please enter two number")
            math_add(num1,num2)
        elif choice == "2":
            math_sub(num1,num2)
        elif choice == "3":
            math_multi(num1,num2)
        elif choice == "4":
            math_divid(num1,num2)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == '__main__':
    main()
