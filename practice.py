if __name__ == "__main__":
    # recieving numbers from user
    num1 = float(input("Please input a number"))
    num2 = float(input("Please input a second number"))
    num3 = float(input("Please input a third number"))
    if num1 == num2 == num3:
        print("All three numbers are equal. There is no largest number.")
    else:
        largest = max(num1, num2, num3)
        # presenting largest number
        print(f"The largest number is: {largest}")

    exit(0)

