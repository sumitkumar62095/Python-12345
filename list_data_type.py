
# #============list data type============#
# name=["sumit","ravi","rohan"]

# print(name[0])


# print(len(name))           #list ka length

# # #======================
# name=[2,3,4,5,8,1,2,3]


# print(len(name))


# name={"sumit","rohan"}                  #value remove

# name.remove("rohan")

# #print(name)

#===============================


# student_address=["sumit kumar",20,"mirganj"]

# print(student_address)
# print(type(student_address))

# marks=[25.5,35.5,78.9]
# marks=[56.7,78.9,67.8]
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(len(marks))
#================================

# sumit_student=["sumit kumar","rohan kumar","bablu kumar"]

# sumit_student[0]="ram"

# print(sumit_student)

# marks=[34,45,67,89,65]

# print(marks[1:4])

# #=================list slicing============#


# marks=[34,45,67,89,87]

# print(marks[0:4])


# marks=[34,56,78,98,89]


# print(marks[1:3:2])


# marks=[23,45,67,89,87,65]

# print(marks[-2:-4])

# #============


# marks=[2,3,4,5,6,7]

# print(marks[2:3:4])




#=================lst methods=============#

# marks=[23,45,67,89]

# marks.append(56)
# print(marks)

# marks=["hindi","english","maths"]

# marks.append("science")
# print(marks)
# #======================
# marks=[3,4,2,1]
               
# marks.sort()                #ascending order
# print(marks)



# marks=[]


# for i in range(1,11):

#     number=int(input())

#     marks.append(number)


#     marks.sort()

# print("sort number:",marks)


# #=====================
# marks=[1,2,3,4,5]           #decending order me print hoga

# print(marks.sort(reverse=True))
# print(marks)


# marks=[]

# for n in range(1,11):

#     number=int(input())

#     marks.append(number)

#     marks.sort(reverse=False)

# print("reverse number:",marks)


# marks=["one","two","three","five","zero","cat"]

# marks.sort()

# print(marks)

# #=======================
# list=['a','b','c','d','e','f']      #ye value ko ulta kar dega

# list.reverse()

# print(list)

# marks=["hindi","eng","maths"]

# # marks.reverse()
# print(marks)
# #===============================

# list=[2,3,4,5]          #new  value insert kar dega

# list.insert(2,9)        

# print(list)

# marks=[12,34,56,45,67,]

# marks.insert(1,22)

# print(marks)
# # #========================

# # list=[2,3,4,5,6]

# list.remove(5)

# print(list)

# marks=["hindi","english","maths"]

# marks.remove("english")

# print(marks)

# marks=["sumit","rohan","rohit"]

# marks.remove("sumit")

# print(marks)


# student_data=[101,"sumit kumar","bihar",{"company_name:indixpert"},
#               "indixpert",5000,
#               "full stock web developer"
              
#               ]

# print(f"student id:{student_data[0]}")
# print(f"student_address:{student_data[1]}")
# print(f"student company :{student_data[2]}")
# print(f"student_college_name:{student_data[3]}")
# print(f"studen_fee_charge:{student_data[4]}")
# print(f"student_course_name:{student_data[5]}")


# #=====================


# # address=["sumit kumar",
# #          20,
# #          {"email:","sumitkumr25@gmail.com"}
    

# # ]
# # print(f"student address:{address[0]}")
# # print(f"student age:{address[1]}")
# print(f"student emaik:{address[2]["email"]}")

#=================================

# student_data=[]


# student_data.append(input("please ente your name:"))
# student_data.append(input("please enter your address:"))
# student_data.append(input("pleasee enter your emailid:"))


# print(f"student name:{student_data[0]}")
# print(f"student address:{student_data[1]}")
# print(f"student email:{student_data[2]}")

#===================index method=====================


# student=[12,34,56,78]

# print(student.index(12))


# #===========================copy methid===============


# student=["sumit","rohan","rohit"]

# name=student.copy()

# print(name)


# #================count=========


# student=[12,34,56,78]

# print(student.count(12))


#====================================extend method============


name=["sumit","rohan","rohit"]
name2=["aman","bablu","rishi"]

name.extend(name2)

print(name)
#=======================

name=["sumit","rohan","rohit"]


print(name)
