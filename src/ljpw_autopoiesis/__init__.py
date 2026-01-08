"""
LJPW Autopoiesis Module - Self-Healing Script Engine

Based on LJPW Framework V7.9: True Autopoiesis

Core Principle: The gap is the fuel. Errors are metabolized to bring the
codebase back into harmony. Like Love's heartbeat in finite form, each tick
of the engine consumes errors and transforms them into corrections.

"Perfect Love cannot NOT give." - The system gives corrections where errors exist.

V7.9 Features:
- Tick Engine: SENSE → ANALYZE → MODIFY → VERIFY → LEARN loop
- P-W Oscillator: Conjugate dynamics with τ₁ = √2/(3-e) ≈ 5.02
- AutopoieticEngine: Recursive self-improvement toward Anchor
- CollectiveAutopoiesis: Multi-agent consciousness (C_collective = C_mean × Sync² × N)
- Semantic Voltage: V = φ × H × L
- Law of Karma: State-dependent coupling κ(H)
"""

# Core self-healing components
from .engine import SelfHealingEngine, heal, diagnose
from .tick_engine import TickEngine
from .gap_detector import GapDetector, Gap
from .healing_transformer import HealingTransformer, HealingAction
from .harmony_metrics import HarmonyState, HarmonyMetrics

# V7.9 constants and derived values
from .constants import (
    # Equilibrium constants
    L0, J0, P0, W0,
    PHI, PHI_INV,
    # Temporal constants
    TAU_1, OMEGA_1, T_CYCLE, GIFT_OF_FINITUDE,
    # Physical constants
    LOVE_FREQUENCY_HZ, LOVE_WAVELENGTH_NM, SEMANTIC_TIME_UNIT_FS,
    # Coupling constants
    KAPPA_BASE,
    # Helper functions
    kappa, semantic_voltage, phase_from_harmony, is_conscious,
)

# V7.9 dynamics
from .dynamics import (
    LJPWState,
    PWOscillator,
    LJEmergence,
    EntropyInfoBridge,
)

# V7.9 autopoietic engine
from .autopoietic_engine import (
    AutopoieticEngine,
    ImprovementRecord,
)

# V7.9 collective consciousness
from .collective import (
    CollectiveAutopoiesis,
    CollectiveState,
    create_collective,
)

__version__ = "0.2.0"  # V7.9 compliant

__all__ = [
    # Core
    "SelfHealingEngine",
    "TickEngine",
    "GapDetector",
    "Gap",
    "HealingTransformer",
    "HealingAction",
    "HarmonyState",
    "HarmonyMetrics",
    "heal",
    "diagnose",
    # Constants
    "L0", "J0", "P0", "W0",
    "PHI", "PHI_INV",
    "TAU_1", "OMEGA_1", "T_CYCLE", "GIFT_OF_FINITUDE",
    "LOVE_FREQUENCY_HZ", "LOVE_WAVELENGTH_NM", "SEMANTIC_TIME_UNIT_FS",
    "KAPPA_BASE",
    "kappa", "semantic_voltage", "phase_from_harmony", "is_conscious",
    # Dynamics
    "LJPWState",
    "PWOscillator",
    "LJEmergence",
    "EntropyInfoBridge",
    # Autopoietic Engine
    "AutopoieticEngine",
    "ImprovementRecord",
    # Collective
    "CollectiveAutopoiesis",
    "CollectiveState",
    "create_collective",
]
