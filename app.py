from aiogram import Bot, Dispatcher, executor, types
import config
import markup as nav
import department_discription

bot = Bot(token=config.bot_api)
dp = Dispatcher(bot)
check_up = open('.idea/check_up/heartLogo.jpg', "rb")

@dp.message_handler(commands=['start'])
async def welcome(message=types.Message):
    await message.answer(
        department_discription.greeting_message)


@dp.message_handler(commands=['information'])
async def information(message=types.Message):  # прикрепить клавиатуру с сайтом, телефоном, локация
    await message.answer(text='\nBangkok Hospital Phuket Address: \n'
                              '\n2, 1 Hongyokutis Rd, Tambon Talat Yai,'
                              'Mueang Phuket District, Phuket 83000 \n'
                              '\nWe speak your language you can call and ask \nTel: 076 254 425, 1719 \n'
                              '\nE-mail: info@phukethospital.com', reply_markup=nav.keyboard1)


@dp.message_handler(
    commands=['appointment'])  # ReplyKeyboard с направлениями > сохранить ответ > дать контакт и нужно ли записываться
async def appointment(message=types.Message):
    await message.answer(text='Please choose from list : ', reply_markup=nav.keyboard2)


@dp.message_handler(commands=['insurance'])  # позвонить в страховку и следовать их инструкциям
async def insurance(message=types.Message):
    await message.answer(text=department_discription.insurance_welcome)
    await message.answer(text=department_discription.documents, reply_markup=nav.keyboard_insurance)
    await message.answer(text='Place your Name and Last name in Email Subject')


@dp.message_handler(commands=['help'])
async def welcome(message=types.Message):
    await message.answer("Hello this is just second keyboard message to reply!")


@dp.message_handler()
async def main_handler(message: types.Message):
    if message.text == 'Dermatology':
        await message.answer(text=department_discription.dermatology_about)
    elif message.text == 'Eye Center':
        await message.answer(text=department_discription.eye_about)
    elif message.text == 'Pediatric':
        await message.answer(text=department_discription.pediatric_about)
    elif message.text == 'General Medicine':
        await message.answer(text=department_discription.general_medicine)
    elif message.text == 'Orthopaedic':
        await message.answer(text=department_discription.orthopedic_sport)
    elif message.text == 'Surgery':
        await message.answer(text=department_discription.surgery_center)
    elif message.text == 'Gastrointestinal Center':
        await message.answer(text=department_discription.gi)
    elif message.text == 'Wellness check-up':
        await message.answer(text=department_discription.wellness_center)
        await message.answer('Make short test to check which program to choose\n'
                             'http://www.phukethospital.com/checkup/en/', reply_markup=nav.check_up)
    elif message.text == 'Gynecology':
        await message.answer(text=department_discription.gyne)
    elif message.text == 'Neurology':
        await message.answer(text=department_discription.nuro)
    elif message.text == 'Colorectal Disease Institute':
        await message.answer(text=department_discription.colon)
    elif message.text == 'Heart Center':
        await message.answer(text=department_discription.heart_center)
    elif message.text == 'Dental Center':
        await message.answer(text=department_discription.dental)
        await message.answer(department_discription.dental_cost_text, reply_markup=nav.dental_cost)
    else:
        await message.answer('Please try again something went wrong')



executor.start_polling(dp)
