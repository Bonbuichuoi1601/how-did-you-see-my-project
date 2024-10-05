# Nhập vào số n, hãy nhân n lên cho 3, rồi cộng 1 sau đó in kết quả ra màn hình
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
   a=int(input())
   if a%2==0:
      print(True)
   else:
      print(False)

def bai_5():
    a=int(input())
    if a<100 and a>50 and a%3==0 :
       print(True)
    else:
        print(False)
bai_5()