import sys
K, N = map(int,input().split())

lenarr= [int(sys.stdin.readline().rstrip()) for _ in range(K)]

start=1
end=sum(lenarr)//N
# end = max(lenarr)

def check(cuttinglength):
    sum = 0
    
    for lenline in lenarr:
        
        result = lenline//cuttinglength
        sum += result

    if (sum >= N):
        return True
    else:
        return False


while (start <= end):
    
    mid = (start + end) // 2
    
    if (check(mid)==True): 
        start = mid+1
        
    else:
        end = mid -1
    
print(end)

    
    

