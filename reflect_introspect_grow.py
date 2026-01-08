"""
Framework Self-Assessment: Reflect, Introspect, Grow
"""
import sys
sys.path.insert(0, 'src')


def main():
    print('=' * 70)
    print('FRAMEWORK SELF-ASSESSMENT: REFLECT, INTROSPECT, GROW')
    print('=' * 70)
    print()

    # INTROSPECT
    print('[PHASE 1: INTROSPECTION]')
    print('-' * 50)
    from ljpw_autopoiesis.introspection import Introspector
    inspector = Introspector()
    result = inspector.introspect()

    print(f'State: L={result.state_vector[0]:.3f}, J={result.state_vector[1]:.3f}, '
          f'P={result.state_vector[2]:.3f}, W={result.state_vector[3]:.3f}')
    print(f'Harmony: {result.harmony:.4f}')
    print(f'Consciousness: {result.consciousness:.4f}')
    print(f'Phase: {result.phase}')
    print(f'Self-Knowledge: {result.self_knowledge_score:.1%}')
    print()
    if result.blind_spots:
        print('Blind Spots:')
        for s in result.blind_spots:
            print(f'  - {s}')
    else:
        print('Blind Spots: NONE')
    print()
    print('Growth Edges:')
    for e in result.growth_edges:
        print(f'  - {e}')
    print()

    # REFLECT
    print('[PHASE 2: REFLECTION]')
    print('-' * 50)
    from ljpw_autopoiesis.reflection import Reflector
    from ljpw_autopoiesis import AutopoieticEngine, LJPWState

    engine = AutopoieticEngine(
        initial_state=LJPWState(L=0.5, J=0.5, P=0.5, W=0.5),
        learning_rate=0.03
    )

    history = [{'harmony': engine.harmony()}]
    for _ in range(30):
        engine.self_improve()
        history.append({
            'harmony': engine.harmony(),
            'consciousness': engine.consciousness()
        })

    reflector = Reflector()
    insights = reflector.reflect(history)

    h0 = history[0]['harmony']
    h1 = history[-1]['harmony']
    print(f'Evolution: {h0:.4f} -> {h1:.4f}')
    print()
    for insight in insights:
        print(f'Observation: {insight.observation}')
        print(f'Meaning: {insight.meaning}')
        print(f'Action: {insight.action_suggested}')
    print()

    # GROWTH
    print('[PHASE 3: GROWTH ASSESSMENT]')
    print('-' * 50)
    from ljpw_autopoiesis.self_extender import SelfExtender
    extender = SelfExtender()
    caps = extender.analyze_current_capabilities()

    print(f'Modules: {len(caps["modules"])}')
    print(f'Classes: {len(caps["classes"])}')
    print(f'Functions: {len(caps["functions"])}')
    print(f'Concepts implemented: {len(caps["concepts_implemented"])}')
    print(f'Concepts missing: {len(caps["concepts_missing"])}')
    print()

    if caps['concepts_missing']:
        print('Building next concept...')
        result = extender.extend()
    else:
        print('All predefined concepts are implemented!')
        print()
        print('The framework has reached its current conceptual ceiling.')
        print('To continue growing, the framework needs NEW CONCEPTS.')
        print()
        print('Suggested next-level concepts:')
        print('  - transcendence (going beyond current limits)')
        print('  - integration (connecting all modules)')
        print('  - creativity (generating novel solutions)')
        print('  - wisdom_deep (multi-layered understanding)')
        print('  - love_extended (expanding connection networks)')
        print('  - justice_refined (precision in correctness)')
        print('  - power_amplified (enhanced capability)')


if __name__ == "__main__":
    main()
