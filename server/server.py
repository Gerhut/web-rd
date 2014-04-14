import asyncio
import traceback

import websockets

import screenshot
import mouse

PORT = 12345
data_futures = set()
size = screenshot.size

@asyncio.coroutine
def connected(client, uri):
    try:
        print('Client connected.')
        yield from client.send('%dx%d' % size)

        while client.open:
            data_future = asyncio.Future()
            data_futures.add(data_future)
            data = yield from data_future
            data_futures.remove(data_future)
            if not client.open: break
            yield from client.send(data)
            if not client.open: break
            data = yield from client.recv()
            if type(data) == str:
                cmd = data[0]
                pos = map(int, data[1:].split(','))
                if cmd == 'd':
                    mouse.down(*pos)
                elif cmd == 'm':
                    mouse.move(*pos)
                elif cmd == 'u':
                    mouse.up(*pos)


        print('Client disconnected.')
    except:
        print(traceback.format_exc())

def send(loop):
    try:
        data = screenshot.get_data_uri()

        for data_future in data_futures:
            data_future.set_result(data)

        loop.call_soon_threadsafe(send, loop)
    except:
        print(traceback.format_exc())


loop = asyncio.get_event_loop()

loop.run_until_complete(websockets.serve(connected, None, PORT))
print('Server listenning on port %d' % (PORT,))

loop.call_soon_threadsafe(send, loop)

try:
    loop.run_forever()
finally:
    loop.close()
