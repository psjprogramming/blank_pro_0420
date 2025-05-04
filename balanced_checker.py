s=input()

stack=[]

if len(s)%2==1:
    print("NO")

else:
    for i in range(0,len(s)//2,1):
        stack.append(s[i])
        
        
    for j in range(len(s)//2,len(s)+1,1): #-1이면 for문 목표값이 미만이 아니라 초과인가?
 
        if stack!=[]:
        
            LastValue=stack.pop()
        
        
            if LastValue=='(':
                if s[j]==')':
                    pass
                else:
                    print("NO")
                    break
                
            elif LastValue=='[':
                    if s[j]==']':
                        pass
                    else:
                        print("NO")
                        break
                
                
            elif LastValue=='{':
                    if s[j]=='}':
                        pass
                    else:
                        print("NO")
                        break
            
            else:
                print("NO")
                break
        
        else:
            print("YES")