# s=[10]*10
# print(s)
# a=s
# print(a)
# b=[1,2,3]
# c=[3,4,5]
# print(b+c)
# e=['f','g','h']
# print(e+c)
# c.append(6)
# print(c)
# c.insert(0,7)
# print(c)
# c.pop(0)
# print(c)
# c.insert(0,7)
# c.sort()
# print(c)
# c.insert(0,9)
# sorted(c)
# print(c)
# sorted(c)
# print(c)
# print(sum(c))
# print(max(c))
# c.insert(0,9)
# print(c.count(9))
# if 10 in c:
#     print('yes it is')
# else: print('nai')
# t='teerayuth yuttagla'
# s=t.split('t')
# print(s)
# v=t.split()
# print('t'.join(s))
# x=[11,12,13,14,15]
# c=x[1::2]
# print(c)
# x[0]=20
# print(x)
# print(x+[1,2])

# n=int(input())
# data=[]
# for k in range(n):
#     data.append(float(input()))
# for i in range(len(data)):
#     if data[i]<30:
#         data[i]+=0.1*data[i]
# print(data)
# # for i,c in enumerate(data):
# #     print(i,c)
# data_1=[]
# for e in data[::-1]:
#     data_1.append(e)
# print(data_1)
# d=0
# print('Input matrix 1')
# v1=[float(e) for e in input().split()]
# print(v1)
# print('Input matrix 2')
# v2=[float(e) for e in input().split()]
# print(v2)
# if len(v1)!=len(v2):
#     print("Data Error")
# else:
#     for k in range(len(v1)):
#         d+=v1[k]*v1[k]
# print(d)

# b=[x for x in range(0,2001)]
# print(b)

# v1=[float(e) for e in input().split()]
# lax=v1[0]
# for index in range(1,len(v1)):
#     if v1[index]>lax:
#         lax=v1[index]
# print(lax)
# a=max(v1)
# print(a)

# vowels=["a","e","i","o","u"]
# c=input("enter a charecter :")
# if c in vowels:
#     print("its a vowels")
# else: print("it's not")

# # List in for cycle.

# x=[1,2,3,4,6,6,7]
# sum=0
# for e in x:
#     sum+=e
# print("sum x= ",sum)

# # change some in list
# for i in range(0,len(x),2):
#     x[i]*=2
# print(x)

# # Find mode of data
# n=int(input("Enter the number of data:"))
# data=[]
# for k in range(n):   
#     data.append(float(input()))

# #list conpehension
# #Calculation moving average
# d = [float(x) for x in input(">>").split()]
# mov_avg= [(d[i-1]+d[i]+d[i+1])/3 for i in range(1,len(d)-1)]
# mov_avg.insert(0,(d[0]+d[1])/2)
# mov_avg.append((d[-2]+d[-1])/2)
# print(mov_avg)
# find pull out charector
# sentence = "teerayuth"
# t="".join([c for c in sentence if c not in "aeiou"])
# print(t)
# # make flatten list
# lists= [[1,2,3],[5,6],[7],[8,9],[10]] # all member shall be list
# x=[e for alist in lists for e in alist]
# print(x)

# #2
# p=[[x,y,z] for x in range(1,15) for y in range(x,115) for z in range(y,15) if x**2+y**2==z**2]
# print(p)
# #3
# n=5
# c=[j for i in range(2,5) for j in range(i*2,n*n,i) ]
# p_2=[x for x in range(2,n*n) if x not in c]
# print(c)
# print(p_2)
