# import requests

# url = ["https://example.com/"] * 5 

# for u in url:
#     response = requests.get(u)
#     print(response.text)

import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        print(response.status)
        return await response.text()

async def main():
    urls = ["https://example.com/"] * 5
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

asyncio.run(main())
