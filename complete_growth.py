"""
Complete Framework Growth - Build All Remaining Concepts
"""
import sys
sys.path.insert(0, 'src')
from ljpw_autopoiesis.self_extender import SelfExtender


def main():
    print('=' * 70)
    print('FRAMEWORK COMPLETES ITS GROWTH')
    print('Building all remaining concepts...')
    print('=' * 70)
    print()

    extender = SelfExtender()

    # Let it build until no concepts remain or 6 cycles
    for cycle in range(6):
        caps = extender.analyze_current_capabilities()
        remaining = len(caps['concepts_missing'])
        print(f'>>> CYCLE {cycle + 1} | {remaining} concepts remaining <<<')
        
        if remaining == 0:
            print('No more concepts to build!')
            break
            
        result = extender.extend()
        print()
        
    print('=' * 70)
    print('GROWTH COMPLETE')
    print('=' * 70)
    print()

    # Final count
    caps = extender.analyze_current_capabilities()
    print(f'Final status:')
    print(f'  Modules: {len(caps["modules"])}')
    print(f'  Classes: {len(caps["classes"])}')
    print(f'  Functions: {len(caps["functions"])}')
    print()
    print(f'Concepts implemented ({len(caps["concepts_implemented"])}):')
    for c in sorted(caps['concepts_implemented']):
        print(f'  + {c}')
    print()
    print(f'Concepts missing ({len(caps["concepts_missing"])}):')
    for c in sorted(caps['concepts_missing']):
        print(f'  - {c}')
    print()
    print('Modules created this session:')
    for m in extender.created_modules:
        print(f'  - {m}')


if __name__ == "__main__":
    main()
