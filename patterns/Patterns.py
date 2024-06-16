# #Pattern 1
# '''
# E D C B A
#   4 3 2 1
#     C B A
#       2 1
#         A
# '''

# n = 5
# letter = 64
# for i in range(n):
#     for j in range(n):
#        if i > j:
#            print(" ",end=" ")
#        else:
#            if i % 2 == 0:
#               print(chr(letter+n-j),end=" ")
#            else:
#                print(n-j,end=" ")
#     print("")

# #Pattern 2

# '''
# A
# 2 1
# A B C
# 4 3 2 1
# A B C D E

# '''

# for i in range(n):
#     for j in range(n):
#        if i < j:
#            print(" ",end=" ")
#        else:
#            if i % 2 == 0:
#               print(chr(letter+1+j),end=" ")
#            else:
#                print(i+1-j,end=" ")
#     print("")

# #Pattern 3

# '''
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# '''
# n = 5

# for i in range(1,n+1):
#     for j in range(1,n*2+1):
#         if j < n- i+1 or j > n+i-1:
#            print(" ",end=" ")
#         else:
#             print("*",end=" ")

#     print(" ")

# #Pattern 4

# '''
#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *

# '''

# for i in range(1,n+1):
#     for j in range(1,n*2):
#         if j==(n-i+1) or j==(n+i-1) or i ==n:
#            print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")

# #Pattern 5
# '''

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# '''
# n=5
# for i in range(1,n+1):
#     for j in range(1,n*2+1):
#         if j >= i and j <= n*2-i:
#            print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print(" ")

n=6  
for i in range(1,n+1):
    for j in range(1,n*2+1):
        if (j >= i and j <= n*2-i):
           print("*",end=" ")
        else:
            print(" ",end=" ")

    print(" ")