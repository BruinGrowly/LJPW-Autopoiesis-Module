"""
LJPW Full Temporal Dynamics - 4D Oscillator

Built according to the framework's own prescription to address its blind spot:
"Temporal dynamics limited to P-W"

This module extends the P-W oscillator to model all four dimensions:
- P and W oscillate (existing behavior)
- L EMERGES from P*W activity (Love from shared Power-Wisdom)
- J EMERGES from |P-W| symmetry (Justice from balance)

The Anchor (1,1,1,1) is the attractor in 4D phase space.
"""

import math
import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Tuple

from .constants import (
    L0, J0, P0, W0,
    OMEGA_1, PHI, PHI_INV,
    MIN_DIMENSION_VALUE,
)
from .dynamics import LJPWState


@dataclass
class LJPWDynamicsParams:
    """Parameters for the full 4D LJPW dynamics."""
    # P-W oscillation parameters
    omega: float = OMEGA_1      # Angular frequency (pi/10)
    gamma: float = 0.02         # Damping coefficient
    
    # L emergence parameters (Love from Power*Wisdom activity)
    kappa_L: float = 0.15       # Love emergence rate
    delta_L: float = 0.05       # Love decay toward equilibrium
    
    # J emergence parameters (Justice from P-W balance)
    kappa_J: float = 0.12       # Justice emergence rate  
    delta_J: float = 0.05       # Justice decay toward equilibrium
    
    # Cross-dimension coupling
    lambda_LP: float = 0.08     # Love -> Power coupling
    lambda_JW: float = 0.06     # Justice -> Wisdom coupling
    lambda_PL: float = 0.04     # Power -> Love feedback
    lambda_WJ: float = 0.04     # Wisdom -> Justice feedback


class LJPWOscillator:
    """
    Full 4D LJPW Dynamics Engine.
    
    This implements the complete temporal evolution of all four dimensions:
    
        dP/dt = omega*(W-W0) - gamma*(P-P0) + lambda_LP*L
        dW/dt = -omega*(P-P0) - gamma*(W-W0) + lambda_JW*J
        dL/dt = kappa_L*(P*W - P0*W0) - delta_L*(L-L0) + lambda_PL*(P-P0)
        dJ/dt = kappa_J*|P-W|_balanced - delta_J*(J-J0) + lambda_WJ*(W-W0)
    
    Key insights:
    - P and W oscillate as conjugate variables (the "heartbeat")
    - L EMERGES from P*W activity (shared creation creates Love)
    - J EMERGES from P-W balance (symmetry creates Justice)
    - All dimensions are coupled (the Law of Karma)
    - The Anchor (1,1,1,1) is the attractor
    """
    
    def __init__(self, params: LJPWDynamicsParams = None):
        self.params = params or LJPWDynamicsParams()
        self.history: List[Dict] = []
        
    def derivatives(
        self, 
        L: float, 
        J: float, 
        P: float, 
        W: float
    ) -> Tuple[float, float, float, float]:
        """
        Calculate dL/dt, dJ/dt, dP/dt, dW/dt at current state.
        
        This is the heart of the 4D dynamics.
        """
        p = self.params
        
        # Deviations from equilibrium
        dL_eq = L - L0
        dJ_eq = J - J0  
        dP_eq = P - P0
        dW_eq = W - W0
        
        # P-W conjugate oscillation (existing, enhanced)
        dP = p.omega * dW_eq - p.gamma * dP_eq + p.lambda_LP * L
        dW = -p.omega * dP_eq - p.gamma * dW_eq + p.lambda_JW * J
        
        # L emergence: Love emerges from P*W activity above baseline
        activity = P * W - P0 * W0
        dL = p.kappa_L * activity - p.delta_L * dL_eq + p.lambda_PL * dP_eq
        
        # J emergence: Justice emerges from P-W balance
        # Maximum justice when P and W are equal (balanced)
        # |P-W| small -> more justice
        balance = 1.0 - abs(P - W)  # 1 when balanced, 0 when maximally unbalanced
        dJ = p.kappa_J * balance - p.delta_J * dJ_eq + p.lambda_WJ * dW_eq
        
        return dL, dJ, dP, dW
    
    def rk4_step(
        self,
        L: float,
        J: float,
        P: float,
        W: float,
        dt: float
    ) -> Tuple[float, float, float, float]:
        """
        Single RK4 integration step for the 4D system.
        """
        # k1
        k1_L, k1_J, k1_P, k1_W = self.derivatives(L, J, P, W)
        
        # k2
        k2_L, k2_J, k2_P, k2_W = self.derivatives(
            L + 0.5 * dt * k1_L,
            J + 0.5 * dt * k1_J,
            P + 0.5 * dt * k1_P,
            W + 0.5 * dt * k1_W
        )
        
        # k3
        k3_L, k3_J, k3_P, k3_W = self.derivatives(
            L + 0.5 * dt * k2_L,
            J + 0.5 * dt * k2_J,
            P + 0.5 * dt * k2_P,
            W + 0.5 * dt * k2_W
        )
        
        # k4
        k4_L, k4_J, k4_P, k4_W = self.derivatives(
            L + dt * k3_L,
            J + dt * k3_J,
            P + dt * k3_P,
            W + dt * k3_W
        )
        
        # Weighted sum
        L_new = L + (dt / 6.0) * (k1_L + 2*k2_L + 2*k3_L + k4_L)
        J_new = J + (dt / 6.0) * (k1_J + 2*k2_J + 2*k3_J + k4_J)
        P_new = P + (dt / 6.0) * (k1_P + 2*k2_P + 2*k3_P + k4_P)
        W_new = W + (dt / 6.0) * (k1_W + 2*k2_W + 2*k3_W + k4_W)
        
        return L_new, J_new, P_new, W_new
    
    def clip(self, L: float, J: float, P: float, W: float) -> Tuple[float, float, float, float]:
        """Clip values to valid range."""
        return (
            max(MIN_DIMENSION_VALUE, min(1.0, L)),
            max(MIN_DIMENSION_VALUE, min(1.0, J)),
            max(MIN_DIMENSION_VALUE, min(1.0, P)),
            max(MIN_DIMENSION_VALUE, min(1.0, W)),
        )
    
    def simulate(
        self,
        initial_state: LJPWState = None,
        duration: float = 100.0,
        dt: float = 0.1,
    ) -> Dict[str, List[float]]:
        """
        Simulate full 4D LJPW dynamics.
        
        Args:
            initial_state: Starting LJPW state (default: equilibrium + perturbation)
            duration: Simulation time
            dt: Time step
            
        Returns:
            Dictionary with time series for t, L, J, P, W, H (harmony), C (consciousness)
        """
        if initial_state is None:
            initial_state = LJPWState(L=L0+0.1, J=J0+0.1, P=P0+0.1, W=W0+0.1)
        
        L, J, P, W = initial_state.L, initial_state.J, initial_state.P, initial_state.W
        
        history = {
            't': [0.0],
            'L': [L],
            'J': [J],
            'P': [P],
            'W': [W],
            'H': [self._harmony(L, J, P, W)],
            'C': [self._consciousness(L, J, P, W)],
            'gap': [self._gap_from_anchor(L, J, P, W)],
        }
        
        self.history = [{'t': 0, 'L': L, 'J': J, 'P': P, 'W': W}]
        
        steps = int(duration / dt)
        for i in range(1, steps + 1):
            L, J, P, W = self.rk4_step(L, J, P, W, dt)
            L, J, P, W = self.clip(L, J, P, W)
            
            t = i * dt
            
            history['t'].append(t)
            history['L'].append(L)
            history['J'].append(J)
            history['P'].append(P)
            history['W'].append(W)
            history['H'].append(self._harmony(L, J, P, W))
            history['C'].append(self._consciousness(L, J, P, W))
            history['gap'].append(self._gap_from_anchor(L, J, P, W))
            
            self.history.append({'t': t, 'L': L, 'J': J, 'P': P, 'W': W})
        
        return history
    
    def _harmony(self, L: float, J: float, P: float, W: float) -> float:
        """Calculate harmony H = (L*J*P*W) / (L0*J0*P0*W0)."""
        return (L * J * P * W) / (L0 * J0 * P0 * W0)
    
    def _consciousness(self, L: float, J: float, P: float, W: float) -> float:
        """Calculate consciousness C = P*W*L*J*H^2."""
        H = self._harmony(L, J, P, W)
        return P * W * L * J * (H ** 2)
    
    def _gap_from_anchor(self, L: float, J: float, P: float, W: float) -> float:
        """Calculate distance from Anchor (1,1,1,1)."""
        return math.sqrt((1-L)**2 + (1-J)**2 + (1-P)**2 + (1-W)**2)
    
    def converges_to_anchor(self, threshold: float = 0.1) -> bool:
        """Check if the simulation converged toward the Anchor."""
        if not self.history:
            return False
        
        first_gap = self._gap_from_anchor(
            self.history[0]['L'],
            self.history[0]['J'],
            self.history[0]['P'],
            self.history[0]['W'],
        )
        last_gap = self._gap_from_anchor(
            self.history[-1]['L'],
            self.history[-1]['J'],
            self.history[-1]['P'],
            self.history[-1]['W'],
        )
        
        return last_gap < first_gap
    
    def report(self) -> str:
        """Generate a dynamics report."""
        if not self.history:
            return "No simulation run yet."
        
        first = self.history[0]
        last = self.history[-1]
        
        lines = [
            "=" * 60,
            "LJPW FULL DYNAMICS REPORT",
            "=" * 60,
            "",
            "Initial State:",
            f"  L={first['L']:.4f}, J={first['J']:.4f}, P={first['P']:.4f}, W={first['W']:.4f}",
            f"  Gap from Anchor: {self._gap_from_anchor(first['L'], first['J'], first['P'], first['W']):.4f}",
            "",
            "Final State:",
            f"  L={last['L']:.4f}, J={last['J']:.4f}, P={last['P']:.4f}, W={last['W']:.4f}",
            f"  Gap from Anchor: {self._gap_from_anchor(last['L'], last['J'], last['P'], last['W']):.4f}",
            "",
            f"Converged toward Anchor: {'YES' if self.converges_to_anchor() else 'NO'}",
            "",
            f"Simulation steps: {len(self.history)}",
            f"Duration: {self.history[-1]['t']:.1f} time units",
            "",
            "=" * 60,
        ]
        
        return "\n".join(lines)


def simulate_full_dynamics():
    """Run a full 4D dynamics simulation and print report."""
    osc = LJPWOscillator()
    
    # Start with a perturbed state
    initial = LJPWState(L=0.5, J=0.4, P=0.6, W=0.5)
    
    history = osc.simulate(initial_state=initial, duration=200.0, dt=0.1)
    
    print(osc.report())
    
    print("\nTime evolution:")
    print("  t=0:   L={:.3f}, J={:.3f}, P={:.3f}, W={:.3f}".format(
        history['L'][0], history['J'][0], history['P'][0], history['W'][0]))
    print("  t=50:  L={:.3f}, J={:.3f}, P={:.3f}, W={:.3f}".format(
        history['L'][500], history['J'][500], history['P'][500], history['W'][500]))
    print("  t=100: L={:.3f}, J={:.3f}, P={:.3f}, W={:.3f}".format(
        history['L'][1000], history['J'][1000], history['P'][1000], history['W'][1000]))
    print("  t=200: L={:.3f}, J={:.3f}, P={:.3f}, W={:.3f}".format(
        history['L'][-1], history['J'][-1], history['P'][-1], history['W'][-1]))
    
    return osc


if __name__ == "__main__":
    simulate_full_dynamics()
