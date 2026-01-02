import asyncio


async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode("utf8")
    addr = writer.get_extra_info("peername")

    print(f"received {message} from {addr}")
    print("sending ack")
    writer.write("ack".encode("utf8"))
    await writer.drain()
    writer.close()


async def main():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 5003)
    # addr = server.sockets[0].getsockname()
    # print("addr:", addr) # addr: ('127.0.0.1', 5003)

    async with server:
        await server.serve_forever()


asyncio.run(main())
