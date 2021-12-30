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
from reptile import search_stock_price, get_article_list, get_wiki
import random

ic = 0
system = 1
stock_type = ic

M = 2454
N = 3034
R = 2379
sea = 2317
way = 6669
tai = 2308
target_company_id = M
target_company_name = ''

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text == "主選單"

    def is_going_to_article(self, event):
        text = event.message.text
        return text == "看看科技業話題"

    def is_going_to_stock_price(self, event):
        text = event.message.text
        return text == "關心科技公司"

    def is_going_to_ic(self, event):
        text = event.message.text
        return text == "IC廠"    

    def is_going_to_system(self, event):
        text = event.message.text
        return text == "系統廠"

    def is_going_to_show_price(self, event):
        text = event.message.text
        global target_company_id
        global target_company_name

        if text == '聯發科':
            target_company_id = M
            target_company_name = text + '科技'
            return True
        elif text == '聯詠':
            target_company_id = N
            target_company_name = text + '科技'
            return True
        elif text == '瑞昱':
            target_company_id = R
            target_company_name = text + '半導體'
            return True
        elif text == '鴻海':
            target_company_id = sea
            target_company_name = text + '科技集團'
            return True
        elif text == '台達電':
            target_company_id = tai
            target_company_name = text + '電子'
            return True
        elif text == '緯穎':
            target_company_id = way
            target_company_name = text + '科技'
            return True

    def is_going_to_position(self, event):
        text = event.message.text
        return text == "科技業職稱簡介"

    def is_going_to_website(self, event):
        text = event.message.text
        return text.lower() == "增進實力"

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

        reply_token = event.reply_token
        title = '推薦的文章'
        text = '看看科技業的前輩們都聊些什麼吧'
        btn = [
            URITemplateAction(
                label = articles[randNum]["topic"],
                uri = articles[randNum]["url"]
            ),
             MessageTemplateAction(
                label = '返回主選單',
                text = '主選單'
            ),
        ]
        send_button_message(event.reply_token, title, text, btn)
        

    def on_enter_stock_price(self, event):
        print("I'm entering stock price")

        reply_token = event.reply_token
        title = '公司類型'
        text = '想要關注哪種類型的科技公司呢?'
        btn = [
            MessageTemplateAction(
                label = 'IC廠',
                text = 'IC廠'
            ),
            MessageTemplateAction(
                label = '系統廠',
                text = '系統廠'
            ),
             MessageTemplateAction(
                label = '返回主選單',
                text = '主選單'
            ),
        ]
        send_button_message(event.reply_token, title, text, btn)

    def on_enter_ic(self, event):
        print("I'm entering stock price")

        reply_token = event.reply_token
        title = '公司名稱'
        text = '想要關注哪個科技公司呢?'
        btn = [
            MessageTemplateAction(
                label = '聯發科',
                text = '聯發科'
            ),
            MessageTemplateAction(
                label = '聯詠',
                text = '聯詠'
            ),
            MessageTemplateAction(
                label = '瑞昱',
                text = '瑞昱'
            ),
             MessageTemplateAction(
                label = '返回主選單',
                text = '主選單'
            ),
        ]
        send_button_message(event.reply_token, title, text, btn)

    def on_enter_system(self, event):
        print("I'm entering stock price")

        reply_token = event.reply_token
        title = '公司名稱'
        text = '想要關注哪個科技公司呢?'
        btn = [
            MessageTemplateAction(
                label = '鴻海',
                text = '鴻海'
            ),
            MessageTemplateAction(
                label = '台達電',
                text = '台達電'
            ),
            MessageTemplateAction(
                label = '緯穎',
                text = '緯穎'
            ),
             MessageTemplateAction(
                label = '返回主選單',
                text = '主選單'
            ),
        ]
        send_button_message(event.reply_token, title, text, btn)
        
    def on_enter_show_price(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token

        info = search_stock_price(str(target_company_id))
        intro = get_wiki(target_company_name)

        msg = message_UI.get_stock_price_message(info[0], info[1], info[2], info[3], intro)
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
        send_text_message(reply_token, "Trigger website")
        

    
