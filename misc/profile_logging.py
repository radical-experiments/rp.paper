#!/usr/bin/env python

import time
import timeit
import pprint
import radical.utils as ru

logger = ru.get_logger('radical.pilot', target='t.log', level='DEBUG')

logger.info('info')
logger.debug('debug')

FREE = 'Free'
BUSY = 'Busy'

url_0 = ru.Url('ssh+pbs://user:pass@titan.ornl.gov:1234/path/to/file?query#stuff')


def get_slots(nodes, cpn):

    slots = list()
    for _ in range(nodes):
        slots.append({'cores' : [FREE] * cpn})
    return slots

slots = get_slots(16, 16)
def slot_status():
    """Returns a multi-line string corresponding to slot status.
    """

    slot_matrix = ""
    for slot in slots:
        slot_matrix += "|"
        for core in slot['cores']:
            if core == FREE:
                slot_matrix += "-"
            else:
                slot_matrix += "+"
    slot_matrix += "|"
    return {'timestamp' : time.time(),
            'slotstate' : slot_matrix}


# a submmethod call to create a cheap log message
def msg_0():
    return 'logme! %f' % time.time()

# a submmethod call to create a costly log message
def msg_1():
    return 'logme! %f: %s' % (time.time(),
                              pprint.pformat(dir(logger)))
# simplestring log
def test_0():
    logger.info('info')

# string log, delayed expansion
def test_1():
    logger.info('info %s', 'test')

# string log, always expanded
def test_2():
    logger.info('info %s' % 'test')

# string log, immediate expansion of a RU.Url
def test_3():
    logger.info('info %s' % str(url_0))

# string log, delayed expansion of generated cheap message
def test_4():
    logger.info('info %s', msg_0())

# string log, immediate expansion of generated cheap message
def test_5():
    logger.info('info %s' % msg_0())

# string log, delayed expansion of generated costly message
def test_6():
    logger.info('info %s', msg_1())

# string log, immediate expansion of generated costly message
def test_7():
    logger.info('info %s' % msg_1())

# string log, immediate expansion of generated costly message
def test_8():
    logger.info('info %s', slot_status())


print 'test_0: %5.2f s/10.000 calls' % timeit.Timer(test_0).repeat(1, 10000)[0]
print 'test_1: %5.2f s/10.000 calls' % timeit.Timer(test_1).repeat(1, 10000)[0]
print 'test_2: %5.2f s/10.000 calls' % timeit.Timer(test_2).repeat(1, 10000)[0]
print 'test_3: %5.2f s/10.000 calls' % timeit.Timer(test_3).repeat(1, 10000)[0]
print 'test_4: %5.2f s/10.000 calls' % timeit.Timer(test_4).repeat(1, 10000)[0]
print 'test_5: %5.2f s/10.000 calls' % timeit.Timer(test_5).repeat(1, 10000)[0]
print 'test_6: %5.2f s/10.000 calls' % timeit.Timer(test_6).repeat(1, 10000)[0]

print
def test_slot_status(nodes):
    global slots
    slots = get_slots(nodes, 16)
    print 'test_7 nodes: %5d  cores: %10d: %5.2f s/10 calls' \
        % (nodes, nodes*16, timeit.Timer(test_7).repeat(1, 10)[0])

for exp in range(16):
    test_slot_status(2**exp)

