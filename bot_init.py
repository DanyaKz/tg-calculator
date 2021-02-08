import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboard import Keyboard
from calculator import Calculator


class Bot_init(Keyboard, Calculator):
    def __init__(self, API_TOKEN):
        logging.basicConfig(level=logging.INFO)
        self.bot = Bot(token=API_TOKEN)
        self.dp = Dispatcher(self.bot)
        self.init_calc_values()

    def execute_bot(self):
        executor.start_polling(self.dp, skip_updates=True)

    def start_handler(self):
        @self.dp.message_handler(commands=['start'])
        async def start(message: types.Message):
            await message.answer(text="Hello, I'm a calculator bot🤓", reply_markup=self.get_keyboard())

    def click_handler(self):
        @self.dp.message_handler()
        async def start(message: types.Message):
            keys = [item for sublist in self.get_keyboard()['keyboard'] for item in sublist]
            if message.text in keys:
                await self.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                if self.prev_msg_id and not self.prev_value:
                    await self.bot.delete_message(chat_id=message.chat.id, message_id=self.prev_msg_id)
                answer = await message.answer(self.set_value(message.text))
                self.prev_msg_id = answer.message_id
            else:
                await message.answer("You sent me something wrong.")
                await message.answer(text="🤬", reply_markup=self.get_keyboard())
