#Write a program that takes a number as input and outputs either "YES" or "NO" depending on the conditions. Conditions:

#if the number is odd, print "YES";
#if the number is even in the range from 2 to 5 (inclusive), then print "NO";
#if the number is even in the range from 6 to 20 (inclusive), then print "YES";
#if the number is even and greater than 20, output "NO".
num = int(input())
if num%2==1:
    print('YES')
elif num%2==0 and num>=2 and num<=5:
    print('NO')
elif num%2==0 and num>=6 and num<=20:
    print('YES')
elif num%2==0 and num>20:
    print('NO')
