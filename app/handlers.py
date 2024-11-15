from aiogram import F , Router
from aiogram.filters import CommandStart, Command 
from aiogram.types import Message , ReplyKeyboardMarkup , KeyboardButton
import keyboards as kb
import asyncio
import datetime
from datetime import timedelta
import pytz
router = Router()

#starter message
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("Привет ,\nвыбери кнопкочку чтобы начать", reply_markup=kb.main)

#test
@router.message(F.text == 'Засечь время следующего приёма пищи')
async def tasks(message: Message):
    await message.answer('Время начало засекаться\nНапоминание придет через 4 часа')
    await asyncio.sleep(25)
    await message.answer(f'Привет')
    
#test
@router.message(F.text == 'Записать прием пищи ')
async def bread(message: Message):
    nowww = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
    formatted_date = nowww.strftime(r"%Y-%m-%d")
    formatted_time = nowww.strftime("%H:%M:%S")
    response_text = f"Время приёма пищи:  {formatted_time} {formatted_date}"
    await message.reply(f'{response_text}')
    await message.answer("Привет михайло,\nвыбери кнопкочку чтобы начать", reply_markup=kb.main)

#make a reminders
@router.message(F.text == 'Создать напоминания')
async def eat(message: Message):
     await message.answer('Что делаем?',reply_markup=kb.eat)
@router.message(F.text == 'Создать напоминания о еде, воде, сне')
async def call_function_eat(message: Message):
    await message.answer('Напоминание успешно созданны: \n для еды на:[6:30],[16:23], [21:20]!\nдля воды на [8:00],[10:00],[12:00],[14:00],[16:00],[18:00],[20:00],[22:00],[23:59]\nдля сна на [23:00],[23:30],[23:59]')
    await eat_check(message)

async def eat_check(message: Message):
    notification_sent = {
         "notification1": False,
         "notification2": False,
         "notification3": False,
         "notification4": False,
         "notification5": False,
         "notification6": False,
         "notification7": False,
         "notification8": False,
         "notification9": False,
         "notification10": False,
         "notification11": False,
         "notification12": False,
         "notification13": False,
         "notification14": False,
         "notification15": False
         
    }
    #notification and notofication update time
    
    notification1 = datetime.time(hour=17,minute=58,second=00)
    notification2 = datetime.time(hour=17,minute=59,second=00)
    notification3 = datetime.time(hour=21,minute=13,second=00)
    notification4 = datetime.time(hour=21,minute=13,second=5)
    notification5 = datetime.time(hour=21,minute=14,second=00)
    notification6 = datetime.time(hour=18,minute=46,second=15)
    notification7 = datetime.time(hour=18,minute=47,second=00)
    notification8 = datetime.time(hour=16,minute=37,second=00)
    notification9 = datetime.time(hour=16,minute=37,second=00)
    notification10 = datetime.time(hour=16,minute=37,second=00)
    notification11 = datetime.time(hour=16,minute=37,second=00)   
    notification12= datetime.time(hour=16,minute=37,second=00)
    notification13 = datetime.time(hour=16,minute=37,second=00)
    notification14 = datetime.time(hour=16,minute=37,second=00)
    notification15 = datetime.time(hour=16,minute=37,second=00)
    
    update_notification =datetime.time(hour=0,minute=0,second=0)
    notification_keys = list(notification_sent.keys())
    
    #function that sent a mesaege every day at the same time 
    while any(notification_sent[key] != True for key in notification_keys):
        nowww = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
        formatted_time = nowww.time()
        #first notification
        if (formatted_time.hour == notification1.hour and          #1
            formatted_time.minute == notification1.minute and 
            formatted_time.second == notification1.second and 
            not notification_sent["notification1"]):
                await message.answer("Уебище пришло время кушать")
                notification_sent["notification1"] = True
        #second notification       
        if (formatted_time.hour == notification2.hour and           #2
            formatted_time.minute == notification2.minute and 
            formatted_time.second == notification2.second and 
            not notification_sent["notification2"]):
                await message.answer("Уебище пришло попить кушать")
                notification_sent["notification2"] = True
        #third notification        
        if (formatted_time.hour == notification3.hour and            #3
            formatted_time.minute == notification3.minute and 
            formatted_time.second == notification3.second and 
            not notification_sent["notification3"]):
                await message.answer("Уебище пришло попить кушать3")
                notification_sent["notification3"] = True
        
        if (formatted_time.hour == notification4.hour and           #4
            formatted_time.minute == notification4.minute and 
            formatted_time.second == notification4.second and 
            not notification_sent["notification4"]):
                await message.answer("Уебище пришло время кушать4")
                notification_sent["notification4"] = True
        
        if (formatted_time.hour == notification5.hour and           #5
            formatted_time.minute == notification5.minute and 
            formatted_time.second == notification5.second and 
            not notification_sent["notification5"]):
                await message.answer("Уебище пришло время кушать5")
                notification_sent["notification5"] = True
        
        if (formatted_time.hour == notification6.hour and           #6
            formatted_time.minute == notification6.minute and 
            formatted_time.second == notification6.second and 
            not notification_sent["notification6"]):
                await message.answer("Уебище пришло время кушать")
                notification_sent["notification6"] = True
        
        if (formatted_time.hour == notification7.hour and           #7
            formatted_time.minute == notification7.minute and 
            formatted_time.second == notification7.second and 
            not notification_sent["notification7"]):
                await message.answer("Уебище пришло время кушать")
                notification_sent["notification7"] = True   
        
        if (formatted_time.hour == notification8.hour and           #8
            formatted_time.minute == notification8.minute and 
            formatted_time.second == notification8.second and 
            not notification_sent["notification8"]):
                await message.answer("Уебище пришло время кушать")
                notification_sent["notification8"] = True
        
        if (formatted_time.hour == notification9.hour and           #9
            formatted_time.minute == notification9.minute and 
            formatted_time.second == notification9.second and 
            not notification_sent["notification9"]):
                await message.answer("Уебище пришло время кушать")
                notification_sent["notification9"] = True
        
        if (formatted_time.hour == notification10.hour and           #10
            formatted_time.minute == notification10.minute and 
            formatted_time.second == notification10.second and 
            not notification_sent["notification10"]):
                await message.answer("Уебище пришло время кушать")
                notification_sent["notification10"] = True
        
        if (formatted_time.hour == notification11.hour and           #11
            formatted_time.minute == notification11.minute and 
            formatted_time.second == notification11.second and 
            not notification_sent["notification11"]):
                await message.answer(string)
                notification_sent["notification11"] = True 
        
        if (formatted_time.hour == notification12.hour and           #12
            formatted_time.minute == notification12.minute and 
            formatted_time.second == notification12.second and 
            not notification_sent["notification12"]):
                await message.answer("Уебище пришло время кушать") 
                notification_sent["notification12"] = True
        
        if (formatted_time.hour == notification13.hour and           #13
            formatted_time.minute == notification13.minute and 
            formatted_time.second == notification13.second and 
            not notification_sent["notification13"]):
                await message.answer("Уебище пришло время кушать")
                notification_sent["notification13"] = True
        
        if (formatted_time.hour == notification14.hour and           # 14
            formatted_time.minute == notification14.minute and 
            formatted_time.second == notification14.second and 
            not notification_sent["notification14"]):
                await message.answer("Уебище пришло время кушать")
                notification_sent["notification14"] = True
        
        if (formatted_time.hour == notification15.hour and               # 15
            formatted_time.minute == notification15.minute and 
            formatted_time.second == notification15.second and 
            not notification_sent["notification15"]):
                await message.answer("Уебище пришло время кушать")
                notification_sent["notification15"] = True
        
        #notification update 
        if (formatted_time.hour == update_notification.hour and
            formatted_time.minute == update_notification.minute and
            formatted_time.second == update_notification.second):
            notification_sent = {
                "notification1": False,
                "notification2": False,
                "notification3": False
            }


        
