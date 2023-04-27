import threading

def count():
    print("Début du thread")
    for i in range(10):
        print(i)
    print("Fin du thread")

thread = threading.Thread(target=count)
thread.start()

print("Le thread est lancé")

# attendre la fin du thread
thread.join()

print("Le thread est terminé")
