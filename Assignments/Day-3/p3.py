# to find biggest of two number using lambda function
n, m, o = eval(input("enter the three numbers"))
biggest = lambda n, m, o: n if n > m and n > o else m if m > o else o
print(biggest(n, m, o))
