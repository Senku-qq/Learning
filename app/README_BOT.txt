 
В идеале когда создаешь бота нужно импортировать токен из другого файла для безопастности
хендлеры надо в идеале закидывать в другие файлы и потом импортировать их в файл запуска бота 
============================================================= ОСНОВНЫЕ ПОНЯТИЯ В aiogram
|x.start_polling(y) - наш бот , а именно эта функция будет отправлять запрос на сервара aiogram если ответ есть то телеграмм даст ответ и наш бот его обратотает а если нет то функция ----будет ожидать ответа от телеграмма 
|Router - Роутер хрень которая помогает сообщить аиограмму что хендлеры находятся в каком то определенном файле. Елси мы делали хендлеры в основном файле который сейчас используется ----под загрузку то нам нужно dp замениить на название обьекта в котором находиться Router(). После того как поменяли dp на Router нам нужно в основном файле обратиться к диспетчеру ----и вызвать метод include_router() в функции main. После чего во все том же файле нам нужно импортировать название обьекта который хранит в себе Router() и передать его в ----unclude_router(router) это все будет выглядеть примерно вот так: 
+ from "файл" import router или же просто обьект который хранит в себе Router()
----async def main():
        dp.include_router(router)
        await dp.start_polling(bot)

---- для работы роутера нужно создать обьект router = Router() , после этого мы можем за
|bot = Bot(токен: token=TOKEN_API)  инициализирует подключение к токену 
|Dispatcher() - диспетчер, работа происходит через него , его задача обрабатывать входящие обновления, сообщения квобеки и так далее
|Логирование - помогает видеть то что происходит в боте, все его действия, то как он запустился или обработал запрос можно увидеть при помощи логирования , логирование требует импорта
---- + import logging
---- это мы добавляем в if __name__ == '__main__': перед try      а добавляем мы строчку logging.basicConfig(level=logging.INFO)
---- handler - хрень для обраточка входящих сообщений для бота , внутри хендлера находятся фильтры
| пока что в конспекте мы имеем следующие хаедлеры:
---- Обработка комманды старт 
---- Получение айди фотки
---- Отправление фото
---- получение айди пользователя

|caption - Текстовое описание картинки
|reply - бот ответит на отправленное сообщение 
|answer - отправить сообщение
Фильтры:
| CommandStart - это фильтр для получения комманды старт 
| Command - можно написать свою комманду в которой уже мы напишем функцию для ее работы  (Синтаксис такой же самый как и в CommandStart )
| Magic_filter - С помощью этого фильтра можно ловить все что отправил нам пользователь, картинки , видео, локации, стикеры, контакты и так далее .
----Для того чтобы им воспользоваться нужно импортировать класс F а потом подставить его в нужный хендлер. 
 
===========================================================МОЖНО ИСПОЛЬЗОВАТЬ MAGICFILTER В РАЗНЫХ ЦЕЛЯХ

========= ПОЛУЧИТЬ ТЕКСТ ОТ ПОЛЬЗОВАТЕЛЯ И ПОТОМ НАПРИМЕР СРАВНИТЬ ТАКОЙ ЖЕ ЛИ ОН С НАШИМ @dp.message(F.text == 'Как дела?')
---Фактически данный фильтр работает по такой схеме, пользователь что то пишет а фильтр сравнивает написал ли пользователь тоже самое что храниться в F.text если да то он запустит функцию и выведет тот текст который на написали. | Синтаксис снова такой же 

========= ПОЛУЧЕНИЕ ФОТО ОТ ПОЛЬЗОВАТЕЛЯ, АЙДИ ФОТО, ЛИБО ЖЕ ОТПРАВКА ФОТО С  ТЕКСТОМ ИСПОЛЬЗУЯ УЖЕ ГОТОВОЕ АЙДИ 
---- Чтобы словить фото от пользователя можно воспользоваться таким синтаксисом
----@dp.message(F.photo)
----async def get_photo(message: Message) 
        await message.answer(f'ID фото: {message.photo[-1].file_id}')  - то что в {} скобках мы используем для того чтобы получить айди картинки. У каждой картинок,видео, музыки есть свой уникальный номер который знает только этот бот если вы ему что то из этого отправляли
----Тут указан индекс фото [-1] потому что это самое лучшее качество ибо телеграмм сжимает картинки и он хранит их у себя на сервере в разном формате от самого плохого качества до ----самого лучшего, поэтому мы достаем последнее самое лучшее значение
----С помощью этого всего когда пользователь отправит картинку бот в ответ отправит ее уникальный номер(айди) и теперь используя метод отправки картинок и используя это айди мы можем 

========= ОТПРАВИТЬ ПОЛЬЗОВАТЕЛЮ ЭТУ КАРТИНКУ НЕ ЗАГРУЖАЯ ЕЁ С УСТРОЙСТВА | ТАК ЖЕ МОЖНО ОТПРАВИТЬ ФОТКУ ИМЕЯ ССІЛКУ НА НЕЕ | ДЕЛАЕТСЯ ЭТО ПОЧТИ ТАКЖЕ КАК ПОЛУЧЕНИЕ АЙДИ НО ЧУТОЧКУ ПО ДРУГОМУ

----@dp.message(Command('get_photo'))
----async def get_photo(message: Message)
        await message.answer(photo=айди который мы получили,либо ссылка на картинку)

========= ПОЛУЧЕНИЕ АЙДИ ПОЛЬЗОВАТЕЛЯ

@dp.message(CommandStart())
    await message.reply(f'Привет.\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}')

=========================================================== КНОПАШКИ ДЛЯ ВВОДА ИНФОРМАЦИИ 
ВНИМАНИЕ! МЫ МОЖЕТ ДОБАВИТЬ ТОЛЬКО ОДНУ КЛАВИАТУРУ К ОДНОМУ СООБЩЕНИЮ 

существует 2 вида кнопашек (то ксть клавиатуры):

ReplyKeyBoard - с помощью которых можно создать кнопки которыми пользователь может отправлять информацию в чат 
InlineKeyBoard - а уже с их помощью бот сам вововид в чат кнопки которыми мы моежт получить доступ к какой то информации но в чат ничего не выводится , одной из задач inline клавиатуры является создание callback'ов
в reply_keyboardMarkup есть  такие аргументы с ключем  как например: (ИХ НАДО ДОБАВЛЯТЬ В ОБЬЕКТ КОТОРЫЙ СОДЕРЖИТ В СЕБЕ КНОПКИ)
resize_keyboard - пример применения в коде resize_keyboard=True   | размер меняеться до минимального значения , то есть до минимального размера
input_field_placeholder - также пример применения input_field_placehoalder='Выберите пункт меню.' | В общем эта штукенция заменяет текст на поле в котором мы пишем текст а затем отправляем, например стандартный текст там это "Write a message..." НО теперь после того то мы написали будет 'Выберите пункт меню.'

Для работы c ReplyKeyboard нам нужно импортироват из aiogram.types ReplyKeyboardMarkup и KeyboardButton
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

для начала создадим клавиатуру и назовем ее main
main = ReplyKeyboardMarkup() здесь внутри скобок мы должны использовать аргумент keyboard= он должен содержать в себе список внутри кторого есть еще один список и внутри этого списка находиться KeyboardButton , это будет выглядеть вот так (каждый ряд списков это новый ряд кнопок):  и добавим в эту клавиутуру добавим какие то кнопки:
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')] keyboardbutton просит от нас текст 
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')] - так мы можем создать несколько кнопок которые будут находиться друг возле дружки
])
После того как мы добавили кнопки нам нужно перейти в файл с хендлерами и импортировать все что мы написали для кнопочек 
то есть 
import "файл" as kb (это сокращенная фотка keyboard)
теперь все что нам нужно сделать так это в сообщении которое мы выводим добавить reply_markup=kb.main
main потому что это тот файл в котором у нас кнопочки | Пример кода:
@dp.message(CommandStart())
    await message.reply(f'Привет.\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}', reply_markup=kb.main)

Для работы c InlineKeyboard нам нужно импортироват из aiogram.types InlineKeyboardMarkup и InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup , InlineKeyboardButton

делаем тоже самое что и с Reply 
НО когда мы создаеи Inline клавиатуру мы всегда должны вписать что то дополнительное , то есть мы не можем вписать просто текст, мы олжны добавить еще что то 
settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=Youtube', url= 'https://youtube.com')] 
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')] - так мы можем создать несколько кнопок которые будут находиться друг возле дружки
])
=========================================================== БИЛДЕР BUILDER
Бывает такое что мы делаем запрос из базы данных и получаем набор чего то , например список с названием автомобилей. Предположим мы получили такой ответ от базы данных:
cars = ['Tesla', 'Mercedes', 'BMW']
и они могут быть всегда разными то есть это не такая статичная клавиатура и мы не хотим постоянно менять эти значения через код. Чтобы это исправить мы в этом случае пользуемся билдером
для работы с билдером нам нужно для начала его импортировать
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder и теперь мы делаем функцию 

async def reply_cars():
    keyboard = ReplyKeyboardBuilde()
    for car in cars:
        keyboard.add(KeyBoardButton(text=car))
    return keyboard.adjust(2).as_markup() - в случае если мы хотим отредактировать размер этой клавиатуры, но не конкретно рвзмер а то сколько кнопок будет в одном ряду в данном случае у нас будет 2 кнопочки. ВНИМАНИЕ! as_markup() нужно дописывать всегда

После этих махинаций нашу функцию нужно еще вызвать в хендлере, ничего сложного в этом нет пример кода:
@dp.message(CommandStart())
    await message.reply(f'Привет.\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}', reply_markup=await kb.reply.cars())

Чтобы сделать Инлайн клавиатуру нужно всего лишь ReplyKeyboardButton заменить на InlineKeyboardButton и к KeyBoardButton добавить в начало Inline и добавить еще что то после текста, потому что inline принимает только текст
=========================================================== CallBackQuery Клавиатура 
Для работы callback нужно оимпортировать из types сам callback. 
Колбек нужно встраивать в функцию пример:
@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.message.answer('Привет')

после этого клавиатура будет постоянно гореть, чтобы это исправить нужно сделать следующее
router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer(''вы выбрали каталог) - короткое уведомление , чтобы сделать уведомление как отдельное окно нужно добавить show_alert = True
    await callback.message.answer('Привет')
Чтобі сделать еще набор кнопок в callback нужно сделать следующее:
async def catalog(callback: CallbackQuery):
    await callback.answer(''вы выбрали каталог) - короткое уведомление , чтобы сделать уведомление как отдельное окно нужно добавить show_alert = True
    await callback.message.edit_text('Привет', reply_markup=await kb.inline_cars())


=========================================================== БАЗА ДЛЯ РАБОТЫ БОТА
import asyncio                
from aiogram import Bot, Dispatcher , types

TOKEN_API = "сам токен"


bot = Bot(токен: token=TOKEN_API)  
dp = Dispatcher()  

async def main():
    await dp.start_polling(bot)    

if __name__ == '__main__': апускает функция мейн позволяет запускать эту функцию только в том случае еслм мы запускаем именно этот файл а не импортируем его 
    
   | При выходе из самого бота во время вызова его в терминале должна быть ошибка raise KeytboardInterrupt() чтобы решить которую нужно сделать try except | 
    
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
    


=========================================================== ОБРАБОТЧИК КОТОРЫЙ ЛОВИТ КОММАНДУ СТАРТ
+ from aiogram.filters import CommandStart
+ from aiogram.types import Message

@dp.message(CommandStart())     dp. является диспетчером и сейчас он использует метод message который говорит о том что диспетчер ждет именно сообщение в данном случае КОМАНДУ СТАРТ
async def cmd_start(message: Message):
    await message.answer('Привет!')





