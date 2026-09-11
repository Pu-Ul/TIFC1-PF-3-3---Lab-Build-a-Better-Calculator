def addmultiplenumbers(numbers):
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result


def isiteven(num):
    if isitaninteger(num) and num % 2 == 0:
        return True
    else:
        return False


def isitaninteger(num):
    if num == int(num):
        return True
    else:
        return False


def main():
    print("Hello learners!")

    while True:
        print("\n--- CALCULATOR ---")
        print("1. Add numbers")
        print("2. Multiply numbers")
        print("3. Is it even?")
        print("4. Is it an integer?")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            numbers = input("Enter numbers separated by spaces: ").split()
            numbers = [float(n) for n in numbers]
            print("Result:", addmultiplenumbers(numbers))
        elif choice == "2":
            numbers = input("Enter numbers separated by spaces: ").split()
            numbers = [float(n) for n in numbers]
            print("Result:", multiplymultiplenumbers(numbers))
        elif choice == "3":
            num = float(input("Enter a number: "))
            print("Is even:", isiteven(num))
        elif choice == "4":
            num = float(input("Enter a number: "))
            print("Is integer:", isitaninteger(num))
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()def main():
  print("Hello learners!")

if __name__=="__main__":
  main()
