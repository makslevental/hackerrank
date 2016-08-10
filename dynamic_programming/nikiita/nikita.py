import sys, itertools
import math
sys.stdin = open("/home/maksim/dev_projects/hackerrank/dynamic_programming/nikiita/input/input00.txt", "r")

# t = int(input().strip())
# for _ in range(t):
#     n = int(input().strip())
#     arr = list(map(int,input().strip().split()))
# #     arr = list(map(math.log2,arr))
# #     arr = list(map(math.floor,arr))
#     sums = [[0 if i!=j else arr[i] for i in range(n)] for j in range(n)]
#     for i in range(n):
#         for j in range(i+1,n):
#             sums[i][j] = sums[i][j-1] + arr[j]
#     
# 
#     
#     
#         
# #     print()
#     splits = [[() for i in range(n)] for j in range(n)]
#     points = [[0 for i in range(n)] for j in range(n)]
#     for k in range(n):
#         for i in range(k+1,n):
#             for j in range(k,i+1):
#                 if sums[k][j] == sums[k][i] - sums[k][j]:
#                     splits[k][i] = (k,j,j+1,i,arr[k:j+1],arr[j+1:i+1],True)
# #                     splits[k][i] = j
# #                     points[k][i] = 1
# #     print('\n'.join(map(str,splits)))   
# #     print('\n'.join(map(str,points)))              
# #     print()                               
#     for i in range(n-1,-1,-1):
#         for j in range(i,n):
#                 if splits[i][j]:
#                     k,_,_,_,_,_,_ = splits[i][j]
# #                     try:
#                     points[i][j] = max(points[i][k],points[k+1][j])+1
# #                     except:
# #                     print(i,j)
# #                     k = splits[i][j]                  
#                                    
# #     print('\n'.join(map(str,points)))              
#     print(points[0][-1])

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    sums = list(itertools.accumulate(arr))
    
    summ = lambda i,j: sums[j]-sums[i-1] if i>0 else sums[j]

#     print("hello")
    splits = [[() for i in range(n)] for j in range(n)]
    points = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(i, j):
                if summ(i,k) == summ(k+1,j):
#                     splits[i][j] = (i,k,k+1,j,arr[i:k+1],arr[k+1:j+1],True)
#                     splits[i][j] = (i,k,k+1,j)
                    splits[i][j] = (True,k)
#                     splits[i][j] = (k)
#     print('\n'.join(map(str,splits)))   
#     print('\n'.join(map(str,points)))              
#     print()                               
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
                if splits[i][j]:
#                     print(i,j)
#                     _, jj, jjp, _ = splits[i][j]   
                    _,k = splits[i][j]
#                     k = splits[i][j]                          
#                     try:         
#                     print(i,j)
                    points[i][j] = max(points[i][k], points[k+1][j]) + 1
#                     except:
#                         print(n)
#                         print(splits[i][j])
#     print('\n'.join(map(str,points)))              
    print(points[0][-1])
