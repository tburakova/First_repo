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
def get_numbers_ticket(min, max, quantity):
    for num in [min, max, quantity]:
        if not (1<=num<=1000):
            return[]
        un_numb = random.sample(range(min,max+1),quantity)
        return sorted(un_numb)
lottery_numbers = get_numbers_ticket(1,100,5)
print("Ваші лотерейні числа:", lottery_numbers)