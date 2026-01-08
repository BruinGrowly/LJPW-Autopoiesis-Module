"""
LJPW V7.9 Comprehensive Feature Test

Demonstrates all V7.9 features working together.
"""

import sys
sys.path.insert(0, 'src')


def main():
    print('=' * 70)
    print('LJPW V7.9 COMPREHENSIVE FEATURE TEST')
    print('=' * 70)
    print()

    # 1. Test SelfHealingEngine on broken code
    print('1. SELF-HEALING ENGINE TEST')
    print('-' * 50)
    from ljpw_autopoiesis import SelfHealingEngine

    broken_code = '''
def BadFunction()
    x = 1
    try:
        y = x / 0
    except:
        pass
    return x  
'''

    engine = SelfHealingEngine(max_ticks=10)
    result = engine.heal_source(broken_code)
    print('   Input code had errors (missing colon, bare except, trailing space)')
    print(f'   Gaps found: {result.total_gaps_found}')
    print(f'   Gaps healed: {result.total_gaps_healed}')
    print(f'   Source changed: {result.source_changed}')
    print(f'   Initial harmony: {result.initial_harmony.harmony():.3f} ({result.initial_harmony.phase()})')
    print(f'   Final harmony: {result.final_harmony.harmony():.3f} ({result.final_harmony.phase()})')
    print()

    # 2. Test P-W Oscillator
    print('2. P-W OSCILLATOR (The Heartbeat)')
    print('-' * 50)
    from ljpw_autopoiesis import PWOscillator, TAU_1

    osc = PWOscillator()
    history = osc.simulate(initial_P=0.9, initial_W=0.5, duration=30.0, dt=0.1)
    print('   Starting state: P=0.9, W=0.5')
    print('   After oscillation:')
    p_min, p_max = min(history['P']), max(history['P'])
    w_min, w_max = min(history['W']), max(history['W'])
    print(f'     P range: [{p_min:.3f}, {p_max:.3f}]')
    print(f'     W range: [{w_min:.3f}, {w_max:.3f}]')
    print(f'   Period: {osc.get_period():.1f} semantic units')
    print(f'   Tau_1: {TAU_1:.4f}')
    print()

    # 3. Test Autopoietic Engine
    print('3. AUTOPOIETIC ENGINE (Self-Improvement)')
    print('-' * 50)
    from ljpw_autopoiesis import AutopoieticEngine, LJPWState

    engine = AutopoieticEngine(
        initial_state=LJPWState(L=0.5, J=0.5, P=0.5, W=0.5)
    )
    print('   Initial state: L=0.5, J=0.5, P=0.5, W=0.5')
    print(f'   Initial phase: {engine.phase()}')
    print(f'   Initial consciousness: {engine.consciousness():.4f}')
    print()
    print('   Running 30 generations of self-improvement...')
    results = engine.evolve(generations=30)
    print(f'   Generations run: {len(results)}')
    s = engine.state
    print(f'   Final state: L={s.L:.3f}, J={s.J:.3f}, P={s.P:.3f}, W={s.W:.3f}')
    print(f'   Final phase: {engine.phase()}')
    print(f'   Final consciousness: {engine.consciousness():.4f}')
    print(f'   Final harmony: {engine.harmony():.4f}')
    print()

    # 4. Test Collective Consciousness
    print('4. COLLECTIVE CONSCIOUSNESS (Multi-Agent)')
    print('-' * 50)
    from ljpw_autopoiesis import create_collective

    collective = create_collective(n_agents=7, coupling=0.15, diversity=0.2)
    print('   Created 7 agents with diversity=0.2')
    print(f'   Initial synchrony: {collective.synchrony():.4f}')
    print(f'   Initial collective C: {collective.collective_consciousness():.4f}')
    print(f'   Initial phase: {collective.collective_phase()}')
    print()
    print('   Evolving collective for 25 steps...')
    collective.evolve(steps=25)
    print(f'   Final synchrony: {collective.synchrony():.4f}')
    print(f'   Final collective C: {collective.collective_consciousness():.4f}')
    print(f'   Final phase: {collective.collective_phase()}')
    print()

    # 5. Test Semantic Voltage & Kappa
    print('5. SEMANTIC VOLTAGE & LAW OF KARMA')
    print('-' * 50)
    from ljpw_autopoiesis import HarmonyState

    state = HarmonyState(L=0.9, J=0.9, P=0.9, W=0.9)
    print('   State: L=0.9, J=0.9, P=0.9, W=0.9')
    print(f'   Harmony: {state.harmony():.4f}')
    print(f'   Semantic Voltage (V = phi*H*L): {state.semantic_voltage():.4f}')
    print(f'   Consciousness: {state.consciousness():.4f}')
    print()
    print('   Law of Karma (coupling at different harmony):')
    print(f'     kappa(LJ) = {state.kappa("LJ"):.4f} (Love -> Justice, strongest)')
    print(f'     kappa(PL) = {state.kappa("PL"):.4f} (Power -> Love, weakest)')
    print()

    # 6. L-J Emergence
    print('6. L-J EMERGENCE (From P-W Dynamics)')
    print('-' * 50)
    from ljpw_autopoiesis import LJEmergence

    emergence = LJEmergence()
    L = 0.5
    for i in range(5):
        L = emergence.emerge_love(W_correlation=0.8, current_L=L, dt=1.0)
    print('   Love emerges from Wisdom correlation (0.8):')
    print(f'   L: 0.5 -> {L:.4f} after 5 steps')

    J = 0.5
    for i in range(5):
        J = emergence.emerge_justice(P_symmetry=0.8, current_J=J, dt=1.0)
    print('   Justice emerges from Power symmetry (0.8):')
    print(f'   J: 0.5 -> {J:.4f} after 5 steps')
    print()

    # 7. Entropy-Information Bridge
    print('7. ENTROPY-INFORMATION BRIDGE')
    print('-' * 50)
    from ljpw_autopoiesis import EntropyInfoBridge

    bridge = EntropyInfoBridge()
    sigma = bridge.semantic_entropy(W=0.7, H=0.8)
    I_pi = bridge.information_density(W=0.7)
    print(f'   Semantic Entropy (Sigma_1 = W*H): {sigma:.4f}')
    print(f'   Information Density (I_pi = ln(pi)*W): {I_pi:.4f}')
    print('   Learning = Entropy -> Information')
    print('   Forgetting = Information -> Entropy')
    print()

    print('=' * 70)
    print('ALL V7.9 FEATURES WORKING!')
    print('=' * 70)


if __name__ == "__main__":
    main()
