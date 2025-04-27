inputvalue=input("문자열을 입력하시오.") #입력받기

stack=[]#stack이 반복문을 다 돌았을 때 []의 상태라면 1을 출력한다.


for j in inputvalue:
    
    if stack!=[] and stack[-1]==j:
        stack.pop()
        
        
    else:
        stack.append(j)

if stack!=[]:
    print(0)
    
else:
    print(1)