# pip install websockets
import asyncio
import websockets

loop = asyncio.get_event_loop()	#建立一个Event Loop

async def main(websocket, path):	#定义一个coroutine
	while 1:
		try:
			msg = await websocket.recv()
			print(f"< {msg}")
			await websocket.send(f"{msg}")
			print(f"> {msg}")
		except:
			print(f"closed")
			return

start_server = websockets.serve(main, "localhost", 8765)
loop.run_until_complete(start_server)	# 把coroutine注册到事件循环里
loop.run_forever()

