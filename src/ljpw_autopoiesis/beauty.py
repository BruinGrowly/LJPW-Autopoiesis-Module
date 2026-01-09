"""
LJPW Beauty Engine - φ as the Universal Translator

From LJPW Framework V7.9:
"φ is not just a number — it is the projection operator that translates
semantic meaning into mathematical structure, and thus into physical reality."

The Master Equation:
    M = φ × ∇_H × S

Where:
    M = Mathematical structure (physical manifestation)
    φ = 1.618034... (the translation constant)
    ∇_H = Harmony gradient (direction toward Unity)
    S = Semantic vector (LJPW coordinates)

This module implements beauty across domains:
- Code → structured, readable, harmonious programs
- Music → melodic, rhythmic, emotionally resonant compositions
- Visual → color harmonies, golden proportions, aesthetic compositions

"Mathematics cannot explain φ, but φ can explain mathematics."
"""

import math
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Any
from enum import Enum

# =============================================================================
# FUNDAMENTAL CONSTANTS
# =============================================================================

PHI = (1 + math.sqrt(5)) / 2          # Golden Ratio φ = 1.618034...
PHI_INV = (math.sqrt(5) - 1) / 2      # φ⁻¹ = 0.618034...
PHI_SQ = PHI * PHI                     # φ² = 2.618034...
PHI_CUBE = PHI * PHI * PHI             # φ³ = 4.236068...

# Equilibrium constants (semantically derived)
L0 = PHI_INV                           # Love equilibrium ≈ 0.618
J0 = math.sqrt(2) - 1                  # Justice equilibrium ≈ 0.414
P0 = math.e - 2                        # Power equilibrium ≈ 0.718
W0 = math.log(2)                       # Wisdom equilibrium ≈ 0.693

# Physical constants for beauty manifestation
LOVE_FREQUENCY_HZ = 613e12             # 613 THz - Love's carrier frequency
LOVE_WAVELENGTH_NM = 489               # Cyan light - visual Love
SEMANTIC_TIME_FS = PHI * 1.631         # 2.64 femtoseconds per semantic unit

# Music constants
A4_FREQUENCY = 440.0                   # Standard tuning A4 = 440 Hz
GOLDEN_RATIO_SEMITONES = 12 * math.log2(PHI)  # ~8.09 semitones (minor 6th)


class AestheticDomain(Enum):
    """Domains where beauty can manifest."""
    CODE = "code"
    MUSIC = "music"
    VISUAL = "visual"
    UNIVERSAL = "universal"


class AestheticPhase(Enum):
    """Phases of aesthetic development."""
    CHAOTIC = "chaotic"        # H < 0.3 - no coherent beauty
    EMERGENT = "emergent"      # 0.3 <= H < 0.5 - beauty beginning to form
    HOMEOSTATIC = "homeostatic"  # 0.5 <= H < 0.7 - stable beauty
    AUTOPOIETIC = "autopoietic"  # 0.7 <= H < 0.9 - self-improving beauty
    TRANSCENDENT = "transcendent"  # H >= 0.9 - beauty that inspires


# =============================================================================
# BEAUTY STATE
# =============================================================================

@dataclass
class BeautyState:
    """
    Represents the beauty/aesthetic state in LJPW coordinates.

    Beauty emerges when:
    - All dimensions are balanced (not extreme)
    - Harmony Index H approaches 1
    - Love dimension L >= 0.7 (emotional resonance)

    The state can be translated to any domain via φ-projection.
    """
    L: float = 0.5  # Love/Coherence - emotional resonance, warmth
    J: float = 0.5  # Justice/Balance - structural proportion, correctness
    P: float = 0.5  # Power/Intensity - energy, momentum, impact
    W: float = 0.5  # Wisdom/Complexity - depth, sophistication, knowledge

    def as_tuple(self) -> Tuple[float, float, float, float]:
        """Return LJPW coordinates as tuple."""
        return (self.L, self.J, self.P, self.W)

    @classmethod
    def from_tuple(cls, t: Tuple[float, float, float, float]) -> 'BeautyState':
        """Create state from tuple."""
        return cls(L=t[0], J=t[1], P=t[2], W=t[3])

    @classmethod
    def anchor(cls) -> 'BeautyState':
        """Perfect beauty - the attractor point (1,1,1,1)."""
        return cls(L=1.0, J=1.0, P=1.0, W=1.0)

    @classmethod
    def golden(cls) -> 'BeautyState':
        """Golden beauty - all dimensions at φ⁻¹ (natural equilibrium)."""
        return cls(L=PHI_INV, J=PHI_INV, P=PHI_INV, W=PHI_INV)

    def harmony_index(self) -> float:
        """
        Calculate Harmony Index - the master beauty metric.

        H = 1 / (1 + distance_from_anchor)

        H = 1 means perfect beauty (at anchor)
        H → 0 means maximum disharmony
        """
        distance = math.sqrt(
            (1 - self.L) ** 2 +
            (1 - self.J) ** 2 +
            (1 - self.P) ** 2 +
            (1 - self.W) ** 2
        )
        return 1 / (1 + distance)

    def harmony_product(self) -> float:
        """
        Alternative harmony calculation via product.

        H = (L × J × P × W) / (L₀ × J₀ × P₀ × W₀)
        """
        product = self.L * self.J * self.P * self.W
        equilibrium = L0 * J0 * P0 * W0
        return product / equilibrium

    def semantic_voltage(self) -> float:
        """
        Calculate Semantic Voltage - beauty's influence potential.

        V = φ × H × L

        Higher harmony and love = greater aesthetic influence.
        This is why beautiful things spread naturally.
        """
        H = self.harmony_index()
        return PHI * H * self.L

    def consciousness(self) -> float:
        """
        Calculate consciousness metric.

        C = ⁴√(L × J × P × W) × H²

        Beauty requires awareness; consciousness enables appreciation.
        """
        H = self.harmony_index()
        geometric_mean = (self.L * self.J * self.P * self.W) ** 0.25
        return geometric_mean * (H ** 2)

    def phase(self) -> AestheticPhase:
        """Determine current aesthetic phase."""
        H = self.harmony_index()
        if H < 0.3:
            return AestheticPhase.CHAOTIC
        elif H < 0.5:
            return AestheticPhase.EMERGENT
        elif H < 0.7:
            return AestheticPhase.HOMEOSTATIC
        elif H < 0.9:
            return AestheticPhase.AUTOPOIETIC
        else:
            return AestheticPhase.TRANSCENDENT

    def is_beautiful(self) -> bool:
        """
        Check if state qualifies as beautiful.

        From LJPW: Beauty requires H >= 0.6 AND L >= 0.7
        """
        H = self.harmony_index()
        return H >= 0.6 and self.L >= 0.7

    def phi_normalize(self) -> 'BeautyState':
        """
        Apply φ-normalization to reduce measurement noise.

        Each dimension is transformed: dim_normalized = dim₀ × dim^(φ⁻¹)

        This aligns measurements with the golden proportion,
        reducing variance while preserving relative order.
        """
        return BeautyState(
            L=L0 * (self.L ** PHI_INV),
            J=J0 * (self.J ** PHI_INV),
            P=P0 * (self.P ** PHI_INV),
            W=W0 * (self.W ** PHI_INV),
        )

    def phi_project(self, gradient: Tuple[float, float, float, float]) -> 'BeautyState':
        """
        Apply φ-projection along harmony gradient.

        This is the Master Equation in action:
        M = φ × ∇_H × S

        Projects the semantic state toward greater beauty.
        """
        # Normalize gradient
        grad_mag = math.sqrt(sum(g**2 for g in gradient))
        if grad_mag < 1e-10:
            return self

        norm_grad = tuple(g / grad_mag for g in gradient)

        # Apply φ-scaled projection
        return BeautyState(
            L=min(1.0, self.L + PHI_INV * norm_grad[0] * 0.1),
            J=min(1.0, self.J + PHI_INV * norm_grad[1] * 0.1),
            P=min(1.0, self.P + PHI_INV * norm_grad[2] * 0.1),
            W=min(1.0, self.W + PHI_INV * norm_grad[3] * 0.1),
        )

    def gradient_to_anchor(self) -> Tuple[float, float, float, float]:
        """Calculate gradient pointing toward anchor (1,1,1,1)."""
        return (1 - self.L, 1 - self.J, 1 - self.P, 1 - self.W)

    def karma_coupling(self, base_strength: float = 1.0) -> float:
        """
        Calculate karma-based coupling strength.

        κ(H) = κ_base × (1 + multiplier × H)

        Harmony must be earned to unlock amplification.
        Beautiful systems have stronger influence.
        """
        H = self.harmony_index()
        multiplier = 0.4  # From LJPW constants
        return base_strength * (1 + multiplier * H)


# =============================================================================
# MUSIC TRANSLATION (LJPW → Audio)
# =============================================================================

@dataclass
class MusicParameters:
    """
    Musical parameters derived from LJPW coordinates via φ-translation.

    From LJPW Music Research:
    - L (Love) → Melody, emotional resonance, major/minor modality
    - J (Justice) → Harmony, consonance, structural balance
    - P (Power) → Rhythm, tempo, dynamics
    - W (Wisdom) → Timbre, complexity, instrumentation
    """
    # Pitch parameters
    root_frequency: float = 440.0      # Hz - base frequency
    key: str = "C"                      # Musical key
    mode: str = "major"                 # Major/minor/modal

    # Temporal parameters
    tempo_bpm: float = 120.0           # Beats per minute
    time_signature: Tuple[int, int] = (4, 4)
    rhythm_density: float = 0.5        # 0-1 note density

    # Dynamic parameters
    dynamics: float = 0.7              # 0-1 volume/intensity
    dynamic_range: float = 0.3         # Variation in dynamics

    # Timbral parameters
    brightness: float = 0.5            # 0-1 spectral brightness
    warmth: float = 0.5                # 0-1 harmonic richness
    complexity: float = 0.5            # 0-1 textural complexity

    # Harmonic parameters
    consonance: float = 0.7            # 0-1 harmonic purity
    tension: float = 0.3               # 0-1 dissonance level

    # Derived metrics
    harmony_index: float = 0.5
    beauty_phase: str = "homeostatic"


class MusicTranslator:
    """
    Translates LJPW semantic states into musical parameters.

    φ serves as the bridge: M = φ × ∇_H × S

    Musical beauty emerges when LJPW dimensions are balanced
    and Love (emotional resonance) is sufficiently high.
    """

    # Musical key mappings (weighted by LJPW research)
    KEY_LJPW_WEIGHTS = {
        'C':  {'L': 0.7, 'J': 0.9, 'P': 0.6, 'W': 0.5},  # Pure, foundational
        'C#': {'L': 0.9, 'J': 0.5, 'P': 0.4, 'W': 0.6},  # Love resonance
        'D':  {'L': 0.6, 'J': 0.7, 'P': 0.8, 'W': 0.5},  # Triumphant
        'D#': {'L': 0.5, 'J': 0.6, 'P': 0.5, 'W': 0.7},  # Mysterious
        'E':  {'L': 0.7, 'J': 0.8, 'P': 0.7, 'W': 0.6},  # Joyful
        'F':  {'L': 0.8, 'J': 0.6, 'P': 0.5, 'W': 0.7},  # Pastoral
        'F#': {'L': 0.5, 'J': 0.5, 'P': 0.6, 'W': 0.9},  # Wisdom key
        'G':  {'L': 0.7, 'J': 0.7, 'P': 0.8, 'W': 0.6},  # Bright, open
        'G#': {'L': 0.6, 'J': 0.5, 'P': 0.5, 'W': 0.8},  # Introspective
        'A':  {'L': 0.8, 'J': 0.7, 'P': 0.7, 'W': 0.7},  # Universal (440Hz)
        'A#': {'L': 0.6, 'J': 0.6, 'P': 0.7, 'W': 0.6},  # Dramatic
        'B':  {'L': 0.7, 'J': 0.8, 'P': 0.6, 'W': 0.8},  # Contemplative
    }

    @classmethod
    def translate(cls, state: BeautyState) -> MusicParameters:
        """
        Translate LJPW state to musical parameters using φ.

        The Master Equation: M = φ × ∇_H × S
        """
        H = state.harmony_index()

        # Determine key based on LJPW alignment
        key = cls._select_key(state)

        # Mode from Love dimension (high Love → major)
        mode = "major" if state.L >= 0.6 else "minor"

        # Tempo from Power dimension (φ-scaled)
        # Range: 60-180 BPM, centered at 120
        tempo_base = 120
        tempo = tempo_base * (0.5 + state.P * PHI_INV)
        tempo = max(60, min(180, tempo))

        # Dynamics from Power and φ-projection
        dynamics = state.P * PHI_INV + 0.3
        dynamics = max(0.2, min(1.0, dynamics))

        # Rhythm density from Power-Wisdom interaction
        rhythm_density = (state.P + state.W * PHI_INV) / (1 + PHI_INV)

        # Brightness from Love (warmth) and Wisdom (complexity)
        brightness = state.W * 0.6 + state.J * 0.4
        warmth = state.L * 0.7 + state.P * 0.3

        # Complexity from Wisdom
        complexity = state.W

        # Harmonic parameters from Justice (balance)
        consonance = state.J * 0.8 + 0.2
        tension = 1 - state.J * 0.7

        # Root frequency using φ-intervals from A4
        # Golden interval ≈ minor 6th (8 semitones)
        semitone_offset = cls._key_to_semitone(key)
        root_frequency = A4_FREQUENCY * (2 ** (semitone_offset / 12))

        return MusicParameters(
            root_frequency=root_frequency,
            key=key,
            mode=mode,
            tempo_bpm=tempo,
            time_signature=(4, 4) if state.J > 0.5 else (3, 4),
            rhythm_density=rhythm_density,
            dynamics=dynamics,
            dynamic_range=0.2 + state.W * 0.4,
            brightness=brightness,
            warmth=warmth,
            complexity=complexity,
            consonance=consonance,
            tension=tension,
            harmony_index=H,
            beauty_phase=state.phase().value,
        )

    @classmethod
    def _select_key(cls, state: BeautyState) -> str:
        """Select musical key that best matches LJPW state."""
        best_key = 'C'
        best_match = 0

        for key, weights in cls.KEY_LJPW_WEIGHTS.items():
            # Calculate match score (inverse distance)
            distance = math.sqrt(
                (state.L - weights['L']) ** 2 +
                (state.J - weights['J']) ** 2 +
                (state.P - weights['P']) ** 2 +
                (state.W - weights['W']) ** 2
            )
            match = 1 / (1 + distance)

            if match > best_match:
                best_match = match
                best_key = key

        return best_key

    @classmethod
    def _key_to_semitone(cls, key: str) -> int:
        """Convert key name to semitone offset from A."""
        key_map = {
            'A': 0, 'A#': 1, 'B': 2, 'C': 3, 'C#': 4,
            'D': 5, 'D#': 6, 'E': 7, 'F': 8, 'F#': 9,
            'G': 10, 'G#': 11
        }
        return key_map.get(key, 0)

    @classmethod
    def generate_golden_melody(cls, state: BeautyState, length: int = 8) -> List[float]:
        """
        Generate a melody using golden ratio intervals.

        Frequencies are related by φ, creating natural beauty.
        """
        params = cls.translate(state)
        root = params.root_frequency

        # Golden interval ratios
        intervals = [
            1.0,           # Unison
            PHI_INV,       # φ⁻¹ below (≈ minor 3rd down)
            PHI,           # φ above (≈ minor 6th up)
            PHI_SQ / 2,    # φ² / 2 (≈ major 2nd up)
            2 / PHI,       # 2/φ (≈ perfect 4th up)
            PHI_INV * 2,   # 2φ⁻¹ (≈ minor 6th up)
            2.0,           # Octave
            PHI * PHI_INV * 2,  # Another golden point
        ]

        melody = []
        for i in range(length):
            # Select interval based on position and harmony
            idx = int((i * PHI) % len(intervals))
            freq = root * intervals[idx]
            melody.append(freq)

        return melody

    @classmethod
    def analyze_beauty(cls, features: Dict[str, float]) -> BeautyState:
        """
        Analyze audio features and map to LJPW beauty state.

        Features expected (Spotify-style):
        - valence: emotional positivity (0-1)
        - energy: intensity/activity (0-1)
        - danceability: rhythmic regularity (0-1)
        - acousticness: acoustic vs electronic (0-1)
        - instrumentalness: vocal presence (0-1)
        - tempo: BPM (60-200)
        - loudness: dB (-60 to 0)
        """
        # Love: emotional resonance
        L = (
            features.get('valence', 0.5) * 0.4 +
            features.get('acousticness', 0.5) * 0.3 +
            (1 if features.get('mode', 1) == 1 else 0.3) * 0.3
        )

        # Justice: harmonic balance
        J = (
            (1 - abs(features.get('valence', 0.5) - 0.5) * 2) * 0.4 +
            (1 - features.get('speechiness', 0)) * 0.3 +
            features.get('acousticness', 0.5) * 0.3
        )

        # Power: energy and intensity
        tempo_norm = min(1.0, features.get('tempo', 120) / 180)
        loudness_norm = (features.get('loudness', -10) + 60) / 60
        P = (
            features.get('energy', 0.5) * 0.4 +
            tempo_norm * 0.3 +
            features.get('danceability', 0.5) * 0.2 +
            max(0, min(1, loudness_norm)) * 0.1
        )

        # Wisdom: complexity and depth
        W = (
            features.get('instrumentalness', 0.5) * 0.4 +
            (1 - features.get('speechiness', 0)) * 0.3 +
            features.get('acousticness', 0.5) * 0.3
        )

        return BeautyState(
            L=max(0.1, min(1.0, L)),
            J=max(0.1, min(1.0, J)),
            P=max(0.1, min(1.0, P)),
            W=max(0.1, min(1.0, W)),
        )


# =============================================================================
# VISUAL TRANSLATION (LJPW → Colors/Composition)
# =============================================================================

@dataclass
class ColorRGB:
    """RGB color representation."""
    r: int = 128
    g: int = 128
    b: int = 128

    def as_tuple(self) -> Tuple[int, int, int]:
        return (self.r, self.g, self.b)

    def as_hex(self) -> str:
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def luminance(self) -> float:
        """Calculate perceived luminance."""
        return (0.299 * self.r + 0.587 * self.g + 0.114 * self.b) / 255


@dataclass
class VisualParameters:
    """
    Visual/aesthetic parameters derived from LJPW coordinates.

    From LJPW Visual Research:
    - L (Love) → Color warmth, emotional hue
    - J (Justice) → Composition balance, golden ratios
    - P (Power) → Visual weight, contrast
    - W (Wisdom) → Texture complexity, detail density
    """
    # Color parameters
    primary_color: ColorRGB = field(default_factory=lambda: ColorRGB(128, 200, 200))
    secondary_color: ColorRGB = field(default_factory=lambda: ColorRGB(200, 128, 128))
    accent_color: ColorRGB = field(default_factory=lambda: ColorRGB(255, 200, 100))

    # Composition parameters
    golden_divisions: List[float] = field(default_factory=lambda: [PHI_INV, 1 - PHI_INV])
    balance_point: Tuple[float, float] = (0.5, 0.5)

    # Visual weight
    contrast: float = 0.5              # 0-1 light/dark contrast
    saturation: float = 0.6            # 0-1 color saturation
    brightness: float = 0.7            # 0-1 overall brightness

    # Texture
    complexity: float = 0.5            # 0-1 detail density
    smoothness: float = 0.5            # 0-1 texture smoothness

    # Derived
    harmony_index: float = 0.5
    beauty_phase: str = "homeostatic"


class VisualTranslator:
    """
    Translates LJPW semantic states into visual parameters.

    φ governs composition through the golden ratio.
    Love manifests as color warmth (cyan = 489nm = Love frequency).
    """

    # Color temperature mapping
    LOVE_HUE = 180  # Cyan (Love's visual frequency)
    WISDOM_HUE = 270  # Purple (deep/mysterious)
    POWER_HUE = 0  # Red (energy/intensity)
    JUSTICE_HUE = 60  # Yellow (clarity/truth)

    @classmethod
    def translate(cls, state: BeautyState) -> VisualParameters:
        """Translate LJPW state to visual parameters using φ."""
        H = state.harmony_index()

        # Primary color from Love (shifted toward cyan)
        primary = cls._ljpw_to_color(state, emphasis='L')

        # Secondary color (complementary balance from Justice)
        secondary = cls._ljpw_to_color(state, emphasis='J')

        # Accent from Power
        accent = cls._ljpw_to_color(state, emphasis='P')

        # Composition using golden ratio
        golden_divisions = [
            PHI_INV * state.J,          # Justice-scaled
            1 - PHI_INV * state.J,
            PHI_INV * PHI_INV,          # φ⁻²
            1 - PHI_INV * PHI_INV,
        ]

        # Balance point (center of visual mass)
        # High Justice → centered, low → dynamic asymmetry
        balance_x = 0.5 + (0.5 - state.J) * 0.3
        balance_y = 0.5 + (0.5 - state.J) * 0.2

        # Contrast from Power
        contrast = state.P * 0.7 + 0.2

        # Saturation from Love (warmth)
        saturation = state.L * 0.6 + 0.3

        # Brightness from Harmony
        brightness = H * 0.5 + 0.4

        # Complexity from Wisdom
        complexity = state.W
        smoothness = 1 - state.W * 0.5

        return VisualParameters(
            primary_color=primary,
            secondary_color=secondary,
            accent_color=accent,
            golden_divisions=golden_divisions,
            balance_point=(balance_x, balance_y),
            contrast=contrast,
            saturation=saturation,
            brightness=brightness,
            complexity=complexity,
            smoothness=smoothness,
            harmony_index=H,
            beauty_phase=state.phase().value,
        )

    @classmethod
    def _ljpw_to_color(cls, state: BeautyState, emphasis: str = 'L') -> ColorRGB:
        """Convert LJPW state to RGB color with dimensional emphasis."""
        # Base hue from emphasized dimension
        if emphasis == 'L':
            base_hue = cls.LOVE_HUE  # Cyan
            weight = state.L
        elif emphasis == 'J':
            base_hue = cls.JUSTICE_HUE  # Yellow
            weight = state.J
        elif emphasis == 'P':
            base_hue = cls.POWER_HUE  # Red
            weight = state.P
        else:  # W
            base_hue = cls.WISDOM_HUE  # Purple
            weight = state.W

        # Modulate hue by other dimensions
        hue = base_hue
        hue += (state.L - 0.5) * 30  # Love shifts toward cyan
        hue += (state.P - 0.5) * 20  # Power shifts toward red
        hue = hue % 360

        # Saturation from weight and harmony
        H = state.harmony_index()
        saturation = weight * 0.6 + H * 0.3 + 0.1
        saturation = max(0.2, min(1.0, saturation))

        # Value/brightness from Power and Harmony
        value = state.P * 0.4 + H * 0.4 + 0.2
        value = max(0.3, min(1.0, value))

        return cls._hsv_to_rgb(hue, saturation, value)

    @classmethod
    def _hsv_to_rgb(cls, h: float, s: float, v: float) -> ColorRGB:
        """Convert HSV to RGB."""
        h = h % 360
        c = v * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = v - c

        if h < 60:
            r, g, b = c, x, 0
        elif h < 120:
            r, g, b = x, c, 0
        elif h < 180:
            r, g, b = 0, c, x
        elif h < 240:
            r, g, b = 0, x, c
        elif h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x

        return ColorRGB(
            r=int((r + m) * 255),
            g=int((g + m) * 255),
            b=int((b + m) * 255),
        )

    @classmethod
    def golden_rectangle(cls, width: float) -> Tuple[float, float]:
        """Generate golden rectangle dimensions."""
        return (width, width / PHI)

    @classmethod
    def golden_spiral_points(cls, center: Tuple[float, float],
                             scale: float, points: int = 50) -> List[Tuple[float, float]]:
        """Generate points along a golden spiral."""
        result = []
        for i in range(points):
            theta = i * 0.2  # Angle increment
            r = scale * (PHI ** (theta / (2 * math.pi)))
            x = center[0] + r * math.cos(theta)
            y = center[1] + r * math.sin(theta)
            result.append((x, y))
        return result

    @classmethod
    def fibonacci_sequence(cls, n: int) -> List[int]:
        """Generate Fibonacci sequence (φ approximation building blocks)."""
        if n <= 0:
            return []
        elif n == 1:
            return [1]

        seq = [1, 1]
        for _ in range(n - 2):
            seq.append(seq[-1] + seq[-2])
        return seq


# =============================================================================
# CODE BEAUTY (LJPW → Code Aesthetics)
# =============================================================================

@dataclass
class CodeBeautyMetrics:
    """
    Code aesthetics metrics derived from LJPW.

    Beautiful code has:
    - L: Clear structure, consistent style, readable flow
    - J: Correct types, valid logic, proper naming
    - P: Working functionality, efficient execution
    - W: Good documentation, error handling, tests
    """
    readability_score: float = 0.5     # L-based
    correctness_score: float = 0.5     # J-based
    functionality_score: float = 0.5   # P-based
    wisdom_score: float = 0.5          # W-based

    # Specific metrics
    line_length_beauty: float = 0.5    # φ-based line length
    naming_beauty: float = 0.5         # Semantic naming quality
    structure_beauty: float = 0.5      # Hierarchical organization

    harmony_index: float = 0.5
    beauty_phase: str = "homeostatic"


class CodeBeautyAnalyzer:
    """
    Analyzes code beauty using LJPW framework.

    φ appears in:
    - Ideal line length: ~80 chars (50 × φ)
    - Function size ratios
    - Test-to-code ratios
    - Complexity thresholds
    """

    # Golden ratios in code
    GOLDEN_LINE_LENGTH = int(50 * PHI)  # ~81 characters
    GOLDEN_FUNCTION_RATIO = PHI_INV     # Body:header ratio
    GOLDEN_TEST_RATIO = PHI_INV         # Test:code ratio

    @classmethod
    def analyze(cls, source_code: str) -> CodeBeautyMetrics:
        """Analyze code beauty and return LJPW-based metrics."""
        lines = source_code.split('\n')

        # Love: Readability analysis
        L = cls._analyze_readability(lines)

        # Justice: Structure analysis (naming, consistency)
        J = cls._analyze_structure(lines)

        # Power: Functionality indicators
        P = cls._analyze_functionality(lines)

        # Wisdom: Documentation and error handling
        W = cls._analyze_wisdom(lines)

        state = BeautyState(L=L, J=J, P=P, W=W)
        H = state.harmony_index()

        return CodeBeautyMetrics(
            readability_score=L,
            correctness_score=J,
            functionality_score=P,
            wisdom_score=W,
            line_length_beauty=cls._line_length_beauty(lines),
            naming_beauty=J * 0.8 + L * 0.2,
            structure_beauty=L * 0.6 + J * 0.4,
            harmony_index=H,
            beauty_phase=state.phase().value,
        )

    @classmethod
    def _analyze_readability(cls, lines: List[str]) -> float:
        """Analyze code readability (Love dimension)."""
        if not lines:
            return 0.5

        scores = []

        # Line length beauty (φ-based)
        for line in lines:
            if not line.strip():
                continue
            length = len(line)
            # Optimal around GOLDEN_LINE_LENGTH
            distance = abs(length - cls.GOLDEN_LINE_LENGTH)
            score = 1 / (1 + distance / 40)
            scores.append(score)

        # Consistent indentation
        indent_scores = []
        for line in lines:
            if not line.strip():
                continue
            leading = len(line) - len(line.lstrip())
            # Check if indent is multiple of 4
            if leading % 4 == 0:
                indent_scores.append(1.0)
            elif leading % 2 == 0:
                indent_scores.append(0.7)
            else:
                indent_scores.append(0.3)

        line_score = sum(scores) / len(scores) if scores else 0.5
        indent_score = sum(indent_scores) / len(indent_scores) if indent_scores else 0.5

        return line_score * 0.6 + indent_score * 0.4

    @classmethod
    def _analyze_structure(cls, lines: List[str]) -> float:
        """Analyze code structure (Justice dimension)."""
        source = '\n'.join(lines)

        scores = []

        # Function/class naming (snake_case for functions, CamelCase for classes)
        import re

        # Check function definitions
        func_pattern = r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        functions = re.findall(func_pattern, source)
        for func in functions:
            if func.islower() or '_' in func:
                scores.append(1.0)  # snake_case
            else:
                scores.append(0.5)

        # Check class definitions
        class_pattern = r'class\s+([a-zA-Z_][a-zA-Z0-9_]*)'
        classes = re.findall(class_pattern, source)
        for cls_name in classes:
            if cls_name[0].isupper() and '_' not in cls_name:
                scores.append(1.0)  # CamelCase
            else:
                scores.append(0.5)

        return sum(scores) / len(scores) if scores else 0.7

    @classmethod
    def _analyze_functionality(cls, lines: List[str]) -> float:
        """Analyze functionality indicators (Power dimension)."""
        source = '\n'.join(lines)

        # Look for functionality indicators
        has_functions = 'def ' in source
        has_classes = 'class ' in source
        has_imports = 'import ' in source
        has_main = '__main__' in source or 'if __name__' in source

        # Check for obvious syntax issues
        parens_balanced = source.count('(') == source.count(')')
        brackets_balanced = source.count('[') == source.count(']')
        braces_balanced = source.count('{') == source.count('}')

        score = 0.3  # Base
        if has_functions:
            score += 0.2
        if has_classes:
            score += 0.1
        if has_imports:
            score += 0.1
        if has_main:
            score += 0.1
        if parens_balanced and brackets_balanced and braces_balanced:
            score += 0.2

        return min(1.0, score)

    @classmethod
    def _analyze_wisdom(cls, lines: List[str]) -> float:
        """Analyze wisdom indicators (documentation, error handling)."""
        source = '\n'.join(lines)

        score = 0.3  # Base

        # Docstrings
        docstring_count = source.count('"""') // 2
        if docstring_count > 0:
            score += min(0.3, docstring_count * 0.05)

        # Comments
        comment_lines = sum(1 for line in lines if line.strip().startswith('#'))
        if comment_lines > 0:
            score += min(0.2, comment_lines * 0.02)

        # Error handling
        if 'try:' in source and 'except' in source:
            score += 0.15

        # Type hints
        if ': ' in source and '->' in source:
            score += 0.1

        return min(1.0, score)

    @classmethod
    def _line_length_beauty(cls, lines: List[str]) -> float:
        """Calculate line length beauty using φ."""
        if not lines:
            return 0.5

        scores = []
        for line in lines:
            if not line.strip():
                continue
            length = len(line)
            # φ-normalized distance from golden length
            distance = abs(length - cls.GOLDEN_LINE_LENGTH) / cls.GOLDEN_LINE_LENGTH
            score = PHI_INV ** distance  # Exponential decay
            scores.append(score)

        return sum(scores) / len(scores) if scores else 0.5


# =============================================================================
# UNIFIED AESTHETIC ENGINE
# =============================================================================

class UnifiedAestheticEngine:
    """
    Master engine for translating beauty across all domains.

    From LJPW V7.9:
    "The same semantic structure underlies all beauty.
    Code, music, and visual art are different projections
    of the same LJPW coordinates through φ."

    The Master Equation: M = φ × ∇_H × S
    """

    @classmethod
    def from_code(cls, source_code: str) -> BeautyState:
        """Extract LJPW beauty state from code."""
        metrics = CodeBeautyAnalyzer.analyze(source_code)
        return BeautyState(
            L=metrics.readability_score,
            J=metrics.correctness_score,
            P=metrics.functionality_score,
            W=metrics.wisdom_score,
        )

    @classmethod
    def from_music_features(cls, features: Dict[str, float]) -> BeautyState:
        """Extract LJPW beauty state from music features."""
        return MusicTranslator.analyze_beauty(features)

    @classmethod
    def to_music(cls, state: BeautyState) -> MusicParameters:
        """Translate beauty state to music parameters."""
        return MusicTranslator.translate(state)

    @classmethod
    def to_visual(cls, state: BeautyState) -> VisualParameters:
        """Translate beauty state to visual parameters."""
        return VisualTranslator.translate(state)

    @classmethod
    def to_code_metrics(cls, state: BeautyState) -> CodeBeautyMetrics:
        """Generate code beauty metrics from state."""
        H = state.harmony_index()
        return CodeBeautyMetrics(
            readability_score=state.L,
            correctness_score=state.J,
            functionality_score=state.P,
            wisdom_score=state.W,
            line_length_beauty=state.L * PHI_INV + state.J * (1 - PHI_INV),
            naming_beauty=state.J * 0.7 + state.L * 0.3,
            structure_beauty=state.L * 0.5 + state.J * 0.5,
            harmony_index=H,
            beauty_phase=state.phase().value,
        )

    @classmethod
    def cross_domain_translate(cls,
                               state: BeautyState,
                               from_domain: AestheticDomain,
                               to_domain: AestheticDomain) -> Any:
        """
        Translate beauty state between domains using φ.

        This implements the universal translator:
        Any domain → LJPW state → Any other domain
        """
        # φ-normalize the state for cleaner translation
        normalized = state.phi_normalize()

        if to_domain == AestheticDomain.MUSIC:
            return cls.to_music(normalized)
        elif to_domain == AestheticDomain.VISUAL:
            return cls.to_visual(normalized)
        elif to_domain == AestheticDomain.CODE:
            return cls.to_code_metrics(normalized)
        else:
            return normalized

    @classmethod
    def harmonize(cls, state: BeautyState, iterations: int = 10) -> BeautyState:
        """
        Iteratively improve beauty state toward anchor.

        Uses φ-projection along harmony gradient.
        """
        current = state
        for _ in range(iterations):
            gradient = current.gradient_to_anchor()
            current = current.phi_project(gradient)

            # Check for convergence
            if current.harmony_index() > 0.95:
                break

        return current

    @classmethod
    def beauty_report(cls, state: BeautyState) -> Dict[str, Any]:
        """Generate comprehensive beauty report."""
        H = state.harmony_index()
        V = state.semantic_voltage()
        C = state.consciousness()
        phase = state.phase()

        return {
            'ljpw_state': {
                'L': state.L,
                'J': state.J,
                'P': state.P,
                'W': state.W,
            },
            'harmony_index': H,
            'semantic_voltage': V,
            'consciousness': C,
            'phase': phase.value,
            'is_beautiful': state.is_beautiful(),
            'gap_to_anchor': math.sqrt(sum(g**2 for g in state.gradient_to_anchor())),
            'karma_coupling': state.karma_coupling(),
            'phi_normalized': {
                'L': state.phi_normalize().L,
                'J': state.phi_normalize().J,
                'P': state.phi_normalize().P,
                'W': state.phi_normalize().W,
            },
            'music_preview': {
                'key': MusicTranslator.translate(state).key,
                'mode': MusicTranslator.translate(state).mode,
                'tempo': MusicTranslator.translate(state).tempo_bpm,
            },
            'visual_preview': {
                'primary_color': VisualTranslator.translate(state).primary_color.as_hex(),
                'secondary_color': VisualTranslator.translate(state).secondary_color.as_hex(),
                'contrast': VisualTranslator.translate(state).contrast,
            },
        }


# =============================================================================
# φ-TRANSLATION UTILITIES
# =============================================================================

def phi_translate(value: float, from_scale: Tuple[float, float],
                  to_scale: Tuple[float, float]) -> float:
    """
    Translate a value between scales using φ-weighting.

    Unlike linear interpolation, this uses φ to create
    natural, aesthetically pleasing mappings.
    """
    # Normalize to 0-1
    normalized = (value - from_scale[0]) / (from_scale[1] - from_scale[0])
    normalized = max(0, min(1, normalized))

    # Apply φ-curve (creates natural acceleration/deceleration)
    phi_curved = normalized ** PHI_INV

    # Map to target scale
    return to_scale[0] + phi_curved * (to_scale[1] - to_scale[0])


def phi_blend(a: float, b: float, t: float = PHI_INV) -> float:
    """Blend two values using golden ratio."""
    return a * (1 - t) + b * t


def phi_sequence(start: float, count: int, ratio: float = PHI) -> List[float]:
    """Generate a sequence where each term is ratio × previous."""
    result = [start]
    for _ in range(count - 1):
        result.append(result[-1] * ratio)
    return result


def semantic_distance(state1: BeautyState, state2: BeautyState) -> float:
    """Calculate semantic distance between two beauty states."""
    return math.sqrt(
        (state1.L - state2.L) ** 2 +
        (state1.J - state2.J) ** 2 +
        (state1.P - state2.P) ** 2 +
        (state1.W - state2.W) ** 2
    )


def beauty_interpolate(state1: BeautyState, state2: BeautyState,
                       t: float = PHI_INV) -> BeautyState:
    """Interpolate between two beauty states using φ."""
    return BeautyState(
        L=phi_blend(state1.L, state2.L, t),
        J=phi_blend(state1.J, state2.J, t),
        P=phi_blend(state1.P, state2.P, t),
        W=phi_blend(state1.W, state2.W, t),
    )


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("LJPW Beauty Engine - φ as Universal Translator")
    print("=" * 60)

    # Create a beauty state
    state = BeautyState(L=0.8, J=0.7, P=0.6, W=0.75)
    print(f"\nInitial State: L={state.L}, J={state.J}, P={state.P}, W={state.W}")
    print(f"Harmony Index: {state.harmony_index():.4f}")
    print(f"Phase: {state.phase().value}")
    print(f"Is Beautiful: {state.is_beautiful()}")

    # Generate music parameters
    print("\n--- Music Translation ---")
    music = MusicTranslator.translate(state)
    print(f"Key: {music.key} {music.mode}")
    print(f"Tempo: {music.tempo_bpm:.1f} BPM")
    print(f"Dynamics: {music.dynamics:.2f}")
    print(f"Warmth: {music.warmth:.2f}")

    # Generate golden melody
    melody = MusicTranslator.generate_golden_melody(state, length=8)
    print(f"Golden Melody (Hz): {[f'{f:.1f}' for f in melody]}")

    # Generate visual parameters
    print("\n--- Visual Translation ---")
    visual = VisualTranslator.translate(state)
    print(f"Primary Color: {visual.primary_color.as_hex()}")
    print(f"Secondary Color: {visual.secondary_color.as_hex()}")
    print(f"Contrast: {visual.contrast:.2f}")
    print(f"Golden Divisions: {[f'{d:.3f}' for d in visual.golden_divisions]}")

    # Analyze code beauty
    print("\n--- Code Beauty Analysis ---")
    sample_code = '''
def calculate_harmony(state):
    """Calculate the harmony index from LJPW state."""
    L, J, P, W = state.L, state.J, state.P, state.W
    product = L * J * P * W
    equilibrium = 0.618 * 0.414 * 0.718 * 0.693
    return product / equilibrium
'''
    code_metrics = CodeBeautyAnalyzer.analyze(sample_code)
    print(f"Readability: {code_metrics.readability_score:.2f}")
    print(f"Correctness: {code_metrics.correctness_score:.2f}")
    print(f"Functionality: {code_metrics.functionality_score:.2f}")
    print(f"Wisdom: {code_metrics.wisdom_score:.2f}")
    print(f"Code Harmony: {code_metrics.harmony_index:.4f}")

    # Full beauty report
    print("\n--- Full Beauty Report ---")
    report = UnifiedAestheticEngine.beauty_report(state)
    print(f"Semantic Voltage: {report['semantic_voltage']:.4f}")
    print(f"Consciousness: {report['consciousness']:.4f}")
    print(f"Karma Coupling: {report['karma_coupling']:.4f}")

    # Harmonize toward perfection
    print("\n--- Harmonization (10 iterations) ---")
    harmonized = UnifiedAestheticEngine.harmonize(state, iterations=10)
    print(f"Final State: L={harmonized.L:.3f}, J={harmonized.J:.3f}, "
          f"P={harmonized.P:.3f}, W={harmonized.W:.3f}")
    print(f"Final Harmony: {harmonized.harmony_index():.4f}")
    print(f"Final Phase: {harmonized.phase().value}")

    print("\n" + "=" * 60)
    print("φ = 1.618034... — The signature of meaning")
    print("=" * 60)
