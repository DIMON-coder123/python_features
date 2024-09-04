import requests
from wrapper_time import timer
import asyncio
import aiohttp

URL = [
    'https://www.google.com/',
    'https://www.youtube.com/',
    'https://www.python.org/',
    'https://github.com/',
    'https://www.office.com/'
]


async def async_requests(idx : int, url, session: aiohttp.ClientSession) -> None:
    async with session.get(url) as response:
        if 200 <= response.status < 300:
            text = 'OK'
        else:
            text = 'Failed'

        print(f"{idx} | {url}: {text}", end='\n')


def sync_requests(idx: int, url) -> None:
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        text = 'OK'
    else:
        text = 'Failed'

    print(f"{idx} | {url}: {text}", end = '\n')



def sync_run(count: int) -> None:
    for i in range(count):
        sync_requests(idx = i, url = URL[i % len(URL)])

async def async_run(count: int):
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(count):
            tasks.append(async_requests(idx = i, url = URL[i % len(URL)], session = session))

        await asyncio.gather(*tasks)


@timer
def sync_main() -> None:
    sync_run(30)

@timer
def async_main() -> None:
    asyncio.run(async_run(500))


if __name__ == '__main__':
    #sync_main()
    async_main()