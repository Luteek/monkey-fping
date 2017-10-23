import asyncio
from subprocess import Popen, PIPE

@asyncio.coroutine
def fping_(ip, parameters):
    print('start ping ip %s' % ip)
    """Если пул свободен, начинаем выполнение и отдаем управление в главный луп"""
    # logging.info(u'start ping ip %s' % ip)
    line = ('fping' + ' ' + ip + ' ' + parameters)
    cmd = Popen(line.split(' '), stdout=PIPE)
    iterr = 0

    while True:
        iterr = 1
        output = cmd.communicate()[0]
        output = str(output)
        print("NUMBER: ", iterr, "  ", output)
        yield from asyncio.sleep(4)

print('hello')
try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fping_('8.8.8.8', ' -Q 10 -p 50 -l'))
except:
    print('some')
finally:
    print('End')