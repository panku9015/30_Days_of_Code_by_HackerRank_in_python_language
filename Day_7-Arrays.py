n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
for i in range(len(arr),0,-1):
    print(arr[i-1])
