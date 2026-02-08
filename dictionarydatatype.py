#==========dictionar data type===========#

marks={"hindi":20,"maths":30,"english":50}

marks2={"sanskrit":20,"computer":30,"science":50}


total_marks=marks["hindi"]+marks["maths"]+marks["english"]

print(marks)
print(total_marks)
print(marks2)

#======================

marks={}


marks["hindi"]=int(input("enter hindi marks:"))
marks["english"]=int(input("enter english marks:"))
marks["maths"]=int(input("please enter maths marks:"))
#total_marks=marks["hindi"]+marks["english"]+marks["maths"]


print(marks)



#========input user===========#


student_marks={}

student_marks["hindi"]=int(input("enter hindi marks:"))
student_marks["english"]=int(input("enter english marks:"))
student_marks["maths"]=int(input("enter maths marks:"))

total_marks=student_marks["hindi"]+student_marks["english"]+student_marks["maths"]

print(student_marks)
print(total_marks)


#==========================#


#===============EK HI VARIABLE ME  5 STUDENT KE DATA===========================



student_address={"student1":{"name":"sumit kumar",
                             "address":"mirganj",
                             "education":{"name":"BA","year":2035}



},"student2":{"name":"rohan kumar",
                             "address":"gopalganj",
                             "education":{"name":"BA","year":2035}


}

}
print(student_address)
print(student_address["student1"]["education"]["name"])



#=======================ekhi variable me user se input==============


student_address={"student1":{"name":input("please enter your name:"),
                             "address":input("please enter address:"),
                             "id":input("please enter id:"),
                             "education":{"name":input("enter education name:"),
                                          "year":input("enter your ysar:")
                                 
                             }

},"student2":{"name":input("please enter name:"),
              "address":input("please enter address:"),
              "id":input("please enter id:"),
              "education":{"name":input("plese enter name:"),"year":input("enter your year:")}



},"student3":{"name":input("please enter name:"),
              "address":input("please enter address:"),
              "id":input("please enter id:"),
              "education":{"name":input("plese enter name:"),"year":input("enter your year:")}






},"student4":{"name":input("please enter name:"),
              "address":input("please enter address:"),
              "id":input("please enter id:"),
              "education":{"name":input("plese enter name:"),"year":input("enter your year:")}



},"student5":{"name":input("please enter name:"),
              "address":input("please enter address:"),
              "id":input("please enter id:"),
              "education":{"name":input("plese enter name:"),"year":input("enter your year:")}






}


}



print(student_address)



#=========================#



student={"id":101,
         "qualification":{"year":2022,"name":"Ba"},
         "experience":{"exp_name":"it company","exp_year":2025},
        
        
         }


ram=student["qualification"]


print(data["name"])


#==================================



first_student={"name":"sumit kumar","address":{"village":"mirganj","mob":6209563088},
               "education":{"name":"BA"},"email_id":"sumitkumar25@gmail.com"
               
               
              }
#address=first_student["education"]
print(first_student["address"])


secoand_student={"name":"rohan kumar","address":{"village":"mirganj","mob":5688987654},    #nested
                 "education":{"name":"greaguation"},"email_id":"rohankumar26@gamil.com"
                 
                 
                }

looka=secoand_student["address"]

print(looka["mob"])

#===========================================

student_address={"name":"sumit kumar",
                 "age":20,
                 "education":
                 {"year":2024,"name":"BA"},
                 "company":
                 {"name":"indixpert"} 
                 
                 }
student_address["name"]="bablu kumar"       #key ka name change
print(student_address)

student_address["year"]=2025
print(student_address)

#===================================

address={"name":"sumit kumar",
         "subject":["c","java","python"],       #disnuary me list use
         "address":("mirganj","gopalganj")      #disnuary me tuple use


}


address={"name":"sumit kumar",
         "address":"mirganj",
         "subject":["hindi","english","maths"]
    

}

print(address["subject"])
print(len(address))
print(address.key())


print(address["subject"])

#========================================

#decionary method  1

student_address={"name":"sumit kumar",
                 "age":20,
                 "education":
                 {"year":2024,"name":"BA"},
                 "company":
                 {"name":"indixpert"} 
                 
                 }


print(len(list(student_address.keys())))       #keys mathod     lenhth

print(len(student_address))                 #length

#===========================================
#decionary method 2

student_address={"name":"sumit kumar",
                 "age":20,
                 "education":
                {"year":2024,"name":"BA"},
                 "company":
                 {"name":"indixpert"} 
                 
                 }
print((list(student_address.values())))         #values method


#========================================
#decionary method  3

student_address={"name":"sumit kumar",
                 "age":20,
                 "education":
                 {"year":2024,"name":"BA"},
                 "company":
                 {"name":"indixpert"} 
                 
                 }
print(student_address.items())          #pura keys values print hoga


#==================================

#decionary method  4


student_address={"name":"sumit kumar",
                 "age":20,
                 "education":
                 {"year":2024,"name":"BA"},
                 "company":
                 {"name":"indixpert"} 
                 
                 }

# print(student_address["name"])

print(student_address)      #name print hoga

#===================================
# decionay mehod 5

student={}
        
         

student.update({"name":"sumit kumar","address":"mirganj","education":{"name":"BA","year":2937}})
print(student)


#======================================pop method =======

student={"name":input("please enter name:"),
        "address":input("please enter address:"),
        "education":{"name":input("please enter your education name:"),"year":input("please enter year:")}







}


student.pop("address")

print(student)

#===============================git method====================



student={"name":input("please enter name:"),
        "address":input("please enter address:"),
        "education":{"name":input("please enter your education name:"),"year":input("please enter year:")}



}



print(student.get("address"))


#================================clear method===================



student={"name":input("please enter name:"),
        "address":input("please enter address:"),
        "education":{"name":input("please enter your education name:"),"year":input("please enter year:")}



}


print(student.clear())
















