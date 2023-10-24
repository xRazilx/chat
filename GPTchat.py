import openai
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.methods.send_message import SendMessage

dp = Dispatcher()

openai.api_key = "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"


@dp.message(Command(commands=["start"]))
async def start(message: Message) -> None:
    await message.answer("Пртвет!\n Я бот - искусственный интеллект")
    return


@dp.message(Command(commands=["chat"]))
async def ii(message: Message) -> None:
    message.text[6:]
    response = openai.Completion.create(
     engine="text-davinci-003",
     prompt='"""\n{}\n"""'.format(message.text),
     temperature=0,
     max_tokens=1200,
     top_p=1,
     frequency_penalty=0,
     presence_penalty=0,
     stop=['"""'])
    await bot.send_message(message.chat.id, f'\n{response["choices"][0]["text"]}', parse_mode='Markdown')
    return


bot = Bot("6960966986:AAGFHHX2wroNFUpXAQpb98BZyWaql34VbSE")
dp.run_polling(bot)
