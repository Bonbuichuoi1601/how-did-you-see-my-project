import math

def bai_1():
   n=int(input())
   inh=(n*3+1)
   print (inh)

def bai_2():
   n=int(input())
   inh=(n**2/3)
   print (inh)

def bai_3():
   n=int(input())
   inh=(n*1.8+32)
   print (inh)
def bai_4():
   b=int(input())
   if b%2==0:
      print(True)
   else:
      print(False)

def bai_5():
    ab=int(input())
    if ab<100 and ab>50 and ab%3==0 :
       print(True)
    else:
        print(False)

def bai_6():
    a= int (input())
    if a<=20 or a>=70:
      if a%5==0:
         print(True)
    else:
        print(False)

def bai_7():
   a= int (input())
   b= int (input())
   if a%2==0 or b%2==0:
      print (True)
   else:
      print(False)

def bai_8():
   a=int(input())
   if a<0:
      print(False)
   else:
      print (True)
def bai_9():
   a=int(input())
   b=(math.sqrt(a))
   if b==round(b):
      print(True)
   else:
      print (False)

def bai_10():
   a=int(input())
   print(a*1/10)

def bai_11():
   a=int(input())
   b=int(input())
   c=int(input())
   print(a+b+c)

def bai_12():
   a=int(input())
   b=int(input())
   c=int(input())
   d=((a+b)**c)
   if d<200 and d>100:
      print(True)
   else:
      print(False)

def bai_15():
   a=float(input())
   b=float(input())
   c=float(input())
   if (a+b)>c and (a+c)>b and (c+b)>a:
      print (True)
   else:
      print(False)

def bai_20():
   cac_thang = {1: "31", 2:28, 3:"31", 4: "30", 5:"31", 6:"30", 7:"31", 8:"31", 9:"30", 10:"31", 11:"30", 12:"31"}
   nam=int(input('nhap nam:'))
   if nam %4==0:
      cac_thang[2] +=1
   thang = int(input("Nhap thang "))
   print(cac_thang[thang])

def bai_21():
   cac_thang = {1: "31", 2:28, 3:"31", 4: "30", 5:"31", 6:"30", 7:"31", 8:"31", 9:"30", 10:"31", 11:"30", 12:"31"}
   nam=int(input('nhap nam '))
   if nam %4==0:
      cac_thang[2] +=1
   thang = int(input("nhap thang "))
   ngay=int(input("nhap ngay "))
   print(cac_thang[thang])
