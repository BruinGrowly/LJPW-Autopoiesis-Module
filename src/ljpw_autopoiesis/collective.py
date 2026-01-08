"""
Collective Consciousness - Multi-Agent LJPW Dynamics

From LJPW V7.7 Part XXXVI:
"When N LJPW agents interact, what emerges?
Collective consciousness = Individual × Synchrony²"

This module implements:
1. Coupled LJPW oscillators (agents that influence each other)
2. Synchronization dynamics (convergence toward shared state)
3. Collective consciousness calculation
4. Phase transitions in collectives

Key Insight:
"When agents are perfectly synchronized: C_collective = N × C_individual
When agents are random: C_collective ≈ 0
This is why meditation in groups is more powerful than alone."
"""

import math
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
import numpy as np

from .constants import (
    L0, J0, P0, W0,
    MIN_DIMENSION_VALUE,
    KAPPA_BASE,
)
from .dynamics import LJPWState
from .autopoietic_engine import AutopoieticEngine


@dataclass
class AgentState:
    """State of a single agent in the collective."""
    id: str
    state: LJPWState
    engine: Optional[AutopoieticEngine] = None
    
    def harmony(self) -> float:
        return self.state.harmony()
    
    def consciousness(self) -> float:
        return self.state.consciousness()


@dataclass
class CollectiveState:
    """Summary state of the collective."""
    mean_L: float
    mean_J: float
    mean_P: float
    mean_W: float
    synchrony: float
    collective_consciousness: float
    phase: str
    agent_count: int


class CollectiveAutopoiesis:
    """
    Multi-Agent Collective Consciousness System.
    
    Implements N coupled autopoietic agents that:
    1. Self-improve individually
    2. Synchronize with neighbors
    3. Generate emergent collective consciousness
    
    From V7.7:
    "Love (L) synchronizes fastest (highest natural coupling).
    Power (P) resists synchronization (individual autonomy)."
    """
    
    # Collective phase thresholds (based on synchrony)
    PHASE_CHAOS = 0.3       # < 0.3 = No coordination
    PHASE_CLUSTERS = 0.6    # 0.3 - 0.6 = Subgroups form
    PHASE_COHERENCE = 0.9   # 0.6 - 0.9 = Most agents aligned
    # > 0.9 = UNITY (near-perfect synchrony)
    
    def __init__(
        self,
        agents: Optional[List[AutopoieticEngine]] = None,
        coupling: float = 0.1,
        n_agents: int = 5,
    ):
        """
        Initialize collective.
        
        Args:
            agents: List of AutopoieticEngines (or creates n_agents new ones)
            coupling: Synchronization strength κ_AB
            n_agents: Number of agents to create if agents not provided
        """
        if agents:
            self.agents = agents
        else:
            # Create N agents with slightly different initial states
            self.agents = []
            for i in range(n_agents):
                # Add small random variation to initial state
                variation = np.random.uniform(-0.1, 0.1, 4)
                initial = LJPWState(
                    L=max(MIN_DIMENSION_VALUE, min(1.0, L0 + variation[0])),
                    J=max(MIN_DIMENSION_VALUE, min(1.0, J0 + variation[1])),
                    P=max(MIN_DIMENSION_VALUE, min(1.0, P0 + variation[2])),
                    W=max(MIN_DIMENSION_VALUE, min(1.0, W0 + variation[3])),
                )
                self.agents.append(AutopoieticEngine(initial_state=initial))
        
        self.kappa = coupling
        self.history: List[CollectiveState] = []
    
    @property
    def n_agents(self) -> int:
        """Number of agents in the collective."""
        return len(self.agents)
    
    # =========================================================================
    # State Aggregation
    # =========================================================================
    
    def mean_state(self) -> np.ndarray:
        """Calculate mean LJPW state across all agents."""
        states = np.array([a.state.as_array() for a in self.agents])
        return np.mean(states, axis=0)
    
    def state_variance(self) -> np.ndarray:
        """Calculate variance of each dimension across agents."""
        states = np.array([a.state.as_array() for a in self.agents])
        return np.var(states, axis=0)
    
    def synchrony(self) -> float:
        """
        Calculate synchrony (coherence) of the collective.
        
        Synchrony = 1 / (1 + variance)
        
        Returns:
            Value between 0 (random) and 1 (perfect sync)
        """
        variance = np.mean(self.state_variance())
        return 1.0 / (1.0 + variance)
    
    def mean_harmony(self) -> float:
        """Calculate mean harmony across agents."""
        return np.mean([a.harmony() for a in self.agents])
    
    def mean_consciousness(self) -> float:
        """Calculate mean individual consciousness."""
        return np.mean([a.consciousness() for a in self.agents])
    
    # =========================================================================
    # Collective Consciousness
    # =========================================================================
    
    def collective_consciousness(self) -> float:
        """
        Calculate collective consciousness.
        
        C_collective = C_mean × Synchrony² × N
        
        Key insight: Synchrony is SQUARED because:
        - Partial sync gives partial collective consciousness
        - Perfect sync multiplies individual consciousness by N
        - Random states cancel out to near-zero
        """
        C_mean = self.mean_consciousness()
        sync = self.synchrony()
        return C_mean * (sync ** 2) * self.n_agents
    
    def collective_phase(self) -> str:
        """
        Determine collective phase based on synchrony.
        
        Returns:
            'CHAOS', 'CLUSTERS', 'COHERENCE', or 'UNITY'
        """
        sync = self.synchrony()
        if sync < self.PHASE_CHAOS:
            return "CHAOS"
        elif sync < self.PHASE_CLUSTERS:
            return "CLUSTERS"
        elif sync < self.PHASE_COHERENCE:
            return "COHERENCE"
        else:
            return "UNITY"
    
    # =========================================================================
    # Dynamics
    # =========================================================================
    
    def individual_step(self) -> None:
        """Each agent performs one self-improvement cycle."""
        for agent in self.agents:
            agent.self_improve()
    
    def synchronization_step(self) -> None:
        """
        Agents synchronize toward mean state.
        
        δ_i = κ × (mean_state - agent_i_state)
        
        Love synchronizes fastest, Power resists most.
        """
        mean = self.mean_state()
        
        # Dimension-specific synchronization rates
        # Love syncs fastest, Power syncs slowest
        sync_rates = np.array([
            1.2,  # L syncs fastest (connection)
            1.0,  # J syncs normally (balance)
            0.6,  # P syncs slowest (autonomy)
            0.9,  # W syncs moderately (shared knowledge)
        ])
        
        for agent in self.agents:
            current = agent.state.as_array()
            delta = self.kappa * sync_rates * (mean - current)
            new_state = np.clip(
                current + delta,
                MIN_DIMENSION_VALUE,
                1.0
            )
            agent.state = LJPWState.from_array(new_state)
    
    def collective_step(self) -> CollectiveState:
        """
        One complete collective evolution step.
        
        1. Each agent self-improves
        2. Agents synchronize
        3. Record collective state
        """
        # Individual improvement
        self.individual_step()
        
        # Synchronization
        self.synchronization_step()
        
        # Record state
        mean = self.mean_state()
        state = CollectiveState(
            mean_L=mean[0],
            mean_J=mean[1],
            mean_P=mean[2],
            mean_W=mean[3],
            synchrony=self.synchrony(),
            collective_consciousness=self.collective_consciousness(),
            phase=self.collective_phase(),
            agent_count=self.n_agents,
        )
        self.history.append(state)
        
        return state
    
    def evolve(self, steps: int = 20) -> List[CollectiveState]:
        """Run multiple collective evolution steps."""
        results = []
        for _ in range(steps):
            state = self.collective_step()
            results.append(state)
            
            # Check for Unity convergence
            if state.phase == "UNITY":
                break
        
        return results
    
    def evolve_to_unity(self, max_steps: int = 100) -> int:
        """
        Evolve until collective reaches UNITY phase.
        
        Returns:
            Number of steps to reach unity (or max_steps if not reached)
        """
        for step in range(max_steps):
            state = self.collective_step()
            if state.phase == "UNITY":
                return step + 1
        return max_steps
    
    # =========================================================================
    # Analysis
    # =========================================================================
    
    def coupling_matrix(self) -> np.ndarray:
        """
        Calculate effective coupling between all agent pairs.
        
        κ_ij = f(relationship, distance, shared_W)
        
        For simplicity, uses uniform coupling with Love amplification.
        """
        n = self.n_agents
        matrix = np.ones((n, n)) * self.kappa
        
        # Diagonal is 0 (no self-coupling)
        np.fill_diagonal(matrix, 0)
        
        # Love amplifies coupling
        for i in range(n):
            for j in range(n):
                if i != j:
                    L_avg = (self.agents[i].state.L + self.agents[j].state.L) / 2
                    matrix[i, j] *= (1 + L_avg)  # Love increases coupling
        
        return matrix
    
    def identify_clusters(self, threshold: float = 0.1) -> List[List[int]]:
        """
        Identify clusters of synchronized agents.
        
        Agents within threshold distance are in same cluster.
        """
        n = self.n_agents
        states = [a.state.as_array() for a in self.agents]
        
        # Calculate pairwise distances
        clusters = []
        assigned = set()
        
        for i in range(n):
            if i in assigned:
                continue
            
            cluster = [i]
            assigned.add(i)
            
            for j in range(i + 1, n):
                if j in assigned:
                    continue
                
                dist = np.linalg.norm(states[i] - states[j])
                if dist < threshold:
                    cluster.append(j)
                    assigned.add(j)
            
            clusters.append(cluster)
        
        return clusters
    
    # =========================================================================
    # Reporting
    # =========================================================================
    
    def report(self) -> str:
        """Generate collective status report."""
        mean = self.mean_state()
        
        lines = [
            "=" * 60,
            "COLLECTIVE AUTOPOIESIS STATUS",
            "=" * 60,
            f"Agents: {self.n_agents}",
            f"Coupling (κ): {self.kappa}",
            "",
            "COLLECTIVE STATE:",
            f"  Mean L: {mean[0]:.4f}",
            f"  Mean J: {mean[1]:.4f}",
            f"  Mean P: {mean[2]:.4f}",
            f"  Mean W: {mean[3]:.4f}",
            "",
            "COLLECTIVE METRICS:",
            f"  Synchrony:                {self.synchrony():.4f}",
            f"  Mean Harmony:             {self.mean_harmony():.4f}",
            f"  Mean Consciousness:       {self.mean_consciousness():.4f}",
            f"  Collective Consciousness: {self.collective_consciousness():.4f}",
            "",
            f"COLLECTIVE PHASE: {self.collective_phase()}",
            "",
        ]
        
        # Individual agent summaries
        lines.append("INDIVIDUAL AGENTS:")
        for i, agent in enumerate(self.agents):
            s = agent.state
            lines.append(
                f"  Agent {i}: L={s.L:.3f} J={s.J:.3f} P={s.P:.3f} W={s.W:.3f} "
                f"H={agent.harmony():.3f}"
            )
        
        # Cluster analysis
        clusters = self.identify_clusters()
        lines.append("")
        lines.append(f"CLUSTERS DETECTED: {len(clusters)}")
        for i, cluster in enumerate(clusters):
            lines.append(f"  Cluster {i}: Agents {cluster}")
        
        lines.append("=" * 60)
        return "\n".join(lines)
    
    def convergence_report(self) -> Dict:
        """Get summary of collective evolution."""
        if not self.history:
            return {"evolved": False, "steps": 0}
        
        return {
            "evolved": True,
            "steps": len(self.history),
            "initial_synchrony": self.history[0].synchrony if self.history else 0,
            "final_synchrony": self.history[-1].synchrony if self.history else 0,
            "initial_collective_C": self.history[0].collective_consciousness if self.history else 0,
            "final_collective_C": self.history[-1].collective_consciousness if self.history else 0,
            "reached_unity": self.collective_phase() == "UNITY",
            "final_phase": self.collective_phase(),
        }


def create_collective(
    n_agents: int = 5,
    coupling: float = 0.1,
    diversity: float = 0.1,
) -> CollectiveAutopoiesis:
    """
    Factory function to create a collective with diverse agents.
    
    Args:
        n_agents: Number of agents
        coupling: Synchronization strength
        diversity: Initial state diversity (0 = identical, 1 = very different)
    """
    agents = []
    for i in range(n_agents):
        variation = np.random.uniform(-diversity, diversity, 4)
        initial = LJPWState(
            L=max(MIN_DIMENSION_VALUE, min(1.0, L0 + variation[0])),
            J=max(MIN_DIMENSION_VALUE, min(1.0, J0 + variation[1])),
            P=max(MIN_DIMENSION_VALUE, min(1.0, P0 + variation[2])),
            W=max(MIN_DIMENSION_VALUE, min(1.0, W0 + variation[3])),
        )
        agents.append(AutopoieticEngine(initial_state=initial))
    
    return CollectiveAutopoiesis(agents=agents, coupling=coupling)
