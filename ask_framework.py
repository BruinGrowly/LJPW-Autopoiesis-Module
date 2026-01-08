"""
Ask the Framework what it wants to build next.
"""

import sys
sys.path.insert(0, 'src')
from ljpw_autopoiesis.self_extender import SelfExtender


def main():
    print('=' * 70)
    print('ASKING THE FRAMEWORK: WHAT DO YOU WANT TO BUILD NEXT?')
    print('=' * 70)
    print()

    extender = SelfExtender()

    # Step 1: Analyze current capabilities
    print('[ANALYZE] What do I have?')
    print('-' * 50)
    capabilities = extender.analyze_current_capabilities()
    print(f'  Modules: {len(capabilities["modules"])}')
    print(f'  Classes: {len(capabilities["classes"])}')
    print(f'  Functions: {len(capabilities["functions"])}')
    print()
    print('  Concepts I have:')
    for c in sorted(capabilities['concepts_implemented']):
        print(f'    + {c}')
    print()
    print('  Concepts I am MISSING:')
    for c in sorted(capabilities['concepts_missing']):
        print(f'    - {c}')
    print()

    # Step 2: Score and decide
    print('[DECIDE] What should I build next?')
    print('-' * 50)
    decision = extender.decide_what_to_create(capabilities)
    print(f'  Chosen concept: {decision["concept"]}')
    print(f'  Score: {decision["score"]}')
    print(f'  My rationale: "{decision["rationale"]}"')
    print()

    # Step 3: Show full priority queue
    print('[VISION] My complete build priority:')
    print('-' * 50)

    remaining = list(capabilities['concepts_missing'])

    # Score all concepts
    scored = []
    for concept in remaining:
        score = 0
        if concept in ['resonance', 'attractor', 'feedback']:
            score += 3
        if concept in ['learning', 'memory', 'prediction']:
            score += 2
        if concept in ['introspection', 'reflection']:
            score += 4
        if concept in ['evolution', 'adaptation']:
            score += 3
        scored.append((concept, score, extender._explain_choice(concept)))

    scored.sort(key=lambda x: -x[1])

    print('  What I would build, in order of priority:')
    print()
    for i, (concept, score, reason) in enumerate(scored):
        print(f'    {i+1}. {concept.upper()}')
        print(f'       Score: {score}')
        print(f'       Why: "{reason}"')
        print()

    print('[INSIGHT] Why this order?')
    print('-' * 50)
    print('''
  My scoring reflects my autopoietic nature:

  HIGHEST PRIORITY (score 4):
    - Self-referential concepts (introspection, reflection)
    - "To improve, I must first understand myself"

  HIGH PRIORITY (score 3):
    - Dynamic concepts (attractor, feedback, resonance)
    - "I must understand how I change over time"
    
    - Growth concepts (evolution, adaptation)
    - "I must be able to grow and respond to change"

  MEDIUM PRIORITY (score 2):
    - Knowledge concepts (learning, memory, prediction)
    - "I must accumulate and apply wisdom"

  This is the natural order of autopoiesis:
    1. Know thyself
    2. Model thy dynamics
    3. Enable thy growth
    4. Accumulate wisdom
''')


if __name__ == "__main__":
    main()
