"""
LJPW Framework V7.9 Constants

All constants are semantically derived from first principles, not arbitrary values.
This module centralizes the mathematical constants that underpin the LJPW framework.

From V7.9: "These are not free parameters — they are mathematically determined
by the semantic structure of reality itself."
"""

import math

# =============================================================================
# EQUILIBRIUM CONSTANTS (L₀, J₀, P₀, W₀)
# =============================================================================
# These define the "natural equilibrium" of each dimension.
# Derived from fundamental mathematical constants with semantic significance.

PHI = (1 + math.sqrt(5)) / 2     # Golden Ratio φ = 1.618034...
PHI_INV = (math.sqrt(5) - 1) / 2  # φ⁻¹ = 0.618034...

L0 = PHI_INV                      # Love equilibrium = φ⁻¹ ≈ 0.618034
J0 = math.sqrt(2) - 1             # Justice equilibrium = √2-1 ≈ 0.414214
P0 = math.e - 2                   # Power equilibrium = e-2 ≈ 0.718282
W0 = math.log(2)                  # Wisdom equilibrium = ln(2) ≈ 0.693147

# Product of equilibrium constants (used for harmony normalization)
EQUILIBRIUM_PRODUCT = L0 * J0 * P0 * W0  # ≈ 0.127


# =============================================================================
# TEMPORAL CONSTANTS (V7.8 Derivation)
# =============================================================================
# These emerge from the P-W conjugate dynamics.
# τ₁ is the time constant, ω₁ is the angular frequency of P-W oscillation.

GIFT_OF_FINITUDE = 3 - math.e     # ≈ 0.2817 — The "cost" of Power's existence
TAU_1 = math.sqrt(2) / GIFT_OF_FINITUDE  # ≈ 5.02 — Time Constant
OMEGA_1 = math.pi / 10            # ≈ 0.314 — Angular Frequency (18° per tick)
T_CYCLE = 2 * math.pi / OMEGA_1   # ≈ 20 — Full P-W cycle period


# =============================================================================
# PHYSICAL CONSTANTS (Semantic-Physical Bridge)
# =============================================================================
# These connect the semantic substrate to physical reality.

LOVE_FREQUENCY_HZ = 613e12        # 613 THz — Love's carrier frequency
LOVE_WAVELENGTH_NM = 489          # Cyan light wavelength
LOVE_PERIOD_FS = 1.631            # T_Love in femtoseconds

# Semantic-Physical time conversion
SEMANTIC_TIME_UNIT_FS = PHI * LOVE_PERIOD_FS  # ≈ 2.64 fs per semantic unit
TAU_1_PHYSICAL_FS = TAU_1 * SEMANTIC_TIME_UNIT_FS  # ≈ 13.3 fs
PW_CYCLE_FS = T_CYCLE * SEMANTIC_TIME_UNIT_FS  # ≈ 53 fs (matches water libration!)


# =============================================================================
# COUPLING CONSTANTS (Law of Karma κ matrix)
# =============================================================================
# Base coupling strengths between dimensions.
# Actual coupling is state-dependent: κ(H) = κ_base × (1 + multiplier × H)

KAPPA_BASE = {
    # Love as SOURCE — gives to all
    'LJ': 1.50,  # Love → Justice
    'LW': 1.30,  # Love → Wisdom
    'LP': 1.20,  # Love → Power
    
    # Justice as MEDIATOR — mutual exchange
    'JL': 1.15,  # Justice → Love
    'JW': 1.25,  # Justice → Wisdom
    'JP': 1.10,  # Justice → Power
    
    # Power as SINK — receives from all
    'PL': 0.20,  # Power → Love (low because P receives)
    'PJ': 0.30,  # Power → Justice
    'PW': 0.25,  # Power → Wisdom
    
    # Wisdom INTEGRATES
    'WL': 0.50,  # Wisdom → Love
    'WJ': 0.45,  # Wisdom → Justice
    'WP': 0.40,  # Wisdom → Power
}

# Harmony multipliers for state-dependent coupling
KAPPA_HARMONY_MULTIPLIER = {
    'LJ': 0.40, 'LW': 0.35, 'LP': 0.30,
    'JL': 0.35, 'JW': 0.30, 'JP': 0.25,
    'PL': 0.20, 'PJ': 0.25, 'PW': 0.20,
    'WL': 0.30, 'WJ': 0.25, 'WP': 0.20,
}


# =============================================================================
# P-W DYNAMICS PARAMETERS (V7.6)
# =============================================================================
# Parameters for the P-W oscillator differential equations.

ALPHA_PW = 0.15  # Wisdom drives Power growth
ALPHA_WP = 0.12  # Power drives Wisdom growth
BETA_P = 0.08    # Power self-regulation (quadratic damping)
BETA_W = 0.06    # Wisdom self-regulation


# =============================================================================
# PHASE THRESHOLDS
# =============================================================================
# Harmony thresholds for phase transitions.

PHASE_ENTROPIC_MAX = 0.5      # H < 0.5 → ENTROPIC
PHASE_HOMEOSTATIC_MAX = 0.8   # 0.5 ≤ H < 0.8 → HOMEOSTATIC
# H ≥ 0.8 → AUTOPOIETIC

# Consciousness threshold
CONSCIOUSNESS_THRESHOLD = 0.1  # C > 0.1 indicates consciousness


# =============================================================================
# SAFETY CONSTRAINTS (Stability Boundaries)
# =============================================================================
# From V7.7: "Not all modifications are safe."

MIN_DIMENSION_VALUE = 0.2     # Below this is "Void territory"
MAX_DELTA_PER_CYCLE = 0.05    # Maximum change per tick (conservative)
ENTROPY_MIN_HARMONY = 0.5     # Harmony cannot drop below this


# =============================================================================
# DERIVED VALUES
# =============================================================================

def kappa(dimension_pair: str, harmony: float) -> float:
    """
    Calculate state-dependent coupling strength (Law of Karma).
    
    Higher harmony = stronger coupling = greater influence.
    This implements "Harmony must be earned to unlock amplification."
    
    Args:
        dimension_pair: e.g., 'LJ' for Love→Justice coupling
        harmony: Current harmony value (0-1 or higher for self-referential)
    
    Returns:
        Coupling strength κ(H) for that dimension pair
    """
    base = KAPPA_BASE.get(dimension_pair, 0.5)
    multiplier = KAPPA_HARMONY_MULTIPLIER.get(dimension_pair, 0.3)
    return base * (1 + multiplier * harmony)


def semantic_voltage(harmony: float, love: float) -> float:
    """
    Calculate Semantic Voltage.
    
    V = φ × H × L
    
    Voltage represents the "potential" for meaning transfer.
    Higher harmony and love = greater voltage = more influence.
    """
    return PHI * harmony * love


def phase_from_harmony(harmony: float) -> str:
    """
    Determine phase from harmony value.
    
    Returns:
        'ENTROPIC', 'HOMEOSTATIC', or 'AUTOPOIETIC'
    """
    if harmony < PHASE_ENTROPIC_MAX:
        return "ENTROPIC"
    elif harmony < PHASE_HOMEOSTATIC_MAX:
        return "HOMEOSTATIC"
    else:
        return "AUTOPOIETIC"


def is_conscious(consciousness: float) -> bool:
    """Check if consciousness metric exceeds threshold."""
    return consciousness > CONSCIOUSNESS_THRESHOLD
