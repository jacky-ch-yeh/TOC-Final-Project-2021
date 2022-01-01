from transitions.extensions import GraphMachine

import os
import sys

from utils import send_text_message, send_button_message 

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, ImageCarouselColumn, URITemplateAction, MessageTemplateAction

load_dotenv()

from bs4 import BeautifulSoup as bs
import requests

import message_UI
from crawling import search_stock_price, get_article_list, get_wiki
import random

ic = 0
system = 1
stock_type = ic

M = 2454
N = 3034
R = 2379
C = 3443
S = 3035

sea = 2317
wayin = 6669
tai = 2308
waytrunc = 3231
ho = 4938

target_company_id = M
target_company_name = ''

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return (text == "主選單" or text.lower() == 'menu')

    def is_going_to_article(self, event):
        text = event.message.text
        return text == "找話題"

    def is_going_to_refind_article(self, event):
        text = event.message.text
        return text == "換一篇文章"

    def is_going_to_info(self, event):
        text = event.message.text
        return text == "探索公司"

    def is_going_to_ic(self, event):
        text = event.message.text
        return text == "IC廠"    

    def is_going_to_system(self, event):
        text = event.message.text
        return text == "系統廠"

    def is_going_to_show_info(self, event):
        text = event.message.text
        global target_company_id
        global target_company_name

        if text == '聯發科':
            target_company_id = M
            target_company_name = text + '技'
            return True
        elif text == '聯詠':
            target_company_id = N
            target_company_name = text + '科技'
            return True
        elif text == '瑞昱':
            target_company_id = R
            target_company_name = text + '半導體'
            return True
        elif text == '創意':
            target_company_id = C
            target_company_name = text + '電子'
            return True
        elif text == '智原':
            target_company_id = S
            target_company_name = text + '科技'
            return True
        elif text == '鴻海':
            target_company_id = sea
            target_company_name = text + '科技集團'
            return True
        elif text == '台達':
            target_company_id = tai
            target_company_name = text + '電子'
            return True
        elif text == '緯穎':
            target_company_id = wayin
            target_company_name = text + '科技'
            return True
        elif text == '緯創':
            target_company_id = waytrunc
            target_company_name = text + '資通'
            return True
        elif text == '和碩':
            target_company_id = ho
            target_company_name = text + '聯合科技'
            return True

    def is_going_to_position(self, event):
        text = event.message.text
        return text == "科技業職稱簡介"

    def is_going_to_website(self, event):
        text = event.message.text
        return text.lower() == "精進自己"

    def is_going_to_coding(self, event):
        text = event.message.text
        return text.lower() == "coding"

    def is_going_to_reading(self, event):
        text = event.message.text
        return text.lower() == "閱讀"

    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        msg = message_UI.main_menu
        reply_msg = FlexSendMessage("主選單", msg)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_msg)

    def on_enter_article(self, event):
        print("I'm entering article")

        articles = get_article_list()
        randNum = random.randint(0, len(articles) - 1)

        limited_title = articles[randNum]["topic"][:20]

        reply_token = event.reply_token
        msg = message_UI.get_article_message(limited_title, articles[randNum]["url"])
        reply_msg = FlexSendMessage("推薦的文章", msg)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_msg)
        

    def on_enter_info(self, event):
        print("I'm entering stock price")

        reply_token = event.reply_token
        msg = message_UI.company_type_message
        reply_msg = FlexSendMessage("公司類型", msg)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_msg)

    def on_enter_ic(self, event):
        print("I'm entering ic")

        reply_token = event.reply_token
        msg = message_UI.company_choices_ic
        reply_msg = FlexSendMessage("ic", msg)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_msg)

    def on_enter_system(self, event):
        print("I'm entering system")

        reply_token = event.reply_token
        msg = message_UI.company_choices_system
        reply_msg = FlexSendMessage("system", msg)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_msg)
        
    def on_enter_show_info(self, event):
        print("I'm entering show price")
        reply_token = event.reply_token

        info = search_stock_price(str(target_company_id))
        intro = get_wiki(target_company_name)

        msg = message_UI.get_stock_price_message(info[0], info[1], target_company_name, info[3], intro)
        reply_msg = FlexSendMessage("科技公司", msg)

        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_msg)

    def on_enter_position(self, event):
        print("I'm entering position")

        reply_token = event.reply_token
        msg = message_UI.position_message
        reply_msg = FlexSendMessage("職稱簡介", msg)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_msg)
        

    def on_enter_website(self, event):
        print("I'm entering website")

        reply_token = event.reply_token
        msg = message_UI.website_type_message
        reply_msg = FlexSendMessage("website", msg)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_msg)
        
    def on_enter_coding(self, event):
        print("I'm entering coding")

        reply_token = event.reply_token
        msg = message_UI.coding_message
        reply_msg = FlexSendMessage("Coding", msg)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_msg)

    def on_enter_reading(self, event):
        print("I'm entering reading")

        reply_token = event.reply_token
        msg = message_UI.reading_message
        reply_msg = FlexSendMessage("Readings", msg)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_msg)

    
