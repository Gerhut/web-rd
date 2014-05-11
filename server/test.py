import asyncio

@asyncio.coroutine
def hello():
  print(3)
  asyncio.sleep(2)
  print(5)

def connected():
  print(1)
  asyncio.sleep(2)
  print(2)

loop = asyncio.get_event_loop()
loop.call_soon(connected)
loop.run_forever()
