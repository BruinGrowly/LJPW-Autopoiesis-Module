"""
LJPW Framework V8.3 Constants

All constants are semantically derived from first principles, not arbitrary values.
This module centralizes the mathematical constants that underpin the LJPW framework.

From V7.9: "These are not free parameters — they are mathematically determined
by the semantic structure of reality itself."

V8.0 Additions: Geometry of Meaning — M = κ = |dT/ds|
V8.1 Additions: Dynamics of Love — Semantic Conductivity, Love as Fuel
V8.2 Additions: Ransom Theology — Singularity Detection, Physics of Remembrance
V8.3 Additions: Physics of Failure — Cost vs Debt, Injection Vector, Diode Status

V8.3 Self-Analysis: C = 75+, Coherence = 0.95+ (THEOLOGICAL DEBUG COMPLETE)
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


# =============================================================================
# V8.0: GEOMETRY OF MEANING CONSTANTS
# =============================================================================
# From V8.0: "Meaning IS curvature. M = κ = |dT/ds|"

CURVATURE_EPSILON = 1e-6  # Minimum step for curvature calculation
CURVATURE_SIGNIFICANCE_THRESHOLD = 0.1  # κ > 0.1 indicates meaningful content


# =============================================================================
# V8.1: DYNAMICS OF LOVE CONSTANTS
# =============================================================================
# From V8.1: "Love is the superconductor of truth."

# Semantic Conductivity: σ = L × H²
# High σ: Truth flows without resistance
# Low σ: Truth encounters friction (burnout)

# Potential Energy: E = L × φ × d
# Love (L) is the "mass", Distance (d) is the "height"


# =============================================================================
# V8.2: RANSOM THEOLOGY CONSTANTS
# =============================================================================
# From V8.2: "The Ransom is the Singularity that prevents reality from dividing by zero."

ANCHOR_POINT = (1.0, 1.0, 1.0, 1.0)  # Perfect Harmony — JEHOVAH
UNCERTAINTY_THRESHOLD = 0.287  # ΔP · ΔW ≥ 0.287

# Void of Mercy coordinates (Forgiveness on Principle)
VOID_OF_MERCY = {'L': 1.0, 'J': 1.0, 'P': 0.6, 'W': 0.6}

# Entropic drift parameters
DEFAULT_DRIFT_RATE = 0.6  # Drift rate per year without calibration
REMEMBRANCE_REALIGNMENT_H = 0.96  # Harmony after remembrance calibration


# =============================================================================
# V8.3: PHYSICS OF FAILURE CONSTANTS
# =============================================================================
# From V8.3: "Cost is not Debt. Finitude is not Sin."

# Diode status constants
KAPPA_JUSTICE_IDEAL = 1.0  # Ideal J coupling coefficient
DIODE_TOLERANCE = 0.1  # Tolerance for diode status check

# System states
class SystemState:
    """Pre-Fall vs Post-Fall system states."""
    PRE_FALL = "PRE_FALL"    # Open-Circuit Autopoiesis (Return Path open)
    POST_FALL = "POST_FALL"  # Closed Diode (Debt accumulation)


# =============================================================================
# V8.0 HELPER FUNCTIONS
# =============================================================================

def curvature_significance(kappa: float) -> str:
    """
    Determine significance of curvature value.
    
    Args:
        kappa: Curvature value (meaning density)
    
    Returns:
        'HIGH', 'MODERATE', 'LOW', or 'FLATLINE'
    """
    if kappa > 0.5:
        return "HIGH"
    elif kappa > CURVATURE_SIGNIFICANCE_THRESHOLD:
        return "MODERATE"
    elif kappa > 0.01:
        return "LOW"
    else:
        return "FLATLINE"


# =============================================================================
# V8.1 HELPER FUNCTIONS
# =============================================================================

def semantic_conductivity(love: float, harmony: float) -> float:
    """
    Calculate Semantic Conductivity (σ).
    
    σ = L × H²
    
    High σ: Truth flows without resistance (superconductivity)
    Low σ: Truth encounters friction, generates "heat" (burnout)
    
    Args:
        love: Love value [0, 1.414]
        harmony: Harmony value (self-referential)
    
    Returns:
        σ = L × H² (conductivity)
    """
    return love * harmony ** 2


def semantic_friction(love: float, harmony: float) -> float:
    """
    Calculate Semantic Friction (1/σ).
    
    Low L or low H = High Friction (Suffering)
    
    Args:
        love: Love value
        harmony: Harmony value
    
    Returns:
        Friction = 1/σ (capped at 1000.0 for near-zero conductivity)
    """
    sigma = semantic_conductivity(love, harmony)
    if sigma < 0.001:
        return 1000.0  # System near collapse
    return 1.0 / sigma


def potential_energy(love: float, distance: float) -> float:
    """
    Calculate Potential Energy from Love and Distance.
    
    E = L × φ × d
    
    Analogy: E = m × g × h (mass × gravity × height)
    Love is the "mass", φ is the "gravity", Distance is the "height"
    
    Args:
        love: Love (the "mass")
        distance: Distance from Anchor
    
    Returns:
        E = L × φ × d
    """
    return love * PHI * distance


def distance_to_anchor(L: float, J: float, P: float, W: float) -> float:
    """
    Calculate Euclidean distance from Anchor Point (1,1,1,1).
    
    Args:
        L, J, P, W: LJPW coordinates
    
    Returns:
        Distance to Anchor
    """
    return math.sqrt(
        (L - ANCHOR_POINT[0])**2 +
        (J - ANCHOR_POINT[1])**2 +
        (P - ANCHOR_POINT[2])**2 +
        (W - ANCHOR_POINT[3])**2
    )


# =============================================================================
# V8.2 HELPER FUNCTIONS
# =============================================================================

def is_singularity(L: float, J: float, P: float, W: float) -> dict:
    """
    Detect if an event is the Ransom Singularity.
    
    The Ransom is the ONLY event that maps to (1,1,1,1),
    violating the Semantic Uncertainty Principle (ΔP · ΔW ≥ 0.287).
    
    Args:
        L, J, P, W: LJPW coordinates
    
    Returns:
        Dictionary with distance, singularity status, and verdict
    """
    distance = distance_to_anchor(L, J, P, W)
    
    # Check if Uncertainty Principle is violated
    delta_P = 1.0 - P
    delta_W = 1.0 - W
    uncertainty_product = delta_P * delta_W
    
    is_sing = (distance < 0.001 and uncertainty_product < UNCERTAINTY_THRESHOLD)
    
    return {
        "distance_to_anchor": distance,
        "is_singularity": is_sing,
        "breaks_uncertainty": uncertainty_product < UNCERTAINTY_THRESHOLD,
        "verdict": "RANSOM SINGULARITY DETECTED" if is_sing else "Not singular"
    }


def remembrance_voltage(harmony: float, love: float) -> dict:
    """
    Calculate Semantic Voltage generated by active remembrance.
    
    V = φ × H × L
    
    Active remembrance triggers a voltage surge for soul calibration.
    
    Args:
        harmony: Current harmony value
        love: Current love value
    
    Returns:
        Dictionary with voltage and interpretation
    """
    voltage = semantic_voltage(harmony, love)
    
    return {
        "voltage": voltage,
        "sufficient_for_year": voltage > 1.5,
        "interpretation": "SURGE DETECTED" if voltage > 1.5 else "Moderate"
    }


def simulate_drift(initial_drift: float = 0.1,
                   years: float = 1.0,
                   drift_rate: float = DEFAULT_DRIFT_RATE) -> dict:
    """
    Simulate entropic drift without calibration.
    
    Without remembrance/calibration, a soul's frequency drifts out of phase.
    
    Args:
        initial_drift: Starting drift value
        years: Time period
        drift_rate: Rate of drift per year
    
    Returns:
        Final drift, harmony impact, and phase
    """
    final_drift = initial_drift + (drift_rate * years)
    final_harmony = max(0.3, 1.0 - final_drift)
    
    if final_harmony < PHASE_ENTROPIC_MAX:
        phase = "ENTROPIC"
    elif final_harmony < PHASE_HOMEOSTATIC_MAX:
        phase = "HOMEOSTATIC"
    else:
        phase = "AUTOPOIETIC"
    
    return {
        "initial_drift": initial_drift,
        "final_drift": min(1.0, final_drift),
        "harmony": final_harmony,
        "phase": phase,
        "needs_calibration": final_drift > 0.3
    }


# =============================================================================
# V8.3 HELPER FUNCTIONS
# =============================================================================

def is_diode_open(J_out: float, P_action: float) -> bool:
    """
    Check if the Return Path (Justice Diode) is open.
    
    In Pre-Fall state: Diode is open, J flows freely
    In Post-Fall state: Diode is closed, debt accumulates
    
    Args:
        J_out: Justice output (acknowledgment of Source)
        P_action: Power output (action taken)
    
    Returns:
        True if Return Path is functional, False if blocked (Sin condition)
    """
    expected_J = P_action * KAPPA_JUSTICE_IDEAL
    return abs(J_out - expected_J) < DIODE_TOLERANCE


def calculate_debt(P: float, time_steps: int, diode_open: bool = True) -> float:
    """
    Calculate accumulated Justice Debt over time.
    
    Cost (impedance) vs Debt (static):
    - If diode open: No debt accumulates (Cost is discharged normally)
    - If diode closed: Debt = integral of P over time
    
    Args:
        P: Power output per tick
        time_steps: Number of action cycles
        diode_open: True = Pre-Fall (Return Path open), False = Post-Fall (blocked)
    
    Returns:
        Accumulated debt (0 if diode open, linear accumulation if closed)
    """
    if diode_open:
        return 0.0  # No debt accumulates when Return Path is open
    else:
        return P * time_steps  # Q_debt = integral of P over time


def classify_cost_vs_debt(value: float, diode_open: bool) -> dict:
    """
    Classify whether a value represents Cost or Debt (V8.3 Critical Distinction).
    
    Cost of Existence: Design (3-e gap), structural impedance, GOOD
    Justice Debt: Injection (Diode Reversal), static accumulation, BAD
    
    Args:
        value: The impedance/charge value
        diode_open: Whether the Return Path is functional
    
    Returns:
        Classification with type, quality, and explanation
    """
    if diode_open:
        return {
            "type": "COST",
            "quality": "GOOD",
            "origin": "Design (Gift of Finitude)",
            "explanation": "Friction that enables 'grip' on reality. Necessary for work."
        }
    else:
        return {
            "type": "DEBT",
            "quality": "BAD",
            "origin": "Injection (Diode Reversal)",
            "explanation": "Charge with no return path. Destructive heat. Requires intervention."
        }


def get_system_state(diode_open: bool) -> str:
    """
    Determine system state based on diode status.
    
    Args:
        diode_open: Whether the Return Path is functional
    
    Returns:
        SystemState.PRE_FALL or SystemState.POST_FALL
    """
    return SystemState.PRE_FALL if diode_open else SystemState.POST_FALL
