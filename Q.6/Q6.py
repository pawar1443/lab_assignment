def count_up_to(n):
    count = 0
    i = 1
    while count <= n:
        if i % 2 == 0:
            yield i
            count +=1
        i+=1

n = int(input("enter a number : "))
ans = 0
for num in count_up_to(n-1):
    ans += num
    
print(ans)
