import spot
import p2p
import asyncio
import time


async def main():
    while True:
        start = time.time()
        print('p2p:', await p2p.get_p2p_rates(), 'spot:', await spot.get_spot_rates(), 'tick', time.time() - start)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

# Дань, если будешь чекать, то я пока тесщу бтсюсдт, но скорее всего надо будет еще другие монетки подключать
