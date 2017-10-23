import asyncio
from subprocess import Popen, PIPE

def fping_(ip, parameters):
    print('start ping ip %s' % ip)
    """Если пул свободен, начинаем выполнение и отдаем управление в главный луп"""
    # logging.info(u'start ping ip %s' % ip)
    line = ('fping' + ' ' + ip + ' ' + parameters)
    cmd = Popen(line.split(' '), stdout=PIPE)
    data_(cmd)

@asyncio.coroutine
def data_(cmd):
    while True:
        if cmd.returncode:
            output = cmd.communicate()[0]
            output = str(output)
            print("NUMBER: ", output)
        yield from asyncio.sleep(4)

print('hello')
try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fping_('8.8.8.8', ' -Q 2 -p 50 -l'))
except:
    print('some')
finally:
    print('End')