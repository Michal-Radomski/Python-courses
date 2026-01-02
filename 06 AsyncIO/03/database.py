import asyncio

import aiosqlite  # type: ignore[import-not-found]


async def create_table(db_name, table_name):
    async with aiosqlite.connect(db_name) as db:
        await db.execute(
            f"Create table if not exists {table_name} (id integer primary key, message text)"
        )
        await db.commit()


async def insert_data(db_name, table_name, message):
    async with aiosqlite.connect(db_name) as db:
        await db.execute(f"insert into {table_name} (message) VALUES (?)", (message,))
        await db.commit()


async def fetch_data(db_name, table_name):
    async with aiosqlite.connect(db_name) as db:
        async with db.execute(f"SELECT id,message FROM {table_name}") as cursor:
            return [row async for row in cursor]


async def main():
    db_name = "test.db"
    table_name = "greetings"
    await create_table(db_name=db_name, table_name=table_name)
    await insert_data(db_name=db_name, table_name=table_name, message="Hello, AsyncIO!")
    greetings = await fetch_data(db_name=db_name, table_name=table_name)
    for greeting in greetings:
        print(f"Greeting {greeting[0]}: {greeting[1]}")


asyncio.run(main())
