#https://www.hackerrank.com/challenges/py-if-else/problem
#python If-Else
def oddeve(n):
    if n%2==0 and 2 <= n <= 5:
        return 'Not Weird'
    elif n%2!=0:
        return 'Weird'
    elif n%2==0 and 6 <= n <= 20:
        return 'Weird'
    elif n%2==0 and n>20:
        return 'Not Weird'

print(oddeve(int(input())))
