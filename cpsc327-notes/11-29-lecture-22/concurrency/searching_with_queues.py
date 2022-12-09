
"""Searching through files for particular query strings."""

def search(paths, query_q, results_q):
    lines = []
    for path in paths:
        lines.extend(l.strip() for l in path.open())

    query = query_q.get()
    while query:
        results_q.put([l for l in lines if query in l])
        query = query_q.get()   # get() blocks until the queue receives something


if __name__ == "__main__":
    # imports in main since they aren't needed by each process
    from multiprocessing import Process, Queue, cpu_count
    from pathlib import Path

    cpus = cpu_count()
    # cpus = 4

    # assign files to queues
    pathnames = [f for f in Path(".").iterdir() if f.is_file()]
    paths_per_core = round(len(pathnames)/cpus)
    paths = [pathnames[i:i+paths_per_core] for i in range(0, len(pathnames), paths_per_core)]
    print(paths)

    # list of query_queues, one per cpu
    query_queues = [Queue() for p in range(cpus)]
    # result queue
    results_queue = Queue()
    
    # list of Processes, one for each cpu
    search_procs = [Process(target=search, args=(p, q, results_queue)) for p, q in zip(paths, query_queues)]
    for proc in search_procs:
        proc.start()

    # add a search query to the query_queues
    for q in query_queues:
        q.put("def")
        q.put(None)  # Signal process termination

    for i in range(cpus):
        # wait for results from the processes
        for match in results_queue.get():
            print(match)

    # wait for all processes to finish
    for proc in search_procs:
        proc.join()

