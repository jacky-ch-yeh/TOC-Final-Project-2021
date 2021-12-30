main_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/Ah47Rpf.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "看看科技業話題",
              "text": "看看科技業話題"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/HUFH8E4.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "關心科技公司",
              "text": "關心科技公司"
            },
            "height": "md",
            "color": "#ff6666",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/JD7rk0V.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "科技業職稱簡介",
              "text": "科技業職稱簡介"
            },
            "height": "md",
            "color": "#ff66b3",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/Jpu3bb4.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "增進實力",
              "text": "增進實力"
            },
            "height": "md",
            "color": "#b366ff",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}


def get_stock_price_message(date, time, name, price, intro):
  stock_price_message = {
    "type": "bubble",
    "size": "giga",
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "當前時間",
          "weight": "bold",
          "size": "lg",
          "margin": "lg",
          "align": "center"
        },
        {
          "type": "text",
          "text": (date + ' ' + time),
          "wrap": True,
          "align": "center"
        },
        {
          "type": "text",
          "text": "公司名稱",
          "weight": "bold",
          "size": "lg",
          "margin": "lg",
          "align": "center"
        },
        {
          "type": "text",
          "text": name,
          "wrap": True,
          "align": "center"
        },
        {
          "type": "text",
          "text": "當前股價",
          "weight": "bold",
          "size": "lg",
          "margin": "lg",
          "align": "center"
        },
        {
          "type": "text",
          "text": (price + ' TWD'),
          "wrap": True,
          "align": "center"
        },
        {
          "type": "text",
          "text": "公司簡介",
          "weight": "bold",
          "size": "lg",
          "margin": "lg",
          "align": "center"
        },
        {
          "type": "text",
          "text": intro,
          "wrap": True,
          "align": "center"
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "返回主選單",
            "text": "主選單"
          }
        }
      ]
    },
    "styles": {
      "footer": {
        "separator": True
      }
    }
  }

  return stock_price_message

position_message = {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "EE",
        "weight": "bold",
        "margin": "lg"
      },
      {
        "type": "text",
        "text": 'Equipment Engineer 設備工程師',
        "wrap": True,
      },
      {
        "type": "text",
        "text": "QA",
        "weight": "bold",
        "margin": "lg",
      },
      {
        "type": "text",
        "text": 'quality assurance engineer 品保工程師',
        "wrap": True,
      },
      {
        "type": "text",
        "text": "QE",
        "weight": "bold",
        "margin": "lg",
      },
      {
        "type": "text",
        "text": 'quality (control) engineer 品管工程師',
        "wrap": True,
      },
      {
        "type": "text",
        "text": "QS",
        "weight": "bold",
        "margin": "lg",
      },
      {
        "type": "text",
        "text": 'quality system engineer 品質系統工程師',
        "wrap": True,
      },
      {
        "type": "text",
        "text": "PM",
        "weight": "bold",
        "margin": "lg",
      },
      {
        "type": "text",
        "text": 'Project Manager 專案經理',
        "wrap": True,
      },
      {
        "type": "text",
        "text": "PE",
        "weight": "bold",
        "margin": "lg",
      },
      {
        "type": "text",
        "text": 'Product Engineer 產品工程師',
        "wrap": True,
      },
      {
        "type": "text",
        "text": "PIE",
        "weight": "bold",
        "margin": "lg",
      },
      {
        "type": "text",
        "text": 'Process Integration Engineer 製程整合工程',
        "wrap": True,
      },
      {
        "type": "text",
        "text": "SA",
        "weight": "bold",
        "margin": "lg",
      },
      {
        "type": "text",
        "text": 'System Analyst 系統分析師',
        "wrap": True,
      },
      {
        "type": "text",
        "text": "SD",
        "weight": "bold",
        "margin": "lg",
      },
      {
        "type": "text",
        "text": 'System Analyst 系統設計師',
        "wrap": True,
      },
      {
        "type": "text",
        "text": "RD",
        "weight": "bold",
        "margin": "lg",
      },
      {
        "type": "text",
        "text": 'Research and Development engineer 研發設計工程師',
        "wrap": True,
      },
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}