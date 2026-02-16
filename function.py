# a=int(input("please enter first number:"))
# b=int(input("please enter your secoand number:"))

# def addition(a,b):
#     print(a+b)

# def subtract(a,b):
#     print(a-b)

# def multiply(a,b):

#     print(a*b)

# # def menu():

# #     print("1. addition")
# #     print("2. subtract")
# #     print("3. multiply")

# #     choice=int(input("please enter your choice:"))
# #     return choice


# # def dashboard():

# #     number=menu()

# #     if number == 1:
# #         addition(a,b)

# #     elif number == 2:
# #         subtract(a, b)

# #     elif number == 3:
# #         multiply(a, b)

# #     else:
# #         print("invalid option")


# # dashboard()

# def calculater():

#     print("1. addition")
#     print("2. subtarct")
#     print("3. multiply")
#     print("4. divided")

#     choice=int(input("please enter your choice:"))

#     a=int(input("please enter number:"))
#     b=int(input("please enter your number:"))

#     if choice==1:

#         print("addition",a+b)

#     elif choice==2:

#         print("subtract",a-b)

#     elif choice==3:

#         print("multiply",a*b)

#     elif choice==4:

#         print("divided",a/b)
#     else:

#         print("invalied choice")

# calculater()
# calculater()
# calculater()
# calculater()
    

    
#==================================


# def student():

#     dictionary={"name":input("please enter your name:"),
#                 "address":input("please enter your address:"),
#                 "state":input("please enter your state:")


#     }

#     print(dictionary)


# def data():

#     getdata=["sumit",101,"bihar","BA"]


#     print(f"student name:{getdata[0]}")
#     print(f"student id:{getdata[1]}")
#     print(f"student state:{getdata[2]}")
#     print(f"student education:{getdata[3]}")



# data()

    
#===========================================


# def cal_sum(a,b):

#     sum=a+b
#     print(sum)
#     return sum

# cal_sum(2,5)

# cal_sum(2,5)

# cal_sum(4,5)


#=============================

# #====function defnication=====
# def cal_sum(a,b):   #perameter

#     return(a+b)


# sum=cal_sum(30,30)      #function call argement

# print(sum)


#=================

#============

# def print_hello():

#     print("hellow")

# print_hello()
# print_hello()

#========================

# student=["sumit","rohan","rohit","ravi"]
# student1=["apple","mango","banana","cat"]

# def print_len(list):

#     print(len(list))


# print_len(student)
# print_len(student1)

#=================================


# def addition():

#     a=10
#     b=20

#     print(a+b)


# addition()
# addition()

#================================

# def addition():
#     a=int(input("please enter your first number:"))
#     b=int(input("please enter your secoand number:"))

#     print(a+b)

# addition()
# addition()

#============================

# a=int(input("please enter your first number:"))
# b=int(input("please enter your secoand number:"))

# def addition(a,b):

#     print(a+b)



# addition(a,b)
# addition(a,b)


#=====================================



# a=int(input("please enter your first number:"))
# b=int(input("please enter your secoand number:"))


# def addition(a,b):
     
#      print(a+b)

# def subtract(a,b):
     
#      print(a-b)

# def multiply(a,b):
#      print(a*b)

# def menu():

#      print("1. addition")
#      print("2. subtract")
#      print("3. multiply")


#      choice=int(input("please enter your choice:"))

#      return choice

# def desboard():
     
#      number=menu()

#      if number==1:
          
#           addition(a,b)
#      elif number==2:

#           subtract(a,b)    
#      elif number==3:

#           multiply(a,b)   
    
# desboard()


    
# #==================================

# def student_data():

#     student={}

#     student["id"]=input("please enter your id:")
#     student["name"]=input("please enter your name:")
#     student["address"]=input("please enter your address:")

#     return student

# def dasboard():

#     data=student_data()

#     print(data)


# dasboard()

#===============================


# def addition():
#     a=20
#     b=30
#     print(a+b)

# def subtract():
#     a=20
#     b=30
#     print(a-b)

# def multiply():
#     a=20
#     b=30
#     print(a*b)


# def menu():

#     print("1. addition")
#     print("2. subtract")
#     print("3. multiply")

#     choice=int(input("please enter your choice:"))

#     return choice

# def dasboard():

#     number=menu()

#     if number==1:
#         addition()
#     elif number==2:

#         subtract()
#     elif number==3:

#         multiply()


# dasboard()
# dasboard()

#==========================

# #===========================================
# student_data=[]
# def student_registration():

#     student={}

#     student["id"]=input("please enter your id:")
#     student["name"]=input("please enter your name:")
#     student["address"]=input("please enter your address:")

#     student_data.append(student)

# def student_search_data():

#     for data in student_data:

#         print(data)

# def search_student_recoard():

#     search_id=input("please enter student search id:")

#     for data in student_data:

#         if data["id"]==search_id:

#             print("id:",data["id"])
#             print("name:",data["name"])
#             print("address:",data["address"])
            

# def student_menu():

#     print("1. registration")
#     print("2. search data")
#     print("3. search student recoard")
#     print("4. program exit")

#     choice=int(input("please enter your choice:"))


#     return choice    

# def dasboard():

#     while True:

#         number=student_menu()

#         if number==1:

#             student_registration()

#         elif number==2:

#             student_search_data()

#         elif number==3:

#             search_student_recoard()


#         elif number==4:

#             print("exit prigram")
#             break
                
#         else:

#             print("envaild number try again")

                

# dasboard()

#======================


# def menu():

    
#     print("1.addition")
#     print("2. subtract")
#     print("3.multiply")
#     print("4.divided")
#     print("5. exit")

#     choice=int(input("please enter your choice:"))


#     a=int(input("please enter first number:"))
#     b=int(input("please enter secoand number"))


    # if choice==1:

    #     print("addition:",a+b)
    
    # elif choice==2:

    #     print("subtract:",a-b)

    # elif choice==3:

    #     print("multiply:",a*b)

    # elif choice==4:

    #     print("divided:",a/b)
    # elif choice==5:

#         print("exit program")

#     else:

#         print("inviled choice")


# menu()

#=================return function==================
# 
# def data():

#     student={"name":input("please enter your name:"),
#              "address":input("please enter your address:")


#     }

#     listdata=["sumit kumar","rohan kumar","rohit kumar"]

#     setdata=(23,34,56,78)

#     return student,listdata,setdata


# def menu():

#     store1,store2,store3=data()

#     print(store1)
#     print(store2)
#     print(store3)


# menu()    

#===========================================


             

    
