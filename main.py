import asyncio
import aiohttp
from crontab import CronTab
import configparser as cp
import smtplib
from datetime import date
import os
from utils import *
import time

base_path = os.path.dirname(os.path.abspath(__file__))
conf_path = os.path.join(base_path, 'config.cfg')
config = cp.ConfigParser()
config.read(conf_path)
args = config['Default']
args['base_path'] = base_path
cur_date = date.today().strftime("%d-%m-%y")
print("Hello!")

# If a notification has been sent in the last hour, wait till an hour elapses
time_since_mail = time_since_last_mail(args)
if time_since_mail < 60:
    time.sleep(int(60-time_since_mail)*60)

async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(args['pincode'], cur_date)
        async with session.get(url) as resp:
            resp_json = await resp.json()
            valid_responses = get_valid_sessions(args, resp_json)
            if len(valid_responses)>0 and args['send_mail']:
                send_mail(args, valid_responses)
                print("Sent email!")
                with open('last_update.txt','w') as f:
                    message_text =  get_mail_text(valid_responses)
                    f.write(message_text)
                    

asyncio.run(main())
