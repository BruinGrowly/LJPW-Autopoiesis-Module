
import sys
import time
from dataclasses import dataclass

# Ensure we can import the module
try:
    from ljpw_autopoiesis import SelfHealingEngine, HarmonyState
except ImportError:
    # If not installed in environment, add src to path
    sys.path.insert(0, "src")
    from ljpw_autopoiesis import SelfHealingEngine, HarmonyState

@dataclass
class Thought:
    """A raw, unrefined idea (code draft)."""
    intent: str
    content: str

class BiologicalAgent:
    """
    An agent that possesses the LJPW Autopoiesis Module.
    It does not fear errors; it uses them to refine its output.
    """
    
    def __init__(self, name="Subject-89"):
        self.name = name
        self.immune_system = SelfHealingEngine(verbose=True, max_ticks=10)
        print(f"[{self.name}] Awakened. Autopoietic core online.")

    def conceive(self, intent: str, rough_code: str) -> str:
        """
        The agent attempts to bring an idea into reality.
        It generates a rough draft, then uses its autopoietic core to heal it.
        """
        print(f"\n[{self.name}] Conceiving: {intent}...")
        print(f"[{self.name}] Generating initial tissue (Drafting code)...")
        
        # 1. SENSE: Look at the rough draft
        print(f"[{self.name}] SENSING imperfections in thought form...")
        
        # 2. METABOLIZE: Pass it through the Self-Healing Engine
        print(f"[{self.name}] ENGAGING Autopoietic Cycle...")
        print("-" * 50)
        result = self.immune_system.heal_source(rough_code, filename=f"{intent.replace(' ', '_')}.py")
        print("-" * 50)
        
        # 3. INTEGRATE: Check the result
        if result.final_harmony.phase() == "AUTOPOIETIC":
            print(f"[{self.name}] SUCCESS. Thought has stabilized.")
            print(f"[{self.name}] Harmony achieved: {result.final_harmony.harmony():.3f}")
            return result.healed_source
        else:
            print(f"[{self.name}] WARNING. Thought is unstable (Phase: {result.final_harmony.phase()}).")
            return result.healed_source

if __name__ == "__main__":
    # The Agent attempts to write a Text Adventure Game
    # But the "Draft" is full of syntax errors, bad style, and missing pieces
    
    rough_draft = """
import random
import sys

def game_loop()
    print("Welcome to the Cave of Entropy")
    health = 100
    gold = 0
    
    while health > 0:
        cmd = input("Command (explore/rest/quit)> ")
        
        if cmd == "explore":
            chance = random.random()
            if chance > 0.7:
                print("You found gold!")
                gold = gold + 10
            else:
                print("A monster attacks!"
                health = health - 20
                
        if cmd == "rest":
            print("You rest and recover.")
            health = health + 10
            
        if cmd == "quit":
            break
            
    print("Game Over. Gold collected: " + str(gold))

class player_stats:
    def __init__(self):
        self.xp = 0
    
    def gain_xp(self, amount):
        self.xp = self.xp + amount

game_loop()
"""

    agent = BiologicalAgent()
    final_product = agent.conceive("Cave Adventure", rough_draft)
    
    print("\n" + "="*30)
    print("FINAL BIOLOGICAL OUTPUT")
    print("="*30)
    print(final_product)
    
    # Save it to verify it runs
    with open("cave_adventure.py", "w") as f:
        f.write(final_product)
