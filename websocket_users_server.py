import asyncio
import websockets


async def handle_client(websocket):
    try:
        print("Клиент подключился")
        message = await websocket.recv()
        print(f"Получено сообщение от пользователя: {message}")

        # Отправляем 5 ответов клиенту
        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}"
            print(f"Отправляю клиенту: {response}")
            await websocket.send(response)
            await asyncio.sleep(0.2)

        print("Все сообщения отправлены")
    except Exception as e:
        print(f"Ошибка при обработке клиента: {e}")


async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        print("WebSocket сервер запущен на ws://localhost:8765")
        await asyncio.Future()  # чтобы сервер работал бесконечно


if __name__ == "__main__":
    asyncio.run(main())
