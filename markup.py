from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


deps = open('.idea/text_files/department_list.txt', 'r')

button1 = InlineKeyboardButton('phukethospital.com', url='https://www.phukethospital.com/')
button2 = InlineKeyboardButton('Location ', url='https://goo.gl/maps/She8QWXjjMntKB1d8')
docs_btn = InlineKeyboardButton('You can submit it via this here\n', url='https://insuranceassist.carrd.co')

keyboard_insurance = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(docs_btn)
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard1 = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2)
check_up = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    InlineKeyboardButton('Find program', url='http://www.phukethospital.com/checkup/en/'), InlineKeyboardButton(text='More check up programs', command='checkup' ))
dental_cost = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(InlineKeyboardButton('Find out '
                                                                                                          'cost',
                                                                                                          url='https://www.phukethospital.com/dental-treatment-cost/'))
for dep in deps:
    btn = KeyboardButton(dep)
    keyboard2.add(btn)