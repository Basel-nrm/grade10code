
if __name__ == "__main__":

    num1 = float(input("input a number: "))
    num2 = float(input("input another number: "))
    product = num1 * num2
    # old style follows
    # print("The product of", num1, "and", num2, "is", round(product, 2))
    print(f"The product of {num1} and {num2} is {round(product, 2)}")
