import mod4

count = 0
for i in range(165432, 707913):
    if mod4.testpassword(i):
        count += 1

print(f"The answer to day 4 part 1 is: {count}")

count = 0
for i in range(165432, 707913):
    if mod4.testpassword(i,2):
        count += 1

print(f"The answer to day 4 part 2 is: {count}")
