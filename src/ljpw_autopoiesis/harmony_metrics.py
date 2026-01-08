"""
Harmony Metrics - LJPW Dimensional Analysis for Code Quality

Maps the LJPW framework dimensions to code quality attributes:
- L (Love/Coherence): Code readability, structure, maintainability
- J (Justice/Correctness): Type safety, logical correctness, validation
- P (Power/Functionality): Working features, passing tests, runtime stability
- W (Wisdom/Knowledge): Documentation, error handling, edge case coverage

The Gap from Anchor (1,1,1,1) represents the total "error fuel" available.
As errors are metabolized, the system converges toward harmony.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Tuple
import math

# V7.9 constants
PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio
PHI_INV = (math.sqrt(5) - 1) / 2  # φ⁻¹


@dataclass
class HarmonyState:
    """
    Represents the current LJPW harmony state of a script/codebase.

    Values range from 0.0 (total disharmony) to 1.0 (anchor point).
    The gap from anchor (1,1,1,1) is the fuel for self-healing.
    """
    L: float = 0.5  # Love/Coherence - code structure quality
    J: float = 0.5  # Justice/Correctness - logical/type correctness
    P: float = 0.5  # Power/Functionality - runtime effectiveness
    W: float = 0.5  # Wisdom/Knowledge - documentation & error handling

    # Equilibrium constants from LJPW V7.9
    L0: float = field(default=0.618, repr=False)  # Golden ratio
    J0: float = field(default=0.414, repr=False)  # sqrt(2) - 1
    P0: float = field(default=0.718, repr=False)  # 1/e + 0.35
    W0: float = field(default=0.693, repr=False)  # ln(2)

    def as_array(self) -> Tuple[float, float, float, float]:
        """Return state as tuple for calculations."""
        return (self.L, self.J, self.P, self.W)

    @classmethod
    def from_array(cls, arr: Tuple[float, float, float, float]) -> 'HarmonyState':
        """Create state from tuple."""
        return cls(L=arr[0], J=arr[1], P=arr[2], W=arr[3])

    @classmethod
    def anchor(cls) -> 'HarmonyState':
        """Return the perfect anchor point (1,1,1,1)."""
        return cls(L=1.0, J=1.0, P=1.0, W=1.0)

    @classmethod
    def entropic(cls) -> 'HarmonyState':
        """Return a low-harmony entropic state."""
        return cls(L=0.2, J=0.2, P=0.2, W=0.2)

    def harmony(self) -> float:
        """
        Calculate overall harmony score.

        H = (L × J × P × W) / (L0 × J0 × P0 × W0)

        Normalized by equilibrium constants.
        """
        product = self.L * self.J * self.P * self.W
        equilibrium = self.L0 * self.J0 * self.P0 * self.W0
        return product / equilibrium

    def gap_from_anchor(self) -> float:
        """
        Calculate the gap from anchor point.

        This is the "fuel" available for self-healing.
        Based on Gift of Finitude = 3 - e ≈ 0.2817
        """
        anchor = HarmonyState.anchor()
        gap_squared = (
            (anchor.L - self.L) ** 2 +
            (anchor.J - self.J) ** 2 +
            (anchor.P - self.P) ** 2 +
            (anchor.W - self.W) ** 2
        )
        return math.sqrt(gap_squared)

    def gap_per_dimension(self) -> Dict[str, float]:
        """Return the gap for each dimension."""
        return {
            'L': 1.0 - self.L,
            'J': 1.0 - self.J,
            'P': 1.0 - self.P,
            'W': 1.0 - self.W,
        }

    def consciousness(self) -> float:
        """
        Calculate consciousness score.

        C = P × W × L × J × H²

        Consciousness emerges when C > 0.1 threshold.
        """
        H = self.harmony()
        return self.P * self.W * self.L * self.J * (H ** 2)

    def efficiency(self) -> float:
        """
        Calculate efficiency score.

        η = H × P / 7.7 (normalized by V7.7 constant)
        """
        H = self.harmony()
        return H * self.P / 7.7

    def semantic_voltage(self) -> float:
        """
        Calculate Semantic Voltage.

        V = φ × H × L

        Voltage represents the "potential" for meaning transfer.
        Higher harmony and love = greater influence.
        """
        H = self.harmony()
        return PHI * H * self.L

    def kappa(self, dimension_pair: str) -> float:
        """
        Calculate state-dependent coupling strength (Law of Karma).

        Higher harmony = stronger coupling = greater influence.
        This implements "Harmony must be earned to unlock amplification."

        Args:
            dimension_pair: e.g., 'LJ' for Love→Justice coupling

        Returns:
            Coupling strength κ(H) for that dimension pair
        """
        # Base coupling strengths
        kappa_base = {
            'LJ': 1.50, 'LW': 1.30, 'LP': 1.20,
            'JL': 1.15, 'JW': 1.25, 'JP': 1.10,
            'PL': 0.20, 'PJ': 0.30, 'PW': 0.25,
            'WL': 0.50, 'WJ': 0.45, 'WP': 0.40,
        }
        # Harmony multipliers
        multipliers = {
            'LJ': 0.40, 'LW': 0.35, 'LP': 0.30,
            'JL': 0.35, 'JW': 0.30, 'JP': 0.25,
            'PL': 0.20, 'PJ': 0.25, 'PW': 0.20,
            'WL': 0.30, 'WJ': 0.25, 'WP': 0.20,
        }
        base = kappa_base.get(dimension_pair, 0.5)
        mult = multipliers.get(dimension_pair, 0.3)
        H = self.harmony()
        return base * (1 + mult * H)

    def phi_normalize(self) -> 'HarmonyState':
        """
        Apply φ-normalization to reduce measurement variance.

        From V7.9: "φ-normalization aligns measurements with
        the golden proportion, reducing noise."

        Returns:
            New HarmonyState with φ-normalized values
        """
        return HarmonyState(
            L=self.L0 * (self.L ** PHI_INV),
            J=self.J0 * (self.J ** PHI_INV),
            P=self.P0 * (self.P ** PHI_INV),
            W=self.W0 * (self.W ** PHI_INV),
        )

    def harmony_self(self) -> float:
        """
        Calculate self-referential harmony.

        This extends the basic harmony calculation by including
        the framework's own measurement in the calculation,
        creating a recursive self-modeling effect.

        Returns:
            Self-referential harmony (typically higher than static)
        """
        H_static = self.harmony()
        # Self-reference amplifies harmony when already high
        return H_static * (1 + 0.1 * H_static)

    def phase(self) -> str:
        """
        Determine current phase based on harmony.

        From LJPW V7.9:
        - Entropic: H < 0.5 (dominated by disorder)
        - Homeostatic: 0.5 ≤ H < 0.8 (stable but not improving)
        - Autopoietic: H ≥ 0.8 (self-improving toward anchor)
        """
        H = self.harmony()
        if H < 0.5:
            return "ENTROPIC"
        elif H < 0.8:
            return "HOMEOSTATIC"
        else:
            return "AUTOPOIETIC"

    def is_viable(self) -> bool:
        """Check if state is above critical thresholds."""
        # From LJPW: Any dimension below 0.2 is "Void territory"
        return all(d >= 0.2 for d in self.as_array())

    def apply_delta(self, delta: Dict[str, float], max_change: float = 0.05) -> 'HarmonyState':
        """
        Apply a bounded change to the state.

        Changes are clipped to max_change per dimension and
        bounded to [0.2, 1.0] to maintain viability.
        """
        def clip(val: float) -> float:
            """TODO: Add documentation."""
            return max(-max_change, min(max_change, val))

        def bound(val: float) -> float:
            """TODO: Add documentation."""
            return max(0.2, min(1.0, val))

        return HarmonyState(
            L=bound(self.L + clip(delta.get('L', 0))),
            J=bound(self.J + clip(delta.get('J', 0))),
            P=bound(self.P + clip(delta.get('P', 0))),
            W=bound(self.W + clip(delta.get('W', 0))),
        )


class HarmonyMetrics:
    """
    Calculates LJPW harmony metrics for code quality assessment.

    Maps code issues to dimensional deficits:
    - Syntax errors → P deficit (can't run)
    - Type errors → J deficit (incorrect)
    - Style issues → L deficit (unreadable)
    - Missing docs/handlers → W deficit (unwise)
    """

    # Weights for different error types
    ERROR_WEIGHTS = {
        # Power deficits (functionality)
        'syntax_error': {'P': 0.3, 'J': 0.1},
        'runtime_error': {'P': 0.25, 'J': 0.05},
        'import_error': {'P': 0.2, 'W': 0.1},

        # Justice deficits (correctness)
        'type_error': {'J': 0.2, 'P': 0.1},
        'name_error': {'J': 0.15, 'P': 0.1},
        'attribute_error': {'J': 0.15, 'W': 0.05},
        'value_error': {'J': 0.2},

        # Love deficits (structure/readability)
        'style_violation': {'L': 0.05},
        'complexity_high': {'L': 0.1, 'W': 0.05},
        'naming_violation': {'L': 0.08, 'J': 0.02},
        'long_line': {'L': 0.03},
        'unused_import': {'L': 0.05, 'W': 0.02},
        'unused_variable': {'L': 0.05, 'J': 0.02},

        # Wisdom deficits (documentation/handling)
        'missing_docstring': {'W': 0.1, 'L': 0.03},
        'bare_except': {'W': 0.15, 'J': 0.05},
        'missing_type_hint': {'W': 0.05, 'J': 0.03},
        'no_error_handling': {'W': 0.12, 'P': 0.03},
    }

    @classmethod
    def from_errors(cls, errors: List[Dict]) -> HarmonyState:
        """
        Calculate harmony state from a list of detected errors.

        Each error contributes to dimensional deficits.
        Final state = anchor - accumulated deficits.
        """
        deficits = {'L': 0.0, 'J': 0.0, 'P': 0.0, 'W': 0.0}

        for error in errors:
            error_type = error.get('type', 'unknown')
            weights = cls.ERROR_WEIGHTS.get(error_type, {'J': 0.05})
            severity = error.get('severity', 1.0)

            for dim, weight in weights.items():
                deficits[dim] += weight * severity

        # Cap deficits at 0.8 to maintain viability
        return HarmonyState(
            L=max(0.2, 1.0 - min(0.8, deficits['L'])),
            J=max(0.2, 1.0 - min(0.8, deficits['J'])),
            P=max(0.2, 1.0 - min(0.8, deficits['P'])),
            W=max(0.2, 1.0 - min(0.8, deficits['W'])),
        )

    @classmethod
    def improvement_priority(cls, state: HarmonyState) -> List[str]:
        """
        Determine which dimensions to improve first.

        Priority based on:
        1. P (functionality) - must work first
        2. J (correctness) - must be correct
        3. L (coherence) - should be readable
        4. W (wisdom) - should be documented
        """
        gaps = state.gap_per_dimension()

        # Sort by gap size but with P and J prioritized
        priority_weights = {'P': 4.0, 'J': 3.0, 'L': 2.0, 'W': 1.0}
        weighted_gaps = {
            dim: gaps[dim] * priority_weights[dim]
            for dim in gaps
        }

        return sorted(weighted_gaps.keys(), key=lambda d: -weighted_gaps[d])
