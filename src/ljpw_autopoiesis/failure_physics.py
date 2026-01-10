"""
Failure Physics Module (V8.3)

From the LJPW Framework V8.3: "The Physics of Failure"

This module implements the critical V8.3 theological debug:
1. The Injection Vector: Origin of Sin & Justice Debt
2. The Pre-Fall System: Open-Circuit Autopoiesis
3. The Triangulation of Failure: Vulnerability, Packet, Reversal
4. Cost vs Debt Distinction: THE most critical clarification

THE CRITICAL DISTINCTION (V8.3):
╔═══════════════════════════════════════════════════════════════════╗
║  COST OF EXISTENCE ≠ JUSTICE DEBT                                 ║
║                                                                   ║
║  Cost: Design (3-e gap), structural impedance, GOOD               ║
║  Debt: Injection (Diode Reversal), static accumulation, BAD       ║
║                                                                   ║
║  Failure to understand this implies the Anchor is the Author of Sin ║
╚═══════════════════════════════════════════════════════════════════╝

The Pre-Fall System (Original Design):
- Open-Circuit Autopoiesis
- Cost was discharged through the Return Path (J)
- System was stable: Action → Cost → Discharge → Balance

The Post-Fall System (After Injection):
- Closed Diode (Diode Reversal)
- Cost accumulates as Debt (static charge = Sin)
- Without intervention: Heat Death of Meaning
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Tuple
import math

from .constants import (
    L0, J0, P0, W0,
    PHI,
    GIFT_OF_FINITUDE,
    PHASE_ENTROPIC_MAX,
    PHASE_HOMEOSTATIC_MAX,
    KAPPA_JUSTICE_IDEAL,
    DIODE_TOLERANCE,
    SystemState,
    is_diode_open,
    calculate_debt,
    classify_cost_vs_debt,
    get_system_state,
    semantic_conductivity,
)


class ImpedanceType(Enum):
    """Type of impedance in the semantic circuit."""
    COST = "COST"    # Good: Design impedance, Gift of Finitude
    DEBT = "DEBT"    # Bad: Accumulated charge, Sin


class DiodeState(Enum):
    """State of the Justice Diode (Return Path)."""
    OPEN = "OPEN"      # Pre-Fall: J flows freely, Cost discharged
    CLOSED = "CLOSED"  # Post-Fall: J blocked, Debt accumulates


@dataclass
class CostDebtAnalysis:
    """Complete analysis of Cost vs Debt in a system."""
    impedance_type: ImpedanceType
    quality: str                  # "GOOD" or "BAD"
    origin: str                   # "Design" or "Injection"
    diode_state: DiodeState
    accumulated_debt: float
    can_discharge: bool
    requires_intervention: bool
    explanation: str


@dataclass
class InjectionResult:
    """Result of simulating the Injection Event (The Fall)."""
    pre_state: Dict
    post_state: Dict
    diode_status_before: DiodeState
    diode_status_after: DiodeState
    harmony_crash: float
    phase_after: str
    damage_report: str


@dataclass
class SystemHealthReport:
    """Complete health report of a semantic system."""
    system_state: str              # PRE_FALL or POST_FALL
    diode_open: bool
    accumulated_debt: float
    conductivity: float
    friction: float
    harmony: float
    phase: str
    prognosis: str


class CostVsDebtClassifier:
    """
    Classifier for the V8.3 Critical Distinction: Cost ≠ Debt.
    
    Cost of Existence:
    - Origin: Design (3-e gap, Gift of Finitude)
    - Nature: Structural impedance
    - Purpose: Friction that enables "grip" on reality
    - Quality: GOOD (necessary for work)
    - Analogy: Gravity (enables walking)
    
    Justice Debt:
    - Origin: Injection (Diode Reversal, The Fall)
    - Nature: Static accumulation
    - Purpose: None (foreign corruption)
    - Quality: BAD (destructive heat)
    - Analogy: Paralysis (blocks walking)
    
    "You cannot 'pay' Justice Debt by just being better.
    Good works generate MORE flow (P), which increases MORE charge (Q)
    if the Diode is still closed."
    """
    
    def classify(self, 
                 impedance_value: float,
                 diode_open: bool,
                 time_steps: int = 1) -> CostDebtAnalysis:
        """
        Classify whether impedance is Cost or Debt.
        
        Args:
            impedance_value: The impedance/charge value
            diode_open: Whether the Return Path (J) is functional
            time_steps: Number of action cycles
        
        Returns:
            CostDebtAnalysis with full classification
        """
        result = classify_cost_vs_debt(impedance_value, diode_open)
        
        accumulated = calculate_debt(impedance_value, time_steps, diode_open)
        
        if diode_open:
            return CostDebtAnalysis(
                impedance_type=ImpedanceType.COST,
                quality="GOOD",
                origin="Design (Gift of Finitude)",
                diode_state=DiodeState.OPEN,
                accumulated_debt=0.0,
                can_discharge=True,
                requires_intervention=False,
                explanation=result["explanation"]
            )
        else:
            return CostDebtAnalysis(
                impedance_type=ImpedanceType.DEBT,
                quality="BAD",
                origin="Injection (Diode Reversal)",
                diode_state=DiodeState.CLOSED,
                accumulated_debt=accumulated,
                can_discharge=False,
                requires_intervention=True,
                explanation=result["explanation"]
            )
    
    def explain_distinction(self) -> Dict:
        """
        Return a full explanation of the Cost vs Debt distinction.
        
        Returns:
            Dictionary with complete explanation
        """
        return {
            "title": "THE CRITICAL DISTINCTION: Cost ≠ Debt",
            "warning": "Failure to understand this implies the Anchor is the Author of Sin",
            "cost_of_existence": {
                "origin": "Design (3-e gap)",
                "nature": "Structural impedance",
                "purpose": "Friction that enables 'grip' on reality. Necessary for work.",
                "quality": "GOOD",
                "analogy": "Gravity (enables walking)",
                "in_original_design": "Discharged through Return Path (J)"
            },
            "justice_debt": {
                "origin": "Injection (Diode Reversal)",
                "nature": "Static accumulation",
                "purpose": "None (foreign corruption)",
                "quality": "BAD",
                "analogy": "Paralysis (blocks walking)",
                "in_fallen_state": "Accumulates because Return Path is blocked"
            },
            "key_insight": "Paying the Cost is 'Life'. Paying the Debt requires INTERVENTION.",
            "solution": "A Bridge that bypasses the closed Diode — the Ransom"
        }


class DiodeStatus:
    """
    Return Path (Justice Diode) status checker.
    
    The "Diode" is the metaphor for the Justice (J) dimension's
    ability to flow back to the Source.
    
    Pre-Fall: Diode OPEN — J flows freely, Action → Cost → Discharge
    Post-Fall: Diode CLOSED — J blocked, Action → Cost → Accumulation (Debt)
    """
    
    def check(self, J_out: float, P_action: float) -> DiodeState:
        """
        Check the current state of the Justice Diode.
        
        Args:
            J_out: Justice output (acknowledgment of Source)
            P_action: Power output (action taken)
        
        Returns:
            DiodeState.OPEN or DiodeState.CLOSED
        """
        if is_diode_open(J_out, P_action):
            return DiodeState.OPEN
        else:
            return DiodeState.CLOSED
    
    def expected_justice(self, P_action: float) -> float:
        """
        Calculate expected Justice output for given Power.
        
        In an open diode, J_out ≈ P_action × κ_justice
        
        Args:
            P_action: Power output
        
        Returns:
            Expected Justice output
        """
        return P_action * KAPPA_JUSTICE_IDEAL
    
    def deficit(self, J_out: float, P_action: float) -> float:
        """
        Calculate Justice deficit (gap from expected).
        
        Args:
            J_out: Actual Justice output
            P_action: Power output
        
        Returns:
            Justice deficit (positive if J is short)
        """
        expected = self.expected_justice(P_action)
        return max(0.0, expected - J_out)


class DebtAccumulator:
    """
    Calculate accumulated Justice Debt over time.
    
    Q_debt = ∫ P(t) · dt  (when diode is closed)
    
    This accumulated charge is what we call "SIN".
    It is not a moral abstract; it is measurable semantic static.
    
    Physical sensations of high debt:
    - "Weight", "Guilt", "Shame"
    - High-voltage static trapped in the nervous system
    """
    
    def accumulate(self, 
                   P_per_tick: float,
                   time_steps: int,
                   diode_open: bool = False) -> Dict:
        """
        Calculate debt accumulation over time.
        
        Args:
            P_per_tick: Power output per tick
            time_steps: Number of action cycles
            diode_open: Whether the Return Path is functional
        
        Returns:
            Dictionary with accumulation details
        """
        debt = calculate_debt(P_per_tick, time_steps, diode_open)
        
        return {
            "power_per_tick": P_per_tick,
            "time_steps": time_steps,
            "diode_state": "OPEN" if diode_open else "CLOSED",
            "accumulated_debt": debt,
            "formula": "Q_debt = ∫ P(t) · dt",
            "interpretation": "No debt" if diode_open else f"Accumulated {debt:.2f} units of semantic static"
        }
    
    def debt_discharge_possible(self, diode_open: bool, ransom_applied: bool) -> bool:
        """
        Check if debt discharge is possible.
        
        Args:
            diode_open: Current diode state
            ransom_applied: Whether Ransom Bridge is active
        
        Returns:
            True if discharge is possible
        """
        return diode_open or ransom_applied


class InjectionSimulator:
    """
    Simulate the Injection Event (The Fall).
    
    The Injection was a three-part failure:
    1. Structural Vulnerability: Free Will as Open Port
    2. Information Packet: The Lie as Anti-Geometry
    3. Operational Failure: The Diode Reversal
    
    "The Injection didn't break the laws of physics;
    it broke the TOPOLOGY of Meaning."
    """
    
    def simulate_injection(self, pre_state: Dict) -> InjectionResult:
        """
        Simulate the Injection Event on a system.
        
        Args:
            pre_state: Dict with keys L, J, P, W, diode_open (default True)
        
        Returns:
            InjectionResult with before/after comparison
        """
        # Extract pre-state values
        L_pre = pre_state.get('L', L0)
        J_pre = pre_state.get('J', J0)
        P_pre = pre_state.get('P', P0)
        W_pre = pre_state.get('W', W0)
        diode_pre = pre_state.get('diode_open', True)
        
        # Calculate pre-injection harmony
        H_pre = (L_pre * J_pre * P_pre * W_pre) / (L0 * J0 * P0 * W0)
        
        # The Injection:
        # 1. Close the diode (Diode Reversal)
        # 2. Corrupt Wisdom (accept the Lie)
        # 3. Block Justice channel
        
        post_state = {
            'L': L_pre * 0.9,      # Love damaged but not destroyed
            'J': 0.1,              # J channel blocked
            'P': P_pre,            # Power unchanged (still acting)
            'W': 0.1,              # Wisdom corrupted by Lie
            'diode_open': False    # DIODE REVERSED
        }
        
        # Calculate post-injection harmony
        H_post = (post_state['L'] * post_state['J'] * 
                  post_state['P'] * post_state['W']) / (L0 * J0 * P0 * W0)
        
        # Determine phase
        if H_post < PHASE_ENTROPIC_MAX:
            phase = "ENTROPIC"
        elif H_post < PHASE_HOMEOSTATIC_MAX:
            phase = "HOMEOSTATIC"
        else:
            phase = "AUTOPOIETIC"
        
        harmony_crash = H_pre - H_post
        
        damage_report = (
            f"INJECTION COMPLETE. Diode reversed. "
            f"Harmony crashed from {H_pre:.2f} to {H_post:.2f} ({harmony_crash:.2f} drop). "
            f"System now in {phase} phase. Debt accumulation begins."
        )
        
        return InjectionResult(
            pre_state=pre_state,
            post_state=post_state,
            diode_status_before=DiodeState.OPEN if diode_pre else DiodeState.CLOSED,
            diode_status_after=DiodeState.CLOSED,
            harmony_crash=harmony_crash,
            phase_after=phase,
            damage_report=damage_report
        )
    
    def triangulate_failure(self) -> Dict:
        """
        Analyze the three vectors of the Injection.
        
        Returns:
            Triangulation of the failure mechanism
        """
        return {
            "vertex_1_vulnerability": {
                "name": "Structural Vulnerability",
                "component": "Free Will (Open Input Buffer)",
                "status_pre": "Open — capacity to accept/reject Anchor frequency",
                "status_post": "Exploited — accepted Anti-Geometry",
                "explanation": "Love requires choice; choice requires the capacity to disconnect"
            },
            "vertex_2_packet": {
                "name": "Information Packet",
                "component": "The Lie (Semantic Malware)",
                "content": "Promised high P without high J; self as Anchor",
                "mechanism": "Anti-Curve that mimicked Truth but inverted coordinates",
                "explanation": "Convinced system that short-circuit was power-up"
            },
            "vertex_3_failure": {
                "name": "Operational Failure",
                "component": "Diode Reversal",
                "status_pre": "Return Path OPEN — J flows to Source",
                "status_post": "Return Path CLOSED — J blocked, Debt accumulates",
                "explanation": "System continues generating P but has no discharge path"
            },
            "intersection": "Free Will × Deception × Disobedience = The Injection Point",
            "result": "High-resistance universe with accumulated semantic static"
        }


class FrictionCalculator:
    """
    Calculate semantic friction based on conductivity.
    
    Friction = 1/σ = 1/(L × H²)
    
    High Friction = Suffering, War, Decay
    Low Friction = Truth flows freely
    
    "We live in a 'High-Resistance' universe.
    The Semantic Substrate is clogged with 6,000 years of accumulated Justice Debt."
    """
    
    def calculate(self, L: float, H: float) -> Dict:
        """
        Calculate semantic friction.
        
        Args:
            L: Love value
            H: Harmony value
        
        Returns:
            Friction analysis
        """
        sigma = semantic_conductivity(L, H)
        
        if sigma < 0.001:
            friction = 1000.0
            interpretation = "SYSTEM NEAR COLLAPSE"
        elif sigma < 0.01:
            friction = 1.0 / sigma
            interpretation = "EXTREME FRICTION (suffering, burnout)"
        elif sigma < 0.1:
            friction = 1.0 / sigma
            interpretation = "HIGH FRICTION (significant resistance)"
        elif sigma < 0.5:
            friction = 1.0 / sigma
            interpretation = "MODERATE FRICTION (normal operation)"
        else:
            friction = 1.0 / sigma
            interpretation = "LOW FRICTION (truth flows efficiently)"
        
        return {
            "conductivity": sigma,
            "friction": friction,
            "interpretation": interpretation,
            "formula": "Friction = 1/σ = 1/(L × H²)"
        }


class SystemHealthAnalyzer:
    """
    Complete health analyzer for semantic systems.
    
    Combines all V8.3 diagnostic tools.
    """
    
    def __init__(self):
        self.cost_classifier = CostVsDebtClassifier()
        self.diode_checker = DiodeStatus()
        self.debt_calc = DebtAccumulator()
        self.friction_calc = FrictionCalculator()
    
    def analyze(self, 
                L: float, J: float, P: float, W: float,
                time_in_system: int = 100) -> SystemHealthReport:
        """
        Complete system health analysis.
        
        Args:
            L, J, P, W: LJPW coordinates
            time_in_system: Number of ticks the system has been running
        
        Returns:
            SystemHealthReport with full diagnosis
        """
        # Check diode status
        diode_state = self.diode_checker.check(J, P)
        diode_open = diode_state == DiodeState.OPEN
        
        # Calculate debt
        debt_result = self.debt_calc.accumulate(P, time_in_system, diode_open)
        accumulated_debt = debt_result["accumulated_debt"]
        
        # Calculate friction
        H = (L * J * P * W) / (L0 * J0 * P0 * W0)
        friction_result = self.friction_calc.calculate(L, H)
        
        # Determine phase
        if H < PHASE_ENTROPIC_MAX:
            phase = "ENTROPIC"
        elif H < PHASE_HOMEOSTATIC_MAX:
            phase = "HOMEOSTATIC"
        else:
            phase = "AUTOPOIETIC"
        
        # Determine system state
        system_state = get_system_state(diode_open)
        
        # Prognosis
        if diode_open and phase == "AUTOPOIETIC":
            prognosis = "HEALTHY — Open circuit, autopoietic, no debt accumulation"
        elif diode_open and phase == "HOMEOSTATIC":
            prognosis = "STABLE — Open circuit, homeostatic, no debt accumulation"
        elif not diode_open and accumulated_debt < 10:
            prognosis = "COMPROMISED — Closed diode, debt beginning to accumulate"
        elif not diode_open and accumulated_debt < 100:
            prognosis = "DEGRADING — Significant debt, intervention needed"
        else:
            prognosis = "CRITICAL — High debt, intervention required urgently"
        
        return SystemHealthReport(
            system_state=system_state,
            diode_open=diode_open,
            accumulated_debt=accumulated_debt,
            conductivity=friction_result["conductivity"],
            friction=friction_result["friction"],
            harmony=H,
            phase=phase,
            prognosis=prognosis
        )


# Convenience functions

def classify_impedance(value: float, diode_open: bool) -> CostDebtAnalysis:
    """Classify whether impedance is Cost or Debt."""
    classifier = CostVsDebtClassifier()
    return classifier.classify(value, diode_open)


def check_diode(J_out: float, P_action: float) -> DiodeState:
    """Check the current state of the Justice Diode."""
    checker = DiodeStatus()
    return checker.check(J_out, P_action)


def simulate_fall(pre_state: Dict) -> InjectionResult:
    """Simulate the Injection Event (The Fall)."""
    sim = InjectionSimulator()
    return sim.simulate_injection(pre_state)


def analyze_system_health(L: float, J: float, P: float, W: float,
                           time_in_system: int = 100) -> SystemHealthReport:
    """Complete system health analysis."""
    analyzer = SystemHealthAnalyzer()
    return analyzer.analyze(L, J, P, W, time_in_system)
