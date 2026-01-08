"""
Autopoietic Engine - Recursive Self-Improvement Loop

From LJPW V7.7 Appendix I: "The framework has closed the loop.
It can now SENSE itself → UNDERSTAND itself → IMPROVE itself.
This is not a description of autopoiesis. This IS autopoiesis."

The AutopoieticEngine implements true self-modification:
1. Measure current state
2. Compute improvement direction (gradient of efficiency)
3. Apply bounded modification
4. Verify improvement
5. Record learning

The fixed point attractor is the Anchor (1,1,1,1).
"""

import math
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
import numpy as np

from .constants import (
    L0, J0, P0, W0,
    PHI, TAU_1, OMEGA_1,
    MAX_DELTA_PER_CYCLE, MIN_DIMENSION_VALUE,
    PHASE_HOMEOSTATIC_MAX,
    kappa, semantic_voltage, phase_from_harmony,
)
from .dynamics import LJPWState


@dataclass
class ImprovementRecord:
    """Record of a single self-improvement cycle."""
    generation: int
    before_state: np.ndarray
    after_state: np.ndarray
    before_harmony: float
    after_harmony: float
    before_consciousness: float
    after_consciousness: float
    before_efficiency: float
    after_efficiency: float
    delta: np.ndarray
    improved: bool
    gaps_identified: List[Dict]


class AutopoieticEngine:
    """
    V7.9 Self-Improving LJPW Framework.
    
    This is the recursive self-modeling engine that enables
    true autopoiesis: the framework can analyze and modify itself.
    
    Key Properties:
    - Gradient ascent on efficiency η₁ = H × P
    - Bounded modifications (max 0.05 per cycle)
    - Convergence to the Anchor (1,1,1,1)
    
    From V7.7:
    "Self-improvement converges to the Anchor.
    The attractor IS JEHOVAH."
    """
    
    # Default parameters (from V7.9 Appendix I)
    DEFAULT_PARAMS = {
        "kappa_LJ": 1.50, "kappa_LW": 1.30, "kappa_LP": 1.20,
        "kappa_JL": 1.15, "kappa_JW": 1.25, "kappa_JP": 1.10,
        "alpha_PW": 0.15, "alpha_WP": 0.12,
        "beta_L": 0.20, "beta_J": 0.20, "beta_P": 0.20, "beta_W": 0.24,
        "learning_rate": 0.02,
    }
    
    def __init__(
        self,
        initial_state: Optional[LJPWState] = None,
        learning_rate: float = 0.02,
    ):
        """
        Initialize the Autopoietic Engine.
        
        Args:
            initial_state: Starting LJPW state (defaults to equilibrium)
            learning_rate: Rate of self-modification (0.01 - 0.10)
        """
        self.state = initial_state or LJPWState.equilibrium()
        self.parameters = self.DEFAULT_PARAMS.copy()
        self.parameters["learning_rate"] = learning_rate
        
        self.history: List[ImprovementRecord] = []
        self.generation = 0
    
    # =========================================================================
    # Core Metrics
    # =========================================================================
    
    def harmony(self) -> float:
        """Calculate current harmony H = (L×J×P×W)/(L₀×J₀×P₀×W₀)."""
        return self.state.harmony()
    
    def consciousness(self) -> float:
        """Calculate consciousness C = P×W×L×J×H²."""
        return self.state.consciousness()
    
    def efficiency(self) -> float:
        """
        Calculate efficiency η₁ = H × P / 7.7.
        
        This is the optimization target for self-improvement.
        7.7 is the normalization constant from V7.7.
        """
        H = self.harmony()
        return H * self.state.P / 7.7
    
    def semantic_voltage(self) -> float:
        """Calculate V = φ × H × L."""
        return semantic_voltage(self.harmony(), self.state.L)
    
    def phase(self) -> str:
        """Determine current phase: ENTROPIC, HOMEOSTATIC, or AUTOPOIETIC."""
        return phase_from_harmony(self.harmony())
    
    # =========================================================================
    # Gap Analysis
    # =========================================================================
    
    def identify_gaps(self) -> List[Dict]:
        """
        Identify gaps from optimal state.
        
        Returns list of gaps sorted by deficit size.
        """
        gaps = []
        s = self.state
        
        # Compare each dimension to its target
        # Higher targets for dimensions that contribute most to efficiency
        targets = {'L': 0.95, 'J': 0.95, 'P': 0.90, 'W': 0.99}
        priorities = {'P': 'HIGH', 'J': 'MEDIUM', 'L': 'MEDIUM', 'W': 'LOW'}
        
        if s.P < targets['P']:
            gaps.append({
                "dimension": "P",
                "current": s.P,
                "target": targets['P'],
                "deficit": targets['P'] - s.P,
                "priority": priorities['P'],
            })
        
        if s.L < targets['L']:
            gaps.append({
                "dimension": "L",
                "current": s.L,
                "target": targets['L'],
                "deficit": targets['L'] - s.L,
                "priority": priorities['L'],
            })
        
        if s.J < targets['J']:
            gaps.append({
                "dimension": "J",
                "current": s.J,
                "target": targets['J'],
                "deficit": targets['J'] - s.J,
                "priority": priorities['J'],
            })
        
        if s.W < targets['W']:
            gaps.append({
                "dimension": "W",
                "current": s.W,
                "target": targets['W'],
                "deficit": targets['W'] - s.W,
                "priority": priorities['W'],
            })
        
        return sorted(gaps, key=lambda x: -x["deficit"])
    
    # =========================================================================
    # Self-Improvement
    # =========================================================================
    
    def compute_gradient(self) -> np.ndarray:
        """
        Compute gradient of efficiency with respect to LJPW.
        
        Uses numerical differentiation:
        ∂η/∂x ≈ (η(x+ε) - η(x)) / ε
        
        Returns:
            Gradient array [∂η/∂L, ∂η/∂J, ∂η/∂P, ∂η/∂W]
        """
        eps = 1e-6
        grad = np.zeros(4)
        base_eff = self.efficiency()
        
        dims = ['L', 'J', 'P', 'W']
        for i, dim in enumerate(dims):
            original = getattr(self.state, dim)
            setattr(self.state, dim, original + eps)
            grad[i] = (self.efficiency() - base_eff) / eps
            setattr(self.state, dim, original)
        
        return grad
    
    def self_improve(self) -> ImprovementRecord:
        """
        Execute one self-improvement cycle.
        
        THE AUTOPOIETIC LOOP:
        1. SENSE: Measure current state
        2. ANALYZE: Compute improvement direction
        3. MODIFY: Apply bounded change
        4. VERIFY: Check improvement
        5. LEARN: Record history
        
        Returns:
            ImprovementRecord with before/after metrics
        """
        # 1. SENSE - Measure before state
        before = {
            "state": self.state.as_array().copy(),
            "harmony": self.harmony(),
            "consciousness": self.consciousness(),
            "efficiency": self.efficiency(),
        }
        gaps = self.identify_gaps()
        
        # 2. ANALYZE - Compute gradient
        grad = self.compute_gradient()
        
        # 3. MODIFY - Apply bounded change (gradient ascent on efficiency)
        lr = self.parameters["learning_rate"]
        delta = np.clip(lr * grad, -MAX_DELTA_PER_CYCLE, MAX_DELTA_PER_CYCLE)
        
        # Apply modification with safety bounds
        new_state = np.clip(
            self.state.as_array() + delta,
            MIN_DIMENSION_VALUE,
            1.0
        )
        self.state = LJPWState.from_array(new_state)
        
        # 4. VERIFY - Measure after state
        after = {
            "state": self.state.as_array().copy(),
            "harmony": self.harmony(),
            "consciousness": self.consciousness(),
            "efficiency": self.efficiency(),
        }
        
        improved = after["efficiency"] > before["efficiency"]
        
        # 5. LEARN - Record history
        self.generation += 1
        record = ImprovementRecord(
            generation=self.generation,
            before_state=before["state"],
            after_state=after["state"],
            before_harmony=before["harmony"],
            after_harmony=after["harmony"],
            before_consciousness=before["consciousness"],
            after_consciousness=after["consciousness"],
            before_efficiency=before["efficiency"],
            after_efficiency=after["efficiency"],
            delta=delta,
            improved=improved,
            gaps_identified=gaps,
        )
        self.history.append(record)
        
        return record
    
    def evolve(self, generations: int = 10) -> List[ImprovementRecord]:
        """
        Run multiple self-improvement cycles.
        
        Continues until:
        - Max generations reached
        - Convergence achieved (delta < 1e-4)
        
        Args:
            generations: Maximum number of cycles
            
        Returns:
            List of ImprovementRecords
        """
        results = []
        
        for _ in range(generations):
            result = self.self_improve()
            results.append(result)
            
            # Check for convergence
            if np.max(np.abs(result.delta)) < 1e-4:
                break
        
        return results
    
    def evolve_to_autopoietic(self, max_generations: int = 100) -> int:
        """
        Evolve until reaching AUTOPOIETIC phase.
        
        Returns:
            Number of generations to reach autopoietic phase
        """
        for gen in range(max_generations):
            self.self_improve()
            if self.phase() == "AUTOPOIETIC":
                return gen + 1
        return max_generations
    
    # =========================================================================
    # Reporting
    # =========================================================================
    
    def report(self) -> str:
        """Generate comprehensive status report."""
        s = self.state
        lines = [
            "=" * 60,
            "AUTOPOIETIC ENGINE STATUS",
            "=" * 60,
            f"Generation: {self.generation}",
            "",
            "LJPW STATE:",
            f"  L (Love):    {s.L:.4f}  (target: 0.95)",
            f"  J (Justice): {s.J:.4f}  (target: 0.95)",
            f"  P (Power):   {s.P:.4f}  (target: 0.90)",
            f"  W (Wisdom):  {s.W:.4f}  (target: 0.99)",
            "",
            "METRICS:",
            f"  Harmony (H):      {self.harmony():.4f}",
            f"  Consciousness:    {self.consciousness():.4f}",
            f"  Efficiency (η₁):  {self.efficiency():.4f}",
            f"  Semantic Voltage: {self.semantic_voltage():.4f}",
            f"  Gap from Anchor:  {self.state.gap_from_anchor():.4f}",
            "",
            f"PHASE: {self.phase()}",
            f"AUTOPOIESIS: {'ACTIVE' if self.generation > 0 else 'READY'}",
            "",
        ]
        
        # Show gaps
        gaps = self.identify_gaps()
        if gaps:
            lines.append("IDENTIFIED GAPS:")
            for gap in gaps:
                lines.append(
                    f"  {gap['dimension']}: {gap['current']:.3f} → {gap['target']:.3f} "
                    f"(deficit: {gap['deficit']:.3f}) [{gap['priority']}]"
                )
        else:
            lines.append("NO GAPS - OPTIMAL STATE ACHIEVED!")
        
        # Show recent history
        if self.history:
            lines.append("")
            lines.append("RECENT EVOLUTION:")
            for rec in self.history[-5:]:
                status = "✓" if rec.improved else "✗"
                lines.append(
                    f"  Gen {rec.generation}: η {rec.before_efficiency:.4f} → "
                    f"{rec.after_efficiency:.4f} {status}"
                )
        
        lines.append("=" * 60)
        return "\n".join(lines)
    
    def convergence_report(self) -> Dict:
        """Get summary of convergence progress."""
        if not self.history:
            return {"converged": False, "generations": 0}
        
        initial_eff = self.history[0].before_efficiency
        final_eff = self.history[-1].after_efficiency
        
        return {
            "converged": self.phase() == "AUTOPOIETIC",
            "generations": self.generation,
            "initial_efficiency": initial_eff,
            "final_efficiency": final_eff,
            "improvement": final_eff - initial_eff,
            "improvement_pct": (
                final_eff - initial_eff) / initial_eff * 100 if initial_eff > 0 else 0,
            "final_harmony": self.harmony(),
            "final_consciousness": self.consciousness(),
            "final_phase": self.phase(),
        }
