#=================================
# number=[1,3,5,6,7,8,9,10]


# for n in number:

#     print(n)

#============================
# name=["sumit","ravi","rohan"]

# for data in name:

#     print(data)
#=============================
# for i in range(10):

#      print("sumit")

# #============================
# fruits = ["apple", "banana", "mango"]

# for f in fruits:
#     print(f)

#=========================
# for i in range(10):

#     print(i)

#=================================
# for i in range(20):

#     print("sumit")




# number=int(input("please enter number:"))

# for i in range(1,11):

#     print(number*i)

# number=[2,3,4,5,6,7]

# for data in range(len(number)):

#     print(number[data])


# number=[2,3,4,5,6,7]

# for n in number:

#     print(n)


# for i in range(1,101):

#     print(i)



#============even odd number===============



# number=[2,4,6,8,3,5,7,9,8]

# for i in number:

#     if i%2==0:

#         print(i)



#==============even number=========

# for i in range(1,11):

#     if  i%2==0:

#         print(i)
# # #=====================odd number============
# for i in range(1,21):

#     if i%2!=0:

#         print(i)

#=================================


# start=int(input("please enter starting number:"))
# end=int(input("please enter end number:"))

# for i in range(start,end+1):

#     if i%2==0:

#         print("even number",i)

# for i in range(start,end+1):

#     if i%2!=0:

#         print("odd number",i)
# #===============================

#=====================list data type====


# name=["sumit","ravi","rohan","rohit"]


# for n in name:

#     print(n) 
# number=[2,3,4,6,8,9,4,5,7,3]

# i=0

# while i<=len(number):

#     print(number[i])

#     i+=1
#====================


# number=[2,3,4,6,8,94,5,7,3]

# for n in number:

#     if n%2==0:

#         print("even number",n)

# for n in number:

#     if n%2!=0:

#         print("odd number",n)

#===================tuple data type==========


# address=("sunday","monday","tuesday","wednesday","thrusday","friday")


# for a in address:

#     print(a)

# #=========================set data type=====


# student={"sumit","ravi","rohan"}

# for s in student:


#     print(s)


# #==================== dictionary data type================


# address={"name":"sumit kumar",
#          "address":"mirganj",
#          "age":18,
#          "state":"bihar"

#  }


# for key,value in address.items():

#     print(value)
# # for key,value in address.items():

#     print(f"{key}={value}")

#     if key=="name":

#         print("value")

# #     # if key=="name":

# #     #     print(values)

#==============================================


        
# name=input("please enter name:")

# for data in address:

#     for key, value in data.items():

#         if value==name:

#             print(data)


        
#==========================================

# address=[{"name":"sumit kumar","address":"bihar","id":101},
#          {"name":"rohan kumar","address":"mirganj","id":102},
#          {"name":"ravi kumar","address":"gopalganj","id":103}

# ]

# user_name=input("please enter your name:")


# found =False


# for data in address:

#     if data["name"] ==user_name:

#         print("recoard successfully")

#         print(data)

#         found =True

#         break

#     if found ==False:

#         print("no recoard found")

#====================================================
        
# address=[{"name":"sumit kumar","address":"bihar","id":101},
#          {"name":"rohan kumar","address":"mirganj","id":102},
#          {"name":"ravi kumar","address":"gopalganj","id":103}

# ]


# user_name=input("please enter your name:")


# for data in address:

#     if data["name"] ==user_name:

#         print("recoard successfully")

#         print(data)

#         break

#     else:

#         print("no recoard found")


# address={"student1":{"name":"sumit kumar",
#                      "age":20,
#                      "state":"bihar"



# },"student2":{"name":"rohan kumar",
#                      "age":30,
#                      "state":"gopalganj"


# }
# }
# user_name=input("please enter your choice:")

# found =False

# for key,value in address.items():

#     if value["name"]==user_name:

#         print("found successful ")

#         print(value)

#         found =True

#         break

# if found ==False:

#     print("found not successful")



        
#=====================================table print hoga 1 to 20=========


# for data in range(1,21):

#     number=int(input("plase enter number table:"))

#     for i in range(1,11):

#         print(number*i)

#===============================

starting=int(input("please enter starting  number:"))
end=int(input("please enter end number:"))


for data in range(starting,end+1):

    print(data)


#====================================


address={"name":"sumit kumar",
                     "age":20,
                     "state":"bihar"

}

for key,value in address.items():

    # print(f"{key}={value}")

    print(key, ":", value )

 #=====================================
address={"name":"sumit kumar",
                     "age":20,
                     "state":"bihar"

}


for key in address:

     print(key)
    

 #===================================       
address={"name":"sumit kumar",
                      "age":20,
                     "state":"bihar"

 }

for value in address.items():

    print(value)
    
student={"name":"sumit kumar",
         "address":"mirganj",
         "state":"bihar",
         "email":"sumitkumar@gmail.com"

}


for key,values in student.items():

    print(key, ":" ,values)