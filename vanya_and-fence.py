lst = []
n, h = int(input("Enter two values: ")).split()
  
count = 0

for i in range(0, n):
    ele = int(input())
    lst.append(ele)   

for j in lst:
    if (j > h):
        count += 2

    else:
        count += 1

print(count)


