from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from keyboards.buttons import back_to_menu_button
import logging

user_router = Router()
logger = logging.getLogger(__name__)

@user_router.message(Command("start"))
async def user_start(message: Message):
    await show_user_menu(message.answer)  # Используем message.answer для отправки нового сообщения
    logger.info(f"💙 Пользователь @{message.from_user.username} ({message.from_user.id}) вызывает меню для юзеров.")

@user_router.message(Command("menu"))
async def user_menu(message: Message):
    await show_user_menu(message.answer)  # Используем message.answer для отправки нового сообщения
    logger.info(f"💙 Пользователь @{message.from_user.username} ({message.from_user.id}) вызывает меню для юзеров.")

async def show_user_menu(edit_function):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎵 Поиск треков", switch_inline_query_current_chat=""),
                InlineKeyboardButton(text="🧠 Настройки ИИ", callback_data="ai_button")
            ],
            [
                InlineKeyboardButton(text="🆘 Помощь", callback_data="help_button"),
                InlineKeyboardButton(text="🫰 Поддержать проект", url="https://boosty.to/mikuplay")
            ],
        ]
    )
    await edit_function('👋 *Приветствую вас в своей музыкальной обители, Пользователь Интернета!*\n\n👀 _Так-так, посмотрим... Ого! Похоже, вы являетесь почётным посетителем здесь! Добро пожаловать! Чувствуйте себя как дома. ᓚᘏᗢ_\n\n💬 *Кстати, ты можешь пообщаться со мной, обращаясь по имени. Пример:* `Мику, привет! Как дела?` _(Условия использования бота и ИИ читайте в меню "Помощь")_\n\n💙 *Выберите действие почётного посетителя:*', reply_markup=keyboard, parse_mode="Markdown")
    
@user_router.callback_query(F.data == "help_button")
async def show_help_menu(callback_query: CallbackQuery, state: FSMContext):
    logger.info(f"🆘 Пользователь @{callback_query.from_user.username} ({callback_query.from_user.id}) зашёл в меню помощи.")
    await callback_query.message.edit_text('💙 *MikuPlayBot* `alpha 0.1.7` *"Первый текст будущего"*\n\n_О проекте: MikuPlay — бесплатный open-source бот для быстрого поиска и скачивания музыки в Telegram со своей базой данных, пополняемой вручную. Доступен inline-режим для поиска. Работает как в личных сообщениях, так и в группах._\n\n🧡 *Powered by Meme Corp.*\n📧 *mikuplaybot@memecorp.ru*\n🌐 *team.memecorp.ru*\n\n*Условия использования и дисклеймер:*\n*1.* Все композиции, представленные в данном боте, были взяты из открытых источников и предоставляются исключительно для ознакомительных целей.\n*2.* Мы не поощряем пиратство и всегда за использование лицензионного контента через соответствующие официальные сервисы с подписками. Если у вас есть возможность и желание поддержать любимого исполнителя, вас ничто не должно останавливать сделать это.\n*3.* Мы не несём ответственности за ответы нейросети и за запросы пользователей к ней. Вся ответственность за запросы пользователей лежит на самих пользователях.\n*4.* Функционал ИИ в данном боте представлен исключительно в развлекательных целях, и ответы нейросети могут содержать ошибки/отсебятину. Проверяйте важную информацию.\n*5.* Используя данного бота, вы автоматически соглашаетесь с этими условиями использования и дисклеймером.\n\n*DMCA:*\nЕсли вы считаете, что ваш контент не должен быть здесь, напишите нам на почту mikuplaybot@memecorp.ru с пометкой `нарушение авторских прав` или `DMCA`.', parse_mode="Markdown", reply_markup=back_to_menu_button)
