
# #===============================================


# # address = [
# #     {"id":101,"name":"sumit kumar","address":"gopalganj"},
# #     {"id":102,"name":"indixpert","address":"patna"},
# #     {"id":103,"name":"rohan kumar","address":"bihar"}
# # ]


# # name=input("please enter name:")

# # found= False


# # for data in address:

# #     if data["name"]==name:

# #         print("found successful")

# #         print("id",data["id"])
# #         print("name",data["name"])
# #         print("address",data["address"])

# #         found= True
# #         break


# # if not found:

# #     print("not found")

# #==================================


# # student_address=[]


# # register=int(input("please enter your register student number(1 to 5) :"))


# # if register >0 and  register <=5:


# #     for i in range(register):

# #         id= input("please enter your id:")
# #         name= input("please enter your name:")
# #         address= input("please enter your address:")
# #         email= input("please enter your email")

# #         print("student id",id)
# # #         print("student name",name)
# # #         print("student address",address)
# #         print("student email",email)

# #         student_address.append([id,name,address,email])

# # else:

# #     print("please enter correct number:")







# #==================================


# # hindi=int(input("please enter hindi marks:"))
# # english=int(input("please enter english marks:"))
# # maths=int(input("please enter english marks:"))
# # science=int(input("please enter science marks:"))
# # computer=int(input("please enter computer marks:"))

# # total_marks=hindi+english+maths+science+computer
# # percentage=total_marks/5

# # print(f"user enter bhindi marks:{hindi}")
# # print(f"user enter english marks:{english}")
# # print(f"user enter maths marks{maths}")
# # print(f"user enter science nmarks:{science}")
# # print(f"user enter computer mareks:{computer}")
# # print(f"user total marks:{total_marks}")
# # print(f"total percentage:{percentage}")


# # if percentage >= 60:

# #     print("student your pass")

# # else:

# #     print("student your fail")


# #=========================================

# # name=input("please enter your name:")

# # name.lower()

# # print("total vowel",name.count('a')+name.count('e')+name.count('i')+name.count('o')+name.count('u'))    


# # name=input("please enter your name:")

# # name.lower()

# # print("name total vowel:",name.count('a')+name.count('e')+name.count('i')+name.count('o')+name.count('u'))
# # #================================


# # listdata=[]


# # for data in range(1,3):

# #     student={}

# #     student["name"]=input("please enter your name:")
# #     student["id"]=input("please enter your id:")
# #     student["address"]=input("please enter your address:")

# #     listdata.append(student)

# #     print(listdata)

# # newname=input("please enter new name replace of(A):")

# # for n in listdata:

# #     if n["name"]=="A":

# #         n["name"]=newname


# #         print(listdata)

# #==================================================
# import json
# student_data=[]


# while True:

#     print("1. student_registration")
#     print("2. student_data_search")
#     print("3. registration_exit")

     
#     choice=input("\nplease enter your choice:")

#     if choice.isdigit():

#         choice=int(choice)
   
#         if choice==1:
            
#             data={"student_id":int(input("please enter student id:")),
#                 "student_name":input("please enter student name:"),
#                 "student_address":input("please enter student address:")
                

#             }

#             student_data.append(data)
                

#         elif choice==2:
            
#             #print(student_data)
#             print(json.dumps(student_data,indent=1))
            
#         elif choice==3:
            

#             print("registration exit")

#             break
#         else:
            
#             print("registration invailed")

     
#     else:

#         print("invalied number please enter digit ")

# #=================================

# # listdata=[2,3,4,5,6,7]
# # listdata2=["sumit","rohan"]

# # merge=listdata+listdata2

# # #===================================

# # import json

# # student_data=[]

# # while True:
    

# #     print("1.registration")
# #     print("2. display student recoard")
# #     print("3. search student")
# #     print("4. exit")

# #     choice=int(input("please enter your choice:"))

# #     if choice == 1:
        
# #         student={}

# #         student["id"]=input("please enter your student id:")
# #         student["name"]=input("please enter your name:")
# #         student["address"]=input("please enter your address:")
# #         student["email"]=input("please enter your email:")

# #         education=input("do you want add more qualification yes/no:")

          
# #         if education=="yes":
            
# #             student["education"]={"name":input("please enter your qualification name:"),
# #                                   "year":input("please enter your qualification year:")

                
# #             }
               
# #             student_data.append(student)

# #             print("registration successfully")
     
# #     elif choice == 2: 
# #         print(json.dumps(student_data,indent=4))
        

# #     elif choice == 3: 
        
# #         search_data=input("please enter your search id:")

# #         for s in student_data:
            
# #             if s["id"]==search_data:
# #                 print(json.dumps(student_data,indent=4))
# #                 print(s)

# #     elif choice ==4:
        
# #         print("registration exit")

# #         break
     

# #     else:    
# #         print("registration invailed")


# # #=================================
# # # # 
# # # def menu():

    
# # #     print("1.addition")
# # #     print("2. subtract")
# # #     print("3.multiply")
# # #     print("4.divided")
# # #     print("5. exit")

# # #     choice=int(input("please enter your choice:"))


# # #     a=int(input("please enter first number:"))
# # #     b=int(input("please enter secoand number"))


# # #     if choice==1:

# # #         print("addition:",a+b)
    
# # #     elif choice==2:

# # #         print("subtract:",a-b)

# # #     elif choice==3:

# # #         print("multiply:",a*b)

# # #     elif choice==4:

# # #         print("divided:",a/b)
# # #     elif choice==5:

# # #         print("exit program")

# # #     else:

# # #         print("inviled choice")


# # # menu()
          
          


     
     
        



     
     

     

     

            

          

     
        
        

        
     
     
        
          

     
          

