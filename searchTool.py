import time

def searched():
    book = '1500 lines written in this paragraph'
    # time.sleep(4)
    while 1:
        txt = yield
        if txt in book:
            print('Found')
        else:
            print('Not found')
search = searched()
# print(time.time_ns())
next(search)
search.send('1500')
# print(time.time_ns())
search.send('this')
# print(time.time_ns())
search.send('Dishant')
# print(time.time_ns())
search.close()