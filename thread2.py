import threading
import time



def uncount(txt):
    global compt
    for i in range(0, 15):
        compt = compt + 1
        print(txt,compt)
        time.sleep(1)


compt = 0
un = threading.Thread(target=uncount, args=("1",))
deux = threading.Thread(target=uncount, args=("2",))


un.start()
deux.start()
un.join()
deux.join()
print ("le thread est terminé")
