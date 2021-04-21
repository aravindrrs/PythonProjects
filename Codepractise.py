
# #1
# def divisible_by_three(st):
#     l = [int(char) for char in st] #splitting a word and converting into an integer
#     sum = 0
#     for item in range(len(l)):
#         sum = sum + l[item]        #adding each item to of the list with the previous item

#     if sum % 3 == 0:
#         return True

#     else:
#         return False

#     pass
#2
# def divisible_by_three(s):
#     return not int(s) % 3

# print (divisible_by_three("120"))


# #convert list of binaries into dec
# def binary_array_to_number(arr):
#     return int(''.join(str(a) for a in arr), 2)

# def song_decoder(song):
#     s=song.replace("WUB" , " ")
#     print (s)
#     ss=s.split()
#     print (ss)
#     sj=' '.join(ss)
#     return sj

# print (song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))

#
#
# class candidate():
#    def __init__(self,name,age,exp_claim):
#     self.name=name
#     self.age=age
#     self.exp_claim=exp_claim
#
#    def experience(self,DOB,application_date,graduation_date):
#         appdate_split= application_date.split('/')
#         for i in appdate_split:
#             appdate_year=int(i)
#         graddate_split=graduation_date.split('/')
#         for j in graddate_split:
#             grad_year=int(j)
#
#         exp_calculated= appdate_year - grad_year
#         print ("calculated experience: {} \nclaimed experience:{}".format(exp_calculated,self.exp_claim))
#         if exp_calculated >= self.exp_claim:
#             print ( "candidate is honest")
#         else:
#             print ("candidate is lying")
#
#
# candidate1=candidate('Aravind',30,8)
# candidate1.experience('04/09/1989','06/14/2020','01/04/2016')



# class candidate():
#     def __init__(self,name,age,education):
#         self.name=name
#         self.age=age
#         self.education=education
#
#     def job(self,exp):
#         print ("experience needed:", exp)
#
#
# candidate1=candidate("aravind",30,"Masters")
# candidate1.job(12)
# print (candidate1.name.upper())
# print ("The experience of {} is {}".format(candidate1.name,candidate1.age-22))




# class c:
#     def __init__(self,a):
#         self.a=a
#
#     def calc(self):
#
#
#         for i in range (0, int(self.a/2)):
#             for j in range(0,int(self.a/2)):
#
#                  if self.a==i**2 + j**2:
#                     return True
#
#         return False
#
# c1=c(25)
# print (c1.calc())
#
#
#
# def calc(self,a):
#     for i in range(0, int(self.a / 2)):
#         for j in range(0, int(self.a / 2)):
#
#             if self.a == i ** 2 + j ** 2:
#                 return True
#
#     return False
#
#
#
# print(calc(5))


#reverse a string using
# inp= input("Enter the string to be reversed:")
# #inp_list =[x for x in inp[::-1]]
# inp_list=list(inp[::-1])
#
# print (''.join(inp_list))

#palindrome
# inps= input("Enter the string to be reversed:")
# if list(inps)==list(inps[::-1]):
#     print ("this is a palindrome")
# else :
#     print ("dumbass")




# class Classy(object):
#     def __init__(self):
#         self.items = []
#
#     def addItem(self, item):
#         self.items.append(item)
#         print(self.items)
#
#     def getClassiness(self):
#         classiness = 0
#         if len(self.items) > 0:
#             for item in self.items:
#                 if item == "tophat":
#                     classiness += 2
#                 elif item == "bowtie":
#                     classiness += 4
#                 elif item == "monocle":
#                     classiness += 5
#         return classiness
#
# # Test cases
# me = Classy()
#
# # Should be 0
# print (me.getClassiness())
#
# me.addItem("tophat")
# # Should be 2
# print (me.getClassiness())
#
# me.addItem("bowtie")
# me.addItem("jacket")
# me.addItem("monocle")
# # Should be 11
# print (me.getClassiness())
#
# me.addItem("bowtie")
# # Should be 15
# print (me.getClassiness())




# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:44:30 2018

@author: Aravind
"""
"""
#                                                           Print some condition
n=[]
for i in range(2000,3201):
     if int(i)%7==0 and int(i)%5!=0:
          n.append(i)
print(n)



l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))
                                                      # Factorial
x=int(input("Enter the number to find its factorial"))
Fact=1;
F=1;

print (Fact,F)
for i in range(1,x):
Fact=(x-i+1) * F
print (Fact,F)
F=Fact
print("Here is the factorial of" ,x," is", Fact)


def fact(n):
    if n==0:
       return 1
    return n* fact(n-1)

print (fact(0))

def fact(x):
   if x == 0:
      return 1
   return x * fact(x - 1)

x=int(input("Enter a number"))
print (fact(x))

    # Dictionary



#def D(n):
#
#     di=dict()
#     for i in range (1,n+1):
#        di[i]=i**2
#     print (di)
#

#c=dict()
#c[0]='zero'
#c[1]='one'
#print(c)

#values=input("enter the values")
#l=values.split(",")
#t=tuple(l)
#print (l)
#print(t)

   #Class


#class interview:
#     def __init__(self,name,degree,expyears):
#          self.name=name
#          self.degree=degree
#          self.expyears=expyears
#
#candidate1=interview("Aravind","Mech",3)
#
#print(candidate1.name)
#print(candidate1.expyears)
#print(candidate1.degree)



#class getprint:
##     def __init__(self):
##          self.x=""
#     def getstring(kingkai):
#          kingkai.se=input("Enter your string")
##          print((s.upper())
#     def printstring(self):
#          print(self.se.upper())
#
#inputobj=getprint()
#inputobj.getstring()
#inputobj.printstring()

#class point(object):
#   def  __init__(self,x=int(input("Enter X:")),y=int(input("Enter Y:"))):
#          self.x=x
#          self.y=y
#
#   def distance(self):
#        print(self.x**2+self.y**2)
#
#d=point()
#d.distance()

                          #split join
#a = input("Enter ph numner")
#a=a.split(" ")
#print("-".join(a))

#import math as ma
#c=50
#h=30
#q=[]
#d=input("Enter D values sperated by comma")
#dList=d.split(",")
#print("dList",dList)
#for dIteration in dList:
# print ("dIteration:",dIteration)
# q.append(str(int(round(ma.sqrt(2*c*float(dIteration)/h)))))#join operation needs str
#print ("q is:",q)
#print(','.join(q))

                            #for loop and matrix
#enterDim=input("Enter the matrix dimensions in numxnum format")
#dim=[int(x)for x in enterDim.split('x')]
#row=dim[0]
#column=dim[1]
#zerolist = [[0 for col in range(column)] for row in range(row)]
#for r in range(row):
#     for c in range(column):
#       zerolist[r][c]=r*c
#print (zerolist)

#infinite loop, while,break,continuous input from user

lines=[]
while True:
s=input("Enter your sentance:\n")
if s:
lines.append(s.upper())
else:
break;

for sentance in lines:
print (sentance)
#Itertools permutation
from itertools import permutations as itp
print (list(itp([1,2,3])))

for i in range(5):
print (i)




def solve(numheads,numlegs):
ns='No solutions!'
for chicken in range(numheads+1):
rabbits=numheads-chicken
if 2*chicken+4*rabbits==numlegs:
return chicken,rabbits
return ns,ns

numheads=36
numlegs=96
solutions=solve(numheads,numlegs)
print (solutions)



s=input("Enter string:\n")
print(s[::3])


#palindrome
l=input("Ebter a senetance:\n")
if l[::-1] ==l:
print("the input sring is a plaindrome")
else:
print("not a plaindrome")


#not able to understand,dict
dic = {}
s=input("Enter a string:\n")
for s in s:
dic[s] = dic.get(s,1)
print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))

#Classes

class Person(object):
def getGender(jumbli):
return "Unknown"

class Male( Person ):         #class 'Person' is being called as an input argument, thats how you inherit another class and its methods
def getGender(kumbli):
return "Male"

class Female( Person ):
def getGender(sumbli):
return "dsdgdsg"

aMale = Male()
aFemale= Female()
print (aMale.getGender())
print (aFemale.getGender())

#fibonacci cannot understand

def f(n):
if n==0:
return 0
if n==1:
return 1
else:
# print(f(n-1))
return f(n-1)+f(n-2)

n=int(input("Enter a number:\n"))
print(f(n))


#fibonacci
def f(n=int(input("Enter the series length:\n"))):
a=0
b=1
series=[]
for i in range(n):
a1=a
a=b
b=a1+b
series.append(b)

return series

print(f())


###fibonnaici makes sense
def f(n=int(input("Enter the series length:\n"))):
    a=0
    b=1
    series=[0,1]
    for i in range(n):

        c=a+b
        a = b
        b = c
        series.append(b)


    return series

print(f())


#Fibonacci that makes sense
def f(n):
if n == 0: return 0
elif n == 1: return 1
else: return f(n-1)+f(n-2)

n=int(input("Enter series length"))

# method 1 to make a list out of this:
series=[]
for i in range(n):
series.append(f(i))

print (series)

#Method 2 to join and display just a bunch of numbers
# series=[str(f(i)) for i in range(n)]
# series=','.join(series)
# print (series)


def f(x=int(input("Enter a number:"))):
v=[]
for i in range(x+2):
if i%2==0:
v.append(i)

return v
print (f())


#yeild
def EvenGenerator(n):
i=0
while i<=n:
if i%2==0:
yield i
i+=1


n=int(input("Enter a number:"))
values = []
for i in EvenGenerator(n):
values.append(str(i))

print (",".join(values))

#assertion

li = [2,4,6,8,9]
for i in li:
assert i%2==0,"odd one out"




import random
print (random.random()*100)


#cannot understand
import re
email=input("Enter the email address:\n")
convertToequivalent="(\w+)@((\w+\.)+(com)"
matching=re.match(convertToequivalent,email)
print (matching.group(1))


def f(x,l=[]):
for i in range(x):
l.append(i*i)
print(l)

f(2)
f(3, [3, 2, 1])
f(3)


n=int(input("series length: \n"))
sum=0.0
for i in range (1,n+1):
sum+=i/(i+1)
print("Sum=%.2f"%sum)          # that % connects both .(how many digits) float  to the variable sum... %.2f %sum


def f(n):
if n==0:return 0
return f(n-1)+100

print (f(int(input("Enter a number"))))



#binary search

def binsearch(element,li=[]):
bottom=0
top=len(li)-1
index=-1
while top>=bottom and index==-1:
mid=int(round((top+bottom)/2))  #it can also be math.floor
if li[mid]==element:
index=mid
elif li[mid]>element:
top=mid-1
elif li[mid]<element:
bottom=mid+1

return index

li=[1,2,3,4,5,6,7,10,11]
element=int(input("Enter the list element:\n"))
print(binsearch(element,li))

import random
print (random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))



#time

from timeit import Timer
print (Timer('1+1').timeit())



from random import shuffle
li = [3,6,7,8]
shuffle(li)
print (li)

def my_function(**kwargs):
print(str(kwargs))

my_function(a=2,c=3,v=4)


import itertools
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
for j in range(len(verbs)):
for k in range(len(objects)):
sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
print (sentence)

# l=list(itertools.product(subjects,verbs,objects))
# for i in range(len(l)):
#    print ((','.join(l[i])).replace(",", " "))


li = [12,24,35,70,88,120,155]
print(list(enumerate(li)))
x=[x for (i,x) in enumerate(li) if x%2==0]
print(x)



#matrix
print([[0 for x in range(3)] for y in range(4)])



threeD= [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print (threeD)



l1=set([2,3,4,56,7,8])
l2=set([2,3,4,90])
l1 &= l2
print(set(l1))



li=[10,30,45,46,555,664,70]
print([x for (i,x) in enumerate(li) if i not in (0,1,2)])


li=[12,24,35,24,88,120,155,88,120,155]
def removedupe(li):
newli=[]
for item in li:
if item not in newli:
newli.append(item)

return newli

print(removedupe(li))



class fruit(object):
def juice(self):
return "unknown"

class pineapple(fruit):
def juice(self):
return "pinacolada"

class banana(fruit):
def juice(self):
return "banana smoothie"

b=banana()
p=pineapple()

print(b.juice())
print(p.juice())

# cannot understand
# dic = {}
# s=input("Enter a string\n")
# for s in s:
#     dic[s] = dic.get(s,0)+1
# # print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
# print(dic)

s="hhhihjlh"
n={}
for i in s:
n[i]=n.get(i,0)+1
print ('\n'.join(["%s: %s"%(i,j) for i,j in n.items()]))

import itertools
print (list(itertools.permutations([1,2,3])))


l=[]
for index in (1,2,3):
l.append(index)

l.insert(4,0)

print (l)



import time
for x in range(0,10):
t0=time.clock()
time.sleep(0.05)
tf=time.clock()
print("delay = %s"%(tf-t0))

"""


"""#Bubble sort

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])

l=[12,3,45,6,78,34,68,55]

t=int(input("Enter list item:"))

"""

"""#Linear Search
def linearsearch(list,target):
    for i in list:
        if list==target:
            return True
    return False
print (linearsearch(l,t))

"""

"""#Binary Search- this will work only in sorted list!!!!!!



lsorted = sorted(l)
print (lsorted)

def BinarySearch(mylist,target):
    startidx = 0
    endidx = len(mylist)-1
    middleidx= (startidx+endidx )//2


    if target==mylist[middleidx]:
        return True, middleidx, "middle identified"

    elif target < mylist[middleidx]:
          for i in mylist[startidx:middleidx]:
              if i==target:
                  return True,mylist.index(i)

    elif target > mylist[middleidx]:
        for i in mylist[middleidx+1:endidx+1]:
            if i==target:
                return True,mylist.index(i)

    return False

print (BinarySearch(lsorted,t))
"""


# l=[12, 3, 45, 6, 78, 34, 68, 55] #first list
# l2=[25,88,150,22,1,3,89,55,456,312,456,500,601]#second list

# s="helpme"
# vowels="aeiouAEIOU"
#p="Was it a cat  I sAw"

# t=int(input("enter the number :"))
# ls = sorted(l)
# print (ls)

"""#Binary search using iteration

def IterativeBinarySearch(mylist, target):
    low=0
    high=len(mylist)-1


    while high >= low :
        mid=(low+high)//2
        if target == mylist[mid]:
            return True
        elif target < mylist[mid]:
            high = mid-1
        else:
            low=mid+1


    return False

print (IterativeBinarySearch(ls, t))
"""


"""  #Binary search recursion

def BinarySearchRecursive (mylist,target,low,high):
    mid = (low+high)//2
    if low> high :
        return False

    elif target == mylist[mid]:
         return True

    elif target > mylist[mid]:
        return BinarySearchRecursive(mylist, target, mid+1, high)

    else:
        return BinarySearchRecursive(mylist, target, low, mid-1)


print (BinarySearchRecursive(ls, t, 0, len(ls)-1))

"""


"""#Quisk Sort
def QuickSort(mylist):


    higherlist=[]
    lowerlist=[]

    if len(mylist) <2:
        return mylist

    else:
        pivot = mylist.pop()

    for i in mylist:
        if i > pivot:
            higherlist.append(i)

        else:
            lowerlist.append(i)

    return QuickSort(lowerlist)+[pivot]+QuickSort(higherlist)

print (QuickSort(l))
print (QuickSort(l2))
"""


""" # REcursion

def CountConsonants(input_str):
    count=0
    for i in range(len(input_str)):
      if input_str[i] not in vowels:
          count +=1
    return count

print (CountConsonants(s))

def CountConsonantsRecursively(inp):
    if inp=='':
       return 0

    if inp[0] not in vowels:
        return 1+ CountConsonantsRecursively(inp[1:])
    else:
        return CountConsonantsRecursively(inp[1:])

print (CountConsonantsRecursively(s))

"""

""" #General Palindrome with less O(n)


def PalindromeSmartApproch(input_str):
    i=0
    j=len(input_str)-1

    while i<j:
        while not input_str[i].isalnum():
            i+=1
        while not input_str[j].isalnum():
            j-=1
        if input_str[i].lower()!=input_str[j].lower():
              return False
        i+=1
        j-=1
    return True


print (p)
print (PalindromeSmartApproch(p))
"""

"""#Hashtable

st = "Dec 29"


class Hashmap:
    def __init__(self):
        self.max= 100
        self.arr=[None for i in range(self.max)]


    def HashFunction(self,str_inp):
      sum=0
      for i in str_inp:
        sum+=ord(i)
      return sum %100

    #def Hdictcreation(self,key,val):
    def __setitem__(self,key,val):
         hk= self.HashFunction(key)
         self.arr[hk]=val

   # def GetValue(self,key):
    def __getitem__(self,key):
         hk=self.HashFunction(key)
         return self.arr[hk]


h=Hashmap()

print(h.arr)

"""
"""

# LinkedList

class Node:
    def __init__(self,data):
        self.data=data
        self.pointer = None

class LList:
    def __init__(self):
        self.StartNode=None

    def InsertAtStart(self,FirstItem):
        NewNode= Node(FirstItem)
        NewNode.pointer= self.StartNode
        self.StartNode = NewNode

    def InsertAtEnd(self,LastItem):
        NewNode = Node (LastItem)

        if self.StartNode is None:
            self.StartNode = NewNode
            return
        #insert at last meaning keep moving till you reach none and assign that None a new node
        #so start with startnode, keep looking at pointer to see if it points to none, then get out of that
        #traversal and assign a node there
        InsertionAtEndLooper= self.StartNode
        while InsertionAtEndLooper.pointer is not None:
           InsertionAtEndLooper = InsertionAtEndLooper.pointer

        InsertionAtEndLooper.pointer = NewNode


    def TraverseList(self):
        if self.StartNode is None:
            print("List is empty")

        else:
            LinkedList=""
            TraverseListLooper = self.StartNode
            while TraverseListLooper is not None:
                LinkedList+=str(TraverseListLooper.data)+"-->"
                TraverseListLooper=TraverseListLooper.pointer

            print (LinkedList)


L=LList()

L.InsertAtEnd(1)
L.InsertAtEnd(87)
L.InsertAtEnd(100)
L.InsertAtStart(3)
L.InsertAtStart(35)
L.InsertAtStart(56)

L.TraverseList()


"""

"""di = {'a1': '12', 'a2': '2345', 'a3': '12', 'a4': '23', 'a5': '80'}
un = [['a1', 'a3', 'a4'],
      ['a3', 'a2', 'a4']]
nn = [['a1', 'a5', 'a3'],
      ['a1', 'a2', 'a4']]
nm = ['a1', 'a2', 'a4']
ch = ['1', '2', '5']
d = ['23', '23', '44', '56', '56', '56']

oo = [['a1', 'a5', 'a3'],
      ['a1', 'a2', 'a4'],
      ['a1', 'a5', 'a3']]

v = [i for i in di.values()]
print (v)
vv=di.values()#this wont support indexing
print (vv)



l = [i for i in di.values() if len(i) == 4]
print ("l:",l)



ry = '59'
r = [i.replace('9', '**') for i in ry]
print ("r:",r)
print (r[0]+r[1])


string = ['1234567890', '567']
ch = ['6', '9']
print(string, 'string before')
for c in ch:
    string = [s.replace(c, '**') for s in string]
print(string, 'string after')

# ul = [un[i] for i in range(0, len(un)) for n in nn if n in un[i]]
# print(ul, 'ul')
#
# cc = list(set(x for x in d if d.count(x) > 1))
# print(cc, 'cc')
#
# dp = ['12', '34']
# ul = [un[i] for i in range(0, len(un)) for k, v in di.items() for c in cc if v in c if k in un[i]]
#
# print(ul, "ul")
#
# j = []
# for i in range(0, len(nn)):
#     j.append([di.get(x) for x in nn[i]])
#
# print(j, "j")
#
# print(oo)
# o = list(set(tuple(row) for row in oo))
# print('o', o)
"""
"""

#import matplotlib.pyplot as plt
# from colorama import Fore
# from colorama import Style
# p=[]
# n=5
# for i in range(n):
#     p.append(1./n)
#
# print (p)
# print (sum(p))
#
# #---------------------------
# #Modify the code below so that the function sense, which
# #takes p and Z as inputs, will output the NON-normalized
# #probability distribution, q, after multiplying the entries
# #in p by pHit or pMiss according to the color in the
# #corresponding cell in world.
#
#
# p=[0.2, 0.2, 0.2, 0.2, 0.2]
# world=['green', 'red', 'red', 'green', 'green']
# Z = 'green'
# pHit = 0.6
# pMiss = 0.2
#
# def sense(p, Z):
#     #
#     #ADD YOUR CODE HERE
#    r= [i for i, j in enumerate(world)if j == Z]
#    g= [x for x,y in enumerate(world) if y!=Z]
#    for i in r:
#        p[i]=p[i]*pHit
#    for j in g:
#        p[j]=p[j]*pMiss
#    q=p
#    s = sum(q)
#    q = [x / s for x in q]
#
#    return q
#
#
# print (f"{Fore.GREEN}My code: Final normalized vec{Style.RESET_ALL}",sense(p,Z))
#
# #-------------------------------------
# p=[0.2, 0.2, 0.2, 0.2, 0.2]
# world=['green', 'red', 'red', 'green', 'green']
# Z = 'green'
# pHit = 0.6
# pMiss = 0.2
#
# def sense(p, Z):
#  q=[]
#  for i in range(len(p)):
#    hit= (Z==world[i])
#    q.append(p[i]*(hit*pHit+(1-hit)*pMiss))
#  s=sum(q)
#  q=[x/s for x in q]
#  print ("q list:",q)
#  print("sum q:",sum(q))
#  # plt.plot(q)
#  # plt.show()
#  return q
#
# print (f"{Fore.RED}Final normalized Vec:{Style.RESET_ALL}",sense(p,Z))
#
# #----------------------------------------------------------------
#
#
# #Modify the code so that it updates the probability twice
# #and gives the posterior distribution after both
# #measurements are incorporated. Make sure that your code
# #allows for any sequence of measurement of any length.
#
#
# p=[0.2, 0.2, 0.2, 0.2, 0.2]
# world=['green', 'red', 'red', 'green', 'green']
# measurements = ['red', 'green']
# pHit = 0.6
# pMiss = 0.2
#
# def sense(p, Z):
#     q=[]
#     for i in range(len(p)):
#         hit = (Z == world[i])
#         q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
#     s = sum(q)
#     for i in range(len(q)):
#         q[i] = q[i] / s
#     return q
# #
# #ADD YOUR CODE HERE
# for Z in measurements:
#     p=sense(p,Z)
#
# #
# print (p)
#
# #------------------------------------------------------------------------
#
# #Program a function that returns a new distribution
# #q, shifted to the right by U units. If U=0, q should
# #be the same as p.
#
# # p=[0, 1, 0, 0, 0]
# # world=['green', 'red', 'red', 'green', 'green']
# # measurements = ['red', 'green']
# # pHit = 0.6
# # pMiss = 0.2
# #
# # def sense(p, Z):
# #     q=[]
# #     for i in range(len(p)):
# #         hit = (Z == world[i])
# #         q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
# #     s = sum(q)
# #     for i in range(len(q)):
# #         q[i] = q[i] / s
# #     return q
# #
# # def move(p, U):
# #     #
# #     #ADD CODE HERE
# #     q=[]
# #     for i in range(len(p)):
# #         q.append(p[(i-U)%len(p)])
# #
# #     return q
# # print (p)
# # print (move(p,3))


def nonneg(c):
    temp = []
    for a in range(c):
        for b in range(c):
            temp.append(a ** 2 + b ** 2)

    if c in temp:
        return True
    else:
        return False



print (nonneg(2))

# Switch statement in python

# def gym(self):
#     workout={
#         0:'biceps',
#         1:'tricpes',
#         2:'lats',
#         3:'bench'

#     }


#     return workout.get(self,"sleep")

# print (gym(int(input("input number"))))

"""



# #first way
#
# class Node:
#     def __init__(self,data):
#         self.data=data
#         #self.next=next
#         self.next=None
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#
#     def create(self):
#         Node1 = Node(1)
#         self.head = Node1
#
#         SecondNode = Node(2)
#         self.head.next = SecondNode
#
#         ThirdNode = Node(3)
#         SecondNode.next = ThirdNode
#
#     def PrintList(self):
#         while self.head:
#             print("""
#                 Node{}
#                 +-------------------+
#                 |       Data: {}     |
#                 +-------------------+
#                 """.format(self.head.data, self.head.data),"""
#                 | Link to next node---> {}     |
#
#                 """.format(self.head.next))
#             self.head = self.head.next
#
#
# LL=LinkedList()
# LL.create()
# LL.PrintList()

"""
# Second Way

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head = None


    def Append(self,data):
        new_node=Node (data)

        if self.head is None:
            self.head=new_node
            print(self.head.data)
            return


        current_node = self.head
        if new_node:
           current_node.next=new_node
           current_node=current_node.next
           print(current_node.data)



LL=LinkedList()
LL.Append(1)
LL.Append(2)
LL.Append(3)
LL.Append(4)
LL.Append(56)

"""
