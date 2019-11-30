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

@shared_task
def p4():
    while True:
        print("i am 4")
    return 'i am 4'

@shared_task
def p3():
    while True:
        print("i am 3")
    return 'i am 3'
@shared_task
def p1(txt):
    while True:
        print(txt)
    return 'p1'

@shared_task
def p2():
    while True:
        print("i am 2")
    return 'p2'