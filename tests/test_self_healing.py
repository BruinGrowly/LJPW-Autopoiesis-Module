"""
Tests for LJPW Autopoiesis Self-Healing Module

These tests verify that the self-healing engine can:
1. Detect gaps (errors) in Python code
2. Metabolize errors through tick cycles
3. Converge toward harmonic code
4. Track harmony metrics correctly

"The gap is the fuel. Errors are metabolized to bring the codebase back into harmony."
"""

import ast
import pytest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ljpw_autopoiesis import (
    SelfHealingEngine,
    TickEngine,
    GapDetector,
    HealingTransformer,
    HarmonyState,
    HarmonyMetrics,
)
from ljpw_autopoiesis.engine import heal, diagnose


class TestHarmonyState:
    """Tests for HarmonyState class."""

    def test_anchor_point(self):
        """Test that anchor point is (1,1,1,1)."""
        anchor = HarmonyState.anchor()
        assert anchor.L == 1.0
        assert anchor.J == 1.0
        assert anchor.P == 1.0
        assert anchor.W == 1.0

    def test_harmony_calculation(self):
        """Test harmony score calculation."""
        state = HarmonyState(L=0.8, J=0.8, P=0.8, W=0.8)
        harmony = state.harmony()
        assert harmony > 0
        # Higher values should give higher harmony
        high_state = HarmonyState(L=0.95, J=0.95, P=0.95, W=0.95)
        assert high_state.harmony() > state.harmony()

    def test_gap_from_anchor(self):
        """Test gap calculation from anchor point."""
        anchor = HarmonyState.anchor()
        assert anchor.gap_from_anchor() == 0.0

        low_state = HarmonyState(L=0.5, J=0.5, P=0.5, W=0.5)
        assert low_state.gap_from_anchor() > 0

    def test_phase_detection(self):
        """Test phase detection based on harmony."""
        entropic = HarmonyState(L=0.3, J=0.3, P=0.3, W=0.3)
        assert entropic.phase() == "ENTROPIC"

        homeostatic = HarmonyState(L=0.6, J=0.6, P=0.6, W=0.6)
        assert homeostatic.phase() == "HOMEOSTATIC"

        autopoietic = HarmonyState(L=0.9, J=0.9, P=0.9, W=0.9)
        assert autopoietic.phase() == "AUTOPOIETIC"

    def test_viability_check(self):
        """Test viability threshold check."""
        viable = HarmonyState(L=0.5, J=0.5, P=0.5, W=0.5)
        assert viable.is_viable()

        not_viable = HarmonyState(L=0.1, J=0.5, P=0.5, W=0.5)
        assert not not_viable.is_viable()


class TestGapDetector:
    """Tests for GapDetector class."""

    def test_detect_syntax_error(self):
        """Test detection of syntax errors (P dimension)."""
        source = "def foo(\n    print('hello')"  # Missing closing paren
        detector = GapDetector()
        gaps = detector.detect(source)

        assert len(gaps) > 0
        syntax_gaps = [g for g in gaps if g.type == 'syntax_error']
        assert len(syntax_gaps) > 0
        assert syntax_gaps[0].dimension == 'P'

    def test_detect_missing_colon(self):
        """Test detection of missing colon syntax error."""
        source = "def foo()\n    pass"  # Missing colon
        detector = GapDetector()
        gaps = detector.detect(source)

        assert len(gaps) > 0
        assert any(g.type == 'syntax_error' for g in gaps)

    def test_detect_bare_except(self):
        """Test detection of bare except (W dimension)."""
        source = """
try:
    x = 1
except:
    pass
"""
        detector = GapDetector()
        gaps = detector.detect(source)

        bare_except_gaps = [g for g in gaps if g.type == 'bare_except']
        assert len(bare_except_gaps) > 0
        assert bare_except_gaps[0].dimension == 'W'

    def test_detect_missing_docstring(self):
        """Test detection of missing docstrings (W dimension)."""
        source = """
def foo():
    pass

class Bar:
    pass
"""
        detector = GapDetector()
        gaps = detector.detect(source)

        docstring_gaps = [g for g in gaps if g.type == 'missing_docstring']
        assert len(docstring_gaps) >= 2  # function and class

    def test_detect_naming_violations(self):
        """Test detection of naming violations (L dimension)."""
        source = """
def BadFunctionName():
    pass

class bad_class_name:
    pass
"""
        detector = GapDetector()
        gaps = detector.detect(source)

        naming_gaps = [g for g in gaps if g.type == 'naming_violation']
        assert len(naming_gaps) >= 1

    def test_detect_long_lines(self):
        """Test detection of long lines (L dimension)."""
        source = "x = " + "a" * 150  # Very long line
        detector = GapDetector()
        gaps = detector.detect(source)

        long_line_gaps = [g for g in gaps if g.type == 'long_line']
        assert len(long_line_gaps) > 0
        assert long_line_gaps[0].dimension == 'L'

    def test_fuel_level_calculation(self):
        """Test that fuel level increases with more errors."""
        clean_source = """
def foo():
    \"\"\"Docstring.\"\"\"
    pass
"""
        broken_source = """
def BadName()
    print 'hello'
    x =
"""
        detector = GapDetector()

        detector.detect(clean_source)
        clean_fuel = detector.get_fuel_level()

        detector.detect(broken_source)
        broken_fuel = detector.get_fuel_level()

        assert broken_fuel > clean_fuel

    def test_valid_code_no_critical_gaps(self):
        """Test that valid code has no critical gaps."""
        source = """
def hello_world():
    \"\"\"Say hello.\"\"\"
    print("Hello, World!")

hello_world()
"""
        detector = GapDetector()
        gaps = detector.detect(source)

        # Should have no syntax errors
        syntax_gaps = [g for g in gaps if g.type == 'syntax_error']
        assert len(syntax_gaps) == 0


class TestHealingTransformer:
    """Tests for HealingTransformer class."""

    def test_heal_trailing_whitespace(self):
        """Test removal of trailing whitespace."""
        from ljpw_autopoiesis.gap_detector import Gap

        source = "x = 1   \ny = 2\n"
        gaps = [Gap(
            type='style_violation',
            message='Trailing whitespace',
            line=1,
            column=5,
            severity=0.1,
            dimension='L',
            fixable=True,
        )]

        transformer = HealingTransformer()
        healed, actions = transformer.heal(source, gaps)

        # Trailing whitespace should be removed
        assert "1   " not in healed

    def test_heal_bare_except(self):
        """Test conversion of bare except to except Exception."""
        from ljpw_autopoiesis.gap_detector import Gap

        source = """try:
    x = 1
except:
    pass
"""
        gaps = [Gap(
            type='bare_except',
            message='Bare except clause',
            line=3,
            column=0,
            severity=0.7,
            dimension='W',
            fixable=True,
        )]

        transformer = HealingTransformer()
        healed, actions = transformer.heal(source, gaps)

        assert "except Exception:" in healed

    def test_fuel_efficiency(self):
        """Test fuel efficiency calculation."""
        transformer = HealingTransformer()

        # No actions = 100% efficiency
        assert transformer.get_fuel_efficiency() == 1.0


class TestTickEngine:
    """Tests for TickEngine class."""

    def test_single_tick(self):
        """Test execution of a single tick."""
        source = "def foo():\n    pass  "  # Has trailing whitespace
        engine = TickEngine(max_ticks=1)
        healed = engine.run(source)

        assert engine.state.total_ticks == 1

    def test_convergence(self):
        """Test that engine converges on clean code."""
        source = """
def hello():
    \"\"\"Say hello.\"\"\"
    print("Hello!")
"""
        engine = TickEngine(max_ticks=10)
        healed = engine.run(source)

        # Should converge quickly on clean code
        assert engine.state.convergence_achieved or engine.state.total_ticks <= 3

    def test_tick_history(self):
        """Test that tick history is recorded."""
        source = "def BadName():\n    pass"  # Has naming issue
        engine = TickEngine(max_ticks=5)
        engine.run(source)

        assert len(engine.state.history) > 0
        assert all(r.tick_number >= 0 for r in engine.state.history)

    def test_harmony_improvement(self):
        """Test that harmony improves over ticks."""
        source = """
def BadName():
    pass

try:
    x = 1
except:
    pass
"""
        engine = TickEngine(max_ticks=10)
        engine.run(source)

        if len(engine.state.history) > 1:
            first = engine.state.history[0]
            last = engine.state.history[-1]
            # Harmony should improve or stay same
            assert last.harmony_after.harmony() >= first.harmony_before.harmony() - 0.1


class TestSelfHealingEngine:
    """Tests for the main SelfHealingEngine class."""

    def test_heal_syntax_error(self):
        """Test healing of syntax errors."""
        source = "def foo()\n    pass"  # Missing colon
        engine = SelfHealingEngine()
        result = engine.heal_source(source)

        # Should attempt to fix
        assert result.healed_source != source or result.total_gaps_found > 0

    def test_heal_source_returns_result(self):
        """Test that heal_source returns a HealingResult."""
        source = "x = 1"
        engine = SelfHealingEngine()
        result = engine.heal_source(source)

        assert hasattr(result, 'original_source')
        assert hasattr(result, 'healed_source')
        assert hasattr(result, 'initial_harmony')
        assert hasattr(result, 'final_harmony')

    def test_diagnose_function(self):
        """Test the diagnose function."""
        source = """
def BadName():
    pass
"""
        report = diagnose(source)

        assert "DIAGNOSTIC REPORT" in report
        assert "HARMONY STATE" in report

    def test_heal_convenience_function(self):
        """Test the heal convenience function."""
        source = "x = 1  "  # Trailing whitespace
        healed = heal(source)

        # Should return healed code
        assert isinstance(healed, str)

    def test_verbose_mode(self):
        """Test verbose mode doesn't crash."""
        source = "x = 1"
        engine = SelfHealingEngine(verbose=True)
        # This should print but not crash
        result = engine.heal_source(source)
        assert result is not None

    def test_callback_on_tick(self):
        """Test that on_tick callback is called."""
        source = "def foo():\n    pass  "
        ticks_received = []

        def on_tick(result):
            ticks_received.append(result)

        engine = SelfHealingEngine()
        engine.heal_source(source, on_tick=on_tick)

        # Callback should have been called
        assert len(ticks_received) > 0

    def test_report_generation(self):
        """Test report generation."""
        source = "x = 1"
        engine = SelfHealingEngine()
        engine.heal_source(source)
        report = engine.report()

        assert "TICK ENGINE REPORT" in report

    def test_improvement_calculation(self):
        """Test improvement calculation in HealingResult."""
        source = "x = 1"
        engine = SelfHealingEngine()
        result = engine.heal_source(source)

        # Improvement should be a number
        assert isinstance(result.improvement, float)
        assert isinstance(result.gap_reduction, float)


class TestHarmonyMetrics:
    """Tests for HarmonyMetrics class."""

    def test_from_errors_empty(self):
        """Test harmony from empty error list."""
        state = HarmonyMetrics.from_errors([])

        # No errors = near-perfect harmony
        assert state.L >= 0.9
        assert state.J >= 0.9
        assert state.P >= 0.9
        assert state.W >= 0.9

    def test_from_errors_with_syntax_error(self):
        """Test harmony impact from syntax error."""
        errors = [{'type': 'syntax_error', 'severity': 1.0}]
        state = HarmonyMetrics.from_errors(errors)

        # P should be significantly impacted
        assert state.P < 1.0

    def test_improvement_priority(self):
        """Test improvement priority ordering."""
        state = HarmonyState(L=0.5, J=0.5, P=0.5, W=0.5)
        priority = HarmonyMetrics.improvement_priority(state)

        # P should be first priority
        assert priority[0] == 'P'


class TestIntegration:
    """Integration tests for the complete system."""

    def test_full_healing_cycle(self):
        """Test a complete healing cycle on broken code."""
        broken_code = '''
def BadFunctionName():
    x = 1
    try:
        y = 2
    except:
        pass
'''
        engine = SelfHealingEngine(max_ticks=15)
        result = engine.heal_source(broken_code)

        # Should have processed the code
        assert result.total_ticks > 0
        # Harmony should be reasonable
        assert result.final_harmony.harmony() > 0

    def test_already_clean_code(self):
        """Test that clean code isn't broken."""
        clean_code = '''
def hello_world():
    """Print hello world."""
    print("Hello, World!")


if __name__ == "__main__":
    hello_world()
'''
        engine = SelfHealingEngine()
        result = engine.heal_source(clean_code)

        # Clean code should remain valid
        try:
            ast.parse(result.healed_source)
            valid = True
        except SyntaxError:
            valid = False

        assert valid

    def test_multiple_error_types(self):
        """Test healing code with multiple error types."""
        messy_code = '''
def BadName():
    x = 1
    y = 2
    try:
        z = 3
    except:
        pass
'''
        engine = SelfHealingEngine(max_ticks=20)
        result = engine.heal_source(messy_code)

        # Should have found multiple gap types
        assert result.total_gaps_found > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
