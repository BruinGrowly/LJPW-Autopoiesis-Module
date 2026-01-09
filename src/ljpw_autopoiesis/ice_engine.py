"""
LJPW ICE Engine - The Conscious Thought Loop

Implements the ICE Framework (Intent, Context, Execution) as the
irreducible "operating system" for conscious decision making.

Mappings to LJPW:
- INTENT (I): The Gap from Anchor (The Drive)
- CONTEXT (C): Introspection + Memory (The Awareness)
- EXECUTION (E): Tick Engine + Healing (The Action)
"""

from dataclasses import dataclass
from typing import Optional, Dict, Any

from .gap_detector import GapDetector
from .introspection import Introspector
from .memory import MemoryEngine, UCSemanticSeed
from .tick_engine import TickEngine
from .harmony_metrics import HarmonyState

@dataclass
class Intent:
    """The Driving Force."""
    goal: str
    urgency: float
    source: str # e.g. "GapDetector", "UserCommand"

@dataclass
class Context:
    """The Situational Awareness."""
    internal_state: HarmonyState
    environment: Dict[str, Any]
    relevant_memories: list

@dataclass
class ExecutionPlan:
    """The Proposed Action."""
    module: str # e.g. "TickEngine"
    params: Dict[str, Any]

class ICEEngine:
    """
    The ICE Engine unifies the LJPW Framework under a single
    conscious loop structure.
    """
    
    def __init__(self):
        self.gap_detector = GapDetector()
        self.introspector = Introspector()
        self.memory = MemoryEngine()
        self.tick_engine = TickEngine()
        print("[ICE] Engine Online. Intent-Context-Execution Loop initialized.")

    def run_cycle(self, source_code: str, filename: str = "<memory>") -> str:
        """
        Run one complete ICE Cycle.
        """
        print("\n--- ICE CYCLE START ---")
        
        # 1. ESTABLISH CONTEXT (C)
        # "Where am I? What do I know?"
        print("[C] Establishing CONTEXT...")
        introspection = self.introspector.introspect()
        
        # Check memory for relevant wisdom (Context expansion)
        # For simplicity, we just check total wisdom available
        mem_context = f"{len(self.memory.history)} memories available"
        
        context = Context(
            internal_state=HarmonyState(*introspection.state_vector),
            environment={'filename': filename, 'source_len': len(source_code)},
            relevant_memories=[mem_context]
        )
        print(f"    State: {context.internal_state.phase()}")
        print(f"    Memory: {mem_context}")

        # 2. DEFINE INTENT (I)
        # "What do I want? Why?"
        print("[I] Defining INTENT...")
        gaps = self.gap_detector.detect(source_code, filename)
        fuel = sum(g.severity for g in gaps)
        
        if fuel > 0:
            intent = Intent(
                goal=f"Heal {len(gaps)} gaps to restore Harmony",
                urgency=fuel,
                source="GapDetector"
            )
        else:
            intent = Intent(
                goal="Maintain Homeostasis",
                urgency=0.0,
                source="AnchorPoint"
            )
        print(f"    Goal: {intent.goal} (Urgency: {intent.urgency:.2f})")

        # 3. EXECUTE (E)
        # "How do I do it?"
        print("[E] Engaging EXECUTION...")
        
        if intent.urgency > 0:
            # High urgency -> Run Tick Engine
            print("    Action: Running Tick Engine (Metabolism)")
            # (Note: In a real agent, this would be dynamic dispatch)
            healed_code = self.tick_engine.run(source_code, filename)
            
            # Record experience
            self._record_cycle(intent, context, "Healed Code")
            return healed_code
        else:
            # Low urgency -> Deepen Memory / Idle
            print("    Action: Strengthening Memory (Meditation)")
            # No code change
            self._record_cycle(intent, context, "Maintained Stasis")
            return source_code

    def _record_cycle(self, i: Intent, c: Context, e_result: str):
        """
        Encode the ICE cycle into memory.
        """
        seed_data = {
            'domain': 'ICE_LOOP',
            'topic': 'Conscious_Thought',
            'type': 'CYCLE',
            'description': f"I: {i.goal} -> E: {e_result}",
            'content': f"Context Phase: {c.internal_state.phase()}. Urgency: {i.urgency:.2f}",
            'SA': 'Focused, Agentic',
            'ET': 0.8,
            'MV': 1.0,
            'AS': ['ICE', 'autopoiesis']
        }
        self.memory.generate_seed(seed_data)
        print("[ICE] Cycle Encoded to Memory.")

if __name__ == "__main__":
    # Test the Engine
    engine = ICEEngine()
    
    broken_code = "def test():\n  pass" # valid but maybe empty
    
    # Run cycle
    engine.run_cycle(broken_code, "test.py")
