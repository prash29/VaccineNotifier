from crontab import CronTab
base_path = os.path.dirname(os.path.abspath(__file__))

cron = CronTab(user='prashant')
job = cron.new(command='python {}/main.py >>  {}/cron.log 2>&1'.format(base_path, base_path))
job.minute.every(1)

cron.write()
