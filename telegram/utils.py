import requests
import random

token = '5893999368:AAFc-3k4HNY5GlykjX0U1d2Uok70yetngRs'
me = '5826204187'


def send_msg(msg, sender_id):
    token = '5893999368:AAFc-3k4HNY5GlykjX0U1d2Uok70yetngRs'
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={sender_id}&text={msg}'
    requests.get(url)

# send_msg('이거 맞아?', me)
'''
https://api.telegram.org/bot5893999368:AAFc-3k4HNY5GlykjX0U1d2Uok70yetngRs/setWebhook?url=pabi.pythonanywhere.com
'''
