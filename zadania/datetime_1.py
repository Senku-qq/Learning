from datetime import datetime 
time_now = datetime.now()

# day = time_now.strftime(r"%d")
# month = time_now.strftime("%m")
# year = time_now.strftime("%Y")
# print(lol)
# print(time_now.hour, ":", time_now.minute, ":", time_now.second)

print(f"День: {time_now.day}\nМесяц: {time_now.month}\nГод: {time_now.year}")