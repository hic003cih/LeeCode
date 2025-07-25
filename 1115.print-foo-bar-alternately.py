#
# @lc app=leetcode id=1115 lang=python3
#
# [1115] Print FooBar Alternately
#

# @lc code=start
from threading import Semaphore, Lock, Condition

class FooBar:
	# 2. Semaphore
    # def __init__(self, n):
    #     self.n = n
    #     # foo_sem is initialized to 1, allowing the first foo() to run.
    #     self.foo_sem = Semaphore(1)
    #     # bar_sem is initialized to 0, forcing bar() to wait initially.
    #     self.bar_sem = Semaphore(0)


    # def foo(self, printFoo: 'Callable[[], None]') -> None:
        
    #    for i in range(self.n):
    #         # Wait for and acquire the permit for foo.
    #         self.foo_sem.acquire()
    #         # Execute the critical section.
    #         printFoo()
    #         # Release the permit for bar, allowing it to run.
    #         self.bar_sem.release()


    # def bar(self, printBar: 'Callable[[], None]') -> None:
        
    #      for i in range(self.n):
    #         # Wait for and acquire the permit for bar. This will block until foo() releases it.
    #         self.bar_sem.acquire()
    #         # Execute the critical section.
    #         printBar()
    #         # Release the permit for foo, allowing the next iteration of foo() to run.
    #         self.foo_sem.release()
	
    # 3. Condition Variable
	def __init__(self, n):
		self.n = n
		self.lock = Lock()
		self. condition = Condition(self.lock)
		# A shared state variable indicating whose turn it is.
		self.turn = 'foo'
	def foo(self, printFoo: 'Callable[[], None]') -> None:
		for i in range(self.n):
			# `with self.lock` automatically acquires and releases the lock.
			with self.lock:
				# wait_for() is a convenient method that combines the while loop and wait().
                # It waits until the predicate (the lambda function) returns True.
				self.condition.wait_for(lambda: self.turn =='foo')
				printFoo()
				# Change the state to signal the other thread.
				self.turn = 'bar'
				# Wake up the other thread (bar) which is waiting on the condition.
				self.condition.notify()
	def bar(self, printBar: 'Callable[[], None]') -> None:
		for i in range(self.n):
			# `with self.lock` automatically acquires and releases the lock.
			with self.lock:
				# Wait until the predicate `self.turn == 'bar'` is true.
				self.condition.wait_for(lambda: self.turn =='bar')
				printBar()
				# Change the state back to 'foo'.
				self.turn = 'foo'
				# Wake up the other thread (bar) which is waiting on the condition.
				self.condition.notify()
		
# @lc code=end

