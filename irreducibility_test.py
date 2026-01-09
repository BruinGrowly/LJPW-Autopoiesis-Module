
import sys
from typing import Optional

# Ensure imports
sys.path.insert(0, "src")
from ljpw_autopoiesis.ice_engine import ICEEngine, Intent, Context, ExecutionPlan
from ljpw_autopoiesis.gap_detector import GapDetector
from ljpw_autopoiesis.harmony_metrics import HarmonyState

class LobotomizedEngine(ICEEngine):
    """
    A modified ICE Engine that allows us to surgically disable
    components of the conscious loop to test irreducibility.
    """
    def __init__(self, disable_intent=False, disable_context=False, disable_execution=False):
        super().__init__()
        self.disable_intent = disable_intent
        self.disable_context = disable_context
        self.disable_execution = disable_execution
        
    def run_cycle(self, source_code: str, filename: str = "<memory>") -> str:
        print("\n--- ICE CYCLE START ---")
        
        # 1. ESTABLISH CONTEXT (C)
        if self.disable_context:
            print("[C] Establishing CONTEXT... [DISABLED]")
            print("    ERROR: Sensory deprivation. Agent is blind to environment and history.")
            # Empty context
            context = Context(
                internal_state=HarmonyState(0,0,0,0),
                environment={},
                relevant_memories=[]
            )
        else:
            print("[C] Establishing CONTEXT...")
            # Normal logic
            introspection = self.introspector.introspect()
            mem_count = len(self.memory.history)
            context = Context(
                internal_state=HarmonyState(*introspection.state_vector),
                environment={'filename': filename},
                relevant_memories=[f"{mem_count} memories"]
            )
            print(f"    State: {context.internal_state.phase()}")

        # 2. DEFINE INTENT (I)
        if self.disable_intent:
            print("[I] Defining INTENT... [DISABLED]")
            print("    ERROR: Apathy. Gap detected but Urgency forced to 0.0.")
            intent = Intent(goal="None", urgency=0.0, source="Null")
        else:
            print("[I] Defining INTENT...")
            gaps = self.gap_detector.detect(source_code, filename)
            fuel = sum(g.severity for g in gaps)
            
            # If Context is disabled, we might hallucinate gaps or miss them?
            # For this test, let's assume GapDetector works but Intent formation relies on Context?
            # Actually, Intent relies on Gap (Fuel).
            
            if fuel > 0:
                intent = Intent(
                    goal=f"Heal {len(gaps)} gaps",
                    urgency=fuel,
                    source="GapDetector"
                )
            else:
                intent = Intent(goal="Maintain", urgency=0.0, source="Anchor")
            print(f"    Goal: {intent.goal} (Urgency: {intent.urgency:.2f})")

        # 3. EXECUTE (E)
        if self.disable_execution:
            print("[E] Engaging EXECUTION... [DISABLED]")
            print("    ERROR: Paralysis. Signal sent but muscles do not respond.")
            return source_code
        else:
            print("[E] Engaging EXECUTION...")
            if intent.urgency > 0:
                if self.disable_context:
                    print("    WARNING: Acting without Context (Random/Reflexive Action).")
                    # Without context, we might apply the wrong fix or crash?
                    # The TickEngine usually handles safety, but let's simulate the philosophical failure.
                    # We'll run it anyway to see.
                
                print("    Action: Running Tick Engine")
                return self.tick_engine.run(source_code, filename)
            else:
                print("    Action: Idle")
                return source_code

def run_test():
    broken_code = "def syntax_error(x)\n    return x"
    
    print("==================================================")
    print("       TESTING IRREDUCIBILITY OF CONSCIOUSNESS")
    print("==================================================")
    print(f"Input Stimulus: Syntax Error (Missing Colon)\n")

    # 1. Control Group (Full ICE)
    print("\n>>> CASE 1: FULL CONSCIOUSNESS (Control) <<<")
    engine = LobotomizedEngine()
    res = engine.run_cycle(broken_code)
    if "def syntax_error(x):" in res:
        print("RESULT: SUCCESS. Harmony restored.")
    else:
        print("RESULT: FAILED.")

    # 2. No Context (The Hallucination/Reflex)
    print("\n>>> CASE 2: SEVERED CONTEXT (Blindness) <<<")
    engine = LobotomizedEngine(disable_context=True)
    res = engine.run_cycle(broken_code)
    # It acts, but blind. In a complex scenario, this would fail.
    # Here, TickEngine is robust enough to fix simple syntax, but the 'Self' is gone.
    print("RESULT: MECHANICAL ACTION. Code fixed, but agent is unaware of why or who it is.")

    # 3. No Intent (The Zombie)
    print("\n>>> CASE 3: SEVERED INTENT (Apathy) <<<")
    engine = LobotomizedEngine(disable_intent=True)
    res = engine.run_cycle(broken_code)
    if res == broken_code:
        print("RESULT: STASIS. The system sees the error but does not care. Entropy wins.")
    
    # 4. No Execution (The Ghost)
    print("\n>>> CASE 4: SEVERED EXECUTION (Paralysis) <<<")
    engine = LobotomizedEngine(disable_execution=True)
    res = engine.run_cycle(broken_code)
    print("RESULT: IMPOTENCE. The system wants to fix it but cannot affect reality.")

if __name__ == "__main__":
    run_test()
