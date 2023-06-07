import math as m

N = int(input())

#틀린 풀이-N이 너무 크면 overflow가 발생함
# M=N
# for _ in range(N-1):
#     M=M*(N-1)
#     N=N-1

#sol1) math.factorial()함수 사용하기
# M=m.factorial(N)
# M_lst=list(str(M))
# M_lst=list(reversed(M_lst))

# cnt=0

# for i in range(len(M_lst)):
#     if M_lst[i]=='0':
#         cnt+=1
#     else:
#         print(cnt)
#         break

# sol2) 5, 25, 125로 나눈 개수로 구하기
print(N//5+N//25+N//125)


