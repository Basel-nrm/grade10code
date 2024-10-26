import time
for i in range(10, 0, -1):
    print(f"Number: {i}")
    time.sleep(0.5)

print("Countdown using for loop is complete!\n")

j = 10
while j > 0:
    print(f"Number: {j}")
    time.sleep(0.5)
    j -= 1

print("Countdown using while loop is complete!\n")

