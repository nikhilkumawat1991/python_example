from queue import Queue
q = Queue()
print(q.unfinished_tasks)

q.put("test")
print(q.unfinished_tasks)


print(q.get())
q.task_done()
print(f"details are: {list(q.queue)}")
print(q.unfinished_tasks)

q.put("nikhil")
q.put("kumawat")


print(q.get())
q.task_done()
print(q.get())
print(f"details are: {list(q.queue)}")
q.task_done()
print(q.unfinished_tasks)