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
              "label": "找話題",
              "text": "找話題"
            },
            "height": "md",
            "color": "#45b39d",
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
              "label": "探索公司",
              "text": "探索公司"
            },
            "height": "md",
            "color": "#ec7063",
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
            "color": "#f5b041",
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
              "label": "精進自己",
              "text": "精進自己"
            },
            "height": "md",
            "color": "#5dade2",
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
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "資料時間",
          "weight": "bold",
          "size": "lg",
          "align": "center"
        },
        {
          "type": "text",
          "text": (date + ' ' + time + '\n'),
          "wrap": True,
          "align": "center"
        },
        {
          "type": "text",
          "text": "公司名稱",
          "weight": "bold",
          "size": "lg",
          "align": "center"
        },
        {
          "type": "text",
          "text": name + '\n',
          "wrap": True,
          "align": "center"
        },
        {
          "type": "text",
          "text": "股價",
          "weight": "bold",
          "size": "lg",
          "align": "center"
        },
        {
          "type": "text",
          "text": (price + ' TWD\n'),
          "wrap": True,
          "align": "center"
        },
        {
          "type": "text",
          "text": "公司簡介",
          "weight": "bold",
          "size": "lg",
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
            "type": "box",
            "layout": "horizontal",
            "spacing": "md",
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "其他IC廠",
                "text": "IC廠"
                }
            },
            {
                "type": "separator"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "其他系統廠",
                "text": "系統廠"
                }
            },
            ]
        },
        {
          "type": "separator"
        },        
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "返回主選單",
            "text": "主選單"
          }
        },
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
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "EE",
        "weight": "bold",
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

company_choices_ic = {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "請選擇公司",
            "weight": "bold",
            "size": "lg",
            "align": "center",
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "contents": [
        {
            "type": "separator"
        },          
        {
            "type": "box",
            "layout": "horizontal",
            "spacing": "md",
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "聯發科",
                "text": "聯發科"
                }
            },
            {
                "type": "separator"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "聯詠",
                "text": "聯詠"
                }
            },
            ]
        },
        {
            "type": "separator"
        },
        {
            "type": "box",
            "layout": "horizontal",
            "spacing": "md",
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "瑞昱",
                "text": "瑞昱"
                }
            },
            {
                "type": "separator"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "創意",
                "text": "創意"
                }
            },
            {
                "type": "separator"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "智原",
                "text": "智原"
                }
            },
            ]
        }
        ]
        
    },

}

company_choices_system = {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "請選擇公司",
            "weight": "bold",
            "size": "lg",
            "align": "center",
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "contents": [
        {
            "type": "separator"
        },          
        {
            "type": "box",
            "layout": "horizontal",
            "spacing": "md",
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "鴻海",
                "text": "鴻海"
                }
            },
            {
                "type": "separator"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "緯穎",
                "text": "緯穎"
                }
            },
            ]
        },
        {
            "type": "separator"
        },
        {
            "type": "box",
            "layout": "horizontal",
            "spacing": "md",
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "台達",
                "text": "台達"
                }
            },
            {
                "type": "separator"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "緯創",
                "text": "緯創"
                }
            },
            {
                "type": "separator"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "和碩",
                "text": "和碩"
                }
            },
            ]
        }
        ]
        
    },

}

company_type_message = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "公司類型",
        "weight": "bold",
        "size": "lg",
        "align": "center"
      },
      {
        "type": "text",
        "text": '想要關注哪種類型的科技公司呢?',
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
          "type": "box",
          "layout": "horizontal",
          "spacing": "md",
          "contents": [
          {
              "type": "button",
              "action": {
              "type": "message",
              "label": "IC廠",
              "text": "IC廠"
              }
          },
          {
              "type": "separator"
          },
          {
              "type": "button",
              "action": {
              "type": "message",
              "label": "系統廠",
              "text": "系統廠"
              }
          },
          ]
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      },
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

website_type_message = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "精進自己",
        "weight": "bold",
        "size": "lg",
        "align": "center"
      },
      {
        "type": "text",
        "text": '實作和知識理論都很重要，想要加強什麼面向呢?',
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
          "type": "box",
          "layout": "horizontal",
          "spacing": "md",
          "contents": [
          {
              "type": "button",
              "action": {
              "type": "message",
              "label": "閱讀",
              "text": "閱讀"
              }
          },
          {
              "type": "separator"
          },
          {
              "type": "button",
              "action": {
              "type": "message",
              "label": "Coding",
              "text": "Coding"
              }
          },
          ]
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      },
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

def get_article_message(title, uri):
  article_message = {
    "type": "bubble",
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "推薦的文章",
          "weight": "bold",
          "size": "lg",
          "align": "center"
        },
        {
          "type": "text",
          "text": '看看科技業的前輩們都聊些什麼吧!',
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
            "type": "uri",
            "label": title,
            "uri": uri
          }
        },
        {
          "type": "separator"
        },
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "換一篇文章",
            "text": "換一篇文章"
          }
        },
        {
          "type": "separator"
        },
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "返回主選單",
            "text": "主選單"
          }
        },
      ]
    },
    "styles": {
      "footer": {
        "separator": True
      }
    }
  }

  return article_message

coding_message = {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
          "type": "text",
          "text": "Coding",
          "weight": "bold",
          "size": "lg",
          "align": "center"
        },
        {
          "type": "text",
          "text": '可以利用這些網站精進自己的coding實力，讓自己更進步!',
          "wrap": True,
          "align": "center"
        },
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "contents": [
        {
          "type": "separator"
        },          
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": 'CodeChef',
            "uri": 'https://www.codechef.com/'
          }
        },          
        {
          "type": "separator"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": 'Topcoder',
            "uri": 'https://www.topcoder.com/thrive/tracks?track=Competitive%20Programming'
          }
        },
        {
          "type": "separator"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": 'LeetCode',
            "uri": 'https://leetcode.com/problemset/all/'
          }
        },
        {
          "type": "separator"
        },
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "返回主選單",
            "text": "主選單"
          }
        },
        ]
        
    },

}

reading_message = {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
          "type": "text",
          "text": "Readings",
          "weight": "bold",
          "size": "lg",
          "align": "center"
        },
        {
          "type": "text",
          "text": '可以利用這些網站補充各種科技的相關知識和新聞，讓自己視野更廣闊!',
          "wrap": True,
          "align": "center"
        },
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "contents": [
        {
          "type": "separator"
        },          
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": 'Techmeme',
            "uri": 'https://www.techmeme.com/'
          }
        },          
        {
          "type": "separator"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": 'DIGITIMES',
            "uri": 'https://www.digitimes.com.tw/'
          }
        },
        {
          "type": "separator"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": 'TechCrunch',
            "uri": 'https://techcrunch.com/'
          }
        },
        {
          "type": "separator"
        },
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "返回主選單",
            "text": "主選單"
          }
        },
        ]
        
    },

}