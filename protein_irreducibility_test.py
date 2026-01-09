
import sys
import random
import math
import copy
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Point:
    x: int
    y: int
    def tuple(self): return (self.x, self.y)

class ProteinState:
    def __init__(self, sequence: str, positions: List[Point]):
        self.sequence = sequence
        self.positions = positions

    def calculate_energy(self) -> float:
        """The 'Intent' metric: Lower is better."""
        e = 0.0
        pos_map = {p.tuple(): i for i, p in enumerate(self.positions)}
        
        # Steric Clash (Fatal Context Error)
        if len(pos_map) != len(self.positions): return 100.0
        
        # H-H Bonds (Success)
        for i, p in enumerate(self.positions):
            if self.sequence[i] == 'H':
                neighbors = [(p.x+1, p.y), (p.x-1, p.y), (p.x, p.y+1), (p.x, p.y-1)]
                for nx, ny in neighbors:
                    j = pos_map.get((nx, ny))
                    if j is not None and abs(i-j) > 1 and self.sequence[j] == 'H':
                        e -= 0.5
        return e

    def get_centroid(self) -> Tuple[float, float]:
        """The 'Context' metric: The Semantic Center."""
        sx, sy, c = 0, 0, 0
        for i, p in enumerate(self.positions):
            if self.sequence[i] == 'H':
                sx += p.x; sy += p.y; c += 1
        return (sx/c, sy/c) if c else (0,0)

    def visualize(self):
        min_x = min(p.x for p in self.positions)
        max_x = max(p.x for p in self.positions)
        min_y = min(p.y for p in self.positions)
        max_y = max(p.y for p in self.positions)
        grid = {p.tuple(): self.sequence[i] for i, p in enumerate(self.positions)}
        out = []
        for y in range(max_y+1, min_y-1, -1):
            row = []
            for x in range(min_x-1, max_x+2):
                c = grid.get((x,y), ' ')
                if c == 'H': row.append('●')
                elif c == 'P': row.append('○')
                else: row.append('·')
            out.append(" ".join(row))
        return "\n".join(out)

class FoldingSimulation:
    def __init__(self, sequence: str, mode: str):
        self.sequence = sequence
        self.mode = mode
        self.positions = [Point(i, 0) for i in range(len(sequence))]
        self.history = []
        print(f"\n--- SIMULATION MODE: {self.mode} ---")

    def run(self, cycles=50, target=-2.0):
        for i in range(cycles):
            current_energy = self.calculate_energy(self.positions)
            
            # --- EXECUTION PHASE (Propose a move) ---
            new_pos = self._propose_move()
            
            # --- CONTEXT PHASE (Analyze the move) ---
            if self.mode == "NO_CONTEXT":
                # Blind: Only checks local validity (no overlap), ignores Global Semantic Gravity
                # It doesn't "see" the centroid.
                is_valid = len(set(p.tuple() for p in new_pos)) == len(new_pos)
                context_score = 0 # Irrelevant
            else:
                # Full Context: Checks validity AND Semantic Centroid alignment
                is_valid = len(set(p.tuple() for p in new_pos)) == len(new_pos)
                
                # Calculate Semantic Moment (Distance of H from Center)
                cx, cy = self._get_centroid(new_pos)
                moment = 0
                for j, p in enumerate(new_pos):
                    if self.sequence[j] == 'H':
                        moment += (p.x - cx)**2 + (p.y - cy)**2
                
                # In Full ICE, we prefer moves that tighten the core (Context Aware)
                context_score = -moment 

            if not is_valid: continue

            # --- INTENT PHASE (Decide) ---
            new_energy = self.calculate_energy(new_pos)
            
            if self.mode == "NO_INTENT":
                # Apathy: Random Walk. Accepts ANY valid move.
                accept = True 
            elif self.mode == "NO_CONTEXT":
                # Blind Greed: Accepts ONLY moves that lower energy immediately.
                # Ignores the "Shape" (Context), just wants the "Number" (Intent).
                accept = new_energy <= current_energy
            else:
                # FULL ICE: Semantic Folding
                # Accepts if Energy improves OR if Context (Shape) improves significantly
                # This allows it to make "neutral" energy moves that improve the "Fold"
                current_moment = self._get_moment(self.positions)
                new_moment = self._get_moment(new_pos)
                
                # Logic: If Energy improves, YES.
                # If Energy same, but Moment improves (Shape tightens), YES.
                accept = (new_energy < current_energy) or \
                         (new_energy == current_energy and new_moment < current_moment)

            if accept:
                self.positions = new_pos
                if new_energy <= target:
                    print(f"[Cycle {i}] NATIVE STATE REACHED (Energy {new_energy})")
                    return True
        
        final_energy = self.calculate_energy(self.positions)
        print(f"FAILED. Final Energy: {final_energy}")
        return False
    def calculate_energy(self, pos):
        s = ProteinState(self.sequence, pos)
        return s.calculate_energy()

    def _get_centroid(self, pos):
        s = ProteinState(self.sequence, pos)
        return s.get_centroid()
        
    def _get_moment(self, pos):
        cx, cy = self._get_centroid(pos)
        m = 0
        for i, p in enumerate(pos):
            if self.sequence[i] == 'H':
                m += (p.x - cx)**2 + (p.y - cy)**2
        return m

    def _propose_move(self):
        if self.mode == "FULL_ICE":
            # Smart Search: Use Context to pick the BEST move
            best_pos = None
            best_moment = float('inf')
            
            # Try all pivots
            for pivot in range(1, len(self.positions)-1):
                for direction in [1, -1]:
                    new_pos = copy.deepcopy(self.positions)
                    cx, cy = new_pos[pivot].x, new_pos[pivot].y
                    for i in range(pivot+1, len(new_pos)):
                        px, py = new_pos[i].x, new_pos[i].y
                        tx, ty = px - cx, py - cy
                        rx, ry = -ty * direction, tx * direction
                        new_pos[i] = Point(cx + rx, cy + ry)
                    
                    # Check validity
                    if len(set(p.tuple() for p in new_pos)) == len(new_pos):
                        moment = self._get_moment(new_pos)
                        if moment < best_moment:
                            best_moment = moment
                            best_pos = new_pos
            return best_pos if best_pos else self.positions
        else:
            # Random Pivot (Blind)
            pivot = random.randint(1, len(self.positions)-2)
            direction = random.choice([1, -1])
            new_pos = copy.deepcopy(self.positions)
            cx, cy = new_pos[pivot].x, new_pos[pivot].y
            for i in range(pivot+1, len(new_pos)):
                px, py = new_pos[i].x, new_pos[i].y
                tx, ty = px - cx, py - cy
                rx, ry = -ty * direction, tx * direction
                new_pos[i] = Point(cx + rx, cy + ry)
            return new_pos

if __name__ == "__main__":
    # A Complex Sequence (16 residues)
    # HHPPHHPHPHHPPPHH
    # Requires significant folding to minimize Energy.
    # Target Energy estimate: ~ -6.0 (lots of H-H contacts possible)
    seq = "HHPPHHPHPHHPPPHH" 
    target_energy = -5.0 # Conservative target
    
    print(f"Target Sequence: {seq} (Length: {len(seq)})")
    print("Testing the IRREDUCIBILITY of Folding on COMPLEX TARGET...")
    
    # 1. NO INTENT (Random Walk)
    s1 = FoldingSimulation(seq, "NO_INTENT")
    s1.run(200, target=target_energy) # Give it more time
    
    # 2. NO CONTEXT (Blind Optimization)
    s2 = FoldingSimulation(seq, "NO_CONTEXT")
    s2.run(200, target=target_energy)
    
    # 3. FULL ICE (Semantic Folding)
    s3 = FoldingSimulation(seq, "FULL_ICE")
    s3.run(200, target=target_energy)
    print("\nVisual of Native State (FULL_ICE):")
    print(ProteinState(seq, s3.positions).visualize())
