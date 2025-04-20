inputvalue=input("문자열을 입력하시오.")

b=0

i=0

s=inputvalue[0]

inputvalue=list(inputvalue)

a=len(inputvalue)-1

for j in range(1,a):
    
    j-=b

    if inputvalue[i]==inputvalue[j]:
  
        inputvalue.remove(inputvalue[i])
        inputvalue.remove(inputvalue[j-1])
        a-=2
        b+=2
        i=0

        
    
    else:
        i+=1    
        
if inputvalue==[]:
    print(1)
else:
    print(0)