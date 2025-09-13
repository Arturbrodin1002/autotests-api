import asyncio
import websockets


async def run_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Отправляем одно сообщение
        await websocket.send("Привет, сервер!")

        # Получаем 5 сообщений от сервера
        for _ in range(5):
            response = await websocket.recv()
            print(response)


if __name__ == "__main__":
    asyncio.run(run_client())
