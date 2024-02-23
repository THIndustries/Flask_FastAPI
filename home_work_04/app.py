import aiohttp
import aiofiles
import asyncio
import os
from urllib.parse import urlparse
from datetime import datetime
import sys

async def download_image(session, url):
    start_time = datetime.now()
    try:
        async with session.get(url) as response:
            if response.status == 200:
                # Извлекаем имя файла из URL
                filename = os.path.basename(urlparse(url).path)
                async with aiofiles.open(filename, mode='wb') as f:
                    await f.write(await response.read())
                print(f"Скачивание завершено: {filename} за {datetime.now() - start_time}")
            else:
                print(f"Ошибка при скачивании {url}: Статус {response.status}")
    except Exception as e:
        print(f"Ошибка при скачивании {url}: {e}")

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
        start_time = datetime.now()
        asyncio.run(main(urls))
        print(f"Общее время выполнения: {datetime.now() - start_time}")
    else:
        print("Пожалуйста, укажите хотя бы один URL в качестве аргумента.")
