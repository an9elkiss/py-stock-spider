from apscheduler.schedulers.background import BackgroundScheduler
import service.stock_info_service as service

# def my_listener(event):
#     if event.exception:
#         print('The job crashed :(') # or logger.fatal('The job crashed :(')
#     else:
#         print('The job worked :)')


scheduler = BackgroundScheduler()
scheduler.start()


def save_yesterday_daily():

    scheduler.add_job(service.save_yesterday_daily, 'cron', hour='6')
    # scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)


def save_history_daily():

    scheduler.add_job(service.save_history_daily, 'cron', minute='*/3')

