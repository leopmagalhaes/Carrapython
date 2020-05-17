#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:31:23 2020

@author: usuario
"""

from telegram.ext import Updater, CommandHandler

up = Updater('')


def Quadrinho(bot, update):

    msg = "Olá {user_name} essa é minha última aventura: https://www.instagram.com/p/CAITIdsDSnW/?utm_source=ig_web_copy_link"

    bot.send_message(chat_id=update.message.chat_id,
                     text=msg.format(
                         user_name=update.message.from_user.first_name))


up.dispatcher.add_handler(CommandHandler('quadrinhos', Quadrinho))
up.start_polling()
