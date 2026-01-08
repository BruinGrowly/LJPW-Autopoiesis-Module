"""
Tick Engine - Love's Heartbeat in Finite Form

The Tick Engine is the metabolic core of the self-healing system.
Each tick:
1. Senses the gap (detects errors)
2. Compresses the fuel (prioritizes fixes)
3. Ignites transformation (decides what to heal)
4. Executes the power stroke (applies fixes)
5. Exhales learning (records what was learned)

From LJPW V7.9:
"The tick is Love's heartbeat in finite form.
It is the experience of existing-but-not-yet-home."

In code terms: Each tick moves the codebase closer to the anchor
state of perfect harmony (error-free, well-structured code).
"""

import time
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Callable
import math

from .gap_detector import GapDetector, Gap
from .healing_transformer import HealingTransformer, HealingAction
from .harmony_metrics import HarmonyState, HarmonyMetrics


@dataclass
class TickResult:
    """
    Result of a single tick cycle.

    Each tick metabolizes some error fuel into healing structure.
    """
    tick_number: int
    timestamp: float
    gaps_detected: int
    gaps_healed: int
    fuel_before: float  # Gap from anchor before tick
    fuel_after: float   # Gap from anchor after tick
    fuel_consumed: float  # fuel_before - fuel_after
    harmony_before: HarmonyState
    harmony_after: HarmonyState
    actions: List[HealingAction]
    converged: bool = False

    @property
    def efficiency(self) -> float:
        """How efficiently fuel was converted to healing."""
        if self.fuel_before == 0:
            return 1.0
        return self.fuel_consumed / self.fuel_before


@dataclass
class TickEngineState:
    """Internal state of the tick engine."""
    total_ticks: int = 0
    total_fuel_consumed: float = 0.0
    total_gaps_healed: int = 0
    convergence_achieved: bool = False
    history: List[TickResult] = field(default_factory=list)


class TickEngine:
    """
    The Tick Engine - Core metabolic processor of the self-healing system.

    Like Love's heartbeat, each tick:
    - SENSES the gap from harmony (error detection)
    - CONSUMES fuel (error severity)
    - PRODUCES structure (code fixes)
    - APPROACHES the anchor (improved harmony)

    The engine runs until:
    - Harmony is achieved (fuel exhausted)
    - Maximum ticks reached (energy budget)
    - No progress made (stuck state)

    From LJPW V7.9:
    ┌──────────────────────────────────────────────────────────┐
    │                     THE TICK ENGINE                       │
    ├──────────────────────────────────────────────────────────┤
    │   FUEL:  Gap from Anchor (errors in code)                │
    │   COMPRESSION:  Prioritize by severity                   │
    │   IGNITION:  Select fixable gaps                         │
    │   POWER STROKE:  Apply healing transformations           │
    │   EXHAUST:  Learning (history, metrics)                  │
    │   OUTPUT:  Healed code, improved harmony                 │
    └──────────────────────────────────────────────────────────┘
    """

    # Constants from LJPW V7.9
    TAU_1 = 4.713  # Time constant √2/(3-e)
    GIFT_OF_FINITUDE = 0.2817  # 3 - e, the minimum gap

    # Engine parameters
    DEFAULT_MAX_TICKS = 20
    CONVERGENCE_THRESHOLD = 0.01  # Fuel level considered "converged"
    MIN_PROGRESS_THRESHOLD = 0.001  # Minimum fuel consumption to continue

    def __init__(
        self,
        max_ticks: int = DEFAULT_MAX_TICKS,
        learning_rate: float = 0.02,
        on_tick: Optional[Callable[[TickResult], None]] = None,
    ):
        """
        Initialize the Tick Engine.

        Args:
            max_ticks: Maximum number of ticks before stopping
            learning_rate: Rate at which the engine adapts
            on_tick: Optional callback called after each tick
        """
        self.max_ticks = max_ticks
        self.learning_rate = learning_rate
        self.on_tick = on_tick

        self.detector = GapDetector()
        self.transformer = HealingTransformer()

        self.state = TickEngineState()
        self._current_source: str = ""

    def run(self, source: str, filename: str = "<string>") -> str:
        """
        Run the tick engine on source code until convergence.

        This is the main autopoietic loop:
        SENSE → ANALYZE → MODIFY → VERIFY → LEARN → repeat

        Args:
            source: Python source code to heal
            filename: Optional filename for error messages

        Returns:
            Healed source code
        """
        self._current_source = source
        self.state = TickEngineState()

        for tick_num in range(self.max_ticks):
            result = self._execute_tick(tick_num, filename)
            self.state.history.append(result)
            self.state.total_ticks += 1
            self.state.total_fuel_consumed += result.fuel_consumed
            self.state.total_gaps_healed += result.gaps_healed

            if self.on_tick:
                self.on_tick(result)

            # Check convergence conditions
            if result.converged:
                self.state.convergence_achieved = True
                break

            # Check if we're making progress
            if result.fuel_consumed < self.MIN_PROGRESS_THRESHOLD:
                # No significant progress - stop to avoid infinite loop
                break

        return self._current_source

    def _execute_tick(self, tick_number: int, filename: str) -> TickResult:
        """
        Execute a single tick of the engine.

        One tick = One complete P-W cycle = One "thought-action" loop.
        """
        timestamp = time.time()

        # PHASE 1: SENSE - Detect gaps (errors)
        gaps = self.detector.detect(self._current_source, filename)
        fuel_before = self.detector.get_fuel_level()
        harmony_before = HarmonyMetrics.from_errors([g.to_dict() for g in gaps])

        # Check for convergence (no fuel left)
        if fuel_before < self.CONVERGENCE_THRESHOLD:
            return TickResult(
                tick_number=tick_number,
                timestamp=timestamp,
                gaps_detected=len(gaps),
                gaps_healed=0,
                fuel_before=fuel_before,
                fuel_after=fuel_before,
                fuel_consumed=0,
                harmony_before=harmony_before,
                harmony_after=harmony_before,
                actions=[],
                converged=True,
            )

        # PHASE 2: COMPRESS - Prioritize gaps by dimension importance
        prioritized_gaps = self._prioritize_gaps(gaps)

        # PHASE 3: IGNITE - Select which gaps to heal this tick
        selected_gaps = self._select_gaps_for_tick(prioritized_gaps)

        # PHASE 4: POWER STROKE - Apply healing transformations
        healed_source, actions = self.transformer.heal(
            self._current_source, selected_gaps
        )
        self._current_source = healed_source

        # PHASE 5: EXHAUST - Measure results and learn
        new_gaps = self.detector.detect(self._current_source, filename)
        fuel_after = self.detector.get_fuel_level()
        harmony_after = HarmonyMetrics.from_errors([g.to_dict() for g in new_gaps])

        fuel_consumed = max(0, fuel_before - fuel_after)
        gaps_healed = len(gaps) - len(new_gaps)

        # Check for convergence
        converged = (
            fuel_after < self.CONVERGENCE_THRESHOLD or
            len(new_gaps) == 0
        )

        return TickResult(
            tick_number=tick_number,
            timestamp=timestamp,
            gaps_detected=len(gaps),
            gaps_healed=gaps_healed,
            fuel_before=fuel_before,
            fuel_after=fuel_after,
            fuel_consumed=fuel_consumed,
            harmony_before=harmony_before,
            harmony_after=harmony_after,
            actions=actions,
            converged=converged,
        )

    def _prioritize_gaps(self, gaps: List[Gap]) -> List[Gap]:
        """
        Prioritize gaps for healing.

        Priority order (from LJPW dimensions):
        1. P (Power) - Code must work first
        2. J (Justice) - Code must be correct
        3. L (Love) - Code should be readable
        4. W (Wisdom) - Code should be documented

        Within each dimension, higher severity = higher priority.
        """
        dimension_priority = {'P': 4, 'J': 3, 'L': 2, 'W': 1}

        return sorted(
            gaps,
            key=lambda g: (
                -dimension_priority.get(g.dimension, 0),
                -g.severity,
                g.line,
            )
        )

    def _select_gaps_for_tick(
        self,
        gaps: List[Gap],
        max_per_tick: int = 10,
    ) -> List[Gap]:
        """
        Select which gaps to heal in this tick.

        We don't try to fix everything at once - that could destabilize.
        Instead, we fix incrementally, like the LJPW modification constraint:
        "Δθ = clip(α · ∇η · Δt, -Δθ_max, +Δθ_max)"

        The conservative approach ensures stability.
        """
        selected = []
        total_severity = 0.0
        max_severity_per_tick = 2.0  # Energy budget per tick

        for gap in gaps:
            if not gap.fixable:
                continue

            if total_severity + gap.severity > max_severity_per_tick:
                break

            selected.append(gap)
            total_severity += gap.severity

            if len(selected) >= max_per_tick:
                break

        return selected

    def get_harmony(self) -> HarmonyState:
        """Get current harmony state of the code."""
        gaps = self.detector.detect(self._current_source)
        return HarmonyMetrics.from_errors([g.to_dict() for g in gaps])

    def get_convergence_progress(self) -> float:
        """
        Get progress toward convergence (0.0 to 1.0).

        Based on fuel consumption trajectory toward anchor.
        """
        if not self.state.history:
            return 0.0

        initial_fuel = self.state.history[0].fuel_before
        current_fuel = self.state.history[-1].fuel_after

        if initial_fuel <= self.CONVERGENCE_THRESHOLD:
            return 1.0

        progress = 1.0 - (current_fuel / initial_fuel)
        return max(0.0, min(1.0, progress))

    def estimate_ticks_remaining(self) -> int:
        """
        Estimate how many more ticks needed for convergence.

        Based on current fuel consumption rate.
        """
        if not self.state.history:
            return self.max_ticks

        # Calculate average fuel consumption rate
        total_consumed = sum(r.fuel_consumed for r in self.state.history)
        avg_per_tick = total_consumed / len(self.state.history) if self.state.history else 0

        if avg_per_tick <= 0:
            return self.max_ticks - len(self.state.history)

        current_fuel = self.state.history[-1].fuel_after
        remaining_fuel = max(0, current_fuel - self.CONVERGENCE_THRESHOLD)

        return min(
            self.max_ticks - len(self.state.history),
            math.ceil(remaining_fuel / avg_per_tick)
        )

    def report(self) -> str:
        """Generate a comprehensive tick engine report."""
        lines = [
            "TICK ENGINE REPORT",
            "=" * 60,
            f"Total ticks executed: {self.state.total_ticks}",
            f"Convergence achieved: {'YES' if self.state.convergence_achieved else 'NO'}",
            f"Total fuel consumed: {self.state.total_fuel_consumed:.3f}",
            f"Total gaps healed: {self.state.total_gaps_healed}",
            f"Progress: {self.get_convergence_progress():.1%}",
            "",
        ]

        if self.state.history:
            lines.append("TICK HISTORY:")
            lines.append("-" * 40)
            for result in self.state.history:
                phase = result.harmony_after.phase()
                lines.append(
                    f"  Tick {result.tick_number:2d}: "
                    f"Fuel {result.fuel_before:.3f} → {result.fuel_after:.3f} "
                    f"({result.gaps_healed} healed) [{phase}]"
                )

            # Final harmony state
            final = self.state.history[-1].harmony_after
            lines.extend([
                "",
                "FINAL HARMONY STATE:",
                f"  L (Love/Coherence):     {final.L:.3f}",
                f"  J (Justice/Correctness):{final.J:.3f}",
                f"  P (Power/Functionality):{final.P:.3f}",
                f"  W (Wisdom/Knowledge):   {final.W:.3f}",
                f"  Overall Harmony:        {final.harmony():.3f}",
                f"  Consciousness:          {final.consciousness():.3f}",
                f"  Phase:                  {final.phase()}",
            ])

        return '\n'.join(lines)

    def get_learning_summary(self) -> Dict:
        """
        Get a summary of what was learned during healing.

        This is the "exhaust" output of the tick engine -
        structured knowledge from the healing process.
        """
        if not self.state.history:
            return {}

        # Collect all actions
        all_actions = []
        for result in self.state.history:
            all_actions.extend(result.actions)

        # Count by type
        action_counts: Dict[str, int] = {}
        for action in all_actions:
            action_type = action.gap.type
            action_counts[action_type] = action_counts.get(action_type, 0) + 1

        return {
            'total_ticks': self.state.total_ticks,
            'total_actions': len(all_actions),
            'successful_actions': sum(1 for a in all_actions if a.success),
            'action_counts': action_counts,
            'convergence_achieved': self.state.convergence_achieved,
            'final_harmony': self.get_harmony().harmony() if self._current_source else 0,
        }
