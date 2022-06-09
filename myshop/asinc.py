import aiohttp
import asyncio

urls = ['http://127.0.0.1:8000/category/', 'http://127.0.0.1:8000/index/']


# async def get_url(url):
#     print(f'getting{url}')
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             data = await response.text()
#             data_len = len(data)
#             print(f'recevied: {data_len}')
#
#
# futures = [get_url(u) for u in urls]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(futures))
results = []

async def get_urls_async(urls):
    loop = asyncio.get_running_loop()

    async with aiohttp.ClientSession() as session:
        tasks = []

        for u in urls:
            print(f"This is the first (HEAD) request we send for {u}")
            tasks.append(loop.create_task(session.get(u)))

        results = []
        for t in asyncio.as_completed(tasks):
            response = await t
            url = response.url

            if "text/html" in response.headers["Content-Type"]:
                print("Sending the 2nd (GET) request to retrive body")
                r = await session.get(url)
                results.append((url, await r.read()))
            else:
                print(f"Not HTML, rejecting: {url}")

        return results

results = asyncio.run(get_urls_async(urls))