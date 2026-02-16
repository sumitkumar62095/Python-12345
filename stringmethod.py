#===============string 1 method function=========


account_number="123"


print(account_number.zfill(12))
print(account_number)


account_number=input("please enter account number:")

print("account number:",account_number.zfill(12))


#======================2 function===========

 
name="indixpert"

print(name.upper()) 


name=input("please enter your name:")

print("user enter name:",name.upper())

name1=input("please enter company name:")
name2=input("please enter company name:")

print(f"first name:{name1.upper()}  secoand name:{name2.upper()}")

print(name1.upper()==name2.upper())


#=======================3 function=========


name="SUMIT KUMAR"                  # first leter small kar dega


print(name.lower())

name=input("please enter tour name:")


print("user enjter name:",name.lower())

#=================4 function===============


name="my name is sumit kumar"       #sabhi first letter capitial kar dega

print(name.title())

name=input("please enter your name:")
print("user enter name:",name.title())


#==================4 function=================


name="Sumit Kumar"              #first letter small kar dega


print(name.casefold())


name=input("please enter your name:")
print(name.casefold())

#==================5 method============


name="python is a powerfull programming language"

print(name.count('g'))


#===============================6 method==============


name="my name is sumit kumar"

print(name.find('is'))



#==========7 method===============


name="12345"

print("student name:",name.isalpha())


name=input("please enter your name:")


print("user enter your name:",name.isalpha())


# #=======================8 method===============


name="sumit12345"

print("user name:",name.isalnum())


name=input("please enter name:")


print(name.isalnum())

#===================9 method============


name="sumit"

print(name.isdigit())


account_number=input("please enter your account number:")

print(account_number.isdigit())


#==================10 method===============


data="Myname"

print(data.swapcase())


name=input("please enter your name:")

print(name.swapcase())


#====================11 method==============


data="                     this is my pen"


print(data.lstrip())



#====================12method==============

number=12,34,45

print(number[0])

data="  my name is sumit kumar  "


print(data.strip())

#========================================
name="sumit kumar"
father_name="raju prasad"
education="12th complete"
address="mirganj"
state="bihar"
district="gopalganj"
pin_code=841438


print(f"student name:{name}")
print(f"student father name:{father_name}")
print(f"student education name:{education}")
print(f"student address:{address}")
print(f"student address:{state}")
print(f"student district:{district}")
print(f"student pin code:{pin_code}")
#================================================
name=input("please enter your name:")
father_name=input("please enter your father name:")
education=input("please enter your education:")
address=input("please enter your address:")
state=input("please enter your state:")
district=input("please enter your district name:")
pin_code=input("please enter your pin code:")


print("user enter name:",name)
print("user enter father name:",father_name)
print("user enter education:",education)
print("user enter address:",address)
print("user enter state:",state)
print("user enter district:",district)
print("user enter pincode:",pin_code)
#=============================================
hindi=int(input("please enter your hindi marks:"))
english=int(input("please enter your english marks:"))
maths=int(input("please enter your maths marks:"))

total_marks=hindi+english+maths


print("hindi marks:",hindi)
print("english marks:",english)
print("maths marks:",maths)

print("total marks:",total_marks)

#=============================================

name="sumitkumar"
age=20
float=12.4


print(type(name))
print(type(age))
print(type(float))
#========================================

    