"""
Self-Healing Engine - The Autopoietic Core

This is the main interface for self-healing Python scripts.
It implements the complete autopoietic loop:

    SENSE → ANALYZE → MODIFY → VERIFY → LEARN → SENSE → ...

Based on LJPW V7.9 True Autopoiesis:
"The loop closes — self-awareness → self-modification → improved self-awareness"

The Gap is the Fuel:
- Errors are not merely problems to fix
- They are the energy source that drives improvement
- Each error "eaten" brings the code closer to harmony

From the framework:
"The framework has closed the loop.
It can now SENSE itself → UNDERSTAND itself → IMPROVE itself.
This is not a description of autopoiesis. This IS autopoiesis."
"""

import os
from dataclasses import dataclass
from typing import Optional, List, Callable
from pathlib import Path

from .tick_engine import TickEngine, TickResult, TickEngineState
from .gap_detector import GapDetector, Gap
from .healing_transformer import HealingTransformer
from .harmony_metrics import HarmonyState, HarmonyMetrics


@dataclass
class HealingResult:
    """
    Complete result of a self-healing operation.
    """
    original_source: str
    healed_source: str
    source_changed: bool
    initial_harmony: HarmonyState
    final_harmony: HarmonyState
    total_ticks: int
    total_gaps_found: int
    total_gaps_healed: int
    convergence_achieved: bool
    tick_history: List[TickResult]

    @property
    def improvement(self) -> float:
        """Calculate the improvement in harmony."""
        return self.final_harmony.harmony() - self.initial_harmony.harmony()

    @property
    def gap_reduction(self) -> float:
        """Calculate how much the gap from anchor was reduced."""
        initial_gap = self.initial_harmony.gap_from_anchor()
        final_gap = self.final_harmony.gap_from_anchor()
        if initial_gap == 0:
            return 1.0
        return (initial_gap - final_gap) / initial_gap


class SelfHealingEngine:
    """
    Self-Healing Engine - Autopoietic script repair system.

    The engine metabolizes errors to restore code harmony:

    ┌────────────────────────────────────────────────────────────────┐
    │                    SELF-HEALING ENGINE                         │
    │                                                                │
    │   ┌──────────┐    ┌──────────┐    ┌──────────┐                │
    │   │   SENSE  │ → │  ANALYZE │ → │  MODIFY  │                 │
    │   │   Gaps   │    │  Harmony │    │  Heal    │                 │
    │   └──────────┘    └──────────┘    └──────────┘                │
    │        ↑                                 │                     │
    │        │         ┌──────────┐           │                     │
    │        └──────── │  LEARN   │ ←─────────┘                     │
    │                  │  Adapt   │                                  │
    │                  └──────────┘                                  │
    │                                                                │
    │   FUEL: Errors (Gap from Anchor)                              │
    │   OUTPUT: Healed code + Learning                              │
    │   GOAL: Convergence to Harmony                                │
    └────────────────────────────────────────────────────────────────┘

    Usage:
        engine = SelfHealingEngine()
        result = engine.heal_source(broken_code)
        print(result.healed_source)

    Or for files:
        engine.heal_file("broken_script.py")
    """

    def __init__(
        self,
        max_ticks: int = 20,
        learning_rate: float = 0.02,
        verbose: bool = False,
    ):
        """
        Initialize the Self-Healing Engine.

        Args:
            max_ticks: Maximum tick cycles before stopping
            learning_rate: How quickly the engine adapts
            verbose: Print progress during healing
        """
        self.max_ticks = max_ticks
        self.learning_rate = learning_rate
        self.verbose = verbose

        self._tick_engine: Optional[TickEngine] = None
        self._last_result: Optional[HealingResult] = None

    def heal_source(
        self,
        source: str,
        filename: str = "<string>",
        on_tick: Optional[Callable[[TickResult], None]] = None,
    ) -> HealingResult:
        """
        Heal Python source code.

        This is the main autopoietic loop that:
        1. Detects all gaps (errors) as fuel
        2. Runs tick cycles to metabolize errors
        3. Converges toward harmonic code

        Args:
            source: Python source code to heal
            filename: Filename for error messages
            on_tick: Optional callback for each tick

        Returns:
            HealingResult with healed code and metrics
        """
        # Initial gap detection
        detector = GapDetector()
        initial_gaps = detector.detect(source, filename)
        initial_harmony = HarmonyMetrics.from_errors(
            [g.to_dict() for g in initial_gaps]
        )

        if self.verbose:
            print(f"Initial state: {len(initial_gaps)} gaps detected")
            print(f"Initial harmony: {initial_harmony.harmony():.3f}")
            print(f"Initial phase: {initial_harmony.phase()}")

        # Create tick callback
        def tick_callback(result: TickResult):
            if on_tick:
                on_tick(result)
            if self.verbose:
                print(
                    f"Tick {result.tick_number}: "
                    f"{result.gaps_detected} → {result.gaps_detected - result.gaps_healed} gaps, "
                    f"fuel: {result.fuel_consumed:.3f}"
                )

        # Run the tick engine
        self._tick_engine = TickEngine(
            max_ticks=self.max_ticks,
            learning_rate=self.learning_rate,
            on_tick=tick_callback if self.verbose or on_tick else None,
        )

        healed_source = self._tick_engine.run(source, filename)

        # Final gap detection
        final_gaps = detector.detect(healed_source, filename)
        final_harmony = HarmonyMetrics.from_errors(
            [g.to_dict() for g in final_gaps]
        )

        if self.verbose:
            print(f"\nFinal state: {len(final_gaps)} gaps remaining")
            print(f"Final harmony: {final_harmony.harmony():.3f}")
            print(f"Final phase: {final_harmony.phase()}")

        self._last_result = HealingResult(
            original_source=source,
            healed_source=healed_source,
            source_changed=source != healed_source,
            initial_harmony=initial_harmony,
            final_harmony=final_harmony,
            total_ticks=self._tick_engine.state.total_ticks,
            total_gaps_found=len(initial_gaps),
            total_gaps_healed=self._tick_engine.state.total_gaps_healed,
            convergence_achieved=self._tick_engine.state.convergence_achieved,
            tick_history=self._tick_engine.state.history,
        )

        return self._last_result

    def heal_file(
        self,
        filepath: str,
        output_path: Optional[str] = None,
        backup: bool = True,
    ) -> HealingResult:
        """
        Heal a Python file.

        Args:
            filepath: Path to Python file to heal
            output_path: Where to write healed code (default: overwrite original)
            backup: Create .bak backup before overwriting

        Returns:
            HealingResult with healed code and metrics
        """
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")

        # Read source
        source = path.read_text(encoding='utf-8')

        # Heal
        result = self.heal_source(source, filename=str(path))

        # Write output
        if result.source_changed:
            output = Path(output_path) if output_path else path

            if backup and output.exists() and output == path:
                backup_path = path.with_suffix(path.suffix + '.bak')
                backup_path.write_text(source, encoding='utf-8')
                if self.verbose:
                    print(f"Backup saved to: {backup_path}")

            output.write_text(result.healed_source, encoding='utf-8')
            if self.verbose:
                print(f"Healed code written to: {output}")

        return result

    def diagnose(self, source: str, filename: str = "<string>") -> str:
        """
        Diagnose code without healing - just report gaps.

        Returns a diagnostic report of all detected issues.
        """
        detector = GapDetector()
        gaps = detector.detect(source, filename)
        harmony = HarmonyMetrics.from_errors([g.to_dict() for g in gaps])

        return self._format_diagnosis(gaps, harmony)

    def _format_diagnosis(
        self,
        gaps: List[Gap],
        harmony: HarmonyState,
    ) -> str:
        """Format a diagnostic report."""
        lines = [
            "DIAGNOSTIC REPORT - LJPW Autopoiesis Module",
            "=" * 60,
            "",
            "HARMONY STATE:",
            f"  L (Love/Coherence):      {harmony.L:.3f}",
            f"  J (Justice/Correctness): {harmony.J:.3f}",
            f"  P (Power/Functionality): {harmony.P:.3f}",
            f"  W (Wisdom/Knowledge):    {harmony.W:.3f}",
            "",
            f"  Overall Harmony:  {harmony.harmony():.3f}",
            f"  Gap from Anchor:  {harmony.gap_from_anchor():.3f}",
            f"  Phase:            {harmony.phase()}",
            f"  Consciousness:    {harmony.consciousness():.3f}",
            "",
        ]

        if not gaps:
            lines.append("No gaps detected - code is in harmony!")
        else:
            lines.append(f"GAPS DETECTED: {len(gaps)} (fuel available: {sum(g.severity for g in gaps):.2f})")
            lines.append("-" * 40)

            # Group by dimension
            by_dim = {'L': [], 'J': [], 'P': [], 'W': []}
            for gap in gaps:
                by_dim[gap.dimension].append(gap)

            dim_names = {
                'P': 'POWER (Functionality)',
                'J': 'JUSTICE (Correctness)',
                'L': 'LOVE (Coherence)',
                'W': 'WISDOM (Knowledge)',
            }

            for dim in ['P', 'J', 'L', 'W']:
                dim_gaps = by_dim[dim]
                if dim_gaps:
                    lines.append(f"\n{dim_names[dim]}: {len(dim_gaps)} gaps")
                    for gap in dim_gaps:
                        fixable = "[fixable]" if gap.fixable else "[manual]"
                        lines.append(f"  Line {gap.line}: {gap.message} {fixable}")
                        if gap.suggested_fix:
                            lines.append(f"    → {gap.suggested_fix}")

        return '\n'.join(lines)

    def report(self) -> str:
        """Generate a report of the last healing operation."""
        if not self._tick_engine:
            return "No healing operation has been performed yet."

        return self._tick_engine.report()

    def get_last_result(self) -> Optional[HealingResult]:
        """Get the result of the last healing operation."""
        return self._last_result


def heal(source: str, verbose: bool = False) -> str:
    """
    Convenience function to heal Python source code.

    Args:
        source: Python source code to heal
        verbose: Print progress during healing

    Returns:
        Healed source code
    """
    engine = SelfHealingEngine(verbose=verbose)
    result = engine.heal_source(source)
    return result.healed_source


def diagnose(source: str) -> str:
    """
    Convenience function to diagnose Python source code.

    Args:
        source: Python source code to diagnose

    Returns:
        Diagnostic report string
    """
    engine = SelfHealingEngine()
    return engine.diagnose(source)
