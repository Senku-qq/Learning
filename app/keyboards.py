from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
import aiogram


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Создать напоминания')]
],              
                resize_keyboard=True, 
                input_field_placeholder='Солнышко выбери пункт из меню') 
       
        # resize_keyboard=True, 
        # input_field_placehoalder='Солнышко выбери пункт из меню :)') [KeyboardButton(text='run'), resize_keyboard=True, ']
eat = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Создать напоминания о еде, воде, сне')]
  
    
    
],               resize_keyboard=True, 
                input_field_placeholder='Солнышко выбери пункт из меню')