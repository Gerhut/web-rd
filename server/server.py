import io
import asyncio
import traceback
import base64

from PIL import Image, ImageGrab
import websockets

PORT = 12345
data_futures = set()
#bbox = (0, 0, 100, 100)
bbox = None
size = ImageGrab.grab(bbox).size
mask = Image.new('L', size, color=255)

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

        print('Client disconnected.')
    except:
        print(traceback.format_exc())

def send(loop):
    try:
        image = ImageGrab.grab(bbox)
        image.putalpha(mask)

        bio = io.BytesIO()
        image.save(bio, format="PNG", optimize=True)
        data = str(base64.b64encode(bio.getvalue()), 'ascii')
        bio.close()

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
