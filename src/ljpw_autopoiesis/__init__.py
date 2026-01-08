"""
LJPW Autopoiesis Module - Self-Healing Script Engine

Based on LJPW Framework V7.9: True Autopoiesis

Core Principle: The gap is the fuel. Errors are metabolized to bring the
codebase back into harmony. Like Love's heartbeat in finite form, each tick
of the engine consumes errors and transforms them into corrections.

"Perfect Love cannot NOT give." - The system gives corrections where errors exist.
"""

# Public API - these imports ARE used (for re-export)
from .engine import SelfHealingEngine, heal, diagnose
from .tick_engine import TickEngine
from .gap_detector import GapDetector
from .healing_transformer import HealingTransformer
from .harmony_metrics import HarmonyState, HarmonyMetrics

__version__ = "0.1.0"
__all__ = [
    "SelfHealingEngine",
    "TickEngine",
    "GapDetector",
    "HealingTransformer",
    "HarmonyState",
    "HarmonyMetrics",
    "heal",
    "diagnose",
]
