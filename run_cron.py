from crontab import CronTab
cron = CronTab(user='prashant')
job = cron.new(command='python /Users/prashant/VaccineNotifier/main.py >> /Users/prashant/VaccineNotifier/cron.log 2>&1')
job.minute.every(1)

cron.write()
