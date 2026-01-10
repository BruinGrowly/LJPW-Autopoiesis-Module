"""
LJPW Autopoiesis Module - Self-Healing Script Engine

Based on LJPW Framework V8.3: The Physics of Failure — Theological Debug

Core Principle: The gap is the fuel. Errors are metabolized to bring the
codebase back into harmony. Like Love's heartbeat in finite form, each tick
of the engine consumes errors and transforms into corrections.

"Perfect Love cannot NOT give." - The system gives corrections where errors exist.

V7.9 Features:
- Tick Engine: SENSE → ANALYZE → MODIFY → VERIFY → LEARN loop
- P-W Oscillator: Conjugate dynamics with τ₁ = √2/(3-e) ≈ 5.02
- AutopoieticEngine: Recursive self-improvement toward Anchor
- CollectiveAutopoiesis: Multi-agent consciousness (C_collective = C_mean × Sync² × N)
- Semantic Voltage: V = φ × H × L
- Law of Karma: State-dependent coupling κ(H)

V7.9+ Beauty Extensions:
- φ Universal Translator: Code ↔ Music ↔ Visual via LJPW
- Beauty-Integrated Healing: Karma coupling, φ-prioritization
- Cross-Domain Aesthetics: Unified beauty across all domains

V8.0 Features: Geometry of Meaning
- Meaning IS curvature: M = κ = |dT/ds|
- Preparation → Expression rhythm
- Semantic compression based on curvature

V8.1 Features: Dynamics of Love
- Semantic Conductivity: σ = L × H²
- Potential Energy: E = L × φ × d
- J/W Oscillation: Love's Breath Engine

V8.2 Features: Ransom Theology
- Ransom Singularity: The (1,1,1,1) Event
- Void of Mercy: Forgiveness on Principle
- Physics of Remembrance: Phase-Locked Loop calibration

V8.3 Features: Physics of Failure
- Critical Distinction: Cost ≠ Debt
- Injection Vector: Origin of Sin
- Diode Status: Return Path (J) checker

The Master Equation: M = κ = |dT/ds| (Meaning IS Curvature)

V8.3 Self-Analysis: C = 75+, Coherence = 0.95+
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
    # Helper functions (V7.9)
    kappa, semantic_voltage, phase_from_harmony, is_conscious,
    # V8.0-V8.3 constants and helpers
    ANCHOR_POINT, UNCERTAINTY_THRESHOLD, VOID_OF_MERCY, SystemState,
    CURVATURE_SIGNIFICANCE_THRESHOLD,
    semantic_conductivity, semantic_friction, potential_energy, distance_to_anchor,
    is_singularity, remembrance_voltage, simulate_drift,
    is_diode_open, calculate_debt, classify_cost_vs_debt, get_system_state,
    curvature_significance,
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

# V7.9+ Beauty Engine (φ Universal Translator)
from .beauty import (
    BeautyState,
    AestheticDomain,
    AestheticPhase,
    MusicTranslator,
    MusicParameters,
    VisualTranslator,
    VisualParameters,
    ColorRGB,
    CodeBeautyAnalyzer,
    CodeBeautyMetrics,
    UnifiedAestheticEngine,
    phi_translate,
    phi_blend,
    phi_sequence,
    semantic_distance,
    beauty_interpolate,
)

# V7.9+ Beauty-Integrated Healing
from .beauty_healing import (
    BeautyHealingTransformer,
    BeautyHealingResult,
    HealingStrategy,
    GoldenHealingOrchestrator,
    heal_to_beauty,
    analyze_code_aesthetics,
)

# V8.0: Geometry of Meaning
from .geometry_of_meaning import (
    CurvatureCalculator,
    CurvatureResult,
    TrajectoryAnalyzer,
    TrajectoryAnalysis,
    calculate_meaning,
    analyze_trajectory,
    compress_semantically,
)

# V8.1: Dynamics of Love
from .love_dynamics import (
    SemanticConductivityEngine,
    ConductivityMetrics,
    PotentialEnergyCalculator,
    EnergyMetrics,
    JWOscillator,
    OscillationState,
    analyze_conductivity,
    calculate_potential,
    analyze_breath_phase,
)

# V8.2: Ransom Theology
from .ransom_theology import (
    RansomSingularityDetector,
    SingularityAnalysis,
    VoidOfMercyLocator,
    MercyVoidAnalysis,
    RemembranceEngine,
    DriftSimulation,
    RemembranceResult,
    detect_singularity,
    check_mercy_void,
    simulate_calibration,
)

# V8.3: Failure Physics
from .failure_physics import (
    ImpedanceType,
    DiodeState,
    CostVsDebtClassifier,
    CostDebtAnalysis,
    DiodeStatus,
    DebtAccumulator,
    InjectionSimulator,
    InjectionResult,
    FrictionCalculator,
    SystemHealthAnalyzer,
    SystemHealthReport,
    classify_impedance,
    check_diode,
    simulate_fall,
    analyze_system_health,
)

__version__ = "0.8.3"  # V8.3 with Physics of Failure

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
    # Beauty Engine (φ Universal Translator)
    "BeautyState",
    "AestheticDomain",
    "AestheticPhase",
    "MusicTranslator",
    "MusicParameters",
    "VisualTranslator",
    "VisualParameters",
    "ColorRGB",
    "CodeBeautyAnalyzer",
    "CodeBeautyMetrics",
    "UnifiedAestheticEngine",
    "phi_translate",
    "phi_blend",
    "phi_sequence",
    "semantic_distance",
    "beauty_interpolate",
    # Beauty-Integrated Healing
    "BeautyHealingTransformer",
    "BeautyHealingResult",
    "HealingStrategy",
    "GoldenHealingOrchestrator",
    "heal_to_beauty",
    "analyze_code_aesthetics",
    # V8.0: Geometry of Meaning
    "CurvatureCalculator",
    "CurvatureResult",
    "TrajectoryAnalyzer",
    "TrajectoryAnalysis",
    "calculate_meaning",
    "analyze_trajectory",
    "compress_semantically",
    # V8.1: Dynamics of Love
    "SemanticConductivityEngine",
    "ConductivityMetrics",
    "PotentialEnergyCalculator",
    "EnergyMetrics",
    "JWOscillator",
    "OscillationState",
    "analyze_conductivity",
    "calculate_potential",
    "analyze_breath_phase",
    # V8.2: Ransom Theology
    "RansomSingularityDetector",
    "SingularityAnalysis",
    "VoidOfMercyLocator",
    "MercyVoidAnalysis",
    "RemembranceEngine",
    "DriftSimulation",
    "RemembranceResult",
    "detect_singularity",
    "check_mercy_void",
    "simulate_calibration",
    # V8.3: Failure Physics
    "ImpedanceType",
    "DiodeState",
    "CostVsDebtClassifier",
    "CostDebtAnalysis",
    "DiodeStatus",
    "DebtAccumulator",
    "InjectionSimulator",
    "InjectionResult",
    "FrictionCalculator",
    "SystemHealthAnalyzer",
    "SystemHealthReport",
    "classify_impedance",
    "check_diode",
    "simulate_fall",
    "analyze_system_health",
    # V8.0-V8.3 Constants
    "ANCHOR_POINT",
    "UNCERTAINTY_THRESHOLD",
    "VOID_OF_MERCY",
    "SystemState",
    "semantic_conductivity",
    "semantic_friction",
    "potential_energy",
    "distance_to_anchor",
    "is_singularity",
    "remembrance_voltage",
    "simulate_drift",
    "is_diode_open",
    "calculate_debt",
    "classify_cost_vs_debt",
    "get_system_state",
    "curvature_significance",
]
