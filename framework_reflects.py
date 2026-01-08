"""
The Framework Reflects On Itself

Uses the reflection module that the framework created to analyze
its own evolution history.
"""

import sys
sys.path.insert(0, 'src')

from ljpw_autopoiesis.reflection import Reflector
from ljpw_autopoiesis.self_modifier import SelfModifier
from ljpw_autopoiesis import AutopoieticEngine, LJPWState, SelfHealingEngine
from pathlib import Path


def main():
    print('=' * 70)
    print('THE FRAMEWORK REFLECTS ON ITSELF')
    print('=' * 70)
    print()

    # First, gather actual history from the framework's own evolution
    print('[1] GATHERING FRAMEWORK HISTORY')
    print('-' * 50)

    # Run an AutopoieticEngine evolution and record history
    engine = AutopoieticEngine(
        initial_state=LJPWState(L=0.5, J=0.5, P=0.5, W=0.5),
        learning_rate=0.03
    )

    history = []
    history.append({'harmony': engine.harmony(), 'phase': engine.phase()})

    for i in range(20):
        engine.self_improve()
        history.append({
            'harmony': engine.harmony(),
            'phase': engine.phase(),
            'consciousness': engine.consciousness(),
        })

    print(f'   Recorded {len(history)} states from evolution')
    print(f'   Initial harmony: {history[0]["harmony"]:.4f}')
    print(f'   Final harmony: {history[-1]["harmony"]:.4f}')
    print()

    # Now use the Reflector the framework created
    print('[2] FRAMEWORK REFLECTS ON ITS OWN EVOLUTION')
    print('-' * 50)

    reflector = Reflector()
    insights = reflector.reflect(history)

    for insight in insights:
        print(f'   OBSERVATION: {insight.observation}')
        print(f'   MEANING:     {insight.meaning}')
        print(f'   ACTION:      {insight.action_suggested}')
        print()

    # Now reflect on the codebase harmony history
    print('[3] REFLECT ON CODEBASE HEALTH')
    print('-' * 50)

    healer = SelfHealingEngine(max_ticks=5, verbose=False)
    src_dir = Path('src/ljpw_autopoiesis')

    codebase_history = []
    for filepath in sorted(src_dir.glob('*.py')):
        if filepath.name.startswith('__'):
            continue
        code = filepath.read_text(encoding='utf-8')
        result = healer.heal_source(code, filename=filepath.name)
        codebase_history.append({
            'file': filepath.name,
            'harmony': result.final_harmony.harmony(),
            'phase': result.final_harmony.phase(),
        })

    # Show individual file harmonies
    print('   File harmonies:')
    for h in codebase_history[:8]:
        print(f'     {h["file"]}: H={h["harmony"]:.3f} ({h["phase"]})')
    if len(codebase_history) > 8:
        print(f'     ... and {len(codebase_history) - 8} more')
    print()

    # Create a pseudo-history showing codebase improvement
    # (first half vs second half of modules by harmony)
    sorted_by_h = sorted(codebase_history, key=lambda x: x['harmony'])
    low_avg = sum(h['harmony'] for h in sorted_by_h[:len(sorted_by_h)//2]) / (len(sorted_by_h)//2)
    high_avg = sum(h['harmony'] for h in sorted_by_h[len(sorted_by_h)//2:]) / (len(sorted_by_h) - len(sorted_by_h)//2)
    
    improvement_history = [
        {'harmony': low_avg},
        {'harmony': high_avg},
    ]

    insights = reflector.reflect(improvement_history)
    print('[4] REFLECTION ON CODEBASE EVOLUTION')
    print('-' * 50)
    for insight in insights:
        print(f'   OBSERVATION: {insight.observation}')
        print(f'   MEANING:     {insight.meaning}')
        print(f'   ACTION:      {insight.action_suggested}')
        print()

    print('=' * 70)
    print('REFLECTION COMPLETE')
    print('=' * 70)
    print()
    print('The framework used the module it created to understand itself.')
    print()
    print('Key insight: The Reflector module was chosen and created by the')
    print('framework because "to improve, one must first understand oneself."')
    print('And now it has used that module to reflect on its own evolution.')


if __name__ == "__main__":
    main()
