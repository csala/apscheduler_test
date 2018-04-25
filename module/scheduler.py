from apscheduler.schedulers.gevent import GeventScheduler

import tasks


def add_jobs(scheduler):
    """Add all the scheduler jobs here."""
    scheduler.add_job(tasks.do_stuff, 'interval', seconds=3)
    scheduler.add_job(tasks.do_more_stuff, 'interval', seconds=5)
    # etc.


def start():
    scheduler = GeventScheduler()

    add_jobs(scheduler)

    try:
        scheduler.start().join()
    except (KeyboardInterrupt, SystemExit):
        pass
