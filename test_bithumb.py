import cloudscraper
import asyncio
import logging
import re

async def bithumb_parse():

    global data
    scraper = cloudscraper.create_scraper()

    url = (f"https://feed.bithumb.com/notice/1648822")

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Priority': 'u=0, i',
    }

    cookies = {
        '_abck': 'E9AAC338C8DEDB8B221A2846C9E4C90C~0~YAAQBFHaFzUKolSYAQAAarYKcA5/1FAkA28RWZ15Xxgb2AzMVcwNFTxVJyboJDcsoxuUU+MryioSHvo7xFkaCxD9iYV/mJmotrykoy5Z87nW1mhDSXmlH3Zo7QvJS79wvnpbwi+BZOz7gw2IFzFvDSCJa7D60PJuK/z0/8FVJXlZ5gcGAJ1RJZ6dDeUDveoaL5VtuKIXmqbtRiVgey6SwUa9tWp/6RSZJ0wocJclh9367xlIYh7ujsTWlSziIfxiicBsYX6iCKz9g4YcS3zO0zOSpemyaV1rpcB3hfQCmJ1Nw98PQRy5nb0+P025t7+lFi8lg92l0dL/Fvllc//bJtzbJ8rljQYWr4JVO6doHI4s8lQau7n9A6BCS8wqlcn3TRuw6P0DkVL5kuH9JaeBgNCDX0H1RO0loM2SUbi6HcHsmiciZp1cHa0T4sNsW+Fp1BqTMH1T//aIV2bNYlwWbHdjA6q3dMbJEy1hWOrJEuP19HVL/X+XIIc+rGbkYoOMkIDDCP7f3ejYkKdpYHFmS6wtrdYjLY2x9FDtkxVh18u/r2Hz2cj9vfI+AAjExgMoiqugy0lqwPvwMOep9nMQuEccRqjWFGtfb4SsrNdi9A0FV4DyeOpxgoIMf3SDF2Kar4a20w==~-1~-1~-1',
        'bt_react': 'Y',
        '_gcl_au': '1.1.1791490407.1753710360',
        '_ga_LZEDLEJTC3': 'GS2.1.s1754383242$o7$g1$t1754383321$j43$l0$h1164541658',
        '_ga': 'GA1.1.1151527467.1753710360',
        'RT': '"z=1&dm=bithumb.com&si=823e2f14-0ab6-492e-a270-05c549b7c217&ss=mdrlalkh&sl=1&tt=0&rl=1&nu=2k8bnwg7&cl=43tm9v&obo=1&ld=43tqbb&r=3d0rzia4&hd=43tqbb"',
        '_fwb': '16394OBBWz9HIB1K7w1nSDG.1753710360430',
        'AMP_b7069d4788': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI3MTVkMjFjNy1jNjZhLTQzMjQtYTI3NC04YTcxNjkxYWNkNGUlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzU0MjI2NDEwNzU5JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc1NDIyNjQyNDE3NyUyQyUyMmxhc3RFdmVudElkJTIyJTNBOSU3RA==',
        'AMP_MKTG_b7069d4788': 'JTdCJTdE',
        'cf_clearance': 'p.nSL6haWEGfwd_dFjrXQdacMX4RziqBUdF2PDjWe6w-1754383241-1.2.1.1-dGMiFawJm5VTMtc6RS4v8HF1jAFlxSKEa0DyFmcZ5i8Ig2k45Hz1Ppd_xH.J4Lo0NL1myBrvVjVEIb90_8stT0Z2D5UUZEK76qAENwFaWPW4y59ZM7u0BDzlqdfussFd21G5M51Vof8wpUOBrver.wIvY0OhkrFkkLNrMM9UxyjvXz8dHGTfOLnipQILs9K_HWi8QNWamVBdHbh5Xt1j0Fe1MpEJ3Kpz4X.j4myOhBY',
        '_ga_V9QC8ZLCKS': 'GS2.1.s1754150221$o2$g0$t1754150221$j60$l0$h0',
        'custom_cookie_theme': 'N',
        '__cf_bm': 'EYLZcD3ebRx2c.OxXYXh7IWqeRww28yqUqQnDzHLGxQ-1754383238-1.0.1.1-CAttku_XvtPtEGsKK9r9LB_edTRZ4hFqxiJa5TQFd.yGsBCzT7CXR6KK9uWgtiye6Dw9MS6eEYVWXQiKnPQmZKr1L_P2S.8J8x8GV6HN0RY',
    }

    try:
        response = scraper.get(url, headers=headers, cookies=cookies)

        if response.status_code == 200:
            data = response.text
            print(f"Полная HTML страница: \n {data}")

            # Поиск всех вхождений "스파크(XYZ)" — где XYZ: 2 и более заглавных латинских букв
            match = re.search(r'스파크\(([A-Z]{2,})\)', data)

            if match:
                ticker = match.group(1)  # Извлекаем тикер из скобок
                print(f"Сам токен: {ticker}")
            else:
                print("Тикер не найден.")

        else:
            print(f"Failed with status code: {response.status_code}")
            print("Response Body:", response.text)

    except Exception as e:
        print(f"Error: {e}")

asyncio.run(bithumb_parse())