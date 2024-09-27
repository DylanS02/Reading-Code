import time
#test
howlong = input("How many minutes do you want to work? ")

# Simple version
# time.sleep(int(howlong) * 60)

# Better version
for i in range(int(howlong)):
    time.sleep(60)
    print(".", end="", flush=True)


print("Stop!")
