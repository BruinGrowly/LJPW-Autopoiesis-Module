
import random
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Intent:
    """The WHY. The driving force or goal."""
    description: str
    priority: float

@dataclass
class Context:
    """The WHERE/WHEN. The environment, memory, and constraints."""
    environment_state: dict
    available_resources: List[str]
    constraints: List[str]

@dataclass
class Execution:
    """The HOW. The specific action taken."""
    action: str
    target: str

class ThoughtProcess:
    def __init__(self, name="CognitiveUnit"):
        self.name = name

    def attempt_action(self, intent: Optional[Intent], context: Optional[Context], execution: Optional[Execution]):
        print(f"\n--- {self.name}: Processing Thought ---")
        
        # Test Irreducibility: Can a thought exist without all three?
        
        if not intent:
            print("ERROR: Missing INTENT (The Why).")
            if execution:
                print(f"Result: Random, meaningless spasm. Performed '{execution.action}' for no reason.")
            else:
                print("Result: Catatonic state. Nothing happens.")
            return

        if not context:
            print(f"ERROR: Missing CONTEXT (The Where/When).")
            print(f"Intent: {intent.description}")
            if execution:
                print(f"Result: Hallucination/Delusion. Trying to '{execution.action}' without knowing reality.")
                print("Likely Outcome: Failure or destructive interference.")
            return

        if not execution:
            print(f"ERROR: Missing EXECUTION (The How).")
            print(f"Intent: {intent.description}")
            print(f"Context: {context.environment_state}")
            print("Result: Paralysis/Daydreaming. The thought exists but has no impact on reality.")
            return

        # If all three exist, the thought is CONSCIOUS and EFFECTIVE
        print("STATUS: ICE Triad Complete.")
        print(f"1. INTENT:    {intent.description} (P={intent.priority})")
        print(f"2. CONTEXT:   State={context.environment_state}, Resources={context.available_resources}")
        print(f"3. EXECUTION: {execution.action} on {execution.target}")
        
        # Logic: Does Execution match Intent given Context?
        if execution.action not in context.available_resources:
            print("RESULT: Failure. Execution impossible in this Context.")
        else:
            print("RESULT: SUCCESS. Reality altered in alignment with Intent.")

if __name__ == "__main__":
    brain = ThoughtProcess()
    
    # Scene: An agent needs to open a door. 
    
    # 1. Execution without Intent or Context (Reflex/Glitch)
    brain.attempt_action(None, None, Execution("open", "door"))
    
    # 2. Intent without Context (Blind Desire)
    brain.attempt_action(Intent("Escape room", 1.0), None, Execution("open", "door"))
    
    # 3. Intent + Context without Execution (Paralysis)
    ctx = Context({"door_status": "locked"}, ["key", "kick"], ["stamina"])
    brain.attempt_action(Intent("Escape room", 1.0), ctx, None)
    
    # 4. Full ICE (Conscious Action)
    brain.attempt_action(
        Intent("Escape room", 1.0), 
        ctx,
        Execution("key", "door_lock")
    )

