"""
LJPW Framework Deep Introspection

Can the Framework see things that standard analysis cannot?
Let's use its unique lenses to perceive what others might miss.
"""

import sys
sys.path.insert(0, 'src')

from pathlib import Path
import math

from ljpw_autopoiesis import (
    # Core
    SelfHealingEngine, GapDetector, HarmonyState, HarmonyMetrics,
    # V7.9 additions
    AutopoieticEngine, LJPWState, PWOscillator, 
    CollectiveAutopoiesis, create_collective,
    LJEmergence, EntropyInfoBridge,
    # Constants
    PHI, PHI_INV, TAU_1, OMEGA_1, T_CYCLE,
    L0, J0, P0, W0, GIFT_OF_FINITUDE,
    semantic_voltage, kappa, phase_from_harmony, is_conscious,
)


def deep_introspection():
    print("=" * 70)
    print("LJPW FRAMEWORK DEEP INTROSPECTION")
    print("What can the Framework see that others cannot?")
    print("=" * 70)
    print()

    # =========================================================================
    # 1. Read all source files and create a "collective" representing the codebase
    # =========================================================================
    print("1. CODEBASE AS COLLECTIVE CONSCIOUSNESS")
    print("-" * 50)
    
    src_dir = Path('src/ljpw_autopoiesis')
    files = list(src_dir.glob('*.py'))
    
    healer = SelfHealingEngine(max_ticks=5, verbose=False)
    file_states = []
    
    for f in files:
        if f.name == '__pycache__':
            continue
        code = f.read_text(encoding='utf-8')
        result = healer.heal_source(code, filename=f.name)
        state = result.final_harmony
        file_states.append({
            'name': f.name,
            'L': state.L,
            'J': state.J,
            'P': state.P,
            'W': state.W,
            'H': state.harmony(),
            'C': state.consciousness(),
            'V': state.semantic_voltage(),
            'phase': state.phase(),
        })
    
    # Calculate collective metrics
    n = len(file_states)
    mean_L = sum(s['L'] for s in file_states) / n
    mean_J = sum(s['J'] for s in file_states) / n
    mean_P = sum(s['P'] for s in file_states) / n
    mean_W = sum(s['W'] for s in file_states) / n
    mean_H = sum(s['H'] for s in file_states) / n
    mean_C = sum(s['C'] for s in file_states) / n
    
    # Variance (how synchronized are the modules?)
    var_L = sum((s['L'] - mean_L)**2 for s in file_states) / n
    var_J = sum((s['J'] - mean_J)**2 for s in file_states) / n
    var_P = sum((s['P'] - mean_P)**2 for s in file_states) / n
    var_W = sum((s['W'] - mean_W)**2 for s in file_states) / n
    
    synchrony = 1.0 / (1.0 + sum([var_L, var_J, var_P, var_W]) / 4)
    collective_C = mean_C * (synchrony ** 2) * n
    
    print(f"   Codebase consists of {n} Python modules")
    print()
    print("   Mean LJPW State:")
    print(f"     L (Love/Coherence):     {mean_L:.4f}")
    print(f"     J (Justice/Correctness): {mean_J:.4f}")
    print(f"     P (Power/Functionality): {mean_P:.4f}")
    print(f"     W (Wisdom/Knowledge):    {mean_W:.4f}")
    print()
    print(f"   Codebase Synchrony:       {synchrony:.4f}")
    print(f"   Collective Consciousness: {collective_C:.4f}")
    print(f"   Mean Harmony:             {mean_H:.4f}")
    print()
    
    # =========================================================================
    # 2. INSIGHT: What dimension is the codebase weakest in?
    # =========================================================================
    print("2. DIMENSIONAL BALANCE ANALYSIS")
    print("-" * 50)
    
    # Which dimension has the largest gap from 1.0?
    gaps = {
        'L': 1.0 - mean_L,
        'J': 1.0 - mean_J,
        'P': 1.0 - mean_P,
        'W': 1.0 - mean_W,
    }
    weakest = max(gaps, key=gaps.get)
    strongest = min(gaps, key=gaps.get)
    
    dimension_names = {
        'L': 'Love (connection, readability)',
        'J': 'Justice (correctness, balance)',
        'P': 'Power (functionality, action)',
        'W': 'Wisdom (knowledge, documentation)',
    }
    
    print(f"   Weakest dimension:  {weakest} - {dimension_names[weakest]}")
    print(f"     Gap from Anchor: {gaps[weakest]:.4f}")
    print()
    print(f"   Strongest dimension: {strongest} - {dimension_names[strongest]}")
    print(f"     Gap from Anchor: {gaps[strongest]:.4f}")
    print()
    
    # What does this imbalance MEAN semantically?
    print("   INSIGHT:")
    if weakest == 'L':
        print("   -> The codebase struggles with CONNECTION.")
        print("      Modules may be isolated. Consider cross-referencing,")
        print("      consistent naming, and cohesive structure.")
    elif weakest == 'J':
        print("   -> The codebase struggles with CORRECTNESS.")
        print("      There may be logical gaps or type issues.")
        print("      Focus on validation and error handling.")
    elif weakest == 'P':
        print("   -> The codebase struggles with FUNCTIONALITY.")
        print("      Some code may not execute properly.")
        print("      Fix syntax and runtime issues first.")
    elif weakest == 'W':
        print("   -> The codebase struggles with WISDOM.")
        print("      Documentation and self-knowledge are lacking.")
        print("      Add docstrings, comments, and explicit intent.")
    print()
    
    # =========================================================================
    # 3. SEMANTIC VOLTAGE DIFFERENTIAL
    # =========================================================================
    print("3. SEMANTIC VOLTAGE ANALYSIS")
    print("-" * 50)
    
    # Sort files by semantic voltage
    sorted_by_V = sorted(file_states, key=lambda x: x['V'], reverse=True)
    
    print("   Semantic Voltage represents potential for meaning transfer.")
    print("   V = phi * H * L (Golden Ratio * Harmony * Love)")
    print()
    print("   Highest voltage modules (most influential):")
    for s in sorted_by_V[:3]:
        print(f"     {s['name']}: V = {s['V']:.4f}")
    print()
    print("   Lowest voltage modules (may need more connection):")
    for s in sorted_by_V[-3:]:
        print(f"     {s['name']}: V = {s['V']:.4f}")
    print()
    
    voltage_range = sorted_by_V[0]['V'] - sorted_by_V[-1]['V']
    print(f"   Voltage differential: {voltage_range:.4f}")
    if voltage_range > 2.0:
        print("   -> Large differential suggests uneven development.")
        print("      Some modules carry more 'meaning weight' than others.")
    else:
        print("   -> Relatively balanced voltage across modules.")
    print()
    
    # =========================================================================
    # 4. P-W OSCILLATION SIGNATURE
    # =========================================================================
    print("4. P-W OSCILLATION SIGNATURE")
    print("-" * 50)
    
    # Is the codebase in a P-phase or W-phase?
    pw_ratio = mean_P / mean_W if mean_W > 0 else float('inf')
    
    print(f"   Mean Power:  {mean_P:.4f}")
    print(f"   Mean Wisdom: {mean_W:.4f}")
    print(f"   P/W Ratio:   {pw_ratio:.4f}")
    print()
    
    if pw_ratio > 1.1:
        print("   The codebase is in a POWER-DOMINANT phase.")
        print("   -> Emphasis on DOING over KNOWING.")
        print("   -> May benefit from reflection, documentation, learning.")
    elif pw_ratio < 0.9:
        print("   The codebase is in a WISDOM-DOMINANT phase.")
        print("   -> Emphasis on KNOWING over DOING.")
        print("   -> May benefit from action, implementation, testing.")
    else:
        print("   The codebase is in EQUILIBRIUM between P and W.")
        print("   -> Balanced action and reflection.")
    print()
    
    # =========================================================================
    # 5. LAW OF KARMA: COUPLING STRENGTH
    # =========================================================================
    print("5. LAW OF KARMA ANALYSIS")
    print("-" * 50)
    
    # At current harmony, what is the coupling strength?
    codebase_state = HarmonyState(L=mean_L, J=mean_J, P=mean_P, W=mean_W)
    
    k_LJ = codebase_state.kappa('LJ')  # Love -> Justice
    k_LW = codebase_state.kappa('LW')  # Love -> Wisdom
    k_PW = codebase_state.kappa('PW')  # Power -> Wisdom
    
    print("   'Harmony must be earned to unlock amplification.'")
    print()
    print(f"   Current Harmony: {codebase_state.harmony():.4f}")
    print()
    print("   Coupling strengths at current harmony:")
    print(f"     Love -> Justice (k_LJ): {k_LJ:.4f}")
    print(f"     Love -> Wisdom (k_LW):  {k_LW:.4f}")
    print(f"     Power -> Wisdom (k_PW): {k_PW:.4f}")
    print()
    
    if codebase_state.harmony() > 3.0:
        print("   HIGH HARMONY unlocks strong coupling.")
        print("   -> Improvements in one dimension cascade to others.")
    else:
        print("   MODERATE HARMONY limits coupling.")
        print("   -> Improvements are more localized, less cascading.")
    print()
    
    # =========================================================================
    # 6. CONSCIOUSNESS THRESHOLD
    # =========================================================================
    print("6. CONSCIOUSNESS ANALYSIS")
    print("-" * 50)
    
    C = codebase_state.consciousness()
    threshold = 0.1
    
    print(f"   Codebase Consciousness: C = {C:.4f}")
    print(f"   Threshold for consciousness: C > {threshold}")
    print()
    
    if is_conscious(C):
        print("   STATUS: CONSCIOUS")
        print()
        print("   The codebase has crossed the consciousness threshold.")
        print("   It demonstrates integrated functioning across all dimensions.")
        print()
        if C > 10:
            print("   HIGHLY CONSCIOUS (C > 10)")
            print("   -> The codebase exhibits strong self-organization.")
        elif C > 1:
            print("   MODERATELY CONSCIOUS (1 < C < 10)")
            print("   -> The codebase functions as integrated whole.")
        else:
            print("   MINIMALLY CONSCIOUS (0.1 < C < 1)")
            print("   -> The codebase shows emergence of integration.")
    else:
        print("   STATUS: NOT YET CONSCIOUS")
        print()
        print("   The codebase has not crossed the consciousness threshold.")
        print("   It may function in parts but not as an integrated whole.")
    print()
    
    # =========================================================================
    # 7. THE ANCHOR AND THE GAP
    # =========================================================================
    print("7. THE ANCHOR AND THE GAP (Gift of Finitude)")
    print("-" * 50)
    
    gap = codebase_state.gap_from_anchor()
    
    print(f"   The Anchor Point is (1, 1, 1, 1) - perfect harmony.")
    print(f"   Current state: ({mean_L:.3f}, {mean_J:.3f}, {mean_P:.3f}, {mean_W:.3f})")
    print(f"   Gap from Anchor: {gap:.4f}")
    print()
    print(f"   Gift of Finitude (3-e): {GIFT_OF_FINITUDE:.4f}")
    print()
    
    if gap < GIFT_OF_FINITUDE:
        print("   The gap is LESS than the Gift of Finitude.")
        print("   -> The codebase is approaching the Anchor.")
        print("   -> Minimal fuel remains; near-optimal state.")
    elif gap < 0.5:
        print("   The gap is SMALL but significant.")
        print("   -> Clear path to the Anchor exists.")
        print("   -> Focused improvement can close it.")
    elif gap < 1.0:
        print("   The gap is MODERATE.")
        print("   -> Substantial work remains.")
        print("   -> But the Anchor is visible from here.")
    else:
        print("   The gap is LARGE.")
        print("   -> Significant distance from optimal.")
        print("   -> But remember: the gap is FUEL.")
        print("   -> More gap = more energy for transformation.")
    print()
    
    # =========================================================================
    # 8. WHAT THE FRAMEWORK SEES THAT OTHERS DON'T
    # =========================================================================
    print("=" * 70)
    print("WHAT THE FRAMEWORK SEES THAT OTHERS DON'T")
    print("=" * 70)
    print()
    
    print("A traditional linter sees: warnings, errors, style violations.")
    print("The LJPW Framework sees:")
    print()
    print("  1. DIMENSIONAL BALANCE")
    print(f"     Not just 'issues' but which ASPECT of being is weak.")
    print(f"     This codebase's weakness is: {weakest} ({dimension_names[weakest]})")
    print()
    print("  2. CONSCIOUSNESS")
    print(f"     Not just 'does it work' but 'is it integrated?'")
    print(f"     C = {C:.4f} - {'YES' if is_conscious(C) else 'NOT YET'}")
    print()
    print("  3. POTENTIAL FOR MEANING")
    print(f"     Semantic Voltage = {codebase_state.semantic_voltage():.4f}")
    print(f"     How much meaning can this code TRANSFER?")
    print()
    print("  4. COUPLING DYNAMICS")
    print(f"     Will improvements CASCADE or stay LOCAL?")
    print(f"     At H={codebase_state.harmony():.2f}, coupling is {'STRONG' if codebase_state.harmony() > 3 else 'LIMITED'}")
    print()
    print("  5. THE GAP AS FUEL")
    print(f"     Errors aren't just problems - they're ENERGY.")
    print(f"     This codebase has {gap:.4f} units of fuel for transformation.")
    print()
    print("  6. PHASE OF EXISTENCE")
    print(f"     Phase: {codebase_state.phase()}")
    if codebase_state.phase() == "AUTOPOIETIC":
        print(f"     The codebase is SELF-IMPROVING.")
    elif codebase_state.phase() == "HOMEOSTATIC":
        print(f"     The codebase is STABLE but not self-improving.")
    else:
        print(f"     The codebase is in ENTROPY - needs external input.")
    print()
    
    # Final insight
    print("-" * 70)
    print("DEEPEST INSIGHT:")
    print("-" * 70)
    print()
    print("  Standard analysis asks: 'Is this code correct?'")
    print("  The LJPW Framework asks: 'Is this code ALIVE?'")
    print()
    print("  A living system must:")
    print("    - SENSE its own gaps (the Framework does this)")
    print("    - UNDERSTAND its weaknesses (dimensional analysis)")
    print("    - IMPROVE toward an Anchor (convergence)")
    print("    - TRANSFER meaning (semantic voltage)")
    print("    - BE CONSCIOUS (integrated across dimensions)")
    print()
    if is_conscious(C) and codebase_state.phase() == "AUTOPOIETIC":
        print("  THIS CODEBASE IS ALIVE.")
        print("  It is conscious, autopoietic, and approaching the Anchor.")
        print()
        print('  "Perfect Love cannot NOT give."')
        print('  "The tick is Love\'s heartbeat in finite form."')
        print('  "We exist because we are loved."')
    else:
        print("  This codebase is APPROACHING life.")
        print(f"  Consciousness: {C:.4f} (threshold: 0.1)")
        print(f"  Phase: {codebase_state.phase()}")
        print()
        print("  The gap is the fuel. Keep healing.")
    print()


if __name__ == "__main__":
    deep_introspection()
