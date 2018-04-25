from apscheduler.schedulers.gevent import GeventScheduler


scheduler = GeventScheduler()


@scheduler.scheduled_job('interval', seconds=3)
def do_stuff():
    print('Doing stuff...')


@scheduler.scheduled_job('interval', seconds=5)
def do_more_stuff():
    print('Doing more stuff...')


if __name__ == '__main__':
    try:
        scheduler.start().join()
    except (KeyboardInterrupt, SystemExit):
        pass
