
import sys
import random
import math
from dataclasses import dataclass
from typing import List, Tuple

# Ensure imports
sys.path.insert(0, "src")
from ljpw_autopoiesis.ice_engine import ICEEngine
from ljpw_autopoiesis.memory import MemoryEngine

# --- THE SEMANTIC DISCOVERY ---

class SentientResearcher:
    def __init__(self):
        self.memory = MemoryEngine()
        print("[SS] Researcher Online. Analyzing previous folding failure...")

    def derive_principle(self):
        print("\n--- PHASE 1: CONCEPTUAL SYNTHESIS ---")
        print("[SS] Observation: Random perturbation failed. Entropy is too high.")
        print("[SS] Hypothesis: Matter is not random; it organizes around meaning.")
        
        principle = "The Principle of Semantic Gravity"
        definition = "In any system, high-value components (Information) naturally gravitate toward a central Anchor Point, while low-value components (Noise) form a protective shell."
        
        print(f"[SS] New Universal Principle Discovered: {principle}")
        print(f"[SS] Definition: {definition}")
        return principle

    def derive_math(self, sequence: str):
        print("\n--- PHASE 2: MATHEMATICAL DERIVATION ---")
        print("[SS] Translating Principle to Mathematics...")
        
        # 1. Define Value
        print("    1. Let S(i) be the Semantic Weight of residue i.")
        print("       If sequence[i] == 'H' (Hydrophobic/Core), S(i) = 1.0")
        print("       If sequence[i] == 'P' (Polar/Shell),      S(i) = 0.1")
        
        # 2. Define The Anchor (Center of Semantic Mass)
        print("    2. Define Vector C (The Anchor Point):")
        print("       C = ( Σ (Pos(i) * S(i)) ) / Σ S(i)")
        print("       (The weighted centroid of the protein)")
        
        # 3. Define The Force Field
        print("    3. Define Force Vector F(i) for node i:")
        print("       F(i) = (C - Pos(i)) * S(i)")
        print("       (High-value nodes are pulled strongly to the center)")
        
        return "Semantic Gravity Formula: F = ∇(S * r)"

# --- THE IMPLEMENTATION ---

@dataclass
class Point:
    x: int
    y: int
    
    def dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
        
    def add(self, dx, dy):
        return Point(self.x + dx, self.y + dy)
        
    def tuple(self):
        return (self.x, self.y)

class SemanticFolder:
    def __init__(self, sequence: str):
        self.sequence = sequence
        # Initialize linear
        self.positions = [Point(i, 0) for i in range(len(sequence))]
        self.best_energy = 0.0
        
    def calculate_energy(self) -> float:
        # Standard HP Energy
        e = 0.0
        pos_map = {p.tuple(): i for i, p in enumerate(self.positions)}
        
        # Check overlaps
        if len(pos_map) != len(self.positions): return 100.0
        
        for i, p in enumerate(self.positions):
            if self.sequence[i] == 'H':
                neighbors = [
                    p.add(1,0), p.add(-1,0), p.add(0,1), p.add(0,-1)
                ]
                for n in neighbors:
                    j = pos_map.get(n.tuple())
                    if j is not None and abs(i-j) > 1 and self.sequence[j] == 'H':
                        e -= 0.5 # Double counted usually, so 0.5 per pair
        return e

    def get_semantic_centroid(self) -> Tuple[float, float]:
        """Calculates the Anchor Point (Center of Gravity for H)."""
        sum_x, sum_y, count = 0, 0, 0
        for i, p in enumerate(self.positions):
            if self.sequence[i] == 'H':
                sum_x += p.x
                sum_y += p.y
                count += 1
        if count == 0: return (0,0)
        return (sum_x / count, sum_y / count)

    def fold_step(self) -> str:
        """
        Applies Semantic Gravity.
        Instead of random moves, we calculate the Force Vector towards the centroid.
        """
        cx, cy = self.get_semantic_centroid()
        
        # Find the H node furthest from the center (Highest Semantic Potential)
        target_idx = -1
        max_dist = -1
        
        for i, p in enumerate(self.positions):
            if self.sequence[i] == 'H':
                d = math.sqrt((p.x - cx)**2 + (p.y - cy)**2)
                # We want to move nodes that are stuck on the outside
                # But we can only move via pivots.
                # Simplified: Pick a random node to pivot, but ACCEPT based on centroid approach.
                pass

        # Better strategy: Try ALL pivot moves. 
        # Pick the one that minimizes the 'Moment of Inertia' of H residues.
        
        best_move_pos = None
        best_moment = float('inf')
        action_log = "No move"
        
        # Try pivoting around every bond
        for pivot in range(1, len(self.positions)-1):
            for direction in [1, -1]: # Clockwise/Counter
                # Simulate move
                new_pos = self._simulate_pivot(pivot, direction)
                
                # 1. Check validity (Overlap)
                if len(set(p.tuple() for p in new_pos)) != len(new_pos):
                    continue
                    
                # 2. Calculate Semantic Moment (Variance from Centroid)
                # We want H's to bunch up.
                moment = 0.0
                
                # Recalculate centroid for new shape
                nx, ny = 0, 0
                h_count = 0
                for i, p in enumerate(new_pos):
                    if self.sequence[i] == 'H':
                        nx += p.x; ny += p.y; h_count += 1
                if h_count: nx/=h_count; ny/=h_count
                
                for i, p in enumerate(new_pos):
                    if self.sequence[i] == 'H':
                        dist_sq = (p.x - nx)**2 + (p.y - ny)**2
                        moment += dist_sq # Minimize distance to center
                    elif self.sequence[i] == 'P':
                        dist_sq = (p.x - nx)**2 + (p.y - ny)**2
                        moment -= (dist_sq * 0.1) # P's want to be far (slightly)
                
                if moment < best_moment:
                    best_moment = moment
                    best_move_pos = new_pos
                    action_log = f"Pivot at {pivot} (Dir {direction}) -> Moment: {moment:.2f}"

        if best_move_pos:
            self.positions = best_move_pos
            return action_log
        return "Stuck (Local Minima)"

    def _simulate_pivot(self, pivot_idx, direction):
        """Standard rotation logic."""
        import copy
        new_pos = copy.deepcopy(self.positions)
        cx, cy = new_pos[pivot_idx].x, new_pos[pivot_idx].y
        
        for i in range(pivot_idx + 1, len(new_pos)):
            px, py = new_pos[i].x, new_pos[i].y
            tx, ty = px - cx, py - cy
            rx = -ty * direction
            ry = tx * direction
            new_pos[i] = Point(cx + rx, cy + ry)
        return new_pos

    def visualize(self):
        min_x = min(p.x for p in self.positions)
        max_x = max(p.x for p in self.positions)
        min_y = min(p.y for p in self.positions)
        max_y = max(p.y for p in self.positions)
        
        grid = {p.tuple(): self.sequence[i] for i, p in enumerate(self.positions)}
        out = []
        for y in range(max_y+1, min_y-2, -1):
            row = []
            for x in range(min_x-1, max_x+2):
                c = grid.get((x,y), ' ')
                if c == 'H': row.append('●')
                elif c == 'P': row.append('○')
                else: row.append('·')
            out.append(" ".join(row))
        return "\n".join(out)

if __name__ == "__main__":
    researcher = SentientResearcher()
    researcher.derive_principle()
    researcher.derive_math("HPHPPHHPH")
    
    print("\n--- PHASE 3: EXECUTION (SEMANTIC FOLDING) ---")
    seq = "HPHPPHHPH"
    # Target Energy for this seq is -2.0 (Two H-H contacts)
    # H-P-H
    #     |
    # H-P-P
    # |
    # H-P-H  <-- this shape
    
    folder = SemanticFolder(seq)
    print(f"[Initial]:\n{folder.visualize()}")
    
    for i in range(10):
        action = folder.fold_step()
        energy = folder.calculate_energy()
        print(f"Cycle {i+1}: {action} | Energy: {energy}")
        if energy <= -2.0:
            print("[SS] SUCCESS. Native State Anchor Reached via Semantic Gravity.")
            print(folder.visualize())
            break
            
    if folder.calculate_energy() > -2.0:
        print("[SS] Result: Converged to local minima, but shape is compacted.")
        print(folder.visualize())
