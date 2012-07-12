import thread, time

def counter(id):
    for i in range(5):
        print 'id %r -- > %r \n' % (id, i)
        time.sleep(0.1)
        

for i in range(5):
    thread.start_new_thread(counter, (i,))

time.sleep(2)
print 'exit'