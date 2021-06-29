n=int(input())
s=0
# for i in range(1,n+1):
#     a=n%i
#     print("i=",i,"a=",a)
#     if(a==0):
#         sum+=i
# print("sum",sum)

print(sum([s+i for i in range(1,n+1) if n%i==0]))
