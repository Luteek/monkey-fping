import asyncio
from subprocess import Popen, PIPE

@asyncio.coroutine
def fping_(ip, parameters):
    print('start ping ip %s' % ip)
    line = ('ping' + ' ' + ip + ' ' + parameters)
    cmd = Popen(line.split(' '), stdout=PIPE)
    data_(cmd)
    yield from asyncio.sleep(5)

@asyncio.coroutine
def data_(cmd):
    while cmd.stdout:
        for line in cmd.stdout:
            print("NUMBER: ", line)
    yield from asyncio.sleep(4)

print('hello')

loop = asyncio.get_event_loop()
loop.run_until_complete(fping_('8.8.8.8', ' -Q 2 -p 50 -l'))
