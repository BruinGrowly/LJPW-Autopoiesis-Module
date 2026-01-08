# LJPW Autopoiesis Module

**Self-Healing Python Script Engine Based on LJPW Framework V7.9**

> *"The gap is the fuel. Errors are metabolized to bring the codebase back into harmony."*

## Overview

The LJPW Autopoiesis Module implements a self-healing system for Python scripts based on the principles of the LJPW Framework V7.9. The core concept is **autopoiesis** - the ability of a system to sense, analyze, and modify itself to improve toward an optimal state.

### Key Principle: The Gap is the Fuel

Instead of treating errors as mere problems to eliminate, this module views them as **fuel** that powers the self-healing process. Like the LJPW Tick Engine, the system:

1. **Senses** the gap from harmony (detects errors)
2. **Compresses** the fuel (prioritizes fixes)
3. **Ignites** transformation (decides what to heal)
4. **Executes** the power stroke (applies fixes)
5. **Exhausts** learning (records what was learned)

## Installation

```bash
pip install -e .
```

## Quick Start

### Heal Source Code

```python
from ljpw_autopoiesis import SelfHealingEngine, heal

# Quick healing
healed_code = heal('''
def BadFunctionName():
    try:
        x = 1
    except:
        pass
''')

# Full control
engine = SelfHealingEngine(verbose=True)
result = engine.heal_source(source_code)
print(f"Harmony improved from {result.initial_harmony.harmony():.3f} to {result.final_harmony.harmony():.3f}")
```

### Diagnose Without Healing

```python
from ljpw_autopoiesis import diagnose

report = diagnose(source_code)
print(report)
```

### Heal a File

```python
engine = SelfHealingEngine()
result = engine.heal_file("broken_script.py")
```

### CLI Usage

```bash
# Heal a file
ljpw-heal script.py

# Diagnose without healing
ljpw-heal --diagnose script.py

# Heal with verbose output
ljpw-heal -v script.py --report
```

## The LJPW Harmony Model

The module maps Python code quality to the four LJPW dimensions:

| Dimension | Meaning | Code Quality Aspect |
|-----------|---------|---------------------|
| **L** | Love/Coherence | Readability, structure, naming |
| **J** | Justice/Correctness | Type safety, logical correctness |
| **P** | Power/Functionality | Runtime stability, working features |
| **W** | Wisdom/Knowledge | Documentation, error handling |

### Harmony Phases

- **Entropic** (H < 0.5): Code dominated by disorder
- **Homeostatic** (0.5 ≤ H < 0.8): Stable but not improving
- **Autopoietic** (H ≥ 0.8): Self-improving toward the anchor

### The Anchor Point

The goal state is the **Anchor Point (1,1,1,1)** - perfect harmony across all dimensions. The gap from anchor represents the "fuel" available for healing.

## How It Works

### The Tick Engine

```
┌──────────────────────────────────────────────────────────────┐
│                     THE TICK ENGINE                          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   FUEL:  Gap from Anchor (errors in code)                   │
│                          ↓                                   │
│   COMPRESSION:  Prioritize by severity                      │
│                          ↓                                   │
│   IGNITION:  Select fixable gaps                            │
│                          ↓                                   │
│   POWER STROKE:  Apply healing transformations              │
│                          ↓                                   │
│   EXHAUST:  Learning (history, metrics)                     │
│                          ↓                                   │
│   OUTPUT:  Healed code, improved harmony                    │
└──────────────────────────────────────────────────────────────┘
```

Each tick of the engine:
1. Detects all gaps (errors) in the current code
2. Calculates harmony state and fuel level
3. Prioritizes gaps by dimension (P > J > L > W)
4. Applies healing transformations
5. Verifies improvement
6. Records learning for adaptation

### What Gets Healed

**P Dimension (Power):**
- Syntax errors
- Missing colons
- Unmatched brackets
- Unclosed strings

**J Dimension (Justice):**
- Type errors (detection)
- Name errors (detection)
- Naming convention violations

**L Dimension (Love):**
- Trailing whitespace
- Mixed tabs/spaces
- Long lines
- Style violations

**W Dimension (Wisdom):**
- Bare except clauses → `except Exception:`
- Missing docstrings → Placeholder added
- Unused imports → Commented

## API Reference

### SelfHealingEngine

```python
engine = SelfHealingEngine(
    max_ticks=20,      # Maximum healing cycles
    learning_rate=0.02, # Adaptation rate
    verbose=False,      # Print progress
)

result = engine.heal_source(source, filename="script.py")
```

### HealingResult

```python
result.original_source     # Original code
result.healed_source       # Healed code
result.source_changed      # Whether changes were made
result.initial_harmony     # HarmonyState before healing
result.final_harmony       # HarmonyState after healing
result.total_ticks         # Number of tick cycles
result.total_gaps_found    # Total errors detected
result.total_gaps_healed   # Errors successfully fixed
result.improvement         # Harmony improvement
result.gap_reduction       # % of gap eliminated
```

### HarmonyState

```python
state = HarmonyState(L=0.9, J=0.85, P=0.8, W=0.75)

state.harmony()           # Overall harmony score
state.gap_from_anchor()   # Distance from (1,1,1,1)
state.phase()             # "ENTROPIC" | "HOMEOSTATIC" | "AUTOPOIETIC"
state.consciousness()     # Consciousness metric (C > 0.1 threshold)
state.is_viable()         # All dimensions above 0.2
```

## Testing

```bash
pytest tests/ -v
```

## Philosophy

From LJPW Framework V7.9:

> *"The framework has closed the loop. It can now SENSE itself → UNDERSTAND itself → IMPROVE itself. This is not a description of autopoiesis. This IS autopoiesis."*

The self-healing engine embodies this principle by treating code as a living system that naturally tends toward harmony when given the mechanism to sense and correct its own gaps.

> *"Perfect Love cannot NOT give."*

The system gives corrections where errors exist - not as punishment, but as the natural flow from disorder toward order.

## License

MIT License - See LICENSE file
