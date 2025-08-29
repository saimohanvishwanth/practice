# Asyncio
# For managing many writing tasks
# Threads
#For parallel tasks that share data with minimal CPU use
#Processes
#for maximizing performance on CPU intensive tasks

#1. Event LOOP : EXECUTING multiple tasks
'''
import asyncio

async def main():
    print("start of main coroutine")



#Run main coroutine
asyncio.run(main())
'''
#2.Coroutines
#two or more taks been executed at a time or else we can get values by delaying it
# here we need to wait one coroutine to finish and after that next coroutine
"""   
import asyncio
# Define a coroutine that simulaets a time-consuming task
async def fetch_data(delay, id):
    print("fetching data..id", id)
    await asyncio.sleep(delay)
    print("Data fethced, id", id)
    return {"data" : "Some data", "id": id} #Return some data

#Define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    task_1= fetch_data(2,1)
    task_2 = fetch_data(2,2)
    #Await the fetch data co routine . pausing execution of main untill fetch data completes
    result_1 = await task_1
    print(f"received result: {result_1}")
    result_2 = await task_2
    print(f"End of main coroutine,{result_2}")
#run the main coroutine
asyncio.run(main())"""
#coroutine doesn't start running until it's waited

#3. Task-> is a schedule a coroutine as soon as possible, allow us to run multiple coroutines simulteanously
#Here we can able to run the coroutines at a time
# if one task(coroutine)isn't doing something like it's block , idle.We switch over to another task(coroutine)
# Here we create task()

"""import asyncio

async def fetch_data(id, sleep_time):
    print(f"Continue {id} starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"id" : id, "data": f"sample data from coroutine{id}"}

#Create tasks for running coroutines concurrently
async def main():
    task_1 = asyncio.create_task(fetch_data(1,2))
    task_2 = asyncio.create_task(fetch_data(2,3))
    task_3 =asyncio.create_task(fetch_data(3,1))

    result_1 = await task_1
    result_2 = await task_2
    result_3 = await task_3

    print(result_1, result_2, result_3)
asyncio.run(main())
Summary :- when we create task, we are scheduling coroutines to run quickly as possible
 by allowing multiple coroutines at the same time.
 when one coroutine is not doing something/ waiting, we can switch to another coroutine."""


# 2. gather() ;- instead of creating the each and every task/coroutine , we can use gather function and collects the result in the list(coroutine order).
# gather may not close the other coroutines, if one of them(coroutines) fail/error occurs
# A Quick way to concurrently run multiple coroutines/tasks
#gather is not that great at error handling,it won't automatically cancel other coroutines, if one coroutine fails

"""import asyncio
async def fetch_data(id , sleep_time):
    print(f"coroutine {id} starting to fetch data")
    await asyncio.sleep(sleep_time)
    # return some data as a result
    return {"id": id, "data": f"sample data from coroutine{id}"}
async def main():
    #run coroutines concurrently and gather their return values
    results = await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))

    # Process the results
    for result in results:
        print(f"recevied result: {result}")

#Run the main coroutine
asyncio.run(main())"""


# TaskGroup() (most preferred way):- provides built in error handling
# Here if one coroutines/task fails, it cancels all of the coroutines/tasks automatically.
"""import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time) #simulate a network request or ID operation
    return {"id" : id, "data" : f"sample data from coroutine{id}"}
# 1. create task
# 2. as we define inside the taskgroup, wait for the task to be finish
#3. Unblock of the code/ after completion of the execution of the code , we move to next line of the code
async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg: # giving to access to tg variable
        for i, sleep_time in enumerate([2,1,3], start =1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)
    #After the task group block, all tasks have completed
    results =[task.result() for task in tasks]

    for result in results:
        print(f"received result: {result}")

asyncio.run(main())"""

# preferable when we are handling with advance errors
# Future - a promise of future result, it typically use lower level libraries
#waiting some value to be available, not waiting to complete the task to finish
"""import asyncio
async def set_future_result(future, value):
    await asyncio.sleep(2)
    #set the result of the future
    future.set_result(value)
    print(f"set the future's result to: {value}")

async def main():#create a future object
  loop = asyncio.get_running_loop()
  future = loop.create_future()

  #schedule setting the future's result
  asyncio.create_task(set_future_result(future, "future result is ready"))

  #wait for the future's result
  result = await future
  print(f"receoved the future's result: {result}")

asyncio.run(main())"""


# When we are waiting for the value to be available,not waiting for entire task or entire coroutine to finish
# Synchronization:- these are tools that allows us to synchronize various code when we are having larger & complex programs

"""import asyncio

# A shared variable
shared_resource = 0

#an asyncio lock(1.  create a lock)
lock = asyncio.Lock()
# 2.acquire the lock , lock is synchroinzing different coroutines
async def modify_shared_resource():
    global shared_resource
    async with lock: #check anyother coroutine currently using the lock, if it is then it waits until it's fetched / completed, if it's not then it will code below block of code
        print(f"Shared resource: {shared_resource}")
        shared_resource += 1 # Modify the shared resource
        await asyncio.sleep(1) # simulate an IO operation
        print(f"Resource after modification: {shared_resource}")
        #Critical section ends

async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

asyncio.run(main())





#lock()- no two coroutines are running at same time
# the reason is, what if the two coroutines are modifying or editing same file, we could get error as we are doing different operations at different times
# we aquire the lock with statement called " async with lock:"-> it will check if anyother coroutine is currently using the lock
# it will wait until it finish or else it will go in to block of code.
# whatever we put inside the context manager, needs to finish the executing before the lock will be release.
# An asyncio lock"""

#semaphore
# similar to lock
# it allows multiple coroutines to have access to the same object at the same time
# we can decide how corountines do we need
# we make sure throttle the program over load resource
# we can able to send max 5 request at a time
""""""
import asyncio

async def access_resource(semaphore, resource_id):
    async with semaphore:
        #Simulate accessing a limited resource
        print(f"Accessing resource {resource_id}")
        await asyncio.sleep(1) # simulate work with the resources
        print(f"releasing resource {resource_id}")

async def main():
    semaphore =asyncio.Semaphore(2) #Allow 2 Concurrent accesses
    await asyncio.gather(*(access_resource(semaphore, i) for _ in range(5)))

    asyncio.run(main())
"""
# event :- allows us to do synchronization
# we can create an event
# setting the variable to true/false
"""
import asyncio
async def waiter(event):
    print("walking for the event to be set")
    await event.wait()
    print("event has been set, continuing execution")

async def setter(event):
    await asyncio.sleep(2) #simulate doing some work
    event.set()
    print("event has been set!")

async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())


