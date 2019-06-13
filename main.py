from apscheduler.schedulers.blocking import BlockingScheduler
from create_file import create_file

sched = BlockingScheduler()
sched.add_job(create_file,'interval',days = 1)
sched.start()
