"""
Love Dynamics Module (V8.1)

From the LJPW Framework V8.1: "Dynamics of Love"

This module implements the dynamic properties of Love:
1. Semantic Conductivity: σ = L × H² — Love is the superconductor of truth
2. Potential Energy: E = L × φ × d — Love as Fuel, Distance as Battery
3. J/W Oscillation: Justice and Wisdom oscillate in anti-phase to power Love's breath

Key Insights:
- "High Love delivers 3.9× more effective work than Low Love"
- "Without Love, distance is just emptiness. With Love, distance becomes Potential."
- "The Gap is not Loss. The Gap is Gift."

The Battery Model:
- Positive Terminal: Anchor Point (1,1,1,1)
- Negative Terminal: Natural Equilibrium
- Potential Difference: Distance (d)
- Electrolyte: Love (L)
- Current: The Tick
- Work Output: Consciousness, Learning, Structure
"""

from dataclasses import dataclass
from typing import Dict, Tuple, Optional
import math

from .constants import (
    L0, J0, P0, W0,
    PHI, PHI_INV,
    ANCHOR_POINT,
    semantic_conductivity,
    semantic_friction,
    potential_energy,
    distance_to_anchor,
    semantic_voltage,
)


@dataclass
class ConductivityMetrics:
    """Result of semantic conductivity analysis."""
    conductivity: float     # σ = L × H²
    friction: float         # 1/σ
    effective_flux: float   # How much work can actually flow
    interpretation: str     # "SUPERCONDUCTOR", "NORMAL", "HIGH_FRICTION", "COLLAPSE"


@dataclass
class EnergyMetrics:
    """Result of potential energy analysis."""
    potential_energy: float     # E = L × φ × d
    distance_from_anchor: float # d
    love_mass: float            # L (the "mass")
    voltage: float              # V = φ × H × L
    can_do_work: bool           # Whether system has potential to act


@dataclass
class OscillationState:
    """State of the J/W oscillation engine."""
    phase: str              # "INHALE" (J-dominant) or "EXHALE" (W-dominant)
    j_value: float          # Current Justice
    w_value: float          # Current Wisdom
    jw_difference: float    # J - W
    love_masked: bool       # Whether L is masking the oscillation (L > 0.95)


class SemanticConductivityEngine:
    """
    σ = L × H² — Love is the superconductor of truth.
    
    High σ: Truth flows without resistance (superconductivity)
    Low σ: Truth encounters friction, generates "heat" (burnout)
    
    "To increase Wisdom (W) or Justice (J), the most efficient path 
    is to first increase Love (L)."
    """
    
    SUPERCONDUCTOR_THRESHOLD = 0.5   # σ > 0.5 = superconducting
    NORMAL_THRESHOLD = 0.1           # σ > 0.1 = normal conductivity
    COLLAPSE_THRESHOLD = 0.01        # σ < 0.01 = near collapse
    
    def analyze(self, love: float, harmony: float) -> ConductivityMetrics:
        """
        Analyze semantic conductivity of a system.
        
        Args:
            love: Love value [0, 1.414]
            harmony: Harmony value (self-referential)
        
        Returns:
            ConductivityMetrics with all derived values
        """
        sigma = semantic_conductivity(love, harmony)
        friction = semantic_friction(love, harmony)
        
        # Effective flux = σ × base flow rate (normalized to 1)
        effective_flux = min(sigma, 1.0)
        
        # Interpretation
        if sigma > self.SUPERCONDUCTOR_THRESHOLD:
            interpretation = "SUPERCONDUCTOR"
        elif sigma > self.NORMAL_THRESHOLD:
            interpretation = "NORMAL"
        elif sigma > self.COLLAPSE_THRESHOLD:
            interpretation = "HIGH_FRICTION"
        else:
            interpretation = "COLLAPSE"
        
        return ConductivityMetrics(
            conductivity=sigma,
            friction=friction,
            effective_flux=effective_flux,
            interpretation=interpretation
        )
    
    def compare_scenarios(self, 
                          low_love: float = 0.30,
                          low_harmony: float = 0.30,
                          high_love: float = 0.95,
                          high_harmony: float = 0.80) -> Dict:
        """
        Compare low-love vs high-love scenarios.
        
        Demonstrates the 3.9× multiplier effect of Love.
        
        Returns:
            Comparison dictionary with ratio
        """
        low = self.analyze(low_love, low_harmony)
        high = self.analyze(high_love, high_harmony)
        
        ratio = high.conductivity / low.conductivity if low.conductivity > 0 else float('inf')
        
        return {
            "low_love_scenario": {
                "L": low_love,
                "H": low_harmony,
                "sigma": low.conductivity,
                "interpretation": low.interpretation
            },
            "high_love_scenario": {
                "L": high_love,
                "H": high_harmony,
                "sigma": high.conductivity,
                "interpretation": high.interpretation
            },
            "effectiveness_ratio": ratio,
            "conclusion": f"High Love delivers {ratio:.1f}× more effective work"
        }


class PotentialEnergyCalculator:
    """
    E = L × φ × d — Love as Fuel, Distance as Battery.
    
    "The 'Fall' (separation from the Source) was not a punishment.
    It was the installation of the battery."
    
    The Cosmic Battery:
    - Positive Terminal: Anchor (1,1,1,1)
    - Negative Terminal: Natural Equilibrium
    - Potential Difference: Distance (d)
    - Electrolyte: Love (L) — the medium that carries charge
    """
    
    def calculate(self, 
                  L: float, J: float, P: float, W: float,
                  harmony: Optional[float] = None) -> EnergyMetrics:
        """
        Calculate potential energy of an LJPW state.
        
        Args:
            L, J, P, W: LJPW coordinates
            harmony: Pre-calculated harmony (optional)
        
        Returns:
            EnergyMetrics with all derived values
        """
        d = distance_to_anchor(L, J, P, W)
        E = potential_energy(L, d)
        
        if harmony is None:
            harmony = (L * J * P * W) / (L0 * J0 * P0 * W0)
        
        V = semantic_voltage(harmony, L)
        
        return EnergyMetrics(
            potential_energy=E,
            distance_from_anchor=d,
            love_mass=L,
            voltage=V,
            can_do_work=(E > 0.1 and L > 0.3)
        )
    
    def compare_unity_vs_finitude(self) -> Dict:
        """
        Compare energy states: near Anchor vs finite existence.
        
        Demonstrates why separation enables work.
        
        Returns:
            Comparison showing energy difference
        """
        # Near Anchor (Unity)
        near = self.calculate(0.99, 0.99, 0.99, 0.99)
        
        # Finite Existence
        finite = self.calculate(0.75, 0.50, 0.70, 0.65)
        
        ratio = finite.potential_energy / near.potential_energy if near.potential_energy > 0 else float('inf')
        
        return {
            "near_anchor": {
                "L": 0.99,
                "distance": near.distance_from_anchor,
                "potential_energy": near.potential_energy,
                "can_do_work": near.can_do_work
            },
            "finite_existence": {
                "L": 0.75,
                "distance": finite.distance_from_anchor,
                "potential_energy": finite.potential_energy,
                "can_do_work": finite.can_do_work
            },
            "energy_ratio": ratio,
            "conclusion": f"Being 'separate' creates +{(ratio-1)*100:.0f}% more Potential Energy"
        }


class JWOscillator:
    """
    J/W Oscillation — Love's Breath Engine.
    
    "Justice and Wisdom oscillate in anti-phase to power Love's breath."
    
    - INHALE (Gravity): J-dominant, structure-building
    - EXHALE (Dark Energy): W-dominant, space-making
    
    The oscillation is FORCED by the P-W Uncertainty Principle:
    ΔP · ΔW ≥ 0.287
    """
    
    # Typical phase coordinates
    INHALE_GRAVITY = {'L': 0.95, 'J': 0.85, 'W': 0.82}
    EXHALE_DARK_ENERGY = {'L': 0.98, 'J': 0.80, 'W': 0.85}
    
    LOVE_MASK_THRESHOLD = 0.95  # L > 0.95 masks the internal oscillation
    
    def analyze_phase(self, J: float, W: float, L: float = 0.9) -> OscillationState:
        """
        Analyze current phase of J/W oscillation.
        
        Args:
            J: Justice value
            W: Wisdom value
            L: Love value (for mask detection)
        
        Returns:
            OscillationState with phase information
        """
        jw_diff = J - W
        
        if jw_diff > 0:
            phase = "INHALE"  # Gravity, J-dominant
        else:
            phase = "EXHALE"  # Dark Energy, W-dominant
        
        love_masked = L > self.LOVE_MASK_THRESHOLD
        
        return OscillationState(
            phase=phase,
            j_value=J,
            w_value=W,
            jw_difference=jw_diff,
            love_masked=love_masked
        )
    
    def oscillation_step(self, 
                          J: float, W: float, 
                          dt: float = 0.1,
                          omega: float = 0.314) -> Tuple[float, float]:
        """
        Simulate one step of J/W oscillation.
        
        Uses coupled oscillator dynamics forced by P-W uncertainty.
        
        Args:
            J: Current Justice
            W: Current Wisdom
            dt: Time step
            omega: Angular frequency (default: π/10)
        
        Returns:
            (new_J, new_W) after oscillation step
        """
        # Simple harmonic oscillation around equilibrium
        # J and W oscillate in anti-phase
        
        J_eq = J0
        W_eq = W0
        
        # Deviation from equilibrium
        dJ = J - J_eq
        dW = W - W_eq
        
        # Anti-phase coupling: when J rises, W falls
        new_dJ = dJ * math.cos(omega * dt) - dW * math.sin(omega * dt) * 0.3
        new_dW = dW * math.cos(omega * dt) + dJ * math.sin(omega * dt) * 0.3
        
        # Add back equilibrium
        new_J = max(0.2, min(1.0, J_eq + new_dJ))
        new_W = max(0.2, min(1.0, W_eq + new_dW))
        
        return new_J, new_W
    
    def analyze_jw_oscillation(self,
                                j_inhale: float, w_inhale: float,
                                j_exhale: float, w_exhale: float) -> Dict:
        """
        Analyze J/W phase shift between Inhale and Exhale.
        
        Args:
            j_inhale: Justice during inhale
            w_inhale: Wisdom during inhale
            j_exhale: Justice during exhale
            w_exhale: Wisdom during exhale
        
        Returns:
            Analysis of the oscillation pattern
        """
        return {
            "j_swing": j_inhale - j_exhale,
            "w_swing": w_inhale - w_exhale,
            "inhale_phase": "J-dominant" if j_inhale > w_inhale else "W-dominant",
            "exhale_phase": "J-dominant" if j_exhale > w_exhale else "W-dominant",
            "oscillation_confirmed": (j_inhale > w_inhale) != (j_exhale > w_exhale),
            "interpretation": "J and W oscillate in anti-phase to power Love's breath"
        }


# Convenience functions

def analyze_conductivity(love: float, harmony: float) -> ConductivityMetrics:
    """Analyze semantic conductivity of a system."""
    engine = SemanticConductivityEngine()
    return engine.analyze(love, harmony)


def calculate_potential(L: float, J: float, P: float, W: float) -> EnergyMetrics:
    """Calculate potential energy of an LJPW state."""
    calc = PotentialEnergyCalculator()
    return calc.calculate(L, J, P, W)


def analyze_breath_phase(J: float, W: float, L: float = 0.9) -> OscillationState:
    """Analyze current phase of Love's breath (J/W oscillation)."""
    osc = JWOscillator()
    return osc.analyze_phase(J, W, L)
