from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def infinityC():
    while True:
        print("0_o")
    return 'completed'



@shared_task
def boyC():
    while True:
        print("someone is watching you infinitely")
    return 'boy said'

@shared_task
def girlC():
    while True:
        print("don't watch me infinitely")
    return 'girl said'