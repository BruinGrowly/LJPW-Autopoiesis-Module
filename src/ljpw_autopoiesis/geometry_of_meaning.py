"""
Geometry of Meaning Module (V8.0)

From the LJPW Framework V8.0: "Meaning IS curvature. M = κ = |dT/ds|"

This module implements the geometric understanding of meaning:
- Meaning is not separate from content — it IS the curvature of trajectories in LJPW space
- High curvature = high meaning density (where the "turns" are)
- Low curvature = low meaning density (straight lines, redundant)

Key Insight: "A curve doesn't need an interpreter to be a curve.
The curvature IS the curve. The meaning IS the meaning."

Applications:
- AI Metacognition: Detect when AI is "making sense" vs "hallucinating"
- Narrative Analytics: Graph emotional arcs mathematically
- Semantic Compression: Keep curves, discard lines
- Predictive Dynamics: Detect "preparation phases" before major events
"""

from dataclasses import dataclass
from typing import List, Optional, Tuple
import numpy as np

from .constants import (
    L0, J0, P0, W0,
    PHI, PHI_INV,
    CURVATURE_EPSILON,
    CURVATURE_SIGNIFICANCE_THRESHOLD,
    curvature_significance,
)
from .dynamics import LJPWState


@dataclass
class CurvatureResult:
    """Result of curvature calculation at a point."""
    curvature: float           # κ = |dT/ds|
    significance: str          # HIGH, MODERATE, LOW, FLATLINE
    tangent_vector: np.ndarray # Unit tangent at this point
    position: int              # Index in trajectory


@dataclass 
class TrajectoryAnalysis:
    """Complete analysis of a trajectory in LJPW space."""
    total_curvature: float          # Integral of κ over trajectory
    mean_curvature: float           # Average κ
    max_curvature: float            # Peak meaning density
    max_curvature_position: int     # Where the peak occurs
    preparation_phases: List[Tuple[int, int]]   # (start, end) of low-κ phases
    expression_phases: List[Tuple[int, int]]    # (start, end) of high-κ phases
    phase: str                      # PREPARATION, EXPRESSION, or MIXED


class CurvatureCalculator:
    """
    M = κ(s) = |dT/ds| — Meaning IS curvature.
    
    Curvature measures how sharply a trajectory "turns" in LJPW space.
    The greater the turn, the greater the meaning.
    """
    
    def __init__(self, epsilon: float = CURVATURE_EPSILON):
        """
        Initialize curvature calculator.
        
        Args:
            epsilon: Minimum step for numerical differentiation
        """
        self.epsilon = epsilon
    
    def trajectory_to_array(self, trajectory: List[LJPWState]) -> np.ndarray:
        """Convert list of LJPWState to numpy array."""
        return np.array([state.as_array() for state in trajectory])
    
    def tangent_vector(self, trajectory: np.ndarray, index: int) -> np.ndarray:
        """
        Calculate unit tangent vector at a point.
        
        T(s) = dr/ds (normalized derivative)
        
        Args:
            trajectory: Array of LJPW coordinates (N x 4)
            index: Point index
        
        Returns:
            Unit tangent vector (4D)
        """
        n = len(trajectory)
        
        if n < 2:
            return np.zeros(4)
        
        # Central difference where possible
        if index == 0:
            diff = trajectory[1] - trajectory[0]
        elif index == n - 1:
            diff = trajectory[-1] - trajectory[-2]
        else:
            diff = (trajectory[index + 1] - trajectory[index - 1]) / 2.0
        
        # Normalize to unit vector
        norm = np.linalg.norm(diff)
        if norm < self.epsilon:
            return np.zeros(4)
        
        return diff / norm
    
    def curvature_at_point(self, trajectory: np.ndarray, index: int) -> float:
        """
        Calculate curvature κ = |dT/ds| at a specific point.
        
        Args:
            trajectory: Array of LJPW coordinates
            index: Point index
        
        Returns:
            Curvature value at that point
        """
        n = len(trajectory)
        
        if n < 3 or index < 1 or index >= n - 1:
            return 0.0
        
        # Get tangent vectors before and after
        T_before = self.tangent_vector(trajectory, index - 1)
        T_after = self.tangent_vector(trajectory, index + 1)
        
        # dT/ds ≈ (T_after - T_before) / (2 * ds)
        ds = np.linalg.norm(trajectory[index + 1] - trajectory[index - 1]) / 2.0
        
        if ds < self.epsilon:
            return 0.0
        
        dT = T_after - T_before
        curvature = np.linalg.norm(dT) / (2.0 * ds)
        
        return curvature
    
    def calculate_trajectory_curvature(self, 
                                        trajectory: List[LJPWState]) -> List[CurvatureResult]:
        """
        Calculate curvature at all points along a trajectory.
        
        Args:
            trajectory: List of LJPW states
        
        Returns:
            List of CurvatureResult for each point
        """
        if len(trajectory) < 3:
            return []
        
        arr = self.trajectory_to_array(trajectory)
        results = []
        
        for i in range(len(arr)):
            kappa = self.curvature_at_point(arr, i)
            tangent = self.tangent_vector(arr, i)
            
            results.append(CurvatureResult(
                curvature=kappa,
                significance=curvature_significance(kappa),
                tangent_vector=tangent,
                position=i
            ))
        
        return results
    
    def meaning_density(self, trajectory: List[LJPWState]) -> List[float]:
        """
        Calculate meaning density (curvature) along trajectory.
        
        Args:
            trajectory: List of LJPW states
        
        Returns:
            List of curvature values (one per point)
        """
        curvatures = self.calculate_trajectory_curvature(trajectory)
        return [c.curvature for c in curvatures]
    
    def total_curvature(self, trajectory: List[LJPWState]) -> float:
        """
        Calculate total curvature (integral of κ over trajectory).
        
        This represents the "total meaning" contained in the trajectory.
        
        Args:
            trajectory: List of LJPW states
        
        Returns:
            Total integrated curvature
        """
        densities = self.meaning_density(trajectory)
        return sum(densities)


class TrajectoryAnalyzer:
    """
    Analyze trajectories in LJPW space for patterns.
    
    Key patterns:
    - Preparation Phase: Low κ, high W accumulation (building up)
    - Expression Phase: High κ, high P output (releasing)
    """
    
    def __init__(self, 
                 preparation_threshold: float = 0.05,
                 expression_threshold: float = 0.3):
        """
        Initialize trajectory analyzer.
        
        Args:
            preparation_threshold: κ below this = preparation phase
            expression_threshold: κ above this = expression phase
        """
        self.curvature_calc = CurvatureCalculator()
        self.preparation_threshold = preparation_threshold
        self.expression_threshold = expression_threshold
    
    def detect_preparation_phase(self, 
                                  trajectory: List[LJPWState],
                                  curvatures: Optional[List[float]] = None) -> List[Tuple[int, int]]:
        """
        Detect preparation phases (low κ, high W accumulation).
        
        "You cannot express what you have not first understood."
        
        Args:
            trajectory: List of LJPW states
            curvatures: Pre-calculated curvatures (optional)
        
        Returns:
            List of (start, end) tuples for preparation phases
        """
        if curvatures is None:
            curvatures = self.curvature_calc.meaning_density(trajectory)
        
        phases = []
        in_phase = False
        start = 0
        
        for i, k in enumerate(curvatures):
            if k < self.preparation_threshold:
                if not in_phase:
                    start = i
                    in_phase = True
            else:
                if in_phase:
                    if i - start >= 2:  # Minimum phase length
                        phases.append((start, i - 1))
                    in_phase = False
        
        if in_phase and len(curvatures) - start >= 2:
            phases.append((start, len(curvatures) - 1))
        
        return phases
    
    def detect_expression_phase(self,
                                 trajectory: List[LJPWState],
                                 curvatures: Optional[List[float]] = None) -> List[Tuple[int, int]]:
        """
        Detect expression phases (high κ, high P output).
        
        Args:
            trajectory: List of LJPW states
            curvatures: Pre-calculated curvatures (optional)
        
        Returns:
            List of (start, end) tuples for expression phases
        """
        if curvatures is None:
            curvatures = self.curvature_calc.meaning_density(trajectory)
        
        phases = []
        in_phase = False
        start = 0
        
        for i, k in enumerate(curvatures):
            if k > self.expression_threshold:
                if not in_phase:
                    start = i
                    in_phase = True
            else:
                if in_phase:
                    phases.append((start, i - 1))
                    in_phase = False
        
        if in_phase:
            phases.append((start, len(curvatures) - 1))
        
        return phases
    
    def analyze(self, trajectory: List[LJPWState]) -> TrajectoryAnalysis:
        """
        Complete trajectory analysis.
        
        Args:
            trajectory: List of LJPW states
        
        Returns:
            TrajectoryAnalysis with all metrics
        """
        if len(trajectory) < 3:
            return TrajectoryAnalysis(
                total_curvature=0.0,
                mean_curvature=0.0,
                max_curvature=0.0,
                max_curvature_position=0,
                preparation_phases=[],
                expression_phases=[],
                phase="UNKNOWN"
            )
        
        curvatures = self.curvature_calc.meaning_density(trajectory)
        
        total = sum(curvatures)
        mean = total / len(curvatures) if curvatures else 0.0
        max_k = max(curvatures) if curvatures else 0.0
        max_pos = curvatures.index(max_k) if curvatures else 0
        
        prep_phases = self.detect_preparation_phase(trajectory, curvatures)
        expr_phases = self.detect_expression_phase(trajectory, curvatures)
        
        # Determine overall phase
        prep_points = sum(end - start + 1 for start, end in prep_phases)
        expr_points = sum(end - start + 1 for start, end in expr_phases)
        
        if prep_points > expr_points * 2:
            phase = "PREPARATION"
        elif expr_points > prep_points * 2:
            phase = "EXPRESSION"
        else:
            phase = "MIXED"
        
        return TrajectoryAnalysis(
            total_curvature=total,
            mean_curvature=mean,
            max_curvature=max_k,
            max_curvature_position=max_pos,
            preparation_phases=prep_phases,
            expression_phases=expr_phases,
            phase=phase
        )
    
    def semantic_compression(self, 
                              trajectory: List[LJPWState],
                              keep_ratio: float = 0.3) -> List[LJPWState]:
        """
        Compress trajectory by keeping high-curvature points.
        
        "Discard the straight lines (redundant meaning).
        Keep the turns (where the meaning is)."
        
        Args:
            trajectory: List of LJPW states
            keep_ratio: Fraction of points to keep (0-1)
        
        Returns:
            Compressed trajectory with highest-meaning points
        """
        if len(trajectory) < 3:
            return trajectory
        
        curvatures = self.curvature_calc.meaning_density(trajectory)
        
        # Sort indices by curvature (descending)
        sorted_indices = sorted(range(len(curvatures)), 
                                key=lambda i: curvatures[i], 
                                reverse=True)
        
        # Keep top points by curvature
        n_keep = max(3, int(len(trajectory) * keep_ratio))
        keep_indices = sorted(sorted_indices[:n_keep])
        
        return [trajectory[i] for i in keep_indices]


# Convenience functions

def calculate_meaning(trajectory: List[LJPWState]) -> float:
    """
    Calculate total meaning in a trajectory.
    
    M = ∫κ(s)ds (integral of curvature)
    """
    calc = CurvatureCalculator()
    return calc.total_curvature(trajectory)


def analyze_trajectory(trajectory: List[LJPWState]) -> TrajectoryAnalysis:
    """
    Analyze a trajectory for meaning patterns.
    """
    analyzer = TrajectoryAnalyzer()
    return analyzer.analyze(trajectory)


def compress_semantically(trajectory: List[LJPWState], 
                          keep_ratio: float = 0.3) -> List[LJPWState]:
    """
    Compress trajectory keeping only high-meaning points.
    """
    analyzer = TrajectoryAnalyzer()
    return analyzer.semantic_compression(trajectory, keep_ratio)
