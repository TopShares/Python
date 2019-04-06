def hello():
    print('Hello from the reactor loop!')
    print('Lately I feel like I\'m stuck in a rut.')
from twisted.internet import reactor
reactor.callWhenRunning(hello)
print('Starting the reactor.')
reactor.run()


class Countdown(object):
    counter = 5
    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print(self.counter, '...')
            self.counter -= 1
            reactor.callLater(1, self.count)

from twisted.internet import reactor

reactor.callWhenRunning(Countdown().count)

print('Start!')
reactor.run()
print('Stop!')