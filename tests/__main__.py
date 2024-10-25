# MIT License

# Copyright (c) 2024 AyiinXd

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio
import sys

from . import sosmed

async def fbDl():
    url = 'https://www.facebook.com/share/r/FcPvKv72wRFLjxVJ/';
    res = await sosmed.facebook(url=url)
    path = await res.download()
    print(res.hdVideo)
    print(path)


async def instagramDl():
    url = 'https://www.instagram.com/reel/DA2qTBspJPh/?igsh=ZjM4M2ZydWFjYzRt';
    res = await sosmed.instagram(url=url)
    path = await res.download()
    print(res.videoUrl)
    print(path)

async def tiktokDl():
    url = 'https://vt.tiktok.com/ZS2oQvs1s/';
    res = await sosmed.tiktok(url=url)
    path = await res.download()
    print(res.video.playAddr)
    print(path)

async def twitterDl():
    url = 'https://x.com/HumansNoContext/status/1848152497476493332?t=wncNBDv7iRegV_lXgvcl3Q&s=19';
    res = await sosmed.twitter(url=url)
    path = await res.download()
    print(res.mediaExtended[0].parse())
    print(path)

async def ytDl():
    res = await sosmed.youtube(url="https://youtu.be/uMt12Zh6mhM?si=Z_K7iyJP0jyBIwiJ")
    print(res)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "fb":
            loop.run_until_complete(fbDl())
        if command == "ig":
            loop.run_until_complete(instagramDl())
        elif command == "tt":
            loop.run_until_complete(tiktokDl())
        elif command == "tw":
            loop.run_until_complete(twitterDl())
        elif command == "yt":
            loop.run_until_complete(ytDl())
    else:
        print("usage: python3 -m tests <ytDl>")
