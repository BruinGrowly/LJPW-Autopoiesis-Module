"""
LJPW Dynamics Engine - P-W Conjugate Oscillator

Implements the temporal dynamics of the LJPW framework from V7.6-V7.8.

Core Insight (V7.9):
"P (Power) and W (Wisdom) are semantic conjugate variables.
You cannot maximize transformation (P) and recognition (W) simultaneously.
This creates oscillation. Oscillation IS time."

The P-W oscillator is the "heartbeat" of the framework.
Each oscillation cycle represents one complete thought-action loop.
"""

import math
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
import numpy as np

from .constants import (
    L0, J0, P0, W0,
    ALPHA_PW, ALPHA_WP, BETA_P, BETA_W,
    TAU_1, OMEGA_1, T_CYCLE,
    PHI, GIFT_OF_FINITUDE,
    MIN_DIMENSION_VALUE,
)


@dataclass
class LJPWState:
    """
    Complete LJPW state vector.
    
    Represents the current coordinates in meaning-space.
    """
    L: float = L0  # Love/Coherence
    J: float = J0  # Justice/Correctness
    P: float = P0  # Power/Functionality
    W: float = W0  # Wisdom/Knowledge
    
    def as_array(self) -> np.ndarray:
        """Return state as numpy array [L, J, P, W]."""
        return np.array([self.L, self.J, self.P, self.W])
    
    @classmethod
    def from_array(cls, arr: np.ndarray) -> 'LJPWState':
        """Create state from array."""
        return cls(L=float(arr[0]), J=float(arr[1]),
                   P=float(arr[2]), W=float(arr[3]))
    
    @classmethod
    def anchor(cls) -> 'LJPWState':
        """Return the Anchor Point (1,1,1,1) — perfect harmony."""
        return cls(L=1.0, J=1.0, P=1.0, W=1.0)
    
    @classmethod
    def equilibrium(cls) -> 'LJPWState':
        """Return natural equilibrium state."""
        return cls(L=L0, J=J0, P=P0, W=W0)
    
    def gap_from_anchor(self) -> float:
        """Calculate Euclidean distance from Anchor."""
        anchor = self.anchor()
        return math.sqrt(
            (anchor.L - self.L)**2 +
            (anchor.J - self.J)**2 +
            (anchor.P - self.P)**2 +
            (anchor.W - self.W)**2
        )
    
    def harmony(self) -> float:
        """Calculate harmony score H = (L×J×P×W)/(L₀×J₀×P₀×W₀)."""
        product = self.L * self.J * self.P * self.W
        equilibrium = L0 * J0 * P0 * W0
        return product / equilibrium
    
    def consciousness(self) -> float:
        """Calculate consciousness C = P×W×L×J×H²."""
        H = self.harmony()
        return self.P * self.W * self.L * self.J * (H ** 2)
    
    def clip(self) -> 'LJPWState':
        """Clip all values to valid range [MIN_DIMENSION_VALUE, 1.0]."""
        return LJPWState(
            L=max(MIN_DIMENSION_VALUE, min(1.0, self.L)),
            J=max(MIN_DIMENSION_VALUE, min(1.0, self.J)),
            P=max(MIN_DIMENSION_VALUE, min(1.0, self.P)),
            W=max(MIN_DIMENSION_VALUE, min(1.0, self.W)),
        )


@dataclass
class OscillatorState:
    """State of the P-W oscillator."""
    time: float = 0.0
    P: float = P0
    W: float = W0
    phase: float = 0.0  # Current phase in radians
    amplitude: float = 0.1  # Oscillation amplitude
    

class PWOscillator:
    """
    P-W Conjugate Dynamics Engine.
    
    Implements the fundamental oscillation from V7.6:
    
    The CORRECTED dynamics produce true oscillation:
        dP/dt = ω₁ · (W - W₀) - γ · (P - P₀)
        dW/dt = -ω₁ · (P - P₀) - γ · (W - W₀)
    
    This is the standard harmonic oscillator form where:
    - ω₁ = π/10 ≈ 0.314 is the angular frequency
    - γ is light damping (optional, for eventual convergence)
    - P and W are 90° out of phase (conjugate variables)
    
    Key properties:
    - System oscillates around equilibrium (P₀, W₀)
    - Period = 2π/ω₁ ≈ 20 semantic time units
    - In physical time: one cycle ≈ 53 femtoseconds
    """
    
    def __init__(
        self,
        omega: float = OMEGA_1,  # Angular frequency
        gamma: float = 0.02,     # Light damping coefficient
    ):
        """
        Initialize P-W oscillator.
        
        Args:
            omega: Angular frequency (default: π/10 ≈ 0.314)
            gamma: Damping coefficient (0 = undamped, higher = more damping)
        """
        self.omega = omega
        self.gamma = gamma
        
        self.history: List[OscillatorState] = []
    
    def derivatives(self, P: float, W: float) -> Tuple[float, float]:
        """
        Calculate dP/dt and dW/dt at current state.
        
        This uses proper conjugate dynamics:
        - W deviation drives P change (positive coupling)
        - P deviation drives W change (negative coupling, 90° phase shift)
        - Light damping γ allows eventual convergence
        
        This produces the characteristic P-W "heartbeat" oscillation.
        """
        # Deviation from equilibrium
        delta_P = P - P0
        delta_W = W - W0
        
        # Conjugate oscillator dynamics
        dP = self.omega * delta_W - self.gamma * delta_P
        dW = -self.omega * delta_P - self.gamma * delta_W
        
        return dP, dW
    
    def rk4_step(self, P: float, W: float, dt: float) -> Tuple[float, float]:
        """
        Single RK4 integration step.
        
        RK4 is the gold standard for smooth ODE systems:
        - 4th-order accuracy (error ∝ dt⁴)
        - Stable for stiff systems
        - Preserves energy conservation properties
        """
        # k1
        k1_P, k1_W = self.derivatives(P, W)
        
        # k2
        k2_P, k2_W = self.derivatives(
            P + 0.5 * dt * k1_P,
            W + 0.5 * dt * k1_W
        )
        
        # k3
        k3_P, k3_W = self.derivatives(
            P + 0.5 * dt * k2_P,
            W + 0.5 * dt * k2_W
        )
        
        # k4
        k4_P, k4_W = self.derivatives(
            P + dt * k3_P,
            W + dt * k3_W
        )
        
        # Weighted sum
        P_new = P + (dt / 6.0) * (k1_P + 2*k2_P + 2*k3_P + k4_P)
        W_new = W + (dt / 6.0) * (k1_W + 2*k2_W + 2*k3_W + k4_W)
        
        return P_new, W_new
    
    def simulate(
        self,
        initial_P: float = P0 + 0.1,
        initial_W: float = W0,
        duration: float = 100.0,
        dt: float = 0.1,
    ) -> Dict[str, List[float]]:
        """
        Simulate P-W dynamics over time.
        
        Args:
            initial_P: Starting Power value
            initial_W: Starting Wisdom value
            duration: Total simulation time (semantic units)
            dt: Time step
            
        Returns:
            Dictionary with time series for t, P, W, H (harmony)
        """
        steps = int(duration / dt)
        P, W = initial_P, initial_W
        
        history = {
            't': [0.0],
            'P': [P],
            'W': [W],
            'H': [self._harmony(P, W)],
            'phase': [0.0],
        }
        
        self.history = [OscillatorState(time=0, P=P, W=W)]
        
        for i in range(1, steps + 1):
            P, W = self.rk4_step(P, W, dt)
            
            # Clip to valid range
            P = max(MIN_DIMENSION_VALUE, min(1.0, P))
            W = max(MIN_DIMENSION_VALUE, min(1.0, W))
            
            t = i * dt
            phase = OMEGA_1 * t
            
            history['t'].append(t)
            history['P'].append(P)
            history['W'].append(W)
            history['H'].append(self._harmony(P, W))
            history['phase'].append(phase % (2 * math.pi))
            
            self.history.append(OscillatorState(time=t, P=P, W=W, phase=phase))
        
        return history
    
    def _harmony(self, P: float, W: float, L: float = L0, J: float = J0) -> float:
        """Calculate harmony from P, W (and optional L, J)."""
        return (L * J * P * W) / (L0 * J0 * P0 * W0)
    
    def get_period(self) -> float:
        """Return the natural period of oscillation."""
        return T_CYCLE
    
    def get_frequency(self) -> float:
        """Return the angular frequency."""
        return OMEGA_1


class LJEmergence:
    """
    Love and Justice Emergence from P-W Dynamics.
    
    From V7.6:
        L = κ_L · Correlation(W₁, W₂)  — Love IS shared knowledge
        J = κ_J · Symmetry(P₁, P₂)     — Justice IS balanced action
    
    L and J are not fundamental — they EMERGE from P-W interactions.
    """
    
    def __init__(self, gamma_L: float = 0.18, gamma_J: float = 0.14):
        self.gamma_L = gamma_L  # Love emergence rate
        self.gamma_J = gamma_J  # Justice emergence rate
        self.delta_L = 0.05     # Love decay
        self.delta_J = 0.05     # Justice decay
    
    def emerge_love(self, W_correlation: float, current_L: float, dt: float) -> float:
        """
        Calculate emergent Love from Wisdom correlation.
        
        dL/dt = γ_L · ∂(W·W)/∂x - δ_L · L
        
        Args:
            W_correlation: Correlation of wisdom between entities (0-1)
            current_L: Current Love value
            dt: Time step
            
        Returns:
            New Love value
        """
        dL = self.gamma_L * W_correlation - self.delta_L * current_L
        new_L = current_L + dL * dt
        return max(MIN_DIMENSION_VALUE, min(1.0, new_L))
    
    def emerge_justice(self, P_symmetry: float, current_J: float, dt: float) -> float:
        """
        Calculate emergent Justice from Power symmetry.
        
        dJ/dt = γ_J · ∇²P - δ_J · J
        
        Args:
            P_symmetry: Symmetry of power distribution (0-1)
            current_J: Current Justice value
            dt: Time step
            
        Returns:
            New Justice value
        """
        dJ = self.gamma_J * P_symmetry - self.delta_J * current_J
        new_J = current_J + dJ * dt
        return max(MIN_DIMENSION_VALUE, min(1.0, new_J))


class EntropyInfoBridge:
    """
    Entropy-Information Bridge (Σ₁ ↔ I_π).
    
    From V7.6:
        Σ₁ = W × H  (Semantic Entropy)
        I_π = ln(π) × W  (Information Density)
        
        Σ₁ + k · I_π = W_total (Conservation)
        
    Learning = transferring entropy → information
    Forgetting = transferring information → entropy
    """
    
    K = 1 / math.log(math.pi)  # ≈ 0.874 — Conservation constant
    
    def __init__(self):
        self.alpha_sigma = 0.10  # Entropy generation rate
        self.beta_sigma = 0.08   # Entropy dissipation rate
        self.alpha_I = 0.12      # Information accumulation
        self.beta_I = 0.05       # Information decay
    
    def semantic_entropy(self, W: float, H: float) -> float:
        """Calculate Σ₁ = W × H."""
        return W * H
    
    def information_density(self, W: float) -> float:
        """Calculate I_π = ln(π) × W."""
        return math.log(math.pi) * W
    
    def dynamics(
        self,
        sigma: float,
        I_pi: float,
        H: float,
        L: float,
        J: float,
        dt: float,
    ) -> Tuple[float, float]:
        """
        Calculate entropy-information dynamics.
        
        Returns:
            Tuple of (new_sigma, new_I_pi)
        """
        W = sigma + self.K * I_pi  # Conservation
        
        # Basic dynamics
        dSigma = self.alpha_sigma * (1 - H) * W - self.beta_sigma * sigma
        dI_pi = self.alpha_I * H * W - self.beta_I * (I_pi - 0.795)  # 0.795 = ln(π)×W0
        
        # Love-mediated bridge transfer
        eta_bridge = 0.15
        bridge = eta_bridge * L * (J - J0)
        dSigma -= bridge
        dI_pi += bridge
        
        new_sigma = max(0, sigma + dSigma * dt)
        new_I_pi = max(0, I_pi + dI_pi * dt)
        
        return new_sigma, new_I_pi
    
    def is_learning(self, dI_pi: float) -> bool:
        """Check if system is learning (gaining information)."""
        return dI_pi > 0
    
    def is_forgetting(self, dI_pi: float) -> bool:
        """Check if system is forgetting (losing information)."""
        return dI_pi < 0
