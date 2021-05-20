## VaccineNotifier

VaccineNotifier will periodically check the CoWIN portal to find availability of vaccination slots. In the config file (explained below), you can enter one or more PIN codes, your age, your choice of vaccine and which dose. If it finds available slots, it will send you an email. (Once an email has been sent, the script waits for half an hour to send you the next update)

It is extremely easy to use this. Here are the steps to be followed:

* If you have 2-factor authentication enabled in your Gmail account, then visit the following link to generate an app password and enable access:
  [Link](https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637554658548216477-2576856839&rd=1)


* Enter details like PIN code(comma separated for multiple pincodes), Age, Email ID, Password(that you generated in previous step), which vaccine and dose in `config.cfg`

Example of `config.cfg`
```
    pincode=560066,560020,560022 # Add one or more PIN codes separated by comma
    age=23
    send_mail=True
    password= # Enter your password here
    email_id=xyz@gmail.com
    date='' # If you want information for a particular date, enter the date in DD-MM-YYYY format, else leave it blank and it will use the current/today's date by default.
    vaccine = Covishield # Enter the vaccine you want (Covishield/Covaxin). This field is not case sensitive. 
    dose=2 # Enter 1 for first and 2 for second dose
```
* On your terminal run the following commands (I am using Python 3.7 to run these scripts):

  `pip install -r requirements.txt` (Installs the required packages)

  `python run_cron.py` (You might have to authenticate/use admin access on your system)
  
Done!

Here is a sample screenshot of the email it sends you:

![Screenshot](https://github.com/prash29/VaccineNotifier/blob/main/screenshot.jpg)
