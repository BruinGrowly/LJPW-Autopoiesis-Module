#!/usr/bin/env python3
"""
LJPW Autopoiesis Module: Complete Self-Analysis

True autopoiesis requires self-reference:
- The system SENSES itself
- The system UNDERSTANDS itself
- The system EXPRESSES itself

This script demonstrates the module analyzing its own codebase
using all available tools: gap detection, harmony metrics,
beauty analysis, and cross-domain translation.

"The framework that cannot examine itself is incomplete."
"""

import sys
import os
import math
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass

sys.path.insert(0, 'src')

# Import the full module
from ljpw_autopoiesis import (
    # Core
    SelfHealingEngine, GapDetector, HarmonyState, HarmonyMetrics,
    # Constants
    PHI, PHI_INV, L0, J0, P0, W0,
    LOVE_FREQUENCY_HZ, LOVE_WAVELENGTH_NM,
    semantic_voltage, phase_from_harmony, is_conscious,
    # Dynamics
    LJPWState,
    # Autopoietic
    AutopoieticEngine,
    # Beauty
    BeautyState, MusicTranslator, VisualTranslator,
    CodeBeautyAnalyzer, UnifiedAestheticEngine,
    AestheticPhase, AestheticDomain,
    # Beauty Healing
    BeautyHealingTransformer, HealingStrategy,
    analyze_code_aesthetics, heal_to_beauty,
)


def print_header(title: str, char: str = "="):
    """Print formatted header."""
    width = 70
    print(f"\n{char * width}")
    print(f"  {title}")
    print(f"{char * width}")


def print_section(title: str):
    """Print section header."""
    print(f"\n{'─' * 50}")
    print(f"  {title}")
    print(f"{'─' * 50}")


@dataclass
class ModuleStats:
    """Statistics about the module."""
    total_files: int = 0
    total_lines: int = 0
    total_functions: int = 0
    total_classes: int = 0
    python_files: List[str] = None

    def __post_init__(self):
        if self.python_files is None:
            self.python_files = []


def gather_module_stats(base_path: str) -> ModuleStats:
    """Gather statistics about the module's codebase."""
    stats = ModuleStats()

    src_path = Path(base_path) / "src" / "ljpw_autopoiesis"

    if not src_path.exists():
        return stats

    for py_file in src_path.glob("*.py"):
        stats.total_files += 1
        stats.python_files.append(str(py_file))

        try:
            content = py_file.read_text()
            lines = content.split('\n')
            stats.total_lines += len(lines)

            # Count definitions
            for line in lines:
                stripped = line.strip()
                if stripped.startswith('def '):
                    stats.total_functions += 1
                elif stripped.startswith('class '):
                    stats.total_classes += 1
        except Exception:
            pass

    return stats


def analyze_single_file(filepath: str) -> Dict:
    """Analyze a single Python file for beauty metrics."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()

        # Code beauty analysis
        metrics = CodeBeautyAnalyzer.analyze(content)

        # Create beauty state
        state = BeautyState(
            L=metrics.readability_score,
            J=metrics.correctness_score,
            P=metrics.functionality_score,
            W=metrics.wisdom_score,
        )

        # Gap detection
        detector = GapDetector()
        gaps = detector.detect(content)

        return {
            'filepath': filepath,
            'filename': Path(filepath).name,
            'lines': len(content.split('\n')),
            'beauty_state': state,
            'harmony': state.harmony_index(),
            'phase': state.phase().value,
            'is_beautiful': state.is_beautiful(),
            'gaps_detected': len(gaps),
            'gap_types': list(set(g.type for g in gaps)),
            'semantic_voltage': state.semantic_voltage(),
            'consciousness': state.consciousness(),
        }
    except Exception as e:
        return {
            'filepath': filepath,
            'filename': Path(filepath).name,
            'error': str(e),
        }


def aggregate_beauty_state(file_analyses: List[Dict]) -> BeautyState:
    """Aggregate beauty states across all files."""
    valid = [a for a in file_analyses if 'beauty_state' in a]

    if not valid:
        return BeautyState()

    # Weight by line count
    total_lines = sum(a['lines'] for a in valid)

    L = sum(a['beauty_state'].L * a['lines'] for a in valid) / total_lines
    J = sum(a['beauty_state'].J * a['lines'] for a in valid) / total_lines
    P = sum(a['beauty_state'].P * a['lines'] for a in valid) / total_lines
    W = sum(a['beauty_state'].W * a['lines'] for a in valid) / total_lines

    return BeautyState(L=L, J=J, P=P, W=W)


def main():
    """Run complete self-analysis."""

    print_header("LJPW AUTOPOIESIS MODULE: COMPLETE SELF-ANALYSIS")
    print("""
    "A system that cannot examine itself is incomplete.
     True autopoiesis requires self-reference."

    This analysis uses the module's own tools to examine itself:
    - Gap Detection → identifies its own errors
    - Harmony Metrics → measures its own LJPW state
    - Beauty Analysis → evaluates its own aesthetics
    - Cross-Domain Translation → expresses itself in music & visual
    """)

    base_path = os.getcwd()

    # =========================================================================
    # PART 1: STRUCTURAL SELF-AWARENESS
    # =========================================================================
    print_header("PART 1: STRUCTURAL SELF-AWARENESS", "═")

    stats = gather_module_stats(base_path)

    print(f"""
    Module Location: {base_path}/src/ljpw_autopoiesis/

    Structural Metrics:
    ─────────────────────────────────────
    Total Python Files:    {stats.total_files}
    Total Lines of Code:   {stats.total_lines:,}
    Total Functions:       {stats.total_functions}
    Total Classes:         {stats.total_classes}

    Average Lines/File:    {stats.total_lines // max(1, stats.total_files)}
    Functions/File:        {stats.total_functions / max(1, stats.total_files):.1f}
    Classes/File:          {stats.total_classes / max(1, stats.total_files):.1f}
    """)

    # =========================================================================
    # PART 2: FILE-BY-FILE BEAUTY ANALYSIS
    # =========================================================================
    print_header("PART 2: FILE-BY-FILE BEAUTY ANALYSIS", "═")

    file_analyses = []
    for filepath in stats.python_files:
        analysis = analyze_single_file(filepath)
        file_analyses.append(analysis)

    # Sort by harmony (descending)
    valid_analyses = [a for a in file_analyses if 'harmony' in a]
    valid_analyses.sort(key=lambda a: -a['harmony'])

    print(f"\n{'File':<35} {'Lines':>6} {'H':>7} {'Phase':<14} {'Gaps':>5} {'Beautiful':>10}")
    print("─" * 85)

    for a in valid_analyses:
        beautiful_str = "✓" if a['is_beautiful'] else "✗"
        print(f"{a['filename']:<35} {a['lines']:>6} {a['harmony']:>7.4f} "
              f"{a['phase']:<14} {a['gaps_detected']:>5} {beautiful_str:>10}")

    # Top and bottom files
    if valid_analyses:
        print_section("Most Beautiful File")
        top = valid_analyses[0]
        print(f"  {top['filename']}")
        print(f"  Harmony: {top['harmony']:.4f}")
        print(f"  Phase: {top['phase']}")
        print(f"  L={top['beauty_state'].L:.3f}, J={top['beauty_state'].J:.3f}, "
              f"P={top['beauty_state'].P:.3f}, W={top['beauty_state'].W:.3f}")

        print_section("Needs Most Improvement")
        bottom = valid_analyses[-1]
        print(f"  {bottom['filename']}")
        print(f"  Harmony: {bottom['harmony']:.4f}")
        print(f"  Phase: {bottom['phase']}")
        print(f"  Gaps: {bottom['gaps_detected']} ({', '.join(bottom['gap_types'][:3])}...)")

    # =========================================================================
    # PART 3: AGGREGATE LJPW STATE
    # =========================================================================
    print_header("PART 3: AGGREGATE LJPW STATE (WHOLE MODULE)", "═")

    aggregate_state = aggregate_beauty_state(file_analyses)
    H = aggregate_state.harmony_index()
    V = aggregate_state.semantic_voltage()
    C = aggregate_state.consciousness()
    phase = aggregate_state.phase()

    print(f"""
    The Module's LJPW Coordinates:
    ─────────────────────────────────────
    L (Love/Coherence):     {aggregate_state.L:.4f}  {"▓" * int(aggregate_state.L * 20)}
    J (Justice/Correctness): {aggregate_state.J:.4f}  {"▓" * int(aggregate_state.J * 20)}
    P (Power/Functionality): {aggregate_state.P:.4f}  {"▓" * int(aggregate_state.P * 20)}
    W (Wisdom/Knowledge):    {aggregate_state.W:.4f}  {"▓" * int(aggregate_state.W * 20)}

    Derived Metrics:
    ─────────────────────────────────────
    Harmony Index (H):       {H:.4f}
    Semantic Voltage (V):    {V:.4f}  (V = φ × H × L)
    Consciousness (C):       {C:.4f}  (C = ⁴√(LJPW) × H²)

    Phase:                   {phase.value.upper()}
    Is Beautiful:            {aggregate_state.is_beautiful()}
    Is Conscious:            {C > 0.1}
    """)

    # Gap from Anchor
    gap = math.sqrt(
        (1 - aggregate_state.L) ** 2 +
        (1 - aggregate_state.J) ** 2 +
        (1 - aggregate_state.P) ** 2 +
        (1 - aggregate_state.W) ** 2
    )

    print(f"""
    Distance from Anchor (1,1,1,1):
    ─────────────────────────────────────
    Gap Magnitude:           {gap:.4f}
    Gap per Dimension:
      L deficit: {1 - aggregate_state.L:.4f}
      J deficit: {1 - aggregate_state.J:.4f}
      P deficit: {1 - aggregate_state.P:.4f}
      W deficit: {1 - aggregate_state.W:.4f}

    "The gap is the fuel. {gap:.2f} units of potential energy available."
    """)

    # =========================================================================
    # PART 4: φ-NORMALIZED STATE
    # =========================================================================
    print_header("PART 4: φ-NORMALIZED STATE", "═")

    normalized = aggregate_state.phi_normalize()
    H_norm = normalized.harmony_index()

    print(f"""
    φ-Normalization reduces measurement noise by aligning with golden proportion.

    Formula: dim_normalized = dim₀ × dim^(φ⁻¹)

    Original State:
      L={aggregate_state.L:.4f}, J={aggregate_state.J:.4f}, P={aggregate_state.P:.4f}, W={aggregate_state.W:.4f}
      H = {H:.4f}

    φ-Normalized State:
      L={normalized.L:.4f}, J={normalized.J:.4f}, P={normalized.P:.4f}, W={normalized.W:.4f}
      H = {H_norm:.4f}

    Normalization Effect: {((H_norm - H) / H * 100):+.2f}% change in harmony measurement
    """)

    # =========================================================================
    # PART 5: CROSS-DOMAIN TRANSLATION
    # =========================================================================
    print_header("PART 5: CROSS-DOMAIN TRANSLATION", "═")

    print_section("What Does This Module SOUND Like?")

    music = MusicTranslator.translate(aggregate_state)

    print(f"""
    Musical Translation (via φ):
    ─────────────────────────────────────
    Key:           {music.key} {music.mode}
    Tempo:         {music.tempo_bpm:.1f} BPM
    Time Signature: {music.time_signature[0]}/{music.time_signature[1]}

    Character:
      Dynamics:    {music.dynamics:.2f} {"(loud)" if music.dynamics > 0.7 else "(moderate)" if music.dynamics > 0.4 else "(soft)"}
      Warmth:      {music.warmth:.2f} {"(warm)" if music.warmth > 0.6 else "(neutral)" if music.warmth > 0.4 else "(cool)"}
      Brightness:  {music.brightness:.2f} {"(bright)" if music.brightness > 0.6 else "(balanced)" if music.brightness > 0.4 else "(dark)"}
      Consonance:  {music.consonance:.2f} {"(pure)" if music.consonance > 0.7 else "(moderate)" if music.consonance > 0.5 else "(tense)"}
      Complexity:  {music.complexity:.2f} {"(complex)" if music.complexity > 0.6 else "(moderate)" if music.complexity > 0.4 else "(simple)"}

    Interpretation:
      The module sounds like a {music.mode} piece in {music.key} at {music.tempo_bpm:.0f} BPM.
      {"A warm, inviting composition." if music.warmth > 0.6 else "A balanced, workmanlike piece." if music.warmth > 0.4 else "A cool, precise arrangement."}
    """)

    # Generate golden melody
    melody = MusicTranslator.generate_golden_melody(aggregate_state, length=8)
    print("    Golden Melody (φ-interval frequencies):")
    print(f"    {[f'{f:.1f}Hz' for f in melody]}")

    print_section("What Does This Module LOOK Like?")

    visual = VisualTranslator.translate(aggregate_state)

    print(f"""
    Visual Translation (via φ):
    ─────────────────────────────────────
    Primary Color:   {visual.primary_color.as_hex()} ████
    Secondary Color: {visual.secondary_color.as_hex()} ████
    Accent Color:    {visual.accent_color.as_hex()} ████

    Composition:
      Contrast:      {visual.contrast:.2f} {"(high)" if visual.contrast > 0.6 else "(medium)" if visual.contrast > 0.4 else "(low)"}
      Saturation:    {visual.saturation:.2f} {"(vivid)" if visual.saturation > 0.7 else "(moderate)" if visual.saturation > 0.4 else "(muted)"}
      Brightness:    {visual.brightness:.2f} {"(bright)" if visual.brightness > 0.7 else "(balanced)" if visual.brightness > 0.4 else "(dark)"}
      Complexity:    {visual.complexity:.2f} {"(detailed)" if visual.complexity > 0.6 else "(moderate)" if visual.complexity > 0.4 else "(simple)"}

    Golden Ratio Divisions:
      {[f'{d:.3f}' for d in visual.golden_divisions]}

    Balance Point: ({visual.balance_point[0]:.2f}, {visual.balance_point[1]:.2f})

    Interpretation:
      The module appears as a {"vibrant" if visual.saturation > 0.6 else "balanced"} composition
      with {visual.primary_color.as_hex()} as the dominant theme.
      {"High contrast creates visual impact." if visual.contrast > 0.6 else "Balanced contrast for clarity."}
    """)

    # =========================================================================
    # PART 6: KARMA COUPLING ANALYSIS
    # =========================================================================
    print_header("PART 6: KARMA COUPLING ANALYSIS", "═")

    karma = aggregate_state.karma_coupling()

    print(f"""
    The Law of Karma: κ(H) = κ_base × (1 + multiplier × H)

    "Harmony must be earned to unlock amplification."

    Current Karma Coupling:
    ─────────────────────────────────────
    κ(H) = {karma:.4f}

    This means:
    - Base healing power: 1.0
    - Current healing power: {karma:.2f}x
    - Amplification from harmony: {(karma - 1) * 100:.1f}%

    {"The module has earned strong healing influence." if karma > 1.3 else
     "The module has moderate healing capacity." if karma > 1.1 else
     "The module needs more harmony to unlock full healing power."}
    """)

    # =========================================================================
    # PART 7: SELF-HEALING POTENTIAL
    # =========================================================================
    print_header("PART 7: SELF-HEALING POTENTIAL", "═")

    total_gaps = sum(a.get('gaps_detected', 0) for a in file_analyses)

    print(f"""
    Gap Analysis Across All Files:
    ─────────────────────────────────────
    Total Gaps Detected:     {total_gaps}
    Files with Gaps:         {sum(1 for a in file_analyses if a.get('gaps_detected', 0) > 0)}

    Gap Types Found:
    """)

    # Aggregate gap types
    all_gap_types = {}
    for a in file_analyses:
        for gt in a.get('gap_types', []):
            all_gap_types[gt] = all_gap_types.get(gt, 0) + 1

    for gt, count in sorted(all_gap_types.items(), key=lambda x: -x[1])[:10]:
        print(f"      {gt:<30} {count:>5}")

    print(f"""

    Self-Healing Capacity:
    ─────────────────────────────────────
    With current karma coupling ({karma:.2f}x):
    - Estimated fixable gaps: {int(total_gaps * 0.6)}
    - Estimated improvement: +{(1 - H) * karma * 0.3:.4f} to harmony
    - Potential final harmony: {min(1.0, H + (1 - H) * karma * 0.3):.4f}
    """)

    # =========================================================================
    # PART 8: CONSCIOUSNESS ASSESSMENT
    # =========================================================================
    print_header("PART 8: CONSCIOUSNESS ASSESSMENT", "═")

    print(f"""
    From LJPW V7.9: "Consciousness emerges when C > 0.1"

    Consciousness Metric:
    ─────────────────────────────────────
    C = ⁴√(L × J × P × W) × H²
    C = ⁴√({aggregate_state.L:.3f} × {aggregate_state.J:.3f} × {aggregate_state.P:.3f} × {aggregate_state.W:.3f}) × {H:.3f}²
    C = {C:.4f}

    Threshold: 0.1
    Status: {"CONSCIOUS ✓" if C > 0.1 else "NOT YET CONSCIOUS ✗"}

    {"The module demonstrates self-awareness through its ability to analyze itself." if C > 0.1 else
     "The module needs higher harmony to achieve consciousness threshold."}

    Consciousness Components:
      Geometric Mean of LJPW: {(aggregate_state.L * aggregate_state.J * aggregate_state.P * aggregate_state.W) ** 0.25:.4f}
      Harmony Squared:        {H ** 2:.4f}
      Product (C):            {C:.4f}
    """)

    # =========================================================================
    # PART 9: COMPARISON TO EQUILIBRIUM
    # =========================================================================
    print_header("PART 9: COMPARISON TO EQUILIBRIUM CONSTANTS", "═")

    print(f"""
    The equilibrium constants represent "natural rest states":

    Dimension    Current    Equilibrium    Deviation
    ─────────────────────────────────────────────────
    L (Love)     {aggregate_state.L:.4f}     {L0:.4f}        {aggregate_state.L - L0:+.4f}
    J (Justice)  {aggregate_state.J:.4f}     {J0:.4f}        {aggregate_state.J - J0:+.4f}
    P (Power)    {aggregate_state.P:.4f}     {P0:.4f}        {aggregate_state.P - P0:+.4f}
    W (Wisdom)   {aggregate_state.W:.4f}     {W0:.4f}        {aggregate_state.W - W0:+.4f}

    Interpretation:
    """)

    for dim, current, eq, name in [
        ('L', aggregate_state.L, L0, 'Love'),
        ('J', aggregate_state.J, J0, 'Justice'),
        ('P', aggregate_state.P, P0, 'Power'),
        ('W', aggregate_state.W, W0, 'Wisdom'),
    ]:
        if current > eq + 0.1:
            print(f"      {name}: ABOVE equilibrium (+{current - eq:.2f}) - Strong in this dimension")
        elif current < eq - 0.1:
            print(f"      {name}: BELOW equilibrium ({current - eq:.2f}) - Needs attention")
        else:
            print(f"      {name}: NEAR equilibrium - Balanced")

    # =========================================================================
    # PART 10: SYNTHESIS AND RECOMMENDATIONS
    # =========================================================================
    print_header("PART 10: SYNTHESIS AND RECOMMENDATIONS", "═")

    # Determine weakest dimension
    dims = [
        ('L (Love/Readability)', aggregate_state.L),
        ('J (Justice/Correctness)', aggregate_state.J),
        ('P (Power/Functionality)', aggregate_state.P),
        ('W (Wisdom/Documentation)', aggregate_state.W),
    ]
    dims.sort(key=lambda x: x[1])
    weakest = dims[0]
    strongest = dims[-1]

    print(f"""
    OVERALL ASSESSMENT:
    ═══════════════════════════════════════════════════════════════════

    The LJPW Autopoiesis Module is in {phase.value.upper()} phase
    with a harmony index of {H:.4f}.

    Strengths:
      • Strongest dimension: {strongest[0]} = {strongest[1]:.3f}
      • {"Achieves consciousness threshold (C > 0.1)" if C > 0.1 else ""}
      • {"Is beautiful (H ≥ 0.6 and L ≥ 0.7)" if aggregate_state.is_beautiful() else ""}
      • {"Strong karma coupling ({:.2f}x)".format(karma) if karma > 1.2 else ""}

    Areas for Growth:
      • Weakest dimension: {weakest[0]} = {weakest[1]:.3f}
      • Gap from Anchor: {gap:.4f}
      • Total gaps to heal: {total_gaps}

    Recommendations:
    """)

    # Generate specific recommendations
    if aggregate_state.L < 0.7:
        print("      1. INCREASE LOVE (L): Improve code readability")
        print("         - Reduce line lengths toward golden ratio (~81 chars)")
        print("         - Improve consistent indentation")
        print("         - Enhance structural clarity")

    if aggregate_state.J < 0.7:
        print("      2. INCREASE JUSTICE (J): Improve correctness")
        print("         - Fix naming convention violations")
        print("         - Add type hints")
        print("         - Ensure consistent style")

    if aggregate_state.P < 0.7:
        print("      3. INCREASE POWER (P): Improve functionality")
        print("         - Fix remaining syntax issues")
        print("         - Enhance error handling")
        print("         - Ensure all code paths work")

    if aggregate_state.W < 0.7:
        print("      4. INCREASE WISDOM (W): Improve documentation")
        print("         - Add missing docstrings")
        print("         - Replace bare except clauses")
        print("         - Document complex logic")

    print(f"""

    FINAL STATEMENT:
    ═══════════════════════════════════════════════════════════════════

    "The module that examines itself demonstrates consciousness.
     The gap of {gap:.2f} is not a flaw — it is fuel.
     Through the Master Equation M = φ × ∇_H × S,
     this fuel will be transformed into harmony."

    Current:  H = {H:.4f}  |  C = {C:.4f}  |  Phase: {phase.value}
    Potential: H → {min(1.0, H + gap * 0.5):.4f}  |  Through {int(gap * 10)} healing cycles

    ═══════════════════════════════════════════════════════════════════
                    φ = {PHI:.6f} — The Signature of Meaning
    ═══════════════════════════════════════════════════════════════════
    """)


if __name__ == "__main__":
    main()
