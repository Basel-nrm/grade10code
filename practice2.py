from time import sleep

if __name__ == "__main__":
    for i in range(1, 11):
        print(i)
        sleep(0.5)
    print("Finished printing numbers using a for loop!\n")

    j = 1
    while (j <= 10):
        print(j)
        sleep(0.5)
        j += 1
    print("Finished printing numbers using a while loop!\n")

