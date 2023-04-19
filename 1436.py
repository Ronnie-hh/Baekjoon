N=int(input())
i=0
flag=0

while True:
    i+=1
    i=str(i)
    cnt=0
    lst=[0]  

    for k in range(len(i)):
        if i[k]=='6':
            cnt=1
            for j in range(k+1,len(i)):
                if i[j]=='6':
                    cnt+=1
                else:
                    break
            lst.append(cnt)
        else:
            pass
    

    contiue_six = max(lst)
    i = int(i)

    if contiue_six>=3:
        flag+=1
        
        if flag==N:
            print(i)
            break
    else:
        pass
        
        

        


