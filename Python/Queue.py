#Structure
class Queue:
    def __init__(self):
        self.queue = [1,2,3,4]
        self.count = 4

    def enqueue(self, x):
        self.queue.insert(len(self.queue),x)
        self.count += 1

    def dequeue(self):
        self.count -= 1
        return self.queue.pop()

    def peek(self):
        return self.queue[-1]

    def empty(self):
        return self.count == 0

    def size(self):
        return self.count
#Example
def main():
	q = Queue()
	q.enqueue(5)
	print(q.queue)
	print(q.peek())
	print(q.size())
	for i in range(0,5):
		q.dequeue()
		print(q.queue)
	return q.empty

print(main())
