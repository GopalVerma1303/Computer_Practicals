#1:
sum_of_number = 0
a = int(input("enter the number: "))
while(a!=0):
    sum_of_number = sum_of_number + a%10
    a = a//10
print(sum)

#2
sum_of_elements = 0
def sum_list(L):
    for i in L:
        sum_of_elements = sum_of_elements + int(L[i])
    return (sum_of_elements)


#3:
def bs(arr, low, high, x):
    if high>=low: midval = low+high//2
    if x==midval: return 0
    if x > midval: 
        bs(arr, low+1 , high, x)
        return (bs)
    if x < midval:
        bs(arr, low, high-1, x)
        return (bs)
findarr = input("enter the array to search: ")
findchar = int(input("enter the char to find: "))
if bs(findarr, 0, len(findarr), findchar): print("found")
else: print("not found")

#4:
def strcomp(str1, str2):
    if len(str1) == len(str2): return True
str1 = str(input("enter the string1: "))
str2 = str(input("enter the string2: "))
if (strcomp(str1, str2)): print("both are are of same lengths")
else: print("both are of different lengths")

#5:
import random
def randomgenerate(a, b):
    return random.randint(a, b)
a = int(input("enter the num1: "))
b = int(input("enter the num2: "))
for i in range (0, 3):
    print(randomgenerate(a, b))

#6:
import csv
fp = open("emp.text", "w")
n = int(input("Enter the number of Records: "))
for i in range(0, n):
    eid  = input("Enter eid: ")
    ename = input("Enter name: ")
    age = input("Enter age: ")
    dn = input("Enter dn: ")
    st = "employ id:"+eid+"employ name"+ename+"employ age"+age+"employ dept. number"+dn
    fp.write(st)
fp.close()

#7:
import csv
fp = open("emp.text", "w")
n = int(input("Enter the number of Records: "))
for i in range(0, n):
    eid  = input("Enter eid: ")
    ename = input("Enter name: ")
    age = input("Enter age: ")
    dn = input("Enter dn: ")
    st = "employ id:"+eid+"employ name"+ename+"employ age"+age+"employ dept. number"+dn
    fp.write(st)
fp.close()
fp = open("emp.text", "r")
a = fp.read()
print(a)
fp.close()

#8:
def count_line(fp):
    count = 0
    for line in fp:
        if (line[0] in ('A', 'T')):
            count = count + 1
        print(line)
    print(count)

import csv
fp = open("emp.text", "r")
Count_line(fp)
Fp.close()

#9:
def count_word(fp):
    count = 0
    for line in fp:
        for word in line:
            if (word in ("are", "the")):
                count = count + 1
    print(count)

import csv
fp = open("stud.text", "r")
Count_word(fp)
Fp.close()

#10:
def read_line(fp):
    for line in fp:
        print (line)

import csv
fp = open("story.text", "r")
Count_word(fp)
Fp.close()

#11:
def count_vowel(fp):
    count = 0
    for line in fp:
        for word in line:
            for char in word:
                if (char in ('a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"))
                count = count + 1
import csv
fp = open("data.txt", "r")
Count_word(fp)
Fp.close()

#12:
import pickle as pl
fp = open("dps.dat", "wb")
while True:
         L = eval(input("Enter detail of student"))
         pl.dump(L,fp)
         ch = input("Do you want to add more records")
         if ch == 'n' or ch=='N':
                  break
fp.close()
 
fp = open("dps.dat", "rb")
while True:
         L = pl.load(fp)
         print(L)
fp.close()

#13:
 def CopyBinary():
         import pickle as pl
         try:
                  f1 = open("souce.dat", "rb")
                  f2 = open("target.dat", "wb")
                  while True:
                           L = pl.load(f1)
                           pl.dump(L,f2)
 
         except FileNotFoundError:
                  print("File name does not exist")
                  
         except EOFError:
                  print("Successfully copied")
                  f1.close()
                  f2.close()
 
#main
CopyBinary()

#14:
import csv
import pickle
fp = open("emp.dat", "rb")
ei = int(input("Enter the eid of the employe: "))
try:
    while True:
        ln = pickle.load(fp)
        if (ln[0]==ei):
            print(ln)
except EOFError:
    print("Thankyou for using.")

#15:
import csv
import pickle
fp = open("flightdps.dat", "rb")
try:
    while True:
        ln = pickle.load(fp)
        if(ln[1]=="Delhi"):
            print(ln)
except EOFError:
    print("Thankyou for using.")

#16:
import csv
import pickle
fp = open("emp.dat", "rb")
try:
    while True:
        ln = pickle.load(fp)
        if(ln[2]<25000):
            ln[2] = ln[2]+2000
except EOFError:
    print("Thankyou for using.")

#17:
import csv
import pickle
fp = open("sub.dat", "wb")
try:
    while True:
        dic = input("Enter the subject code and subject name: ")
        pickle.dump(dic, fp)
        c = input("Wanna Enter more ?: ")
        if(c in ("n", "N")):
            break
except EOFError:
    print("Thankyou for using")
fp = open("stud.dat", "rb")
try:
    while True:
        ln = pickle.load(fp)
        if(ln[41] != "Mathematics"):
            ln[41] = "Mathematics"
except EOFError:
    print("thankyou for using.")

#18:
import csv
Column = ['RNo','Name','Marks']
fp = open("student.csv", "w")
wp = csv.writer(fp, delimiter = ',')
while True:
    L = eval(input("Enter the records: "))
    wp.writerow(L)
    c = input("Wanna enter more: ")
    if(c in ("n", "N")):
        print("Thankyou fro using: ")
        break
fp.close()

#19:
def Addnew(lib, book):
    lib.append(book)
    top = len(lib)-1

def Remove(lib, book):
    if lib==[]:
        return "Underflow"
    else:
        book = lib.pop()
    if len(lib)==0:
        top = None
    else:
        top = len(stk)-1
    return book


#20:
def PUSH(stk, item): 
stk.append(item)
top = len(stk)-1

def POP(stk): 
	if stk==[]: 
		return “Underflow” 
	else: 
		item = stk.pop() 
		if len(stk)==0: 
			top = None 
		else: 
			top = len(stk)-1 
	return item

#21:
def MakePush(Package, package_title):
    package_title.append(Package)
    top = len(package_title)-1
def MakePop(Package, package_title):
    if len(package_title)==0:
        print("stack underflow")
    else:
        package = package_title.pop(package)
    if len(package_title)==0:
        top = None
    else:
        top = len(package_title)-1
    return (package)

  



        




   

    


