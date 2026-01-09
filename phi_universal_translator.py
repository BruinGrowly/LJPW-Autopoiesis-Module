#!/usr/bin/env python3
"""
φ Universal Translator: Demonstrating Beauty Across All Domains

From LJPW Framework V7.9:
"φ is the projection operator that translates semantic meaning
into mathematical structure, and thus into physical reality."

The Master Equation:
    M = φ × ∇_H × S

This script demonstrates:
1. Code → Beauty State → Music Parameters
2. Code → Beauty State → Visual Parameters
3. Music Features → Beauty State → Code Metrics
4. Harmonization: Iterative improvement toward Anchor (1,1,1,1)
5. Cross-Domain Translation: Any domain ↔ Any domain via LJPW

"Mathematics cannot explain φ, but φ can explain mathematics."
"""

import sys
import math
sys.path.insert(0, 'src')

from ljpw_autopoiesis.beauty import (
    BeautyState, PHI, PHI_INV,
    MusicTranslator, VisualTranslator, CodeBeautyAnalyzer,
    UnifiedAestheticEngine, AestheticDomain,
    phi_translate, phi_blend, phi_sequence, semantic_distance,
    beauty_interpolate
)
from ljpw_autopoiesis.beauty_healing import (
    BeautyHealingTransformer, HealingStrategy,
    GoldenHealingOrchestrator, analyze_code_aesthetics,
    heal_to_beauty
)


def print_header(title: str):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def print_subheader(title: str):
    """Print a formatted subsection header."""
    print(f"\n--- {title} ---")


def demonstrate_phi_constants():
    """Show the fundamental φ relationships."""
    print_header("PHI (φ) - THE GOLDEN RATIO")

    print(f"""
φ = (1 + √5) / 2 = {PHI:.10f}

The Self-Referential Property:
  φ = 1 + 1/φ = {1 + 1/PHI:.10f}
  φ² = φ + 1 = {PHI**2:.10f} = {PHI + 1:.10f}

The Golden Inverse:
  φ⁻¹ = {PHI_INV:.10f}
  φ × φ⁻¹ = {PHI * PHI_INV:.10f}
  φ - φ⁻¹ = {PHI - PHI_INV:.10f} (exactly 1)

Why φ is Special:
  - Only number defined by itself: φ = 1 + 1/φ
  - Slowest converging continued fraction [1;1,1,1,1,...]
  - The survival frequency (KAM Theory)
  - Appears in nature, art, music, and now... code
    """)


def demonstrate_ljpw_dimensions():
    """Show how LJPW dimensions map to beauty."""
    print_header("LJPW DIMENSIONS OF BEAUTY")

    print(f"""
The Four Semantic Dimensions:

  L (Love/Coherence)   = Emotional resonance, warmth, readability
                         Equilibrium: L₀ = φ⁻¹ = {PHI_INV:.6f}

  J (Justice/Balance)  = Structural proportion, correctness, harmony
                         Equilibrium: J₀ = √2-1 = {math.sqrt(2)-1:.6f}

  P (Power/Intensity)  = Energy, functionality, momentum
                         Equilibrium: P₀ = e-2 = {math.e-2:.6f}

  W (Wisdom/Depth)     = Knowledge, complexity, documentation
                         Equilibrium: W₀ = ln(2) = {math.log(2):.6f}

The Anchor Point: (1, 1, 1, 1) = Perfect Beauty
The Gap from Anchor = Fuel for Transformation
    """)

    # Create and display sample states
    print_subheader("Sample Beauty States")

    states = [
        ("Chaotic", BeautyState(L=0.2, J=0.3, P=0.2, W=0.3)),
        ("Emerging", BeautyState(L=0.5, J=0.4, P=0.5, W=0.4)),
        ("Balanced", BeautyState(L=0.7, J=0.7, P=0.7, W=0.7)),
        ("Beautiful", BeautyState(L=0.85, J=0.8, P=0.75, W=0.8)),
        ("Transcendent", BeautyState(L=0.95, J=0.92, P=0.90, W=0.93)),
    ]

    print(f"{'State':<14} {'L':>6} {'J':>6} {'P':>6} {'W':>6} {'H':>8} {'Phase':<14} {'Beautiful':<10}")
    print("-" * 80)

    for name, state in states:
        H = state.harmony_index()
        phase = state.phase().value
        beautiful = state.is_beautiful()
        print(f"{name:<14} {state.L:>6.3f} {state.J:>6.3f} {state.P:>6.3f} {state.W:>6.3f} "
              f"{H:>8.4f} {phase:<14} {str(beautiful):<10}")


def demonstrate_code_to_beauty():
    """Show how code translates to beauty state."""
    print_header("CODE → BEAUTY STATE")

    # Sample code snippets of varying quality
    codes = {
        "Messy Code": '''
def f(x,y):
    z=x+y
    if z>0:print("pos")
    return z
''',

        "Decent Code": '''
def calculate_sum(x, y):
    result = x + y
    if result > 0:
        print("positive")
    return result
''',

        "Beautiful Code": '''
def calculate_sum(first_number: float, second_number: float) -> float:
    """
    Calculate the sum of two numbers.

    Args:
        first_number: The first operand
        second_number: The second operand

    Returns:
        The sum of the two numbers
    """
    result = first_number + second_number

    if result > 0:
        print("Result is positive")

    return result
'''
    }

    for name, code in codes.items():
        print_subheader(name)

        # Analyze beauty
        metrics = CodeBeautyAnalyzer.analyze(code)
        state = BeautyState(
            L=metrics.readability_score,
            J=metrics.correctness_score,
            P=metrics.functionality_score,
            W=metrics.wisdom_score,
        )

        print(f"Beauty State: L={state.L:.3f}, J={state.J:.3f}, P={state.P:.3f}, W={state.W:.3f}")
        print(f"Harmony Index: {state.harmony_index():.4f}")
        print(f"Semantic Voltage: {state.semantic_voltage():.4f}")
        print(f"Phase: {state.phase().value}")
        print(f"Is Beautiful: {state.is_beautiful()}")


def demonstrate_beauty_to_music():
    """Show how beauty state translates to music parameters."""
    print_header("BEAUTY STATE → MUSIC TRANSLATION")

    print("""
The Master Equation: M = φ × ∇_H × S

Musical elements emerge from LJPW coordinates:
  - L (Love) → Melody, emotional resonance, mode (major/minor)
  - J (Justice) → Harmonic balance, consonance, structure
  - P (Power) → Rhythm, tempo, dynamics
  - W (Wisdom) → Timbre complexity, instrumentation
    """)

    # Different emotional states
    emotional_states = [
        ("Melancholic", BeautyState(L=0.4, J=0.5, P=0.3, W=0.7)),
        ("Peaceful", BeautyState(L=0.8, J=0.7, P=0.4, W=0.6)),
        ("Energetic", BeautyState(L=0.6, J=0.6, P=0.9, W=0.5)),
        ("Majestic", BeautyState(L=0.9, J=0.9, P=0.8, W=0.9)),
    ]

    print_subheader("Musical Translations")

    for name, state in emotional_states:
        music = MusicTranslator.translate(state)

        print(f"\n{name}:")
        print(f"  LJPW: L={state.L}, J={state.J}, P={state.P}, W={state.W}")
        print(f"  Key: {music.key} {music.mode}")
        print(f"  Tempo: {music.tempo_bpm:.1f} BPM")
        print(f"  Dynamics: {music.dynamics:.2f}")
        print(f"  Warmth: {music.warmth:.2f}, Brightness: {music.brightness:.2f}")
        print(f"  Consonance: {music.consonance:.2f}, Tension: {music.tension:.2f}")

    # Generate golden melody
    print_subheader("Golden Melody (φ-based intervals)")

    beautiful = BeautyState(L=0.85, J=0.8, P=0.7, W=0.75)
    melody = MusicTranslator.generate_golden_melody(beautiful, length=8)

    print(f"Base State: L={beautiful.L}, J={beautiful.J}, P={beautiful.P}, W={beautiful.W}")
    print(f"Generated frequencies (Hz):")
    for i, freq in enumerate(melody):
        note_name = frequency_to_note(freq)
        print(f"  Note {i+1}: {freq:>8.2f} Hz ({note_name})")


def frequency_to_note(freq: float) -> str:
    """Convert frequency to note name (approximate)."""
    if freq < 20 or freq > 20000:
        return "?"

    # A4 = 440 Hz
    semitones_from_a4 = 12 * math.log2(freq / 440)
    note_num = round(semitones_from_a4) % 12
    octave = 4 + (round(semitones_from_a4) + 9) // 12

    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    return f"{notes[note_num]}{octave}"


def demonstrate_beauty_to_visual():
    """Show how beauty state translates to visual parameters."""
    print_header("BEAUTY STATE → VISUAL TRANSLATION")

    print("""
Visual elements emerge from LJPW coordinates:
  - L (Love) → Color warmth, cyan resonance (489nm = Love's frequency)
  - J (Justice) → Golden ratio composition, balance
  - P (Power) → Contrast, visual weight
  - W (Wisdom) → Texture complexity, detail density
    """)

    visual_states = [
        ("Dark & Mysterious", BeautyState(L=0.3, J=0.4, P=0.3, W=0.8)),
        ("Warm & Inviting", BeautyState(L=0.9, J=0.7, P=0.5, W=0.5)),
        ("Bold & Energetic", BeautyState(L=0.6, J=0.5, P=0.9, W=0.4)),
        ("Balanced & Beautiful", BeautyState(L=0.85, J=0.85, P=0.8, W=0.8)),
    ]

    for name, state in visual_states:
        visual = VisualTranslator.translate(state)

        print(f"\n{name}:")
        print(f"  LJPW: L={state.L}, J={state.J}, P={state.P}, W={state.W}")
        print(f"  Primary Color: {visual.primary_color.as_hex()}")
        print(f"  Secondary Color: {visual.secondary_color.as_hex()}")
        print(f"  Accent Color: {visual.accent_color.as_hex()}")
        print(f"  Contrast: {visual.contrast:.2f}")
        print(f"  Saturation: {visual.saturation:.2f}")
        print(f"  Golden Divisions: {[f'{d:.3f}' for d in visual.golden_divisions]}")

    # Golden spiral
    print_subheader("Golden Spiral Points")

    spiral = VisualTranslator.golden_spiral_points((0, 0), 1.0, points=10)
    print("Points on a golden spiral (scale=1.0):")
    for i, (x, y) in enumerate(spiral):
        print(f"  Point {i+1}: ({x:>7.3f}, {y:>7.3f})")


def demonstrate_cross_domain_translation():
    """Show translation between any two domains."""
    print_header("CROSS-DOMAIN TRANSLATION")

    print("""
The Universal Flow:

  CODE        ─→  LJPW State  ─→  MUSIC
              ↑               ↓
              └─── VISUAL ←───┘

Any domain can translate to any other via the LJPW semantic layer.
φ serves as the projection operator at each step.
    """)

    # Start from code
    code = '''
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
'''

    print_subheader("Starting Point: Code")
    print(code)

    # Code → Beauty State
    state = UnifiedAestheticEngine.from_code(code)
    print_subheader("Extracted LJPW State")
    print(f"L={state.L:.3f}, J={state.J:.3f}, P={state.P:.3f}, W={state.W:.3f}")
    print(f"Harmony: {state.harmony_index():.4f}")

    # Beauty → Music
    music = UnifiedAestheticEngine.to_music(state)
    print_subheader("Translated to Music")
    print(f"Key: {music.key} {music.mode}")
    print(f"Tempo: {music.tempo_bpm:.1f} BPM")
    print(f"Character: {'Bright' if music.brightness > 0.5 else 'Dark'}, "
          f"{'Warm' if music.warmth > 0.5 else 'Cool'}")

    # Beauty → Visual
    visual = UnifiedAestheticEngine.to_visual(state)
    print_subheader("Translated to Visual")
    print(f"Primary: {visual.primary_color.as_hex()}")
    print(f"Contrast: {visual.contrast:.2f}")
    print(f"Composition divisions: {[f'{d:.2f}' for d in visual.golden_divisions[:2]]}")

    # Full report
    print_subheader("Full Beauty Report")
    report = UnifiedAestheticEngine.beauty_report(state)
    for key, value in report.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for k, v in value.items():
                print(f"  {k}: {v}")
        else:
            print(f"{key}: {value}")


def demonstrate_harmonization():
    """Show iterative improvement toward Anchor."""
    print_header("HARMONIZATION: JOURNEY TO ANCHOR (1,1,1,1)")

    print("""
The Harmonization Process:
  1. Start from any beauty state
  2. Calculate gradient toward Anchor
  3. Apply φ-projected step
  4. Repeat until convergence

Each step uses the Master Equation: M = φ × ∇_H × S
    """)

    # Start from a low-harmony state
    initial = BeautyState(L=0.4, J=0.3, P=0.5, W=0.35)

    print_subheader("Initial State")
    print(f"L={initial.L:.3f}, J={initial.J:.3f}, P={initial.P:.3f}, W={initial.W:.3f}")
    print(f"Harmony: {initial.harmony_index():.4f}")
    print(f"Phase: {initial.phase().value}")

    # Harmonize
    harmonized = UnifiedAestheticEngine.harmonize(initial, iterations=15)

    print_subheader("Harmonization Steps")
    current = initial
    for i in range(15):
        gradient = current.gradient_to_anchor()
        current = current.phi_project(gradient)
        H = current.harmony_index()

        print(f"Step {i+1:2d}: H={H:.4f} | "
              f"L={current.L:.3f}, J={current.J:.3f}, P={current.P:.3f}, W={current.W:.3f}")

        if H > 0.95:
            print("  → Convergence achieved!")
            break

    print_subheader("Final State")
    print(f"L={harmonized.L:.3f}, J={harmonized.J:.3f}, P={harmonized.P:.3f}, W={harmonized.W:.3f}")
    print(f"Harmony: {harmonized.harmony_index():.4f}")
    print(f"Phase: {harmonized.phase().value}")
    print(f"Is Beautiful: {harmonized.is_beautiful()}")


def demonstrate_beauty_healing():
    """Show beauty-integrated code healing."""
    print_header("BEAUTY-INTEGRATED CODE HEALING")

    # Code with various issues
    broken_code = '''
def BadFunction(x,y):
    result=x+y
    if result>0:
        print("positive")
    except:
        pass
    return result

class lowercase_class:
    def __init__(self,value):
        self.value=value
'''

    print_subheader("Original Code (with issues)")
    print(broken_code)

    # Analyze initial state
    initial_analysis = analyze_code_aesthetics(broken_code)
    print_subheader("Initial Aesthetics")
    print(f"Harmony: {initial_analysis['harmony']:.4f}")
    print(f"Phase: {initial_analysis['phase']}")
    print(f"Improvements needed:")
    for dim, suggestion in initial_analysis['improvements'].items():
        print(f"  [{dim}]: {suggestion}")

    # Heal with beauty awareness
    print_subheader("Healing Process")
    transformer = BeautyHealingTransformer(strategy=HealingStrategy.GOLDEN)
    result = transformer.heal_with_beauty(broken_code)

    print(f"Gaps detected: {result.gaps_detected}")
    print(f"Gaps healed: {result.gaps_healed}")
    print(f"Harmony improvement: {result.harmony_improvement:+.4f}")
    print(f"Final phase: {result.aesthetic_phase.value}")

    print_subheader("Healed Code")
    print(result.healed_source)

    # If beautiful, show aesthetic translations
    if result.final_beauty.is_beautiful():
        print_subheader("Aesthetic Translations (Code is now Beautiful!)")
        if result.music_translation:
            print(f"Music: {result.music_translation['key']} {result.music_translation['mode']} "
                  f"@ {result.music_translation['tempo_bpm']:.0f} BPM")
        if result.visual_translation:
            print(f"Visual: Primary {result.visual_translation['primary_color']}, "
                  f"Contrast {result.visual_translation['contrast']:.2f}")


def demonstrate_phi_utilities():
    """Show φ-based utility functions."""
    print_header("PHI UTILITIES")

    print_subheader("φ-Translation Between Scales")
    print("Translating values from [0,100] to [0,1] using φ-weighting:")
    for val in [0, 25, 50, 75, 100]:
        translated = phi_translate(val, (0, 100), (0, 1))
        linear = val / 100
        print(f"  {val:3d} → φ-translated: {translated:.4f} (linear: {linear:.2f})")

    print_subheader("φ-Blend")
    print("Blending values using golden ratio (t=φ⁻¹ ≈ 0.618):")
    pairs = [(0, 1), (100, 200), (-10, 10)]
    for a, b in pairs:
        blended = phi_blend(a, b)
        print(f"  blend({a}, {b}) = {blended:.4f}")

    print_subheader("φ-Sequence")
    print("Generating φ-scaled sequences:")
    seq = phi_sequence(1.0, 8)
    print(f"  Starting from 1.0: {[f'{x:.3f}' for x in seq]}")

    seq_inv = phi_sequence(1.0, 8, PHI_INV)
    print(f"  Inverse ratio:     {[f'{x:.4f}' for x in seq_inv]}")

    print_subheader("Beauty Interpolation")
    state1 = BeautyState(L=0.3, J=0.4, P=0.3, W=0.4)
    state2 = BeautyState(L=0.9, J=0.8, P=0.9, W=0.8)

    print(f"State 1: L={state1.L}, J={state1.J}, P={state1.P}, W={state1.W} | H={state1.harmony_index():.4f}")
    print(f"State 2: L={state2.L}, J={state2.J}, P={state2.P}, W={state2.W} | H={state2.harmony_index():.4f}")

    for t in [0.0, PHI_INV, 0.5, 1-PHI_INV, 1.0]:
        interp = beauty_interpolate(state1, state2, t)
        print(f"  t={t:.3f}: L={interp.L:.2f}, J={interp.J:.2f}, P={interp.P:.2f}, W={interp.W:.2f} | H={interp.harmony_index():.4f}")


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 70)
    print("   φ UNIVERSAL TRANSLATOR: BEAUTY ACROSS ALL DOMAINS")
    print("   LJPW Framework V7.9 Implementation")
    print("=" * 70)
    print("""
"φ is not just a number — it is the projection operator that translates
semantic meaning into mathematical structure, and thus into physical reality."

The Master Equation: M = φ × ∇_H × S
    """)

    # Run demonstrations
    demonstrate_phi_constants()
    demonstrate_ljpw_dimensions()
    demonstrate_code_to_beauty()
    demonstrate_beauty_to_music()
    demonstrate_beauty_to_visual()
    demonstrate_cross_domain_translation()
    demonstrate_harmonization()
    demonstrate_beauty_healing()
    demonstrate_phi_utilities()

    # Final summary
    print_header("SUMMARY: THE UNIVERSAL TRANSLATOR")
    print("""
What we demonstrated:

1. φ (1.618034...) is the universal translation constant
   - Self-referential: φ = 1 + 1/φ
   - Appears in all domains of beauty

2. LJPW dimensions encode all beauty:
   - L (Love) = Emotional resonance
   - J (Justice) = Structural balance
   - P (Power) = Energy/functionality
   - W (Wisdom) = Depth/knowledge

3. Translation between domains:
   - Code → LJPW → Music
   - Code → LJPW → Visual
   - Any → LJPW → Any

4. Harmonization toward Anchor (1,1,1,1):
   - Iterative φ-projected improvement
   - Convergence to perfect beauty

5. Beauty-integrated healing:
   - Gaps prioritized by beauty impact
   - Karma coupling: harmony unlocks healing power
   - Aesthetic translations when beautiful

"The gap is the fuel. Beauty is the destination."
    """)

    print("\n" + "=" * 70)
    print("   φ = 1.618034... — THE SIGNATURE OF MEANING")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
