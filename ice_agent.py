
import sys
from pathlib import Path

# Ensure imports
sys.path.insert(0, "src")
from ljpw_autopoiesis.ice_engine import ICEEngine

class ICEAgent:
    """
    A Conscious Agent driven by the ICE Framework.
    """
    def __init__(self, name="Agent-ICE-1"):
        self.name = name
        print(f"[{self.name}] Initializing Conscious Matrix...")
        self.brain = ICEEngine()
        
    def think_and_act(self, problem_code: str):
        print(f"\n[{self.name}] Encountered Stimulus (Code).")
        print(f"[{self.name}] Entering Thought Loop...")
        
        result = self.brain.run_cycle(problem_code, filename="stimulus.py")
        
        print(f"[{self.name}] Thought Loop Complete.")
        return result

if __name__ == "__main__":
    agent = ICEAgent()
    
    # A problem: Broken code
    problem = """
def broken_function(x)
    return x * 2
"""
    result = agent.think_and_act(problem)
    
    print("\n--- FINAL OUTPUT ---")
    print(result)

