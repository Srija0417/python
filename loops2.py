'''lst=[1,4,9,16,25,36,49,64,81,100]
n=int(input())
c=0
for e in lst:
    c+=1
    if e==n:
        print("found",e,"at",c)
        break
    else:
        continue 
else:
    print("not found")    '''


'''
for e in range(100,0,-1):
    print(e)'''



'''#multiplication table
n=int(input())
for e in range(1,11):
    print(str(n)+"*"+str(e)+"=",n*e)
'''

'''#factorial
n=int(input())
f=1
for e in range(1,n+1):
    f*=e 
print(f)    '''


n=int(input())
s=0 
for e in range(1,n+1):
    s+=e 
print(s)    

 