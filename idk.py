
import threading

# Called by each thread
def thread_fun(words):
    while True:
        print(words)

var = "good school"
t = threading.Thread(target=thread_fun, args = (var,))
t.start()
