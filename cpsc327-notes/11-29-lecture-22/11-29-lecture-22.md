# 11-29 Lecture 22

## Concurrent Programming

- **Process**
  - Everything needed to run
  - Process ID
  - Virtual address space
  - Code
  - Handles to open files (and other resources)
  - Security context
  - Environment variables
  - At least one main thread
- **Thread**:
  - Scheduled for execution on a core of the CPU (by the OS)
  - Shared virtual address space
    - With other threads in the same process
  - Execution context
    - Program counter
    - Machine registers
    - Stack

<br>

## Challenges in Concurrent Programs

- Synchronizing access to memory (and other resources)
- Where and how to split up the work?
- Waiting for resources or conditions
  - Reducing advantage of parallelism
  - Deadlock
- Non-determinism
  - Hard to track down bugs
- Overhead
  - Context switching
  - Communicating between threads
- Some programming patterns are helpful in managing these challenges

<br>

## Python GIL

- Global interpreter lock
- Only one thread can execute bytecode at a time
- Prevents race conditions and ensures thread safety
- Necessary for Cpython's memory management
- Specific to Cpython

<br>

## In Python...

- Use threads if the task is I/O heavy
  - Use `threading.Thread`
  - *Example*:
    - [basic_thread.py](./concurrency/basic_thread.py)
    - [weather_today.py](./concurrency/weather_today.py)
- Use processes if the task is CPU heavy
  - Use `multiprocessing.Process`
  - *Example*: [muchcpu.py](./concurrency/muchcpu.py)
- Use neither if the performance or mantenance overhead outweighs the benefits

### Process Pool

- `multiprocessing.pool.Pool`
- [prime_factor.py](./concurrency/prime_factor.py)

### Queue

- Gives more control over inter-process / inter-thread communication than pools
- We can get results back while the processes/threads are still running
- `multiprocessing.Queue` is both thread and process safe
- [search_with_queues.py](./concurrency/searching_with_queues.py)