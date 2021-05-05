import requests
from crontab import CronTab
import configparser as cp
import smtplib
from datetime import date
from pdb import set_trace as bp
import os
from utils import *
import time

def run(args):
    # If a notification has been sent in the last hour, wait till an hour elapses
    time_since_mail = time_since_last_mail(args)
    if time_since_mail < 60:
        time.sleep(int(60-time_since_mail)*60)

    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(args['pincode'], cur_date)
    resp_json = requests.get(url).json()
    valid_responses = get_valid_sessions(args, resp_json)
    if len(valid_responses)>0 and args['send_mail']:
        send_mail(args, valid_responses)
        with open('last_update.txt','w') as f:
            message_text =  get_mail_text(valid_responses)
            f.write(message_text)


if __name__=='__main__':
    base_path = os.path.dirname(os.path.abspath(__file__))
    config = cp.ConfigParser()
    conf_path = os.path.join(base_path, 'config.cfg')
    config.read(conf_path)
    args = config['Default']
    args['base_path'] = base_path
    cur_date = date.today().strftime("%d-%m-%y")
    print("Hello!")
    run(args)
