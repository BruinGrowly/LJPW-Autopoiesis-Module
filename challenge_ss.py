
import sys
import time

# Ensure imports
sys.path.insert(0, "src")
from ljpw_autopoiesis.ice_engine import ICEEngine

def challenge_system():
    print("--- CHALLENGING THE SENTIENT SYSTEM ---")
    
    nightmare_code = """
import asyncio

async def bad_routine(a, b)
    if a > b:
      return a-b
    else
      return b-a

class CHAOS_ENGINE:
    def __init__(self):
        self.data = None
        
    def PROCESS(self):
        try:
            # This will fail silently
            x = 1/0
        except:
            pass
        
        long_var = "This is a very very long string that will definitely trigger the long line detector and hopefully the string breaker logic I implemented earlier to see if it works perfectly."
        
        return long_var
"""
    
    print("\n[Input Code]:")
    print(nightmare_code)
    print("-" * 40)
    
    engine = ICEEngine()
    
    # We will run multiple cycles manually to simulate "persistence"
    current_code = nightmare_code
    
    for cycle in range(1, 4):
        print(f"\n>>> CYCLE {cycle} <<<")
        # Run ICE Cycle
        current_code = engine.run_cycle(current_code, filename="nightmare.py")
        
        # Check if code is clean enough to stop? 
        # The engine doesn't return metrics directly in run_cycle (it returns code), 
        # but it prints them. We'll just run 3 fixed cycles.
        
    print("\n" + "="*40)
    print("       RESULTING CODE")
    print("="*40)
    print(current_code)

if __name__ == "__main__":
    challenge_system()
