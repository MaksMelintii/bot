from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import random
from openai import OpenAI




bot = Bot('7582857917:AAFQoaGQJNAEfdjlBBvnTgWQRGSfsQtxHSQ')
dp = Dispatcher(bot=bot)
main= ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

catalog = InlineKeyboardMarkup(row_width=1)
catalog.add(InlineKeyboardButton(text='Покажи хто сама лутша девочка в міре',url='https://www.instagram.com/lyubchinska.al/'))
main.add('Скажи Комплемент', 'Хто сама лутша девочка?','Хочу пообщятись')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.forward_message(-4717577853, message.from_user.id, message.message_id)
    await message.answer(f'Киць цей бот буде відправляти тобі комплементи.', reply_markup=main)
    await bot.send_message(-4717577853, 'Киць цей бот буде відправляти тобі комплементи.')

@dp.message_handler(content_types=['photo'])
async def photo(message: types.Message):
    await bot.forward_message(-4717577853, message.from_user.id, message.message_id)
    await message.answer('а я відправив цю фотку Максіку\U0001F92D\U0001F92D')

@dp.message_handler(text='Хочу пообщятись')
async def ai(message: types.Message):
    completion = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": message.message_id}
        ]
    )
    await message.answer(completion.messages[0]['content'])

@dp.message_handler(text='Хто сама лутша девочка?')
async def url(message: types.Message):
    await bot.forward_message(-4717577853, message.from_user.id, message.message_id)
    await message.answer('Сама лутша девочка в міре тут', reply_markup=catalog)
    await bot.send_message(-4717577853, text=f'{message.from_user.first_name} нажав на кнопку Сама лутша девочка в міре тут')

@dp.message_handler(text='Скажи Комплемент')
async def complement(message: types.Message):
    await bot.forward_message(-4717577853,message.from_user.id, message.message_id)
    random_number = random.randint(1, 33)
    if random_number == 1 or random_number == 9:
        com1 = 'Киця ти така гарна\U0001F60D'
        await message.answer(com1)
        await bot.send_message( -4717577853,com1)
    if random_number == 9 or random_number == 8:
        com8 = 'Ти сама лутша киця моя на світі\U00002764\U00002764'
        await message.answer(com8)
        await bot.send_message(-4717577853,com8)
    if random_number == 2:
        com2 = '\U00002764Кожен раз коли ти мені снишся, то я сама щаслива людина на світі\U00002764'
        await message.answer(com2)
        await bot.send_message(-4717577853, com2)
    if random_number == 3:
        com3 = 'Вибач, що я так пильно дивлюся на тебе. Хочу у найдрібніших деталях запам\'ятати твої прекрасні риси'
        await  message.answer(com3)
        await bot.send_message(-4717577853,com3)
    if random_number == 4:
        com4 = 'Я не помню чи це казав, у тебе дуже гарна ДУША\U0001F60D'
        await  message.answer(com4)
        await bot.send_message(-4717577853,com4)
    if random_number == 5:
        com5 = 'Це тобі букет з 101 роз \U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339\U0001F339'
        await message.answer(com5)
        await bot.fsend_message(-4717577853, com5)
    if random_number == 6:
        com6 = 'Я тебе люблю сильно\U00002764\U00002764\U00002764'
        await message.answer(com6)
        await bot.send_message(-4717577853,com6)
    if random_number == 7:
        com7 = 'Ти є одною з найцікавіших людей в моєму оточенні, з тобою час летить непомітно.'
        await message.answer(com7)
        await bot.send_message(-4717577853,com7)
    if random_number == 11:
        com8 = 'Твоя доброта підкорила моє серце.'
        await message.answer(com8)
        await bot.send_message(-4717577853, com8)
    if random_number == 12:
        com9 = 'Твій голос схожий на чарівну мелодію, і мені дуже подобається його слухати.'
        await message.answer(com9)
        await bot.send_message(-4717577853, com9)
    if random_number == 13:
        com10 = 'Шкода, що ми не познайомилися раніше. Занадто багато часу згаяно!'
        await message.answer(com10)
        await bot.send_message(-4717577853, com10)
    if random_number == 14:
        com11 = 'Ти завжди вмієш заспокоїти та підтримати мене.'
        await message.answer(com11)
        await bot.send_message(-4717577853, com11)
    if random_number == 15:
        com12 = 'Ти даруєш мені затишок і тепло.'
        await message.answer(com12)
        await bot.send_message(-4717577853, com12)
    if random_number == 16:
        com13 = 'Я тобою повністю підкорений.'
        await message.answer(com13)
        await bot.send_message(-4717577853, com13)
    if random_number == 17:
        com14 = 'Ти схожа на принцесу з казки.'
        await message.answer(com14)
        await bot.send_message(-4717577853, com14)
    if random_number == 18:
        com15 = 'Хочу поїхати з тобою на край світу.'
        await message.answer(com15)
        await bot.send_message(-4717577853, com15)
    if random_number == 19:
        com16 = 'Ти – моя мрія, що збулася.'
        await message.answer(com16)
        await bot.send_message(-4717577853, com16)
    if random_number == 20:
        com17 = 'Твої губи створені для поцілунків.'
        await message.answer(com17)
        await bot.send_message(-4717577853, com17)
    if random_number == 21:
        com18 = 'Сьогодні ти прекрасна, як і завжди.'
        await message.answer(com18)
        await bot.send_message(-4717577853, com18)
    if random_number == 22:
        com19 = 'Твоя фігура приголомшує уяву!'
        await message.answer(com19)
        await bot.send_message(-4717577853, com19)
    if random_number == 23:
        com20 = 'Я готовий на все заради твого щастя.'
        await message.answer(com20)
        await bot.send_message(-4717577853, com20)
    if random_number == 24:
        com21 = 'У тебе такі тонкі і витончені пальчики, що мені хочеться весь час тримати тебе за руку.'
        await message.answer(com21)
        await bot.send_message(-4717577853, com21)
    if random_number == 25:
        com22 = 'Хочеться цілувати кожен сантиметр твого тіла і весь час насолоджуватися тобою.'
        await message.answer(com22)
        await bot.send_message(-4717577853, com22)
    if random_number == 26:
        com23 = 'Мені шалено хочеться тебе обійняти прямо зараз, але я боюся, що, зробивши це, вже не зможу втриматися від продовження.'
        await message.answer(com23)
        await bot.send_message(-4717577853, com23)
    if random_number == 27:
        com24 = 'Я хочу, щоб те, що є між нами, тривало дуже, дуже довго. Ні, не так. Хочу, щоб це було назавжди і саме з тобою.'
        await message.answer(com24)
        await bot.send_message(-4717577853, com24)
    if random_number == 28:
        com25 = 'Мені важко висловити свої почуття до тебе, тому що таких сильних емоцій я ніколи не відчував.'
        await message.answer(com25)
        await bot.send_message(-4717577853, com25)
    if random_number == 29:
        com26 = 'У дитинстві мріяв стати піратом. Схоже, став. Ром пив, бороду відпускав, на кораблі плавав, тепер ось скарб знайшов.'
        await message.answer(com26)
        await bot.send_message(-4717577853, com26)
    if random_number == 30:
        com27 = 'Кажуть, потрібно брати від життя тільки найкраще. Тож я тебе забираю.'
        await message.answer(com27)
        await bot.send_message(-4717577853, com27)
    if random_number == 31:
        com28 = 'Мій світ крутиться навколо тебе'
        await message.answer(com28)
        await bot.send_message(-4717577853, com28)
    if random_number == 32:
        com29 = 'Сто тисяч бурундуків, кошенят і панд не зрівняються з тобою по м\'якості й пухнастості!'
        await message.answer(com29)
        await bot.send_message(-4717577853, com29)
    if random_number == 33:
        com30 = 'Якби краса вимірювалася в балах, як землетрус, то твоїй би привласнили 12 балів, адже вона має величезну силу і настільки неповторна, що зустріти подібну практично неможливо.'
        await message.answer(com30)
        await bot.send_message(-4717577853, com30)












@dp.message_handler()
async def a(message: types.Message):
    await bot.forward_message(-4717577853,message.from_user.id, message.message_id)
    await message.answer('шось не то написала')
    await bot.send_message(-4717577853,'шось не то написала')

@dp.message_handler(content_types=['sticker'])
async def sticker(message: types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_message(message.from_user.id, message.chat.id)

if __name__ == '__main__':
    executor.start_polling(dp)

