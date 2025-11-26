n = int(input())
total = 1
for i in range(1, n+1):
    print()
    for j in range(i):
        print(total, end=' ')
        total += 1