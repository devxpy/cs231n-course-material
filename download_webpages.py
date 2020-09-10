#!/usr/bin/env python3

from pyppeteer import launch
import asyncio
import os



async def main():
    b = await launch()
    p = await b.newPage()    

    with open("webpages.txt", "r") as f:
        y = f.read().strip().split()

    try:
        os.mkdir("webpages")
    except FileExistsError:
        pass

    for l in y:
        print('link:', l)
        await p.goto(l)

        path = f"webpages/{l.split('/')[-1]}.pdf"
        print('path:', path)
        await p.pdf(path=path)

    await b.close()


if __name__ == '__main__':
    asyncio.run(main())
