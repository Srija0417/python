'''def show(n):
    if n==0:
        return 
    print(n)
    show(n-1)
    print("END")
show(9)    '''

'''def fact(n):
    if n ==0 or n==1 :
        return 1
    else:
        return fact(n-1)*n 
print(fact(5))
'''


'''def sumn(n):
    if n==0:
        return 0
    return sumn(n-1) + n 
sum=sumn(8)
print(sum)'''

lst=["a","b","c","d","t",5,4,6,7,7.9]
def lnth(list,idx=0):
    if idx==len(list):
        return
    print(list[idx])
    lnth(list,idx+1)
lnth(lst)    



 