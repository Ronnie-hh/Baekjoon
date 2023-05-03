N = int(input())
arr_A = list(map(int,input().split()))
M = int(input())
arr_B = list(map(int,input().split()))
arr_A.sort()

# for b in arr_B:
#     if b in arr_A:
#         print("1")
#     else:
#         print("0")

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end)//2

        if array [mid] == target:
            return 1
        elif array [mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return 0

for b in arr_B:
    result = binary_search(arr_A,b,0,N-1)
    print(result)