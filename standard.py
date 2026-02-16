# # import calendar

# # yy=int(input("please enter your year:"))
# # mm=int(input("please enter your month:"))

# # print(calendar.month(yy,mm))


# #==============================================


# # import datetime

# # def report_menu():
# #     print("\n--- Select Date Report ---")
# #     print("1. Last 1 Week")
# #     print("2. Last 6 Months")
# #     print("3. Last 1 Year")

# #     choice = input("Enter your choice (1/2/3): ")

# #     if not choice.isdigit():
# #         print(" Invalid input! Number only.")
# #         return None

# #     return int(choice)


# # def date_report():
# #     today = datetime.date.today()
# #     choice = report_menu()

# #     if choice == 1:
# #         from_date = today - datetime.timedelta(days=7)
# #         print(f" Report from {from_date} to {today}")

# #     elif choice == 2:
# #         from_date = today - datetime.timedelta(days=180)
# #         print(f" Report from {from_date} to {today}")

# #     elif choice == 3:
# #         from_date = today - datetime.timedelta(days=365)
# #         print(f" Report from {from_date} to {today}")

# #     else:
# #         print(" Invalid choice! Please select 1, 2 or 3")


# # date_report()

# #==============date time ====================

# # import datetime

# # today=datetime.datetime.today()

# # print(today.strftime("%d/%m/%y"))
# #=========future date time==========



# # import datetime

# # today_datetime = datetime.datetime.now()

# # future_date = today_datetime + datetime.timedelta(days=-30)

# # print(future_date)



# #===========time sleep =============
# # import time
# # data=[1,2,3,4,5,6,7,8]

# # print("searching..............")

# # time.sleep(2)

# # for n in data:

# #     print(n)
# #================================
# import time

# student={"name":"sumit kumar",
#          "address":"mirganj",
#          "state":"bihar"

#          }

# print("searching.....................................")
# time.sleep(3)

# print(student)
# #==============calendar================

# # import calendar

# # year=calendar.calendar(2026)

# # print(year)


# #======================

# # import calendar

# # year=calendar.month(2026,3)

# # print(year)



# #====================================

# # import datetime

# # today_datetime=datetime.datetime.now()

# # student={"name":"sumit kumar",
# #          "address":"mirganj",
# #          "state":"bihar",
# #          "creat_data":str(today_datetime)

         

# #          }




# # print(student)


# #===================================

# # import datetime

# # time_now=datetime.datetime.now().time()
# # print(time_now)



# #===================================

# # import datetime
# # d=datetime.datetime.now()

# # print(d.year)
# # print(d.month)
# # print(d.day)

# # #============================

# # import datetime

# # now=datetime.datetime.now()
# # print(now.strftime("%d/%m/%y"))


#=====================



import math

print(math.sqrt(25))

print(math.pow(2,3))