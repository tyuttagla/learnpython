#string test

month=input(">>").strip().upper()
#     012345678901234567890123456789012345
abbr="JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDEC"
k=abbr.find(month)
if k==-1:
       print("invalid month abbreviation")
else:
       print(month,"---->",1+k//3)
       
       


#1 s=input().strip()
# b=''
# for e in s:
#     b+=e*2
# print(b)
# #2
# s=input().strip()
# t=''
# s=' '+s+' '
# for i in range(1,len(s)-1):
#     t+=s[i]
#     if s[i-1]!=s[i]!=s[i+1]:
#         t+=s[i]
# print(t)

#3
# s=input().strip()
# print("length=",len(s))
# # if len(s)%2==0:
# #     for i in range(0,int((len(s)/2))):
# #         if s[i]==s[len(s)-1-i]:
# #             print("ok")
# #         else: print('false')
# # else:
# #     for i in range(0,int((len(s)//2))):
# #         if s[i]==s[len(s)-1-i]:
# #             print("ok")
# #         else: print('false')
# print(s)
# print(s[::-1])
# if s==s[::-1]:
#     print('OK')
# else: print('NG')

#4
# d=int(input())
# n=int(input())
# if len(str(d))>=n:
#     od=str(d)
# else:
#     c=int(n-len(str(d)))
#     od='0'*c+str(d)
# print (d,n,od)
# #4-Ans
# t="0"*n+str(d)
# t=t[-max(n,len(str(d))):]
# print(t)
# #5
# num16=input().strip()
# num16set='0123456789ABCDEF'
# num10='012345678910111213141516'
# upernum16=num16.upper()
# for c in upernum16:
#    k=num16set.find(c)
#    if k==-1:break
            










