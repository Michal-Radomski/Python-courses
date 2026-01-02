import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection("127.0.0.1", 5003)
    print(f"Send {message}")
    writer.write(message.encode("utf8"))

    data = await reader.read(100)
    print(f"Received {data.decode('utf8')}")
    print("Close the connection")

    writer.close()
    await writer.wait_closed()


asyncio.run(tcp_echo_client("Hello world !"))
