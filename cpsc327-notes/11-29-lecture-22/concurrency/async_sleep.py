import asyncio
import random

# await is allowed only within async functions
async def random_sleep(counter):
    delay = random.random() * 5
    print("{} sleeps for {:.2f} seconds".format(counter, delay))
    await asyncio.sleep(delay)
    print("{} awakens".format(counter))


async def five_sleepers():
    print("Creating five tasks")
    tasks = [asyncio.create_task(random_sleep(i)) for i in range(5)]
    print("Sleeping after starting five tasks")
    await asyncio.sleep(2) # this line allows other coroutines to execute
    print("Waking and waiting for five tasks")
    await asyncio.gather(*tasks)


asyncio.get_event_loop().run_until_complete(five_sleepers())
print("Done five tasks")
