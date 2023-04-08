import puppyTime
print("Welcome to the test runner! This is just for test purposes to verify that the test works.")
while True:
    print("Enter the test command:")
    req = input("")
    output = puppyTime.time(req)
    print(f'{output}\n')