import random
import nltk
from aiogram import Bot, Dispatcher, executor, types
import config
import markup as nav
import department_discription
import brain

bot = Bot(token=config.bot_api)
dp = Dispatcher(bot)
check_up = open('.idea/check_up/heartLogo.jpg', "rb")
brain_as_list_greetings = list(brain.BOT_CONFIG['intents']['greeting']['examples'])
brain_as_list_buy = list(brain.BOT_CONFIG['intents']['buy']['examples'])
brain_as_list_insurance = list(brain.BOT_CONFIG['intents']['insurance']['examples'])
brain_as_list_help = list(brain.BOT_CONFIG['intents']['help']['examples'])
department_list = open('.idea/text_files/department_list.txt')
department_as_list = list(department_list)

nltk.edit_distance('ghbdtn', 'ghbdtn')


def clean_text(text):
    final_text = ''
    for a in text:
        if a in department_discription.alphabet_eng_rus:
            final_text = final_text + a
    return final_text


@dp.message_handler(commands=['start'])
async def welcome(message=types.Message):
    if message.from_user.username is None:
        await message.answer('Hi Dear Visitor' + department_discription.greeting_message, parse_mode='HTML')

    else:
        await message.answer('Hi ' + message.from_user.username.title() + '👋' +
                             department_discription.greeting_message, parse_mode='HTML')
        await bot.send_sticker(chat_id=message.from_user.id,
                                              sticker='CAACAgIAAxkBAAEGfGVjexGXme_6rf8d8gkcBypWXDcExAACUQQAAsxUSQn4nKzXWabcsysE')


@dp.message_handler(commands=['information'])
async def information(message=types.Message):  # прикрепить клавиатуру с сайтом, телефоном, локация
    await message.answer(text='\nBangkok Hospital Phuket Address: \n'
                              '\n2, 1 Hongyokutis Rd, Tambon Talat Yai,'
                              'Mueang Phuket District, Phuket 83000 \n'
                              '\nWe speak your language, You can call phone us and ask \nTel: 076 254 425, 1719 \n'
                              '\nE-mail: info@phukethospital.com', reply_markup=nav.keyboard1, parse_mode='HTML')
    await bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgIAAxkBAAEGfGljexULIgNHRgHirnTu-8NF_KKsEAACXQQAAsxUSQnVyH2YU9hl-CsE')


@dp.message_handler(
    commands=['appointment'])  # ReplyKeyboard с направлениями > сохранить ответ > дать контакт и нужно ли записываться
async def appointment(message=types.Message):
    await message.answer(text='Please choose from list : ', reply_markup=nav.keyboard2)


@dp.message_handler(commands=['insurance'])  # позвонить в страховку и следовать их инструкциям
async def insurance(message=types.Message):
    await message.answer(text=department_discription.insurance_welcome, parse_mode='HTML')
    await message.answer(text=department_discription.documents, reply_markup=nav.keyboard_insurance, parse_mode='HTML')
    await message.answer(text='Place your Name and Last name in Email Subject')


@dp.message_handler(commands=['help'])
async def welcome(message=types.Message):
    await message.answer(text=department_discription.help_answer, parse_mode='HTML')


@dp.message_handler()
async def main_handler(message: types.Message):
    message_clean = clean_text(message.text.lower().strip())
    if message_clean == 'dermatology':
        await message.answer(text=department_discription.dermatology_about)
    elif message_clean == 'eye center':
        await message.answer(text=department_discription.eye_about)
    elif message_clean == 'pediatric':
        await message.answer(text=department_discription.pediatric_about)
    elif message_clean == 'general medicine':
        await message.answer(text=department_discription.general_medicine)
    elif message_clean == 'orthopaedic':
        await message.answer(text=department_discription.orthopedic_sport)
    elif message_clean == 'surgery':
        await message.answer(text=department_discription.surgery_center)
    elif message_clean == 'gastrointestinal center':
        await message.answer(text=department_discription.gi)
    elif message_clean == 'wellness check-up':
        await message.answer('Make short test to check which program to choose\n'
                             '\nhttp://www.phukethospital.com/checkup/en/', reply_markup=nav.check_up)
        await message.answer(text=department_discription.wellness_center)
    elif message_clean == 'gynecology':
        await message.answer(text=department_discription.gyne)
    elif message_clean == 'neurology':
        await message.answer(text=department_discription.nuro)
    elif message_clean == 'colorectal Disease Institute':
        await message.answer(text=department_discription.colon)
    elif message_clean == 'heart Center':
        await message.answer(text=department_discription.heart_center)
    elif message_clean == 'dental Center':
        await message.answer(text=department_discription.dental)
        await message.answer(department_discription.dental_cost_text, reply_markup=nav.dental_cost)
    elif message_clean in brain_as_list_greetings:
        for intent in brain.BOT_CONFIG['intents'].keys():
            for example in brain.BOT_CONFIG['intents'][intent]['examples']:
                s1 = message_clean
                s2 = example
                if message_clean == example:
                    if nltk.edit_distance(s1, s2) / max(len(s1), len(s2)) < 0.4:
                        await message.answer(
                            random.choice(brain.BOT_CONFIG['intents']['greeting']['response']))
    elif message_clean in brain_as_list_buy:
        for intent in brain.BOT_CONFIG['intents'].keys():
            for example in brain.BOT_CONFIG['intents'][intent]['examples']:
                s1 = message_clean
                s2 = example
                if message_clean == example:
                    if nltk.edit_distance(s1, s2) / max(len(s1), len(s2)) < 0.4:
                        await message.answer(
                            random.choice(brain.BOT_CONFIG['intents']['buy']['response']))
    elif message_clean in brain_as_list_insurance:
        for intent in brain.BOT_CONFIG['intents'].keys():
            for example in brain.BOT_CONFIG['intents'][intent]['examples']:
                s1 = message_clean
                s2 = example
                if message_clean == example:
                    if nltk.edit_distance(s1, s2) / max(len(s1), len(s2)) < 0.4:
                        await message.answer(text=department_discription.insurance_welcome, parse_mode='HTML')
                        await message.answer(text=department_discription.documents, reply_markup=nav.keyboard_insurance, parse_mode='HTML')
                        await message.answer(text='Place your Name and Last name in Email Subject')
    elif message_clean in brain_as_list_help:
        for intent in brain.BOT_CONFIG['intents'].keys():
            for example in brain.BOT_CONFIG['intents'][intent]['examples']:
                s1 = message_clean
                s2 = example
                if message_clean == example:
                    if nltk.edit_distance(s1, s2) / max(len(s1), len(s2)) < 0.4:
                        await message.answer(text=department_discription.help_answer, parse_mode='HTML')

    else:
        await message.answer('I dont understand you')


executor.start_polling(dp)
