from apscheduler.schedulers.background import BackgroundScheduler
import service.stock_info_service as service

# def my_listener(event):
#     if event.exception:
#         print('The job crashed :(') # or logger.fatal('The job crashed :(')
#     else:
#         print('The job worked :)')


def save_yesterday_daily():

    scheduler = BackgroundScheduler()
    scheduler.add_job(service.save_yesterday_daily, 'cron', hour='6')
    # scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()

