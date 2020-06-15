#list

# 1. Write a Python program to sum all the items in a list.
# 2. Write a Python program to multiplies all the items in a list.

# l=[1,1,1,1,1]
# def sum(items):
#     sum=0
#     m=0
#     for i in items:
#         sum=sum+i
#         m=sum*i
#
#     print("sum=",sum)
#     print("mul=",m)
#
# sum([10,10,10])
# print(sum([1,1,1]))

# 3. Write a Python program to get the largest number from a list.

# ls=[4,5,2,3,7,98,89]
# n=len(ls)
# temp=0
# min=ls[0]
# def large(list):
#     max=list[0]
#     for i in list:
#         # if max<ls[i]:
#         #     temp=ls[i]
#         #     ls[i]=max
#         #     max=temp
#         if i>max:
#             max = list[i]
#     print("max=",max)
#
# large([4,5,2,3,7,98,89])

# 4. Write a Python program to get the smallest number from a list.

# def min(ls):
#     min=ls[0]
#     for i in ls:
#         if min>i:
#             min=ls[i]
#     print("min=",min)
#
# min([4,5,2,3,7,98,89])

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

# def fnl(words):
#     cnt=0
#     for word in words:
#         if len(word)>2 and word[0]==word[-1]:
#             cnt+=1
#     print(cnt)
#
# fnl(['abc','xyz','aba','1221'])

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# def last(n):
#     return n[-1]
#
# def sort_list_last(tuples):
#     return sorted(tuples, key=last)
#
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# q
# a = [10,20,30,20,10,50,60,40,80,50,40]
#
# dup_items=set()
# uniq_items=[]
#
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)
# print(uniq_items)

# q
# l=[1]
#
# if not l:
#     print("Empty list")
# else:
#     print("not empty",l)

# q
# l1=[1,2,3,4,5]
# l2=l1.copy()
# print(l1)
# print(l2)

# q
# def long_words(n,str):
#     word_len=[]
#     txt=str.split(" ")
#
#     for x in txt:
#         if len(x)>n:
#             word_len.append(x)
#     return word_len
#
# print(long_words(3,"The quick brown fox jumps over the lazy dog"))

#q
# l1=[1,'abc']
# l2=[1,2,'abc']

# def common(l1,l2):
#     for x in l1:
#         for y in l2:
#             if x==y:
#                 pass
#     print("true")
#
#
# common([1,2,3,4,5],[4,5,6,7,8])

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # color =[ for (i,x) in enumerate(color) if i not in (0,4,5)]
#
# l=[value for index,value in enumerate(l)
#         if index not in(0,4,5)]
# print(l)

# q

# array=[[['*' for i in range(6)]
#         \n for i in range(4)]
#        \n for i in range(3)]
# print(array)

# q
# ls=[1,2,3,4,5,6,7,8,9

# ls=[x for x in ls if x%2!=0]
# print(ls)

# q

# for i in range(1,31):
# #     sq=i**2
# #     if i>=6 and i<=25:
# #         continue
# #     print("square of",i,"=",sq)

# or

# ls=[]
# for i in range(1,21):
#     sq=i**2
#     ls.append(sq)
# print(ls[:5])
# print(ls[-5:])

#q
# import itertools
# ls=['a','b','c']
# ls2=list(itertools.permutations(ls))
# print(ls2)
# # print(list(itertools.permutations(ls)))

# q
# l1=[1,1,1,2,3,4]
# l2=[4,4,4]
#
# dif=list(set(l1)-set(l2))
# print(dif)

# q
# l=[1,2,3,4,5]
# for index,val in enumerate(l):
#     print(index,val)

# q
# char=['j','a','v','a']
# # print(char)
# # str=" "
# # for i in char:
# #     str+=i
# # print(str)
#
#
# print(''.join(char))
# # print(str)

# q
# num=[1,2,3,4,5,6]
# print(num.index(3))

# q
# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# new=[]
# for x in enumerate(original_list):
#     new.append(x)
# print(new)

# or
# import itertools
#
# og_ls=[[2,4,3],[1,5,6],[9],[7,9,0]]
# new_ls=list(itertools.chain(*og_ls))
# print(new_ls)

# q
# l1=[1,2,3,4]
# l2=list()
# l2.append(l1)
# print(l2)

# l1=[1,2,3,4]
# l2=[]
# for i in l1:
#     l2.append(i)
# print(l2)

# q
# import random
# color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print(random.choice(color))

#q
# l1=[1,2,3,4]
# l2=[1,3,2,7]
#
# [i for i in enumerate(l1)]
# [j for j in enumerate(l2)]
# if i==j:
#     print("identical")

#or
# list1 = [10, 10, 0, 0, 10]
# list2 = [10, 10, 10, 0, 0]
# list3 = [1, 10, 10, 0, 0]
# #
# print('Compare list1 and list2')
# print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
# print('Compare list1 and list3')
# print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

#q
import itertools

# def second_smallest(numbers1):
#   numbers=list(itertools.chain(*numbers1))
#   if (len(numbers)<2):
#     return
#   if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
#     return
#   dup_items = set()
#   uniq_items = []
#   for x in numbers:
#     if x not in dup_items:
#       uniq_items.append(x)
#       dup_items.add(x)
#   uniq_items.sort()
#   return  uniq_items[1]
#
# print(second_smallest([[1, 2], [-8, -2], 0, -2]))
# print(second_smallest([1, 2, -8, -2, 0, -2]))
# print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
# print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# print(second_smallest([2,2]))
# print(second_smallest([2]))

# q
# ls=[1,1,5,2,6,3,7,4]
# dup_items=set()
# uniq_items=[]
# for x in ls:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)
# print(uniq_items)

#or
# ls=[1,1,5,2,6,3,7,4]
# newset=set(ls)
# new=list(newset)
# print(new)

# qls=[5,5,5,6,6,6,6,2,2,1,1,1,1,1,8]
ls=[5,5,5,6,6,6,6,2,2,1,1,1,1,1,8]
# # n=len(ls)
# cnt=0
# dup=set()
# for i in ls:
#     cnt=ls.count(i)
#     if i not in dup:
#         dup.add(i)
#         print(i,"=",cnt)

#or
# import collections
# # ls=[5,5,5,6,6,6,6,2,2,1,1,1,1,1,8]
# # ctr=collections.Counter(ls)
# # print(ctr)

#q

# def count_range(list,min,max):
#     cnt=0
#     for x in list:
#         if min<=x<=max:
#             cnt+=1
#     print(cnt)
#
# count_range([10,20,30,40,40,40,70,80,99],40,100)
# count_range(['a','b','c','d','e','f'],'a','e')

# q
# import itertools
# ls=['a','b','c','d']
# new=list((itertools.permutations(ls)))
# print(new)

#q
# def prime_eratosthenes(n):
#     prime_list = []
#     for i in range(2, n+1):
#         if i not in prime_list:
#             print (i)
#             for j in range(i*i, n+1, i):
#                 prime_list.append(j)
#
# print(prime_eratosthenes(100))

#or
# r=int(input("Enter upper limit: "))
# for a in range(2,r+1):
#     k=0
#     for i in range(2,a//2+1):
#         if(a%i==0):
#             k=k+1
#     if(k<=0):
#         print(a)

#q
# ls=['p','q']
# n=4
# new=['{}{}'.format(x,y)
#      for y in range(1,n+1)
#      for x in ls]
# print(new)

#q
# x=100
# print((id(x)))

#q
# l1=[1,2,3,4,5,6]
# l2=[4,5,6,7,4]
#
# # print(set(l1) & set(l2))
#
# dup=set()
# for x in l1:
#     for y in l2:
#         if x==y:
#            print(x)

# q
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]

# ls=[0,1,2,3,4,5]
# n=len(ls)
# temp=0
# for i in range(0,n,2):
#     temp=ls[i+1]
#     ls[i+1]=ls[i]
#     ls[i]=temp
#
# print(ls)

# Sample list: [11, 33, 50]
# Expected Output: 113350

# ls=[11,33,50]
# x="".join(map(str,ls))
# print(x)


#q
from itertools import groupby
from operator import itemgetter
# word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
#      'look','want','give','use','find','tell','ask','work','apple','seem','feel','leave','call']
# word_list.sort()
# for x in word_list:
#     print(x[0]),x)

# for i,x in groupby(sorted(word_list),key=itemgetter(0)):
#     print(i)
#     for y in x:
#         print(y)

#q
# obj={}
# for i in range(1,21):
#     obj[i]=[]
# print(obj)

#q
# list1 = ['a','b','c','d','e','f']
# list2 = ['d','e','f','g','h']
#
# print("Missing val:")
# for i in list1:
#     if i not in list2:
#         print(i,end=" ")
#
# print("\nAdditional val:")
# for i in list2:
#     if i not in list1:
#         print(i,end=" ")

# print('Missing values in second list: ', ','.join(set(list1).difference(list2)))
# print('Additional values in second list: ',','.join(set(list2).difference(list1)))

#q
# color=[('Black', '#000000', 'rgb(0, 0, 0)'),
# #         ('Red', '#FF0000', 'rgb(255, 0, 0)'),
# #         ('Yellow', '#FFFF00', 'rgb(255, 255, 0)')]
# #
# # # var1,var2,var3=color
# #
# # print(color[0])
# # # print(var2)
# # # print(var3)

#q
# l=[[5*i+j for j in range(1,6)] for i in range(5)]
# print(l)

#q
import itertools
# ls=[(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
# #  (7, 8), (9, 10)]
# #
# # # new=list(itertools.chain(*ls))
# # # nset=set(new)
# # # print(nset)
# #
# # # or
# # print(set().union(*ls))

#q
#
# ls=[1,2,3,4,5,6,7,8,9,10]
# # l=[i for i in (ls) if i%2!=0]
# # print(l)
#
# print(ls[0::2])

#q
# color=['red','green','blue']
# print(color)
# color=[i for x in(color) for i in('c',x)]
# print(color)

#q
# color=[['red'],['green'],['blue']]
# # for x in color:
# #     print(list(x))
#
# print('\n'.join([str(x) for x in color]))

#q
# name=["Black", "Red", "Maroon", "Yellow"]
# code=["#000000", "#FF0000", "#800000", "#FFFF00"]
# print([{'name':n,'code':c} for n,c in zip(name,code)])

#q
from operator import itemgetter
# ls=[{'key':{'subkey':5}},{'key':{'subkey':10}},{'key':{'subkey':1}}]
# # new=sorted(ls,key=itemgetter('subkey'))
#
# ls.sort(key=lambda e: e['key']['subkey'],reverse=True)
# print(ls)

#q
# ls=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
#
# for i in range(3):
#     print(ls[i::3],end=" ")

# q
from collections import Counter
# l1=["red", "orange", "green", "blue", "white"]
# l2=["black", "yellow", "green", "blue"]
#1
# cnt1=Counter(l1)
# cnt2=Counter(l2)
# print(list(cnt1-cnt2))
# print(list(cnt2-cnt1))
#2
# for x in l1:
#     if x not in l2:
#         print(x)
#3
# print(set(l1).difference(l2))
# print(set(l2).difference(l1))
#4---common
# print(set(l1) & set(l2))

#q
# ls=[]
# n=int(input("Enter the no: "))
# # new=list()
# for i in range(1,n+1):
#      if i<=n:
#           ls.append(i)
# print(ls)

#q
# ls=['h','i','i','e']
# print(''.join(ls))
# print('-'.join(ls))

#q
# ls=[{'key1':'val1','key2':'val2'},
#     {'key1':'val1','key2':'val2'}]
#
# new=[{k: v for k,v in x.items() if k!='key1'} for x in ls]
# print(new)

#q
# import ast
# # ls=[]
# string="the hustle"
# # for i in string:
# #      if i==" ":
# #           pass
# #      else:
# #           ls.append(i)
# # print(ls)
#
# print(ast.literal_eval(string))

#q
# color1 = ["green", "orange", "black", "white"]
# color2 = ["green", "green", "green", "green"]
# # n=len(color1)
# [c for c  in (color2) if c=='green']
# print(True)

#or
# color1 = ["green", "orange", "black", "white"]
# color2 = ["green", "green", "green", "green"]
#
# print(all(x=="green" for x in color1))
# print(all(x=="green" for x in color2))

#q
import itertools
# a=[1, 3, 5, 7, 9, 10]
# b=[2, 4, 6, 8]
#
# a[-1: ]=b
# print(a)

#q
# x=[55,66,77,88,99,44]
#
# xlen=len(x)-1
# print(x[xlen])

#q
# l=[{} for i in range(5)]
# print(l)
# # for i in range(5):
# #      l.append({})
# # print(l)

#q

# ls=[1,2,3,4]
# d={'k1':1,'k2':2}
# # n=" ".join(ls)
# # print(n)
#
# print(*ls)
# print(**d)

#q
# list = [1,2,3,4]
#
# print(['emp{0}'.format(i) for i in list])

# n=len(list)
# ls=str(list)
# x = 'emp'
# for i in range(n):
#      if i<=n:
#           print(x.join(ls))
# # print(list)

#q

# num=[1,2,3]
# color=['red','yellow','green']
#
# for a,b in zip(num,color):
#      print(a,b)

#q
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# print(list(num)[0])

#q
# num = [[1,2,3],[1,2,4] ,[4,5,6], [10,11,12], [7,8,9]]
# print(min(num))

#q
# l1=[1,2,3,4,5,6,7,8,8]
# l2=[201,400,500]
#
# print(all(x>=200 for x in l2))

# n=5
# for i in l1:
#      if i>n:
#           print(i)

#q
# x = [10, 20, 30]
# y = [40, 50, 60]
#
# x[len(x): ]=y
# print(x)

#q
# ls=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# # n=len(ls)
# # for i in range(n):
# #      if ls[i]!=ls[i+1]:
# #           print(ls[i])
# ls.sort()
# print(ls)
# new=list(x for x,i in itertools.groupby(ls))
# print(new)

#q
ls= {'a':1, 'b': {'c': {'d': {}}}}
new=[{k: v for k,v in ls.items() for d in ls}]
print(len(new))



