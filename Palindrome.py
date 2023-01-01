# # for string
# def isPalindrome(s):
#     return s == s[::-1]
# s = "malayalam"
# ans = isPalindrome(s)
#
# if ans:
#     print("Yes")
# else:
#     print("No")

# for Numbers
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")