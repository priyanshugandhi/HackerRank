# Enter your code here. Read input from STDIN. Print output to STDOUT
a = [raw_input()]
a.append(raw_input())
print "Hello"+str(a[0])+" "+str(a[1])+"! You just delved into python."

#optimized:
a = raw_input()
b = raw_input()
a,b=(b,a)
print a
print b
