from aiogram import Bot, Dispatcher, executor, types
from googlesearch import search


bot = Bot(token="Your_bot_Token")

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello!\nWrite me what you want to find and i will send you a couple of links to what you are looking for!")
    
    
@dp.message_handler(content_types='text')
async def search_from_user(message: types.Message):
    x = search(message.text, lang='eng', stop=3)
    for i in x:
        await message.reply(i)
        
        
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
