from queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            print(simqueue)


        simqueue.dequeue()
        print(simqueue)
    return simqueue.dequeue()


names = []
for i in range(6):
    name = input('Enter names: ')
    names.append(name)

number = int(input('Enter number: '))
lastPerson = hotPotato(names, number)

print(lastPerson)