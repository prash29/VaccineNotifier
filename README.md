### VaccineNotifier

VaccineNotifier will periodically check the CoWIN portal to find availability of vaccination slots in your PIN code and your age. If it finds available slots, it will send you an email. (Once an email has been sent, the script waits for an hour to send you the next update)

It is extremply easy to use this. Here are the steps to be followed:

* If you have 2-factor authentication enabled in your Gmail account, then visit the following link to generate an app password and enable access:
  [Link](https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637554658548216477-2576856839&rd=1)

* Enter details like PIN code, Age, Email ID, Password(that you generated in previous step) in `config.cfg`

* On your terminal run the following commands:
  `pip install -r requirements.txt` 
  `python run_cron.py` (You might have to authenticate/use admin access on your system)
  
Done!

Here is a sample screenshot of the email it sends you:

![Screenshot](https://github.com/prash29/VaccineNotifier/blob/main/screenshot.jpg | width=200)
