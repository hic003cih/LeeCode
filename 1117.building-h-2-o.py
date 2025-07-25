#
# @lc app=leetcode id=1117 lang=python3
#
# [1117] Building H2O
#

# @lc code=start
from threading import Semaphore, Barrier,Lock, Condition
# #1. Semaphore + Barrier
# class H2O:
#     def __init__(self):
#         # Permit for 2 hydrogen atoms to enter the barrier zone.
#         self.h_sem = Semaphore(2)
#         # Permit for 1 oxygen atom to enter the barrier zone.
#         self.o_sem = Semaphore(1)
#         # A barrier that waits for 3 threads (2 H, 1 O) to assemble.
#         self.barrier = Barrier(3)




#     def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
#         #Acquire a hydrogen permit. Blocks if 2 hydrogens are already waiting.
#         self.h_sem.acquire()
#         # Wait at the barrier for the other atoms.
#         self.barrier.wait()
#         # releaseHydrogen() outputs "H". Do not change or remove this line.
#         releaseHydrogen()
#         # Release the permit for the next hydrogen atom in the next molecule.
#         self.h_sem.release()


#     def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
#         # Acquire an oxygen permit. Blocks if 1 oxygen is already waiting.
#         self.o_sem.acquire()
#         # Wait at the barrier for the other atoms.
#         self.barrier.wait()
#         # releaseOxygen() outputs "O". Do not change or remove this line.
#         releaseOxygen()
#         # Release the permit for the next oxygen atom in the next molecule.
#         self.o_sem.release()

# 2. Lock + Condition Variable
class H2O:
    def __init__(self):
        self.lock = Lock()
        self.condition = Condition(self.lock)
        self.h_count = 0
        self.o_count = 0
    
    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.lock:
            # Wait until there's a spot for a hydrogen atom.
            self.condition.wait_for(lambda: self.h_count < 2)
            
            # Announce its arrival.
            self.h_count += 1
            
            # Check if a molecule can be formed.
            if self.h_count == 2 and self.o_count == 1:
                # If so, reset counters and notify all waiting threads for the next molecule.
                self.h_count = 0
                self.o_count = 0
                self.condition.notify_all()
            
        releaseHydrogen()
    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.lock:
            # Wait until there's a spot for an oxygen atom.
            self.condition.wait_for(lambda: self.o_count < 1)

            # Announce its arrival.
            self.o_count += 1

            # Check if a molecule can be formed.
            if self.h_count == 2 and self.o_count == 1:
                # If so, reset counters and notify all waiting threads for the next molecule.
                self.h_count = 0
                self.o_count = 0
                self.condition.notify_all()
        
        releaseOxygen()
# @lc code=end

