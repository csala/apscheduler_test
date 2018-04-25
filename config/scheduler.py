import importlib

import configparser
from apscheduler.schedulers.gevent import GeventScheduler


def get_task(task_name):
    package, name = task_name.rsplit('.', 1)
    return getattr(importlib.import_module(package), name)


def add_jobs(scheduler, config):
    for task_name, args in config.items():
        task = get_task(task_name)
        args = args.split(':')
        trigger = args.pop(0)
        kwargs = {key: eval(value) for key, value in zip(args[0::2], args[1::2])}

        scheduler.add_job(task, trigger, **kwargs)


def start():
    scheduler = GeventScheduler()

    config = configparser.ConfigParser()
    config.read('scheduler.conf')

    add_jobs(scheduler, config['jobs'])

    try:
        scheduler.start().join()
    except (KeyboardInterrupt, SystemExit):
        pass
