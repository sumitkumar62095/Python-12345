
# #==========default value  hai===========

# def getnumber(a,b=30):

#     return a//2

# print(getnumber(20,30))

# #===========================
# def getnumber(a=20,b=30):

#     return a/2

# def userinput():

#     data=getnumber()

#     print(data)

# userinput()

#===========================
# def getnumber():


#     a=20
#     b=30


#     return a/2

# def userinput():

#     data=getnumber()

#     print(data)

# userinput()


#=================================

# def getnumber(a,b):

#     return (a+b)/2

# print(getnumber(40,30))


#========================

# def getnumber():

#     a=20
#     b=30

#     (a+b)/2

#     return (a+b)/2

# def getinput():

#     data=getnumber()

#     print(data)

# getinput()


#================================

# 
# def getnumber(a,b):

#     (a+b)/2

#     return (a+b)/2

# def getinput():

#     data=getnumber(20,30)

#     print(data)

# getinput()

#=====================
# def getnumber(a,b):

#     return (a+b)/100

# print(getnumber(200,300))

# #==========================

# def getnumber(a,b=79):

#     return a/100

# print(getnumber(200,300))

# #================================

# def number(a,b=30):
    
#     (a+b)/2

#     return (a+b)/2

# def data():


#     maa=number(20,40)

#     print(maa)

# data()



# #========================

# def getdata():

#     return ""

# getdata()

# # #==========return type============

# def getdata():

#     return [1,2,3,4,5,6,7]



# def show_data():

#     data=getdata()

#     print(data)


# show_data()



# #==============================


# def user_input():

#     student={}

#     student["id"]=input("please enter student id:")
#     student["name"]=input("please enter your student name:")

#     return student

# def user_output():

#     data=user_input()

#     print(data)

# user_output()

# #============================
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
    
# def sumit():

#     pass

# def student():

#     dictionary={"name":"sumit kumar","id":101,"address":"mirganj"


#     }

#     listdata=[23,45,67,89,]

#     string="my name is sumit kumar"


#     return dictionary,listdata,string


# def datatype():

#     student1,student2,student3=student()

#     print(student1)
#     print(student2)
#     print(student3)

# datatype()
    
#================return value==================

def student_data():

    dictionary={"name":"sumit kumar",
                "address":"mirganj",
                "state":"bihar"


    }

    listdata=[12,34,56,78]


    set={12,34,56,78}


    tuple=(12,34,56,77)


    return dictionary,listdata,set,tuple

def outputdata():

    data1,data2,data3,data4=student_data()

    print(data1)
    print(data2)
    print(data3)
    print(data4)

outputdata()

