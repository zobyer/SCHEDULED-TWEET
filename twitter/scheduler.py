from twitter.views import sendScheduledTweets
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        sendScheduledTweets, 'interval', minutes=3)
    scheduler.start()