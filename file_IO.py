'''f=open("demo.txt","r")
#data=f.read(7)
data=f.readline()
print(data)
data=f.readline()
print(data)
f.close()
'''

f=open("demo.txt","w")
f.write("hoiii.. this is sonam frome delhi")
print(f)

f=open("demo.txt","a")
f.write(" \nhow are you all")
print(f)
f.close()   