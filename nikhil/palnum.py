n=int(input())
n=n+int(str(n)[::-1])
def is_palindrome(s):
    b=str(s)
    a=b[::-1]
    if b==a:
        return True
    return False
while(not is_palindrome(n)):
    n=n+int(str(n)[::-1])

print(n)