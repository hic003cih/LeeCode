#
# @lc app=leetcode id=1115 lang=python3
#
# [1115] Print FooBar Alternately
#

# @lc code=start
from threading import Lock
class FooBar:
    # Synchronization
    def __init__(self, n):
        self.n = n
        self.lock = Lock()
        self.foo_turn = True
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            while True:
                self.lock.acquire()
                if self.foo_turn:
                    # printFoo() outputs "foo". Do not change or remove this line.
                    printFoo()
                    self.foo_turn =False
                    self.lock.release()
                    break
                else:
                     self.lock.release()
                    # time.sleep(0.0001) # Optionally yield CPU

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lock.acquire()
            if not self.foo_turn:
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.foo_turn = True
                self.lock.release()
                break
            else:
                self.lock.release()
                # time.sleep(0.0001)
# @lc code=end

