n=94431605
m=679262176
s=5284458
if m > n:
        rem=m%n
        warn=(rem+s)-1
        print(warn)
elif m < n:
        warn=(s+m)-1
        print(warn)
else:
        print(s) 


# one line code --> return (s + m - 2) % n + 1; O(1)
