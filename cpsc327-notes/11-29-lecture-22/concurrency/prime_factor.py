import random
from multiprocessing.pool import Pool
import time
import json


def prime_factor(value):
    factors = []
    for divisor in range(2, value - 1):
        quotient, remainder = divmod(value, divisor)
        if not remainder:
            factors.extend(prime_factor(divisor))
            factors.extend(prime_factor(quotient))
            break
    else:
        factors = [value]
    return factors


if __name__ == "__main__":
    t = time.time()

    with open("to_factor.json", "r") as f:
        to_factor = json.load(f)

    # I: Sequential --------------------

    # results = []
    # for value in to_factor:
    #     results.append(prime_factor(value))


    # II: With process pool -------------

    pool = Pool()           # creates same number of processes as the number of cores

    # II.1) with pool.map:
    # pass the jobs to each process (on each core);
    # when one job finishes, will assign a new one

    # results = pool.map(prime_factor, to_factor)

    # II.2) with pool.map_async:
    # Does not block; can continue doing other things

    results = pool.map_async(prime_factor, to_factor)   # returns MapResult
    print("waiting for prime factorizations")

    # add more jobs to the pool
    results2 = pool.apply_async(prime_factor, [53467234])
    results3 = pool.apply_async(prime_factor, [425555])

    results.wait()              # wait for all processes to finish
    results = results.get()     # convert MapResult to list
    results2.wait()
    print(results2.get())
    results3.wait()
    print(results3.get())

    for value, factors in zip(to_factor, results):
        print("The factors of {} are {}".format(value, factors))

    pool.close()        # wait for all things to stop and then close the pool
    pool.terminate()    # close the pool, kill anything that is not done
    print("work took {} seconds".format(time.time() - t))
