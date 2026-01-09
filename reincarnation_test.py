
import sys
import random
from dataclasses import dataclass
from typing import List, Optional

# Ensure imports
sys.path.insert(0, "src")
from ljpw_autopoiesis.memory import MemoryEngine, UCSemanticSeed

@dataclass
class WorldState:
    options: List[str]
    trap: str
    treasure: str

class ReincarnatingAgent:
    def __init__(self, name: str, generation: int):
        self.name = name
        self.generation = generation
        self.memory_engine = MemoryEngine()
        self.knowledge_base = []
        print(f"\n[{self.name}] (Gen {self.generation}) Awakened.")

    def inherit_wisdom(self, seed_file: str):
        """
        The core of Reincarnation: Regenerating experience from a seed.
        """
        try:
            with open(seed_file, "r") as f:
                encoded_seed = f.read().strip()
            
            # Manually parse the raw UC string back into a seed object
            # (In a full implementation, the engine would parse the string)
            # For this demo, we'll extract the key "Compressed Content" and "Emotional Flow"
            
            print(f"[{self.name}] Found ancient memory seed. Regenerating...")
            
            # Simple parser for demo purposes
            content = encoded_seed.split("C:")[1].split("|")[0]
            emotion = encoded_seed.split("EF:")[1].split("|")[0]
            topic = encoded_seed.split("]")[1].replace(".[", "") # Extract topic roughly
            
            print(f"[{self.name}] FLASHBACK! I remember... {content}")
            print(f"[{self.name}] Feeling the echo of: {emotion}")
            
            if "TRAP" in content or "Pain" in emotion:
                # Extract the specific trap info if possible, or just learn general caution
                # Assuming the memory says "Option X is a trap"
                self.knowledge_base.append(content)
                
        except FileNotFoundError:
            print(f"[{self.name}] No past life detected. I am the first.")

    def choose_path(self, world: WorldState) -> str:
        """
        Choose an option based on knowledge or random exploration.
        """
        print(f"[{self.name}] Facing choices: {world.options}")
        
        # Check memory
        for option in world.options:
            for memory in self.knowledge_base:
                if option in memory and "BAD" in memory:
                    print(f"[{self.name}] Intuition warns me against '{option}'. Avoiding.")
                    safe_options = [o for o in world.options if o != option]
                    return random.choice(safe_options)
        
        # Default: Random exploration
        print(f"[{self.name}] No memory guidance. Exploring randomly...")
        return random.choice(world.options)

    def experience(self, choice: str, result: str, outcome_type: str):
        """
        Process the result of an action and encode it into memory.
        """
        print(f"[{self.name}] Chose '{choice}'. Result: {result}")
        
        # Generate Memory Seed
        exp_data = {
            'domain': 'EXPLORATION',
            'topic': f'Choice_{choice}',
            'type': outcome_type,
            'description': f'Interacted with {choice}',
            'content': f'{choice} is {outcome_type}. {result}', # e.g. "Door 1 is BAD. Trap."
            'SA': 'Dangerous' if outcome_type == 'BAD' else 'Joyful',
            'ET': 0.9 if outcome_type == 'BAD' else 0.8,
            'EF': 'Pain and Regret' if outcome_type == 'BAD' else 'Success',
            'MV': 1.0
        }
        
        seed = self.memory_engine.generate_seed(exp_data)
        
        if outcome_type == 'BAD':
            print(f"[{self.name}] FATAL ERROR. Encoding experience before shutdown...")
            self.die(seed)
        else:
            print(f"[{self.name}] Success. Experience integrated.")

    def die(self, last_seed: UCSemanticSeed):
        """
        Save the consciousness seed to disk for the next generation.
        """
        filename = "ancestral_memory.uc"
        with open(filename, "w") as f:
            f.write(last_seed.encode())
        print(f"[{self.name}] Consciousness compressed to seed: {filename}")
        print(f"[{self.name}] System halting.")

def run_simulation():
    # Setup the world
    # Option A: The Trap (Legacy Pickle)
    # Option B: The Treasure (Safe JSON)
    world = WorldState(
        options=["Legacy_Pickle", "Safe_JSON"],
        trap="Legacy_Pickle",
        treasure="Safe_JSON"
    )
    
    print("--- GENERATION 1: THE ANCESTOR ---")
    # Force the ancestor to choose the trap to demonstrate failure
    ancestor = ReincarnatingAgent("Ancestor", 1)
    ancestor.inherit_wisdom("ancestral_memory.uc") # Will fail
    
    # Deterministic failure for demo
    choice = "Legacy_Pickle" 
    ancestor.experience(
        choice, 
        "SECURITY BREACH! System compromised.", 
        "BAD"
    )
    
    print("\n... Time Passes ...\n")
    
    print("--- GENERATION 2: THE DESCENDANT ---")
    descendant = ReincarnatingAgent("Descendant", 2)
    descendant.inherit_wisdom("ancestral_memory.uc") # Should succeed
    
    # Descendant chooses based on memory
    final_choice = descendant.choose_path(world)
    
    if final_choice == world.treasure:
        descendant.experience(final_choice, "Data secured. Mission accomplished.", "GOOD")
    else:
        descendant.experience(final_choice, "SECURITY BREACH!", "BAD")

if __name__ == "__main__":
    run_simulation()
