import smtplib
from datetime import datetime
import os

def send_mail(args,responses):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(args['email_id'],args['password'])
    message_subject = "Vaccine Availability for PIN: {}".format(args['pincode'])
    message_text =  get_mail_text(responses)
    message = "From: %s\r\n" % args['email_id']+ "To: %s\r\n" % args['email_id']+ "Subject: %s\r\n" % message_subject+"\r\n"+ str(message_text)
    server.set_debuglevel(1)
    server.sendmail(args['email_id'], args['email_id'], message)
    server.quit()

def get_mail_text(responses):
    message_text = "Vaccine Availability Information \n\n"
    for i, resp in enumerate(responses):
        message_text+= "{}.\nName: {} \nDistrict: {} \nVaccine Name:{}\nPIN: {}\nAvailable Capacity: {} \nSlots: {}\nCost:{}\n\n\n".format(i+1,resp['name'], resp['district_name'], resp['vaccine'], resp['pincode'], resp['available_capacity'], resp['slots'], resp['fee'])
    return message_text

def get_valid_sessions(args, resp_json):
    sessions = resp_json['sessions']
    valid_sessions = []
    for sess in sessions:
        if (int(args['age'])>=sess['min_age_limit']) and (sess['available_capacity']>0):
            valid_sessions.append(sess)
    return valid_sessions

def time_since_last_mail(args):
    last_update_path = os.path.join(args['base_path'],'last_update.txt')
    if not os.path.exists(last_update_path):
        return 1000
    b = os.stat(os.path.join(args['base_path'], 'last_update.txt')).st_mtime
    time_diff = datetime.now() - datetime.fromtimestamp(b)
    mins = (time_diff.total_seconds())/60
    return mins
