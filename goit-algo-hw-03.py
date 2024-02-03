#TASK_1
import datetime
from datetime import datetime
def get_days_from_today(date=input("Введіть дату YYYY-MM-DD: ")):
    try:
        date1 = datetime.strptime(date, "%Y-%m-%d")
    except Exception as e:
        print(f"{e}")
    date_now = datetime.today()
    return(date1-date_now).days

print(get_days_from_today())

#TASK_2
import random
def get_numbers_tickets(min,max,quantity):
    if (min<1 or max>1000 or max<min or quantity not in range(min,max)) or (quantity>(max-min)):
        return "Error"
    list1=[]
    while(len(list1)<quantity):
        a=random.randint(min,max)
        if a not in list1:
            list1.append(a)
    list1.sort()
    return list1
        
print(get_numbers_tickets(1,49,6))

#Task_3
import re
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
def normalize_phone(phone_number):
    pat = r"[\d\+]+"
    phone_number = ''.join(re.findall(pat,phone_number))
    if len(phone_number)==10:
       phone_number = '+38'+phone_number
    elif  len(phone_number)==12:
       phone_number = '+'+phone_number   
    elif  len(phone_number)<10:
       print("Введені дані не є номером телефону")      
    return phone_number 

for phone in raw_numbers:
    print(normalize_phone(phone))

#TASK_4
import datetime as dt
from datetime import datetime as dtdt
users = [
    {"name": "John Doe", "birthday": "1985.02.05"},
    {"name": "Jane Smith", "birthday": "1990.02.03"}
]

def get_upcoming_birthdays(users=None):
    tdate=dtdt.today().date() 
    birthdays=[] 
    for user in users: 
        bdate=user["birthday"] 
        bdate=str(tdate.year)+bdate[4:] 
        bdate=dtdt.strptime(bdate, "%Y.%m.%d").date() 
        week_day=bdate.isoweekday() 
        days_between=(bdate-tdate).days 
        if 0<=days_between<7: 
            if week_day<6: 
                birthdays.append({'name':user['name'], 'birthday':bdate.strftime("%Y.%m.%d")})               
            else:
                if (bdate+dt.timedelta(days=1)).weekday()==0:
                    birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                elif (bdate+dt.timedelta(days=2)).weekday()==0: 
                    birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
    return birthdays

print(get_upcoming_birthdays(users))