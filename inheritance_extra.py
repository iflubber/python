'''

Imagine you are writing some code to control virtual machines running
on the cloud. Create several classes for the abstractions in your
program:

>>> web1 = WebServer('www1.example.com')
>>> web2 = WebServer('www2.example.com')
>>> web3 = WebServer('www3.example.com')

>>> db1 = DatabaseServer('db1.example.com')
>>> db2 = DatabaseServer('db2.example.com')

>>> lb = LoadBalancer('lb.example.com')

>>> ml1 = MachineLearningNode('ml1.example.com')
>>> ml2 = MachineLearningNode('ml2.example.com')
>>> ml3 = MachineLearningNode('ml3.example.com')
>>> ml4 = MachineLearningNode('ml4.example.com')

>>> web1.start()
>>> web2.start()
>>> db1.start()
>>> ml2.start()
>>> web2.stop()
>>> db2.stop()

>>> web1.is_running()
True
>>> web2.is_running()
False
>>> db1.is_running()
True
>>> db2.is_running()
False
>>> ml2.is_running()
True

Make each of them subclass a base called Server. Put as much code
into this base class as you can:

>>> isinstance(web1, Server)
True
>>> isinstance(db1, Server)
True
>>> isinstance(ml1, Server)
True

For example, the is_running(), start() and stop() methods:

>>> hasattr(Server, 'is_running')
True
>>> hasattr(Server, 'start')
True
>>> hasattr(Server, 'stop')
True

(hasattr() returns True if the class has that method defined, else it
returns False. It works on regular objects, too.)

Since we have a lot of machines to manage, let's create some
abtractions to manage groups of them.

>>> webapp_fleet = WebAppFleet([
...     web1, web2, web3,
...     db1, db2, lb])
>>> small_deep_fleet = DeepLearningFleet([ml1, ml2, lb])
>>> big_deep_fleet = DeepLearningFleet([
...     ml1, ml2, ml3, ml4, lb])

As before, these will share a common base: a class called Fleet. Fleet
objects have methods that tell you which machines are currently
running, and also let you start or stop all machines in the fleet.

>>> webapp_fleet.running()
['www1.example.com', 'db1.example.com']

>>> webapp_fleet.stop_all()
>>> webapp_fleet.running()
[]
>>> webapp_fleet.start_all()
>>> webapp_fleet.running()
['www1.example.com', 'www2.example.com', 'www3.example.com', 'db1.example.com', 'db2.example.com', 'lb.example.com']


>>> small_deep_fleet.running()
['ml2.example.com', 'lb.example.com']
>>> big_deep_fleet.running()
['ml2.example.com', 'lb.example.com']
>>> big_deep_fleet.start_all()
>>> big_deep_fleet.running()
['ml1.example.com', 'ml2.example.com', 'ml3.example.com', 'ml4.example.com', 'lb.example.com']

And of course, put as many of these in the Fleet class as you can, so
they can all be used by the subclasses.

>>> hasattr(Fleet, 'running')
True
>>> hasattr(Fleet, 'start_all')
True
>>> hasattr(Fleet, 'stop_all')
True

Often, your subclasses will have their own specialized methods, not
shared by the base class:

>>> webapp_fleet.webservers()
['www1.example.com', 'www2.example.com', 'www3.example.com']

>>> big_deep_fleet.calculating_nodes()
4
>>> small_deep_fleet.calculating_nodes()
2

'''

# Write your code here:
class Server:
    running = False
    def __init__(self,name):
        self.name = name
    def start(self):
        self.running = True
    def stop(self):
        self.running = False
    def is_running(self):
        return self.running

class WebServer(Server):
    def __init__(self,name):
        self.name = name

class DatabaseServer(Server):
    def __init__(self,name):
        self.name = name

class LoadBalancer(Server):
    def __init__(self,name):
        self.name = name

class MachineLearningNode(Server):
    def __init__(self,name):
        self.name = name

class Fleet:
    def __init__(self,fleets):
        self.fleets = fleets
    def running(self):
        running_fleet = []
        for fleet in self.fleets:
            if(fleet.is_running()):
                running_fleet.append(fleet.name)
        return running_fleet
    def start_all(self):
        for fleet in self.fleets:
            fleet.start()
    def stop_all(self):
        for fleet in self.fleets:
            fleet.stop()

class WebAppFleet(Fleet):
    def __init__(self,fleets):
        self.fleets = fleets
    def webservers(self):
        ws = []
        for fleet in self.fleets:
            if(fleet.__class__.__name__ == 'WebServer'):
                ws.append(fleet.name)
        return ws

class DeepLearningFleet(Fleet):
    def __init__(self,fleets):
        self.fleets = fleets
    def calculating_nodes(self):
        nodes = 0
        for fleet in self.fleets:
            if(fleet.__class__.__name__ == 'MachineLearningNode'):
                nodes +=1
        return nodes



# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

