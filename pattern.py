R = 5
for i in range(0, R):
    for j in range(0, i+1):
        print("*", end=" ")
    print("\r")
for i in range(R, 0, -1):
    for j in range(0, i-1):
        print("*", end= " ")
    print("\r")
