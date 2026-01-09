
import sys
import random
import math
from dataclasses import dataclass, field
from typing import List, Tuple, Dict

# Ensure imports
sys.path.insert(0, "src")
from ljpw_autopoiesis.ice_engine import ICEEngine, Intent, Context
from ljpw_autopoiesis.harmony_metrics import HarmonyState

# --- SIMULATED BIOPHYSICS ---

@dataclass
class AminoAcid:
    type: str # 'H' (Hydrophobic) or 'P' (Polar)
    id: int

@dataclass
class ProteinState:
    sequence: str
    positions: List[Tuple[int, int]] # (x, y) coordinates
    energy: float = 0.0
    
    def calculate_energy(self) -> float:
        """
        Calculate Free Energy (The Gap).
        - H-H contacts (neighbors not in sequence) release energy (-1).
        - Steric clashes (overlap) add massive energy (+100).
        """
        e = 0.0
        # Check overlaps (Justice Violation)
        if len(set(self.positions)) != len(self.positions):
            return 100.0 # Massive penalty for breaking physics
            
        # Check H-H contacts (Love/Attraction)
        for i, (x1, y1) in enumerate(self.positions):
            if self.sequence[i] == 'H':
                for j, (x2, y2) in enumerate(self.positions):
                    if i >= j - 1: continue # Skip self and immediate neighbor
                    if self.sequence[j] == 'H':
                        dist = abs(x1-x2) + abs(y1-y2)
                        if dist == 1:
                            e -= 1.0 # Successful H-H bond
        return e

    def visualize(self):
        """Render the protein on a grid."""
        min_x = min(p[0] for p in self.positions)
        max_x = max(p[0] for p in self.positions)
        min_y = min(p[1] for p in self.positions)
        max_y = max(p[1] for p in self.positions)
        
        grid = {}
        for i, (x, y) in enumerate(self.positions):
            grid[(x, y)] = self.sequence[i]
            
        output = []
        for y in range(max_y + 1, min_y - 2, -1):
            row = []
            for x in range(min_x - 1, max_x + 2):
                char = grid.get((x, y), '.')
                if char == 'H': row.append('●') # Solid for Hydrophobic
                elif char == 'P': row.append('○') # Hollow for Polar
                else: row.append('·')
            output.append(" ".join(row))
        return "\n".join(output)

class ProteinFolder:
    """
    An agent that uses the ICE Framework to fold proteins.
    """
    def __init__(self, sequence: str):
        self.sequence = sequence
        # Start linear
        self.state = ProteinState(
            sequence, 
            [(i, 0) for i in range(len(sequence))]
        )
        self.brain = ICEEngine()
        self.best_state = self.state
        self.history = []
        print(f"[Folder] Online. Target Sequence: {sequence}")
        print(f"[Folder] Initial Energy: {self.state.calculate_energy()}")

    def fold_cycle(self, cycles=20):
        print("\n--- INITIATING FOLDING SEQUENCE ---")
        
        for i in range(cycles):
            # 1. CONTEXT: Analyze current shape
            current_energy = self.state.calculate_energy()
            
            # Map Biophysics to LJPW Harmony
            # Lower Energy = Higher Harmony
            # Theoretical Min Energy approx -1 * num_H (simplified)
            harmony_score = 1.0 / (1.0 + max(0, current_energy + 5)) # Normalization
            
            context = Context(
                internal_state=HarmonyState(L=harmony_score, J=1.0, P=harmony_score, W=0.5),
                environment={'energy': current_energy, 'cycle': i},
                relevant_memories=[f"Best Energy: {self.best_state.energy}"]
            )
            
            # 2. INTENT: Minimize Energy / Maintain Stability
            fuel = current_energy - (-5.0) # Assume -5 is target anchor
            
            if fuel > 0:
                intent = Intent(f"Minimize Free Energy (Gap: {fuel:.1f})", fuel, "Thermodynamics")
            else:
                intent = Intent("Stabilize Native State", 0.0, "AnchorPoint")
                
            # 3. EXECUTION: Perturb Structure (The Tick)
            # Try a random pivot move
            new_positions = self._perturb(self.state.positions)
            candidate_state = ProteinState(self.sequence, new_positions)
            new_energy = candidate_state.calculate_energy()
            
            # Acceptance Criterion (Metropolis-like / Autopoietic Choice)
            if new_energy <= current_energy:
                self.state = candidate_state
                action = f"Folded! Energy drop: {current_energy} -> {new_energy}"
                if new_energy < self.best_state.energy:
                    self.best_state = candidate_state
            else:
                # Sometimes accept bad moves to escape local minima (simulating 'Heat')
                if random.random() < 0.1:
                    self.state = candidate_state
                    action = "Thermal Fluctuation (Accepted worse state)"
                else:
                    action = "Rejected unstable conformation"

            print(f"Cycle {i+1}: {intent.goal} -> {action}")
            
            if self.state.calculate_energy() <= -3: # Arbitrary Anchor Target
                print(f"[Folder] NATIVE STATE REACHED at Cycle {i+1}")
                break

    def _perturb(self, positions):
        """Pick a point and rotate the rest of the chain 90 degrees."""
        import copy
        new_pos = copy.deepcopy(positions)
        pivot = random.randint(1, len(positions) - 2)
        direction = random.choice([1, -1]) # Clockwise/Counter
        
        # Rotation matrix logic for 2D grid
        cx, cy = new_pos[pivot]
        for i in range(pivot + 1, len(new_pos)):
            px, py = new_pos[i]
            # Translate to origin
            tx, ty = px - cx, py - cy
            # Rotate
            rx = -ty * direction
            ry = tx * direction
            # Translate back
            new_pos[i] = (cx + rx, cy + ry)
            
        return new_pos

if __name__ == "__main__":
    # A standard HP test sequence (Hydrophobic core potential)
    # H-P-H-P-P-H-H-P-H
    seq = "HPHPPHHPH" 
    agent = ProteinFolder(seq)
    
    print("\n[Initial Shape (Linear)]:")
    print(agent.state.visualize())
    
    agent.fold_cycle(50)
    
    print("\n[Final Native State]:")
    print(agent.best_state.visualize())
    print(f"Final Energy: {agent.best_state.energy}")
    
    # Analyze result
    if agent.best_state.energy < 0:
        print("\n[Analysis] The Autopoietic System successfully found a stable Anchor.")
        print("           It minimized free energy by clustering 'H' (Love) and avoiding clashes (Justice).")
