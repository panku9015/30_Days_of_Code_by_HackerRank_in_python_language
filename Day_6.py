T = int(input("Enter no:- "))

for i in range(T):
    even = ""
    odd = ""
    S = input("Enter string:- ")
    for j in range(1, (len(S)+1)):
        if j % 2 == 0:
            even += S[j - 1]
        else:
            odd += S[j - 1]
    print(odd," ",even)
