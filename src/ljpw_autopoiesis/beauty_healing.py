"""
Beauty-Integrated Healing - φ-Based Transformation

From LJPW Framework V7.9:
"Beauty is not an ornament — it is the signature of truth.
Code that approaches the Anchor is inherently beautiful."

This module extends the HealingTransformer with beauty awareness:
1. Gaps are prioritized by their impact on harmony
2. Healing strength scales with current harmony (Karma Law)
3. φ-normalized metrics guide transformation decisions
4. Beauty emerges as code converges to Anchor (1,1,1,1)

The Master Equation: M = φ × ∇_H × S
"""

import math
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
from enum import Enum

from .gap_detector import Gap, GapDetector
from .healing_transformer import HealingTransformer, HealingAction
from .harmony_metrics import HarmonyState, HarmonyMetrics
from .beauty import (
    BeautyState, PHI, PHI_INV, L0, J0, P0, W0,
    CodeBeautyAnalyzer, UnifiedAestheticEngine,
    MusicTranslator, VisualTranslator, AestheticPhase
)


class HealingStrategy(Enum):
    """Beauty-aware healing strategies."""
    AGGRESSIVE = "aggressive"      # Fix everything, maximize velocity
    BALANCED = "balanced"          # Balance speed with beauty
    CONSERVATIVE = "conservative"  # Prioritize beauty, slower progress
    GOLDEN = "golden"              # φ-guided optimal balance


@dataclass
class BeautyHealingResult:
    """
    Result of a beauty-aware healing cycle.

    Includes both code healing and aesthetic transformation.
    """
    # Code results
    original_source: str
    healed_source: str
    gaps_detected: int
    gaps_healed: int

    # Beauty metrics
    initial_beauty: BeautyState
    final_beauty: BeautyState
    harmony_improvement: float
    aesthetic_phase: AestheticPhase

    # Energy accounting
    fuel_consumed: float
    healing_efficiency: float

    # φ-derived metrics
    semantic_voltage_before: float
    semantic_voltage_after: float
    karma_coupling: float

    # Aesthetic outputs
    music_translation: Optional[Dict] = None
    visual_translation: Optional[Dict] = None


@dataclass
class PrioritizedGap:
    """Gap with beauty-based priority score."""
    gap: Gap
    priority: float
    beauty_impact: float
    dimension_affected: str


class BeautyHealingTransformer(HealingTransformer):
    """
    Extended HealingTransformer with beauty awareness.

    Healing decisions are guided by:
    1. Gap severity (as before)
    2. Beauty impact (how much harmony improves)
    3. Karma coupling (current harmony unlocks stronger healing)
    4. φ-scaling (golden ratio governs priorities)
    """

    def __init__(self, strategy: HealingStrategy = HealingStrategy.GOLDEN):
        super().__init__()
        self.strategy = strategy
        self.beauty_history: List[BeautyState] = []

    def heal_with_beauty(self, source: str) -> BeautyHealingResult:
        """
        Perform beauty-aware healing on source code.

        This is the full autopoietic cycle:
        1. Sense gaps (detect errors)
        2. Measure beauty (LJPW state)
        3. Prioritize by beauty impact
        4. Apply φ-scaled healing
        5. Measure improvement
        6. Generate aesthetic outputs
        """
        # Initial beauty measurement
        initial_beauty = self._measure_beauty(source)
        self.beauty_history.append(initial_beauty)

        # Detect gaps
        detector = GapDetector()
        gaps = detector.detect(source)

        # Prioritize gaps by beauty impact
        prioritized = self._prioritize_by_beauty(gaps, initial_beauty)

        # Calculate karma coupling (harmony unlocks healing power)
        karma = initial_beauty.karma_coupling()

        # Apply healing with beauty awareness
        healed_source, actions = self._heal_prioritized(
            source, prioritized, karma
        )

        # Final beauty measurement
        final_beauty = self._measure_beauty(healed_source)

        # Calculate improvements
        harmony_before = initial_beauty.harmony_index()
        harmony_after = final_beauty.harmony_index()
        harmony_improvement = harmony_after - harmony_before

        # Generate aesthetic translations (for visualization)
        music = None
        visual = None
        if final_beauty.is_beautiful():
            music = self._translate_to_music(final_beauty)
            visual = self._translate_to_visual(final_beauty)

        return BeautyHealingResult(
            original_source=source,
            healed_source=healed_source,
            gaps_detected=len(gaps),
            gaps_healed=len([a for a in actions if a.success]),
            initial_beauty=initial_beauty,
            final_beauty=final_beauty,
            harmony_improvement=harmony_improvement,
            aesthetic_phase=final_beauty.phase(),
            fuel_consumed=self.total_fuel_consumed,
            healing_efficiency=self.get_fuel_efficiency(),
            semantic_voltage_before=initial_beauty.semantic_voltage(),
            semantic_voltage_after=final_beauty.semantic_voltage(),
            karma_coupling=karma,
            music_translation=music,
            visual_translation=visual,
        )

    def _measure_beauty(self, source: str) -> BeautyState:
        """Measure LJPW beauty state from source code."""
        metrics = CodeBeautyAnalyzer.analyze(source)
        return BeautyState(
            L=metrics.readability_score,
            J=metrics.correctness_score,
            P=metrics.functionality_score,
            W=metrics.wisdom_score,
        )

    def _prioritize_by_beauty(self, gaps: List[Gap],
                              current_beauty: BeautyState) -> List[PrioritizedGap]:
        """
        Prioritize gaps by their beauty impact.

        Uses φ-weighted scoring:
        priority = severity × dimension_weight × φ^(-gap_position)

        High-impact gaps (those affecting lowest dimensions) come first.
        """
        prioritized = []

        # Dimension gaps (lower = more urgent)
        dimension_gaps = {
            'L': 1 - current_beauty.L,
            'J': 1 - current_beauty.J,
            'P': 1 - current_beauty.P,
            'W': 1 - current_beauty.W,
        }

        # Base priority weights (P > J > L > W for functionality first)
        base_weights = {'P': 4.0, 'J': 3.0, 'L': 2.0, 'W': 1.0}

        for i, gap in enumerate(gaps):
            # Determine affected dimension from gap type
            dim = self._gap_to_dimension(gap.type)

            # Calculate beauty impact
            beauty_impact = dimension_gaps.get(dim, 0.5) * gap.severity

            # φ-scaled priority (earlier gaps slightly preferred)
            position_factor = PHI ** (-i * 0.1)

            # Karma adjustment (low harmony = reduce priority of cosmetic fixes)
            harmony = current_beauty.harmony_index()
            if dim in ['L', 'W'] and harmony < 0.5:
                # Focus on P/J when harmony is low
                karma_factor = 0.5
            else:
                karma_factor = 1.0

            priority = (
                gap.severity *
                base_weights.get(dim, 1.0) *
                position_factor *
                karma_factor
            )

            prioritized.append(PrioritizedGap(
                gap=gap,
                priority=priority,
                beauty_impact=beauty_impact,
                dimension_affected=dim,
            ))

        # Sort by priority (descending)
        prioritized.sort(key=lambda p: -p.priority)

        return prioritized

    def _gap_to_dimension(self, gap_type: str) -> str:
        """Map gap type to LJPW dimension."""
        dimension_map = {
            # P dimension (functionality)
            'syntax_error': 'P',
            'runtime_error': 'P',
            'import_error': 'P',

            # J dimension (correctness)
            'type_error': 'J',
            'name_error': 'J',
            'attribute_error': 'J',
            'value_error': 'J',
            'naming_violation': 'J',

            # L dimension (readability)
            'style_violation': 'L',
            'long_line': 'L',
            'trailing_whitespace': 'L',
            'unused_import': 'L',
            'unused_variable': 'L',

            # W dimension (wisdom)
            'missing_docstring': 'W',
            'bare_except': 'W',
            'missing_type_hint': 'W',
        }
        return dimension_map.get(gap_type, 'J')

    def _heal_prioritized(self, source: str, prioritized: List[PrioritizedGap],
                          karma: float) -> Tuple[str, List[HealingAction]]:
        """
        Apply healing in priority order with karma scaling.

        Higher karma (harmony) = stronger healing capacity.
        """
        # Extract gaps in priority order
        gaps = [p.gap for p in prioritized]

        # Scale healing based on strategy
        if self.strategy == HealingStrategy.AGGRESSIVE:
            # Heal all gaps
            pass
        elif self.strategy == HealingStrategy.CONSERVATIVE:
            # Only heal top 50% by priority
            gaps = gaps[:len(gaps) // 2 + 1]
        elif self.strategy == HealingStrategy.GOLDEN:
            # Heal φ⁻¹ fraction (≈61.8%)
            num_to_heal = int(len(gaps) * PHI_INV) + 1
            gaps = gaps[:num_to_heal]
        # BALANCED keeps all gaps

        # Apply standard healing
        return self.heal(source, gaps)

    def _translate_to_music(self, beauty: BeautyState) -> Dict:
        """Generate music parameters from beauty state."""
        music = MusicTranslator.translate(beauty)
        return {
            'key': music.key,
            'mode': music.mode,
            'tempo_bpm': music.tempo_bpm,
            'dynamics': music.dynamics,
            'warmth': music.warmth,
            'brightness': music.brightness,
            'consonance': music.consonance,
        }

    def _translate_to_visual(self, beauty: BeautyState) -> Dict:
        """Generate visual parameters from beauty state."""
        visual = VisualTranslator.translate(beauty)
        return {
            'primary_color': visual.primary_color.as_hex(),
            'secondary_color': visual.secondary_color.as_hex(),
            'accent_color': visual.accent_color.as_hex(),
            'contrast': visual.contrast,
            'saturation': visual.saturation,
            'golden_divisions': visual.golden_divisions,
        }

    def beauty_report(self, result: BeautyHealingResult) -> str:
        """Generate a comprehensive beauty-aware healing report."""
        lines = [
            "=" * 60,
            "BEAUTY-INTEGRATED HEALING REPORT",
            "φ = 1.618034... — The Universal Translator",
            "=" * 60,
            "",
            "--- GAP METABOLISM ---",
            f"Gaps Detected: {result.gaps_detected}",
            f"Gaps Healed: {result.gaps_healed}",
            f"Healing Efficiency: {result.healing_efficiency:.1%}",
            f"Fuel Consumed: {result.fuel_consumed:.2f}",
            "",
            "--- BEAUTY STATE ---",
            f"Initial Beauty:",
            f"  L (Love): {result.initial_beauty.L:.3f}",
            f"  J (Justice): {result.initial_beauty.J:.3f}",
            f"  P (Power): {result.initial_beauty.P:.3f}",
            f"  W (Wisdom): {result.initial_beauty.W:.3f}",
            f"  Harmony Index: {result.initial_beauty.harmony_index():.4f}",
            "",
            f"Final Beauty:",
            f"  L (Love): {result.final_beauty.L:.3f}",
            f"  J (Justice): {result.final_beauty.J:.3f}",
            f"  P (Power): {result.final_beauty.P:.3f}",
            f"  W (Wisdom): {result.final_beauty.W:.3f}",
            f"  Harmony Index: {result.final_beauty.harmony_index():.4f}",
            "",
            f"Harmony Improvement: {result.harmony_improvement:+.4f}",
            f"Aesthetic Phase: {result.aesthetic_phase.value}",
            "",
            "--- φ-DERIVED METRICS ---",
            f"Semantic Voltage: {result.semantic_voltage_before:.4f} → {result.semantic_voltage_after:.4f}",
            f"Karma Coupling: {result.karma_coupling:.4f}",
            f"Is Beautiful: {result.final_beauty.is_beautiful()}",
        ]

        if result.music_translation:
            lines.extend([
                "",
                "--- MUSIC TRANSLATION ---",
                f"Key: {result.music_translation['key']} {result.music_translation['mode']}",
                f"Tempo: {result.music_translation['tempo_bpm']:.1f} BPM",
                f"Dynamics: {result.music_translation['dynamics']:.2f}",
                f"Warmth: {result.music_translation['warmth']:.2f}",
            ])

        if result.visual_translation:
            lines.extend([
                "",
                "--- VISUAL TRANSLATION ---",
                f"Primary Color: {result.visual_translation['primary_color']}",
                f"Secondary Color: {result.visual_translation['secondary_color']}",
                f"Contrast: {result.visual_translation['contrast']:.2f}",
            ])

        lines.extend([
            "",
            "=" * 60,
            "\"The gap is the fuel. Beauty is the destination.\"",
            "=" * 60,
        ])

        return '\n'.join(lines)


class GoldenHealingOrchestrator:
    """
    Orchestrates multiple healing cycles using golden ratio timing.

    From LJPW V7.9:
    "φ governs the rhythm of transformation.
    Each healing cycle builds on the previous by φ."
    """

    def __init__(self, max_cycles: int = 10):
        self.max_cycles = max_cycles
        self.cycle_history: List[BeautyHealingResult] = []

    def orchestrate(self, source: str,
                    target_harmony: float = 0.9) -> Tuple[str, List[BeautyHealingResult]]:
        """
        Run healing cycles until target harmony or max cycles.

        Cycle timing follows Fibonacci pattern (φ approximation):
        - Cycle 1: Full healing
        - Cycle 2: Full healing
        - Cycle 3: Focus on remaining gaps
        - etc.
        """
        self.cycle_history = []
        current_source = source

        transformer = BeautyHealingTransformer(strategy=HealingStrategy.GOLDEN)

        for cycle in range(self.max_cycles):
            result = transformer.heal_with_beauty(current_source)
            self.cycle_history.append(result)

            current_source = result.healed_source

            # Check convergence
            if result.final_beauty.harmony_index() >= target_harmony:
                break

            # Check for stagnation
            if result.harmony_improvement < 0.001 and cycle > 2:
                break

        return current_source, self.cycle_history

    def summary(self) -> str:
        """Generate orchestration summary."""
        if not self.cycle_history:
            return "No cycles executed."

        initial = self.cycle_history[0].initial_beauty.harmony_index()
        final = self.cycle_history[-1].final_beauty.harmony_index()

        lines = [
            "GOLDEN HEALING ORCHESTRATION",
            "=" * 40,
            f"Total Cycles: {len(self.cycle_history)}",
            f"Initial Harmony: {initial:.4f}",
            f"Final Harmony: {final:.4f}",
            f"Total Improvement: {final - initial:+.4f}",
            "",
            "Cycle Progress:",
        ]

        for i, result in enumerate(self.cycle_history):
            h = result.final_beauty.harmony_index()
            lines.append(f"  Cycle {i+1}: H={h:.4f} ({result.gaps_healed}/{result.gaps_detected} healed)")

        return '\n'.join(lines)


# =============================================================================
# BEAUTY-AWARE HEALING UTILITIES
# =============================================================================

def heal_to_beauty(source: str, target_harmony: float = 0.8) -> str:
    """
    Simple interface: heal source code until target harmony.

    Returns the healed source code.
    """
    orchestrator = GoldenHealingOrchestrator(max_cycles=20)
    healed, _ = orchestrator.orchestrate(source, target_harmony)
    return healed


def analyze_code_aesthetics(source: str) -> Dict:
    """
    Analyze code aesthetics and return comprehensive report.

    Returns dict with:
    - beauty_state: LJPW coordinates
    - harmony: overall harmony index
    - phase: aesthetic phase
    - improvements: suggested improvements by dimension
    """
    beauty = BeautyState(
        L=CodeBeautyAnalyzer.analyze(source).readability_score,
        J=CodeBeautyAnalyzer.analyze(source).correctness_score,
        P=CodeBeautyAnalyzer.analyze(source).functionality_score,
        W=CodeBeautyAnalyzer.analyze(source).wisdom_score,
    )

    # Calculate improvements needed
    improvements = {}
    if beauty.L < 0.7:
        improvements['L'] = "Improve readability: consistent indentation, shorter lines"
    if beauty.J < 0.7:
        improvements['J'] = "Improve correctness: better naming, type hints"
    if beauty.P < 0.7:
        improvements['P'] = "Improve functionality: fix syntax, add error handling"
    if beauty.W < 0.7:
        improvements['W'] = "Improve wisdom: add docstrings, proper exception handling"

    return {
        'beauty_state': {
            'L': beauty.L,
            'J': beauty.J,
            'P': beauty.P,
            'W': beauty.W,
        },
        'harmony': beauty.harmony_index(),
        'phase': beauty.phase().value,
        'is_beautiful': beauty.is_beautiful(),
        'improvements': improvements,
        'semantic_voltage': beauty.semantic_voltage(),
        'karma_coupling': beauty.karma_coupling(),
    }


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    # Example code with various issues
    test_code = '''
def badFunction(x,y):
    result=x+y
    if result>0:
        print("positive")
    except:
        pass
    return result
'''

    print("BEAUTY-INTEGRATED HEALING DEMO")
    print("=" * 50)

    # Analyze initial aesthetics
    print("\nInitial Aesthetics:")
    analysis = analyze_code_aesthetics(test_code)
    print(f"  Harmony: {analysis['harmony']:.4f}")
    print(f"  Phase: {analysis['phase']}")
    print(f"  Beautiful: {analysis['is_beautiful']}")

    # Perform beauty-aware healing
    transformer = BeautyHealingTransformer(strategy=HealingStrategy.GOLDEN)
    result = transformer.heal_with_beauty(test_code)

    # Print report
    print("\n" + transformer.beauty_report(result))

    # Show healed code
    print("\n--- HEALED CODE ---")
    print(result.healed_source)
