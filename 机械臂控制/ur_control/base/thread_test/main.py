import threading
from mainloop import mainloop
from real_loop import real_loop

if __name__ == '__main__':
    t = threading.Thread(target=real_loop)
    t.start()
    # t.join()
    mainloop()
