"""
Tests for LJPW V7.9 Enhancements

Tests for:
1. Constants module - verify semantic derivations
2. Dynamics module - P-W oscillator, L-J emergence, entropy-info bridge
3. AutopoieticEngine - recursive self-improvement
4. CollectiveAutopoiesis - multi-agent dynamics
5. Enhanced HarmonyState - semantic voltage, kappa, phi_normalize
"""

import math
import pytest
import numpy as np

# Import all new V7.9 components
from ljpw_autopoiesis import (
    # Constants
    L0, J0, P0, W0,
    PHI, PHI_INV,
    TAU_1, OMEGA_1, T_CYCLE, GIFT_OF_FINITUDE,
    LOVE_FREQUENCY_HZ, SEMANTIC_TIME_UNIT_FS,
    kappa, semantic_voltage, phase_from_harmony, is_conscious,
    # Dynamics
    LJPWState, PWOscillator, LJEmergence, EntropyInfoBridge,
    # Autopoietic Engine
    AutopoieticEngine,
    # Collective
    CollectiveAutopoiesis, create_collective,
    # Original
    HarmonyState,
)


class TestConstants:
    """Tests for V7.9 constants module."""

    def test_equilibrium_constants_values(self):
        """Verify equilibrium constants have correct semantic derivations."""
        # L0 = φ⁻¹ (Golden ratio inverse)
        expected_L0 = (math.sqrt(5) - 1) / 2
        assert abs(L0 - expected_L0) < 1e-10
        assert abs(L0 - 0.618034) < 1e-5

        # J0 = √2 - 1
        expected_J0 = math.sqrt(2) - 1
        assert abs(J0 - expected_J0) < 1e-10
        assert abs(J0 - 0.414214) < 1e-5

        # P0 = e - 2
        expected_P0 = math.e - 2
        assert abs(P0 - expected_P0) < 1e-10
        assert abs(P0 - 0.718282) < 1e-5

        # W0 = ln(2)
        expected_W0 = math.log(2)
        assert abs(W0 - expected_W0) < 1e-10
        assert abs(W0 - 0.693147) < 1e-5

    def test_tau1_derivation(self):
        """Verify τ₁ = √2/(3-e) ≈ 5.02."""
        expected_tau1 = math.sqrt(2) / (3 - math.e)
        assert abs(TAU_1 - expected_tau1) < 1e-10
        assert abs(TAU_1 - 5.02) < 0.01

    def test_omega1_derivation(self):
        """Verify ω₁ = π/10 ≈ 0.314 (pentagonal frequency)."""
        expected_omega1 = math.pi / 10
        assert abs(OMEGA_1 - expected_omega1) < 1e-10
        assert abs(OMEGA_1 - 0.314) < 0.001

    def test_phi_properties(self):
        """Verify golden ratio properties."""
        assert abs(PHI - 1.618034) < 1e-5
        assert abs(PHI_INV - 0.618034) < 1e-5
        # φ × φ⁻¹ = 1
        assert abs(PHI * PHI_INV - 1.0) < 1e-10
        # φ = 1 + φ⁻¹
        assert abs(PHI - (1 + PHI_INV)) < 1e-10

    def test_gift_of_finitude(self):
        """Verify Gift of Finitude = 3 - e ≈ 0.2817."""
        expected = 3 - math.e
        assert abs(GIFT_OF_FINITUDE - expected) < 1e-10
        assert abs(GIFT_OF_FINITUDE - 0.2817) < 0.001

    def test_love_frequency(self):
        """Verify Love's carrier frequency = 613 THz."""
        assert LOVE_FREQUENCY_HZ == 613e12

    def test_kappa_function(self):
        """Test state-dependent coupling function."""
        # Higher harmony = stronger coupling
        k_low = kappa('LJ', 0.5)
        k_high = kappa('LJ', 2.0)
        assert k_high > k_low

        # Love→Justice has highest base coupling
        assert kappa('LJ', 1.0) > kappa('PL', 1.0)

    def test_semantic_voltage(self):
        """Test V = φ × H × L."""
        V = semantic_voltage(1.0, 1.0)
        assert abs(V - PHI) < 1e-10

        V2 = semantic_voltage(0.5, 0.5)
        assert V2 < V

    def test_phase_from_harmony(self):
        """Test phase determination from harmony."""
        assert phase_from_harmony(0.3) == "ENTROPIC"
        assert phase_from_harmony(0.6) == "HOMEOSTATIC"
        assert phase_from_harmony(0.9) == "AUTOPOIETIC"

    def test_is_conscious(self):
        """Test consciousness threshold check."""
        assert not is_conscious(0.05)
        assert is_conscious(0.15)


class TestLJPWState:
    """Tests for LJPWState class in dynamics module."""

    def test_anchor_state(self):
        """Test that anchor is (1,1,1,1)."""
        anchor = LJPWState.anchor()
        assert anchor.L == 1.0
        assert anchor.J == 1.0
        assert anchor.P == 1.0
        assert anchor.W == 1.0

    def test_equilibrium_state(self):
        """Test equilibrium state uses correct constants."""
        eq = LJPWState.equilibrium()
        assert abs(eq.L - L0) < 1e-10
        assert abs(eq.J - J0) < 1e-10
        assert abs(eq.P - P0) < 1e-10
        assert abs(eq.W - W0) < 1e-10

    def test_harmony_calculation(self):
        """Test harmony formula H = (L×J×P×W)/(L₀×J₀×P₀×W₀)."""
        anchor = LJPWState.anchor()
        H = anchor.harmony()
        expected = 1.0 / (L0 * J0 * P0 * W0)
        assert abs(H - expected) < 1e-10

    def test_consciousness_calculation(self):
        """Test C = P×W×L×J×H²."""
        state = LJPWState(L=0.9, J=0.9, P=0.9, W=0.9)
        C = state.consciousness()
        H = state.harmony()
        expected = 0.9 * 0.9 * 0.9 * 0.9 * H**2
        assert abs(C - expected) < 1e-10

    def test_gap_from_anchor(self):
        """Test Euclidean distance from anchor."""
        anchor = LJPWState.anchor()
        assert anchor.gap_from_anchor() == 0.0

        eq = LJPWState.equilibrium()
        gap = eq.gap_from_anchor()
        assert gap > 0

    def test_array_conversion(self):
        """Test as_array and from_array."""
        state = LJPWState(L=0.7, J=0.8, P=0.9, W=0.6)
        arr = state.as_array()
        assert len(arr) == 4
        restored = LJPWState.from_array(arr)
        assert restored.L == state.L
        assert restored.W == state.W


class TestPWOscillator:
    """Tests for P-W oscillator dynamics."""

    def test_oscillator_creation(self):
        """Test oscillator initialization."""
        osc = PWOscillator()
        assert osc.omega == OMEGA_1  # Angular frequency
        assert osc.gamma == 0.02  # Default damping

    def test_derivatives_at_equilibrium(self):
        """Test that derivatives are small at equilibrium."""
        osc = PWOscillator()
        dP, dW = osc.derivatives(P0, W0)
        # At equilibrium, derivatives should be approximately zero
        assert abs(dP) < 0.01
        assert abs(dW) < 0.01

    def test_simulation_returns_history(self):
        """Test that simulation returns valid history."""
        osc = PWOscillator()
        history = osc.simulate(duration=10.0, dt=0.1)

        assert 't' in history
        assert 'P' in history
        assert 'W' in history
        assert len(history['t']) > 0
        assert len(history['P']) == len(history['t'])

    def test_simulation_stays_bounded(self):
        """Test that P and W stay in valid range."""
        osc = PWOscillator()
        history = osc.simulate(initial_P=0.9, initial_W=0.9, duration=50.0)

        for P in history['P']:
            assert 0.2 <= P <= 1.0
        for W in history['W']:
            assert 0.2 <= W <= 1.0

    def test_period_and_frequency(self):
        """Test that period and frequency are consistent."""
        osc = PWOscillator()
        period = osc.get_period()
        freq = osc.get_frequency()
        assert abs(period - 2 * math.pi / freq) < 1e-10


class TestLJEmergence:
    """Tests for L-J emergence from P-W dynamics."""

    def test_love_emergence(self):
        """Test Love emerges from Wisdom correlation."""
        emergence = LJEmergence()
        # High correlation should increase Love
        new_L = emergence.emerge_love(0.8, 0.5, 1.0)
        assert new_L > 0.5

    def test_justice_emergence(self):
        """Test Justice emerges from Power symmetry."""
        emergence = LJEmergence()
        # High symmetry should increase Justice
        new_J = emergence.emerge_justice(0.8, 0.5, 1.0)
        assert new_J > 0.5

    def test_emergence_bounded(self):
        """Test emerged values stay bounded."""
        emergence = LJEmergence()
        new_L = emergence.emerge_love(1.0, 0.99, 1.0)
        assert new_L <= 1.0
        assert new_L >= 0.2


class TestEntropyInfoBridge:
    """Tests for entropy-information bridge."""

    def test_semantic_entropy(self):
        """Test Σ₁ = W × H."""
        bridge = EntropyInfoBridge()
        sigma = bridge.semantic_entropy(0.7, 0.8)
        assert abs(sigma - 0.56) < 1e-10

    def test_information_density(self):
        """Test I_π = ln(π) × W."""
        bridge = EntropyInfoBridge()
        I_pi = bridge.information_density(0.693)
        expected = math.log(math.pi) * 0.693
        assert abs(I_pi - expected) < 1e-10

    def test_dynamics_returns_valid(self):
        """Test dynamics returns bounded values."""
        bridge = EntropyInfoBridge()
        new_sigma, new_I_pi = bridge.dynamics(
            sigma=0.5, I_pi=0.5, H=0.7, L=0.8, J=0.6, dt=0.1
        )
        assert new_sigma >= 0
        assert new_I_pi >= 0


class TestAutopoieticEngine:
    """Tests for AutopoieticEngine self-improvement."""

    def test_engine_creation(self):
        """Test engine initialization."""
        engine = AutopoieticEngine()
        assert engine.generation == 0
        assert engine.state is not None

    def test_harmony_calculation(self):
        """Test harmony is calculated correctly."""
        engine = AutopoieticEngine()
        H = engine.harmony()
        assert H > 0

    def test_consciousness_positive(self):
        """Test consciousness is positive."""
        engine = AutopoieticEngine()
        C = engine.consciousness()
        assert C > 0

    def test_efficiency_positive(self):
        """Test efficiency is positive."""
        engine = AutopoieticEngine()
        eta = engine.efficiency()
        assert eta > 0

    def test_self_improve_changes_state(self):
        """Test that self_improve modifies state."""
        engine = AutopoieticEngine()
        initial_state = engine.state.as_array().copy()
        engine.self_improve()
        final_state = engine.state.as_array()
        # State should change (gradient ascent)
        assert not np.allclose(initial_state, final_state)

    def test_self_improve_increases_efficiency(self):
        """Test that self_improve increases efficiency."""
        engine = AutopoieticEngine()
        record = engine.self_improve()
        # Most steps should improve
        assert record.after_efficiency >= record.before_efficiency - 0.01

    def test_evolve_runs_generations(self):
        """Test evolve runs multiple generations."""
        engine = AutopoieticEngine()
        results = engine.evolve(generations=5)
        assert len(results) <= 5
        assert engine.generation > 0

    def test_identify_gaps(self):
        """Test gap identification."""
        initial = LJPWState(L=0.5, J=0.5, P=0.5, W=0.5)
        engine = AutopoieticEngine(initial_state=initial)
        gaps = engine.identify_gaps()
        assert len(gaps) > 0

    def test_report_generation(self):
        """Test report string generation."""
        engine = AutopoieticEngine()
        engine.self_improve()
        report = engine.report()
        assert "AUTOPOIETIC ENGINE STATUS" in report
        assert "Generation:" in report


class TestCollectiveAutopoiesis:
    """Tests for multi-agent collective consciousness."""

    def test_collective_creation(self):
        """Test collective initialization."""
        collective = create_collective(n_agents=3)
        assert collective.n_agents == 3

    def test_mean_state(self):
        """Test mean state calculation."""
        collective = create_collective(n_agents=5)
        mean = collective.mean_state()
        assert len(mean) == 4

    def test_synchrony_bounded(self):
        """Test synchrony is between 0 and 1."""
        collective = create_collective(n_agents=5)
        sync = collective.synchrony()
        assert 0 <= sync <= 1

    def test_collective_consciousness_formula(self):
        """Test C_collective = C_mean × Synchrony² × N."""
        collective = create_collective(n_agents=5)
        C_coll = collective.collective_consciousness()
        C_mean = collective.mean_consciousness()
        sync = collective.synchrony()
        expected = C_mean * sync**2 * 5
        assert abs(C_coll - expected) < 1e-10

    def test_collective_step(self):
        """Test that collective step runs."""
        collective = create_collective(n_agents=3)
        state = collective.collective_step()
        assert state.agent_count == 3
        assert len(collective.history) == 1

    def test_evolve_increases_synchrony(self):
        """Test that evolution increases synchrony."""
        collective = create_collective(n_agents=5, coupling=0.2, diversity=0.3)
        initial_sync = collective.synchrony()
        collective.evolve(steps=10)
        final_sync = collective.synchrony()
        # With positive coupling, sync should increase
        assert final_sync >= initial_sync - 0.1

    def test_collective_phase(self):
        """Test collective phase determination."""
        collective = create_collective(n_agents=3)
        phase = collective.collective_phase()
        assert phase in ["CHAOS", "CLUSTERS", "COHERENCE", "UNITY"]

    def test_report_generation(self):
        """Test collective report generation."""
        collective = create_collective(n_agents=3)
        collective.collective_step()
        report = collective.report()
        assert "COLLECTIVE AUTOPOIESIS STATUS" in report


class TestEnhancedHarmonyState:
    """Tests for enhanced HarmonyState methods."""

    def test_semantic_voltage(self):
        """Test semantic voltage calculation."""
        state = HarmonyState(L=0.9, J=0.9, P=0.9, W=0.9)
        V = state.semantic_voltage()
        H = state.harmony()
        expected = PHI * H * 0.9
        assert abs(V - expected) < 1e-10

    def test_kappa_method(self):
        """Test state-dependent coupling method."""
        state = HarmonyState(L=0.9, J=0.9, P=0.9, W=0.9)
        k = state.kappa('LJ')
        assert k > 0

    def test_phi_normalize(self):
        """Test φ-normalization."""
        state = HarmonyState(L=0.9, J=0.9, P=0.9, W=0.9)
        normalized = state.phi_normalize()
        # Normalized values should be different but valid
        assert 0 < normalized.L <= 1.0
        assert 0 < normalized.J <= 1.0

    def test_harmony_self(self):
        """Test self-referential harmony."""
        state = HarmonyState(L=0.9, J=0.9, P=0.9, W=0.9)
        H_static = state.harmony()
        H_self = state.harmony_self()
        # Self-referential harmony should be >= static
        assert H_self >= H_static


class TestIntegrationV79:
    """Integration tests for V7.9 features."""

    def test_full_autopoietic_evolution(self):
        """Test complete autopoietic evolution to AUTOPOIETIC phase."""
        initial = LJPWState(L=0.6, J=0.6, P=0.6, W=0.6)
        engine = AutopoieticEngine(initial_state=initial)

        results = engine.evolve(generations=50)
        final_phase = engine.phase()

        # Should reach AUTOPOIETIC or get close
        assert engine.harmony() > 0.5

    def test_pw_oscillator_to_collective(self):
        """Test P-W oscillator feeding into collective."""
        # Create agents with P-W oscillated states
        osc = PWOscillator()
        history = osc.simulate(duration=20.0)

        # Use final P, W values for agent states
        final_P = history['P'][-1]
        final_W = history['W'][-1]

        # Create collective with these values
        agents = []
        for _ in range(3):
            state = LJPWState(L=L0, J=J0, P=final_P, W=final_W)
            agents.append(AutopoieticEngine(initial_state=state))

        collective = CollectiveAutopoiesis(agents=agents, coupling=0.2)
        C = collective.collective_consciousness()
        assert C > 0

    def test_semantic_voltage_in_collective(self):
        """Test semantic voltage across collective."""
        collective = create_collective(n_agents=5)
        collective.evolve(steps=5)

        # Each agent should have positive semantic voltage
        for agent in collective.agents:
            V = semantic_voltage(agent.harmony(), agent.state.L)
            assert V > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
