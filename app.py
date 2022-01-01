import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, MessageTemplateAction

from fsm import TocMachine
from utils import send_text_message, send_image_url, send_button_message

load_dotenv()

machine = TocMachine(
    states=["user", "menu", "article", "info", "ic", "system", "show_info", "position", "website", "coding", "reading"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "article",
            "conditions": "is_going_to_article",
        },
        {
            "trigger": "advance",
            "source": "article",
            "dest": "article",
            "conditions": "is_going_to_refind_article",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "info",
            "conditions": "is_going_to_info",
        },
        {
            "trigger": "advance",
            "source": "info",
            "dest": "ic",
            "conditions": "is_going_to_ic",
        },
        {
            "trigger": "advance",
            "source": "info",
            "dest": "system",
            "conditions": "is_going_to_system",
        },
        {
            "trigger": "advance",
            "source": "ic",
            "dest": "show_info",
            "conditions": "is_going_to_show_info",
        },
        {
            "trigger": "advance",
            "source": "system",
            "dest": "show_info",
            "conditions": "is_going_to_show_info",
        },
        {
            "trigger": "advance",
            "source": "show_info",
            "dest": "ic",
            "conditions": "is_going_to_ic",
        },
        {
            "trigger": "advance",
            "source": "show_info",
            "dest": "system",
            "conditions": "is_going_to_system",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "position",
            "conditions": "is_going_to_position",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "website",
            "conditions": "is_going_to_website",
        },
        {
            "trigger": "advance",
            "source": "website",
            "dest": "coding",
            "conditions": "is_going_to_coding",
        },
        {
            "trigger": "advance",
            "source": "website",
            "dest": "reading",
            "conditions": "is_going_to_reading",
        },
        {
            "trigger": "advance",
            "source": "article",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "info",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "ic",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "system",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "show_info",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "position",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "website",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "coding",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "reading",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        #{"trigger": "go_back", "source": ["article", "info", "position", "website"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            if event.message.text.lower() == 'fsm':
                send_image_url(event.reply_token, 'https://2a18-42-75-147-16.ngrok.io/show-fsm')
            else:
                title = '【提醒】'
                text = '請依照按鈕指示進行操作哦!'
                btn = [
                    MessageTemplateAction(
                        label = '返回主選單',
                        text = '主選單'
                    ),
                ]
                send_button_message(event.reply_token, title, text, btn)

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
