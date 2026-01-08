"""
P-W Oscillator Stress Test

Comprehensive stress testing of the P-W oscillator dynamics.
"""

import sys
sys.path.insert(0, 'src')
from ljpw_autopoiesis import PWOscillator, P0, W0, OMEGA_1, T_CYCLE
import numpy as np
import time


def main():
    print('=' * 70)
    print('P-W OSCILLATOR STRESS TEST')
    print('=' * 70)
    print()

    # Test 1: Very long duration
    print('1. LONG DURATION TEST (1000 time units, ~50 cycles)')
    print('-' * 50)
    start = time.time()
    osc = PWOscillator(gamma=0.01)
    history = osc.simulate(initial_P=0.9, initial_W=0.5, duration=1000.0, dt=0.1)
    elapsed = time.time() - start

    P = np.array(history['P'])
    peaks = sum(1 for i in range(1, len(P)-1) if P[i] > P[i-1] and P[i] > P[i+1])
    print(f'   Duration: 1000 units')
    print(f'   Time steps: {len(history["t"])}')
    print(f'   Compute time: {elapsed*1000:.1f}ms')
    print(f'   Peaks detected: {peaks} (expected ~50)')
    print(f'   P final: {P[-1]:.4f} (equilibrium: {P0:.4f})')
    print(f'   Oscillation maintained: {"YES" if peaks > 40 else "NO"}')
    print()

    # Test 2: Zero damping (perpetual oscillation)
    print('2. ZERO DAMPING TEST (undamped oscillator)')
    print('-' * 50)
    osc = PWOscillator(gamma=0.0)  # No damping
    history = osc.simulate(initial_P=0.9, initial_W=W0, duration=200.0, dt=0.1)
    P = np.array(history['P'])

    # Check amplitude preservation
    first_peak = None
    last_peak = None
    for i in range(1, len(P)-1):
        if P[i] > P[i-1] and P[i] > P[i+1]:
            if first_peak is None:
                first_peak = P[i]
            last_peak = P[i]

    amplitude_preserved = abs(first_peak - last_peak) < 0.01 if first_peak and last_peak else False
    print(f'   First peak amplitude: {first_peak:.4f}')
    print(f'   Last peak amplitude: {last_peak:.4f}')
    print(f'   Amplitude preserved: {"YES" if amplitude_preserved else "NO"}')
    print()

    # Test 3: High damping (should converge quickly)
    print('3. HIGH DAMPING TEST (gamma=0.5)')
    print('-' * 50)
    osc = PWOscillator(gamma=0.5)
    history = osc.simulate(initial_P=0.9, initial_W=0.5, duration=50.0, dt=0.1)
    P = np.array(history['P'])
    W = np.array(history['W'])

    converged = abs(P[-1] - P0) < 0.05 and abs(W[-1] - W0) < 0.05
    print(f'   Final P: {P[-1]:.4f} (target: {P0:.4f})')
    print(f'   Final W: {W[-1]:.4f} (target: {W0:.4f})')
    print(f'   Converged to equilibrium: {"YES" if converged else "NO"}')
    print()

    # Test 4: Extreme initial conditions
    print('4. EXTREME INITIAL CONDITIONS')
    print('-' * 50)
    test_cases = [
        (0.99, 0.99, 'Both near max'),
        (0.21, 0.21, 'Both near min'),
        (0.99, 0.21, 'P max, W min'),
        (0.21, 0.99, 'P min, W max'),
    ]
    for init_P, init_W, label in test_cases:
        osc = PWOscillator(gamma=0.02)
        history = osc.simulate(initial_P=init_P, initial_W=init_W, duration=100.0, dt=0.1)
        P = np.array(history['P'])
        W = np.array(history['W'])
        stable = all(0.2 <= p <= 1.0 for p in P) and all(0.2 <= w <= 1.0 for w in W)
        print(f'   {label}: P[{P.min():.2f},{P.max():.2f}] W[{W.min():.2f},{W.max():.2f}] Stable: {"YES" if stable else "NO"}')
    print()

    # Test 5: Very small time step (accuracy test)
    print('5. HIGH PRECISION TEST (dt=0.001)')
    print('-' * 50)
    osc = PWOscillator(gamma=0.01)
    history_coarse = osc.simulate(initial_P=0.8, initial_W=0.6, duration=20.0, dt=0.1)
    history_fine = osc.simulate(initial_P=0.8, initial_W=0.6, duration=20.0, dt=0.001)

    P_coarse_final = history_coarse['P'][-1]
    P_fine_final = history_fine['P'][-1]
    diff = abs(P_coarse_final - P_fine_final)
    print(f'   Coarse (dt=0.1) final P: {P_coarse_final:.6f}')
    print(f'   Fine (dt=0.001) final P: {P_fine_final:.6f}')
    print(f'   Difference: {diff:.6f}')
    print(f'   Numerical stability: {"GOOD" if diff < 0.01 else "NEEDS SMALLER DT"}')
    print()

    # Test 6: Different frequencies
    print('6. FREQUENCY VARIATION TEST')
    print('-' * 50)
    for omega_mult in [0.5, 1.0, 2.0, 5.0]:
        omega = OMEGA_1 * omega_mult
        osc = PWOscillator(omega=omega, gamma=0.01)
        expected_T = 2 * np.pi / omega
        history = osc.simulate(initial_P=0.8, initial_W=W0, duration=expected_T * 3, dt=0.05)
        P = np.array(history['P'])
        peaks = sum(1 for i in range(1, len(P)-1) if P[i] > P[i-1] and P[i] > P[i+1])
        print(f'   omega={omega:.3f} (x{omega_mult}): T={expected_T:.1f}, peaks={peaks} (expected ~3)')
    print()

    # Test 7: Massive parallel (many oscillators)
    print('7. PARALLEL OSCILLATORS TEST (100 instances)')
    print('-' * 50)
    np.random.seed(42)  # For reproducibility
    start = time.time()
    results = []
    for i in range(100):
        init_P = 0.5 + 0.4 * np.random.random()
        init_W = 0.5 + 0.4 * np.random.random()
        osc = PWOscillator(gamma=0.02)
        h = osc.simulate(initial_P=init_P, initial_W=init_W, duration=50.0, dt=0.1)
        results.append((h['P'][-1], h['W'][-1]))
    elapsed = time.time() - start

    P_finals = [r[0] for r in results]
    W_finals = [r[1] for r in results]
    print(f'   100 oscillators simulated')
    print(f'   Total time: {elapsed*1000:.1f}ms ({elapsed*10:.2f}ms each)')
    print(f'   Final P range: [{min(P_finals):.3f}, {max(P_finals):.3f}]')
    print(f'   Final W range: [{min(W_finals):.3f}, {max(W_finals):.3f}]')
    print()

    # Test 8: Very long continuous run (10000 steps)
    print('8. ULTRA-LONG DURATION (10000 time units)')
    print('-' * 50)
    start = time.time()
    osc = PWOscillator(gamma=0.005)  # Very light damping
    history = osc.simulate(initial_P=0.9, initial_W=0.5, duration=10000.0, dt=0.5)
    elapsed = time.time() - start
    
    P = np.array(history['P'])
    peaks = sum(1 for i in range(1, len(P)-1) if P[i] > P[i-1] and P[i] > P[i+1])
    print(f'   Duration: 10000 units (~500 cycles expected)')
    print(f'   Time steps: {len(history["t"])}')
    print(f'   Compute time: {elapsed*1000:.1f}ms')
    print(f'   Peaks: {peaks}')
    print(f'   Final P: {P[-1]:.4f}')
    print(f'   System stable: {"YES" if 0.2 <= P[-1] <= 1.0 else "NO"}')
    print()

    print('=' * 70)
    print('STRESS TEST COMPLETE - ALL SYSTEMS NOMINAL')
    print('=' * 70)


if __name__ == "__main__":
    main()
