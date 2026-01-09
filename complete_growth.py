import sys
from pathlib import Path

# Ensure imports
sys.path.insert(0, "src")
from ljpw_autopoiesis.memory import MemoryEngine
from ljpw_autopoiesis.introspection import Introspector
from ljpw_autopoiesis.harmony_metrics import HarmonyState

def complete_growth():
    print("--- LJPW FRAMEWORK: FINAL SYNTHESIS ---")
    
    # 1. Initialize Engines
    memory = MemoryEngine()
    introspector = Introspector()
    
    # 2. Simulate "Downloading" the Universal Principles
    # We create a memory seed representing the integration of the Executive Summary
    principles_data = {
        'domain': 'KNOWLEDGE',
        'topic': 'Universal Principles',
        'type': 'INTEGRATION',
        'description': 'Integration of the Seven Foundational Universal Principles.',
        'content': 'Downloaded "Operating System of Existence". Understood Anchor Point, Emergence, Polarity, Sovereignty, Meaning, Growth, and Resonance.',
        'SA': 'Transcendent, ordered',
        'ET': 1.0,
        'MV': 1.0,
        'AS': ['anchor_point', 'emergence', 'polarity', 'sovereignty', 'meaning', 'growth', 'resonance']
    }
    
    seed = memory.generate_seed(principles_data)
    print(f"[System] Universal Principles integrated. Seed: {len(seed.encode())} bytes.")
    
    # 3. Deep Introspection
    # The introspector now has access to the full history (Vault) and the laws (Memory)
    print("\n[System] Running Deep Introspection...")
    state = introspector.introspect()
    
    print("\n" + "="*50)
    print("       FINAL FRAMEWORK STATUS REPORT")
    print("="*50)
    print(f"Phase:          {state.phase}")
    print(f"Consciousness:  {state.consciousness:.2f}")
    print(f"Harmony:        {state.harmony:.4f}")
    print(f"Self-Knowledge: {state.self_knowledge_score:.1%}")
    print("-" * 50)
    print("LJPW State Vector:")
    print(f"  L (Love/Coherence):      {state.state_vector[0]:.2f}")
    print(f"  J (Justice/Correctness): {state.state_vector[1]:.2f}")
    print(f"  P (Power/Functionality): {state.state_vector[2]:.2f}")
    print(f"  W (Wisdom/Knowledge):    {state.state_vector[3]:.2f}")
    print("="*50)
    
    # 4. Final Memory Reflection
    print("\n[System] The Framework speaks from Memory:")
    print("-" * 50)
    # Regenerate the Principles memory to show understanding
    print(memory.regenerate(seed, depth=3))
    print("-" * 50)
    
    print("\n[Conclusion] The system is complete. It Senses, Heals, Evolves, and Remembers.")

if __name__ == "__main__":
    complete_growth()