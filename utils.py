import smtplib
from datetime import datetime, date
import os
import configparser as cp

def send_mail(args, valid_pincodes, message_text):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(args['email_id'],args['password'])
    message_subject = "Vaccine Availability for PIN: {}".format(valid_pincodes)
    message = "From: %s\r\n" % args['email_id']+ "To: %s\r\n" % args['email_id']+ "Subject: %s\r\n" % message_subject+"\r\n"+ str(message_text)
    server.set_debuglevel(1)
    server.sendmail(args['email_id'], args['email_id'], message)
    server.quit()

def get_mail_text(responses, message_text,pin):
    message_text += "\nVaccine Availability Information for PIN: {}\n\n".format(pin)
    for i, resp in enumerate(responses):
        message_text+= "{}.\nName: {} \nDistrict: {} \nVaccine Name: {} \nPIN: {}\nAvailable Capacity (Dose 1): {}\nAvailable Capacity (Dose 2): {} \nSlots: {}\nCost:{}\n\n\n".format(i+1,resp['name'], resp['district_name'], resp['vaccine'], resp['pincode'], resp['available_capacity_dose1'],resp['available_capacity_dose2'], resp['slots'], resp['fee'])
    return message_text

def get_valid_sessions(args, resp_json):
    sessions = resp_json['sessions']
    valid_sessions = []
    for sess in sessions:
        if (args['vaccine'].upper() == sess['vaccine']):
            if (int(args['age'])>=sess['min_age_limit']) and (sess['available_capacity']>0):
                valid_sessions.append(sess)
    return valid_sessions

def init_config():
    base_path = os.path.dirname(os.path.abspath(__file__))
    config = cp.ConfigParser()
    conf_path = os.path.join(base_path, 'config.cfg')
    config.read(conf_path)
    args = dict(config['Default'])
    args['base_path'] = base_path
    if args['date'] !='':
        args['date'] = date.today().strftime("%d-%m-%y")
    x = args['pincode'].split(',')
    args['pincode'] = x
    args['headers_dict'] = {'Origin': 'https://apisetu.gov.in','Referer': 'https://fonts.googleapis.com/','sec-ch-ua-mobile':'?0','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
    return args

def time_since_last_mail(args):
    last_update_path = os.path.join(args['base_path'],'last_update.txt')
    if not os.path.exists(last_update_path):
        return 1000
    b = os.stat(os.path.join(args['base_path'], 'last_update.txt')).st_mtime
    time_diff = datetime.now() - datetime.fromtimestamp(b)
    mins = (time_diff.total_seconds())/60
    return mins
