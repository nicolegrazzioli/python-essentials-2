"""Your task is to slightly extend the Queue class's capabilities. We want it to have a parameterless method that returns True if the queue is empty and False otherwise.

Complete the code we've provided in the editor. Run it to check whether it outputs a similar result to ours.

Expected output
1
dog
False
Queue empty"""

class QueueError(Exception):  # Choose base class for the new exception.
    def __init___(self):
        raise 


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if self.isempty():
            raise QueueError
        val = self.queue[-1]
        del self.queue[-1]
        return val
    
    # def isempty(self):
    #     return len(self.__queue) == 0


class SuperQueue(Queue):
    # def __init__(self):
    #     super().__init__()
    
    # def put(self, elem):
    #     super().put(elem)

    # def get(self):
    #     return super().get()

    # def isempty(self):
    #     return super().isempty()
    
    def isempty(self):
        return len(self.queue) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
    