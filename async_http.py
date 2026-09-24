import aiohttp
import asyncio

async def func():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://example.com/') as response:
            data = await response.text()
            print(data)


asyncio.run(func())