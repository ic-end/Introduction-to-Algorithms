# �㷨����-�ڶ���-2.2
# ð������
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ð��������ǰ�С��Ԫ����ǰ�����߰Ѵ��Ԫ�������
# �Ƚ����ڵ�Ԫ�ء������һ���ȵڶ����󣬾ͽ�������������
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# BUBBLE-SORT��A��
# bubble_sort(A)
# {
#    for i = 1 to length[A]
#    {
#        for j = length[A] to i+1
#        {
#            if A[j] < A[j-1]
#            {
#                 exchane A[j] and A[j-1];
#            }
#        }
#    }
# }
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 2014. 09. 09
# lichao

import random

#import random
# �����������
# NΪ���鳤��
def gen_rand_n(N):
  A = []
  for i in range(1, N+1):
    A.append(random.randint(1,10*N)) 
  return A

# ð������
# ��A[0]��ʼ
# range(0,10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(10,0,-1) = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def bubbl_sort(A, N):
  temp = 0;
  for i in range(0, N):
    for j in range(N-1, i, -1):
        if A[j] < A[j-1]:
          temp = A[j]
          A[j] = A[j-1]
          A[j-1] = temp

  return A

# ������
N = 10
A = gen_rand_n(N)

print A

A = bubbl_sort(A, N)

print A
