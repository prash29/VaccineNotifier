import requests
from utils import *
import time

def run(args):
    # If a notification has been sent in the last half hour, wait till the time elapses
    time_since_mail = time_since_last_mail(args)
    if time_since_mail < 30:
        time.sleep(int(60-time_since_mail)*60)

    valid_pincodes, mail_text = [], ""
    for pin in args['pincode']:
        url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pin, args['date'])
        resp_json = requests.get(url, headers=args['headers_dict']).json()
        valid_responses = get_valid_sessions(args, resp_json)
        if len(valid_responses)>0 and args['send_mail']:
            valid_pincodes.append(pin)
            mail_text = get_mail_text(valid_responses, mail_text, pin)
    if len(valid_pincodes)>0 and args['send_mail']:
        send_mail(args, valid_pincodes, mail_text)
        with open('last_update.txt','w') as f:
            f.write(mail_text)

if __name__=='__main__':
    args = init_config()
    run(args)