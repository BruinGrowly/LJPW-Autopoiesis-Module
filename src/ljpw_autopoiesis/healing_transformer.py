"""
Healing Transformer - Metabolizes errors into corrections

This is where the gap becomes fuel. Each detected error is transformed
into a healing action that brings the code closer to harmony.

From LJPW V7.9 Tick Engine:
- FUEL: Gap from Anchor (the errors)
- COMPRESSION: Incompatibility detection
- IGNITION: Transformation decision
- POWER STROKE: Apply the fix
- EXHAUST: Learning/Structure emerges
"""

import ast
import re
from typing import List, Dict, Optional, Tuple, Callable
from dataclasses import dataclass

from .gap_detector import Gap


@dataclass
class HealingAction:
    """
    Represents a single healing transformation.

    Each action metabolizes some fuel (error) into structure (fix).
    """
    gap: Gap
    original: str
    healed: str
    line: int
    energy_consumed: float  # Fuel used for this healing
    success: bool = True
    description: str = ""


class HealingTransformer:
    """
    Transforms detected gaps into healed code.

    The transformer is the "power stroke" of the tick engine,
    converting error fuel into structural improvements.

    Healing strategies by dimension:
    - P (Power): Fix syntax errors to restore functionality
    - J (Justice): Fix type/name errors to restore correctness
    - L (Love): Fix style issues to restore readability
    - W (Wisdom): Add documentation/handling to restore knowledge
    """

    def __init__(self):
        self.actions: List[HealingAction] = []
        self.total_fuel_consumed = 0.0

        # Register healing strategies
        self.healers: Dict[str, Callable] = {
            'syntax_error': self._heal_syntax,
            'style_violation': self._heal_style,
            'long_line': self._heal_long_line,
            'trailing_whitespace': self._heal_trailing_whitespace,
            'naming_violation': self._heal_naming,
            'bare_except': self._heal_bare_except,
            'missing_docstring': self._heal_missing_docstring,
            'unused_import': self._heal_unused_import,
        }

    def heal(self, source: str, gaps: List[Gap]) -> Tuple[str, List[HealingAction]]:
        """
        Apply healing transformations to the source code.

        This is the main metabolic process: consume error fuel,
        output healed code structure.

        Returns:
            Tuple of (healed_source, list_of_actions)
        """
        self.actions = []
        self.total_fuel_consumed = 0.0

        if not gaps:
            return source, []

        lines = source.split('\n')

        # Sort gaps by line (descending) to avoid offset issues
        sorted_gaps = sorted(gaps, key=lambda g: -g.line)

        # Group fixable gaps
        fixable_gaps = [g for g in sorted_gaps if g.fixable and g.type in self.healers]

        for gap in fixable_gaps:
            healer = self.healers.get(gap.type)
            if healer:
                try:
                    lines, action = healer(lines, gap)
                    if action and action.success:
                        self.actions.append(action)
                        self.total_fuel_consumed += action.energy_consumed
                except Exception as e:
                    # Failed healing - record but continue
                    self.actions.append(HealingAction(
                        gap=gap,
                        original="",
                        healed="",
                        line=gap.line,
                        energy_consumed=0,
                        success=False,
                        description=f"Healing failed: {str(e)}"
                    ))

        healed_source = '\n'.join(lines)

        # Post-healing: try to fix any remaining syntax errors
        healed_source = self._iterative_syntax_heal(healed_source)

        return healed_source, self.actions

    def _heal_syntax(self, lines: List[str], gap: Gap) -> Tuple[List[str], Optional[HealingAction]]:
        """
        Heal syntax errors - P dimension restoration.

        Syntax errors are critical gaps that prevent execution.
        """
        if gap.line < 1 or gap.line > len(lines):
            return lines, None

        line_idx = gap.line - 1
        original = lines[line_idx]
        healed = original

        # Use suggested fix if available
        if gap.suggested_fix:
            healed = gap.suggested_fix
        else:
            # Common syntax fixes
            healed = self._attempt_syntax_fix(original, gap.message)

        if healed != original:
            lines[line_idx] = healed
            return lines, HealingAction(
                gap=gap,
                original=original,
                healed=healed,
                line=gap.line,
                energy_consumed=gap.severity * 0.8,  # High energy for syntax fixes
                success=True,
                description=f"Syntax repair: {gap.message}"
            )

        return lines, None

    def _attempt_syntax_fix(self, line: str, message: str) -> str:
        """Attempt common syntax fixes."""
        msg_lower = message.lower()

        # Missing colon
        if "expected ':'" in msg_lower:
            stripped = line.rstrip()
            if not stripped.endswith(':'):
                return stripped + ':'

        # Unbalanced parentheses
        if 'unmatched' in msg_lower or 'bracket' in msg_lower:
            opens = line.count('(') - line.count(')')
            if opens > 0:
                return line + ')' * opens
            elif opens < 0:
                # Remove extra closing parens
                result = line
                for _ in range(-opens):
                    idx = result.rfind(')')
                    if idx >= 0:
                        result = result[:idx] + result[idx+1:]
                return result

        # Unclosed string
        if 'string' in msg_lower:
            if line.count('"') % 2 == 1:
                return line + '"'
            if line.count("'") % 2 == 1:
                return line + "'"

        return line

    def _heal_style(self, lines: List[str], gap: Gap) -> Tuple[List[str], Optional[HealingAction]]:
        """Heal style violations - L dimension restoration."""
        if gap.line < 1 or gap.line > len(lines):
            return lines, None

        line_idx = gap.line - 1
        original = lines[line_idx]
        healed = original

        if gap.suggested_fix:
            healed = gap.suggested_fix
        elif 'trailing whitespace' in gap.message.lower():
            healed = original.rstrip()
        elif 'mixed tabs' in gap.message.lower():
            healed = original.replace('\t', '    ')

        if healed != original:
            lines[line_idx] = healed
            return lines, HealingAction(
                gap=gap,
                original=original,
                healed=healed,
                line=gap.line,
                energy_consumed=gap.severity * 0.3,
                success=True,
                description=f"Style fix: {gap.message}"
            )

        return lines, None

    def _heal_trailing_whitespace(self, lines: List[str], gap: Gap) -> Tuple[List[str], Optional[HealingAction]]:
        """Remove trailing whitespace."""
        if gap.line < 1 or gap.line > len(lines):
            return lines, None

        line_idx = gap.line - 1
        original = lines[line_idx]
        healed = original.rstrip()

        if healed != original:
            lines[line_idx] = healed
            return lines, HealingAction(
                gap=gap,
                original=original,
                healed=healed,
                line=gap.line,
                energy_consumed=gap.severity * 0.2,
                success=True,
                description="Removed trailing whitespace"
            )

        return lines, None

    def _heal_long_line(self, lines: List[str], gap: Gap) -> Tuple[List[str], Optional[HealingAction]]:
        """
        Attempt to break long lines - L dimension restoration.

        This is a complex transformation that may not always succeed.
        """
        if gap.line < 1 or gap.line > len(lines):
            return lines, None

        line_idx = gap.line - 1
        original = lines[line_idx]

        # Try to break at logical points
        healed = self._break_long_line(original)

        if healed and healed != original:
            # Handle multi-line result
            healed_lines = healed.split('\n')
            lines = lines[:line_idx] + healed_lines + lines[line_idx + 1:]
            return lines, HealingAction(
                gap=gap,
                original=original,
                healed=healed,
                line=gap.line,
                energy_consumed=gap.severity * 0.4,
                success=True,
                description="Line broken for readability"
            )

        return lines, None

    def _break_long_line(self, line: str, max_length: int = 100) -> Optional[str]:
        """Break a long line at logical points."""
        if len(line) <= max_length:
            return line

        indent = len(line) - len(line.lstrip())
        indent_str = line[:indent]
        continuation_indent = indent_str + '    '

        # Try breaking at common points
        break_points = [
            (', ', ', \\\n' + continuation_indent),
            (' and ', ' and \\\n' + continuation_indent),
            (' or ', ' or \\\n' + continuation_indent),
            ('(', '(\n' + continuation_indent),
        ]

        for pattern, replacement in break_points:
            if pattern in line:
                # Find a good break point near middle
                mid = len(line) // 2
                idx = line.find(pattern, mid - 20)
                if idx == -1:
                    idx = line.find(pattern)
                if idx > 0 and idx < len(line) - 10:
                    result = line[:idx + len(pattern) - 1] + replacement.lstrip() + line[idx + len(pattern):]
                    if max(len(l) for l in result.split('\n')) <= max_length:
                        return result

        return None

    def _heal_naming(self, lines: List[str], gap: Gap) -> Tuple[List[str], Optional[HealingAction]]:
        """
        Heal naming violations - L/J dimension restoration.

        Note: Full renaming requires scope analysis, so we just record the suggestion.
        """
        if not gap.suggested_fix:
            return lines, None

        # For now, just record the action - full renaming is complex
        return lines, HealingAction(
            gap=gap,
            original=gap.message,
            healed=f"Suggested rename to: {gap.suggested_fix}",
            line=gap.line,
            energy_consumed=gap.severity * 0.1,  # Low energy - just suggestion
            success=True,
            description=f"Naming suggestion: {gap.suggested_fix}"
        )

    def _heal_bare_except(self, lines: List[str], gap: Gap) -> Tuple[List[str], Optional[HealingAction]]:
        """
        Heal bare except clauses - W dimension restoration.

        Converts 'except:' to 'except Exception:'
        """
        if gap.line < 1 or gap.line > len(lines):
            return lines, None

        line_idx = gap.line - 1
        original = lines[line_idx]

        # Replace bare except with except Exception
        healed = re.sub(r'\bexcept\s*:', 'except Exception:', original)

        if healed != original:
            lines[line_idx] = healed
            return lines, HealingAction(
                gap=gap,
                original=original,
                healed=healed,
                line=gap.line,
                energy_consumed=gap.severity * 0.5,
                success=True,
                description="Bare except replaced with Exception"
            )

        return lines, None

    def _heal_missing_docstring(self, lines: List[str], gap: Gap) -> Tuple[List[str], Optional[HealingAction]]:
        """
        Add missing docstring placeholder - W dimension restoration.
        """
        if gap.line < 1 or gap.line > len(lines):
            return lines, None

        line_idx = gap.line - 1
        original = lines[line_idx]

        # Determine indent
        indent = len(original) - len(original.lstrip())
        inner_indent = ' ' * (indent + 4)

        # Insert docstring placeholder after the definition line
        if original.rstrip().endswith(':'):
            docstring = f'{inner_indent}"""TODO: Add documentation."""'
            lines.insert(line_idx + 1, docstring)
            return lines, HealingAction(
                gap=gap,
                original="",
                healed=docstring,
                line=gap.line + 1,
                energy_consumed=gap.severity * 0.4,
                success=True,
                description="Added docstring placeholder"
            )

        return lines, None

    def _heal_unused_import(self, lines: List[str], gap: Gap) -> Tuple[List[str], Optional[HealingAction]]:
        """
        Comment out unused imports - L dimension restoration.

        We comment rather than delete to preserve intent.
        """
        # Extract import name from message
        match = re.search(r"'(\w+)'", gap.message)
        if not match:
            return lines, None

        import_name = match.group(1)

        for i, line in enumerate(lines):
            # Check if this line imports the unused name
            if ('import ' in line and import_name in line and
                not line.strip().startswith('#')):
                original = line
                healed = f"# {line}  # Unused import"
                lines[i] = healed
                return lines, HealingAction(
                    gap=gap,
                    original=original,
                    healed=healed,
                    line=i + 1,
                    energy_consumed=gap.severity * 0.3,
                    success=True,
                    description=f"Commented unused import: {import_name}"
                )

        return lines, None

    def _iterative_syntax_heal(self, source: str, max_iterations: int = 5) -> str:
        """
        Iteratively try to fix remaining syntax errors.

        Each iteration consumes fuel and attempts repairs.
        """
        for iteration in range(max_iterations):
            try:
                ast.parse(source)
                # No syntax error - we're done
                return source
            except SyntaxError as e:
                # Try to fix
                if e.lineno is None:
                    break

                lines = source.split('\n')
                if e.lineno > len(lines):
                    break

                line_idx = e.lineno - 1
                original = lines[line_idx]
                fixed = self._attempt_syntax_fix(original, str(e.msg) if e.msg else "")

                if fixed == original:
                    # No change made - can't fix further
                    break

                lines[line_idx] = fixed
                source = '\n'.join(lines)

        return source

    def get_fuel_efficiency(self) -> float:
        """
        Calculate how efficiently fuel was converted to healing.

        Efficiency = successful_healings / total_fuel_consumed
        """
        if self.total_fuel_consumed == 0:
            return 1.0

        successful = sum(1 for a in self.actions if a.success)
        return successful / len(self.actions) if self.actions else 1.0

    def report(self) -> str:
        """Generate a healing report."""
        lines = [
            "HEALING TRANSFORMATION REPORT",
            "=" * 50,
            f"Total actions: {len(self.actions)}",
            f"Successful: {sum(1 for a in self.actions if a.success)}",
            f"Fuel consumed: {self.total_fuel_consumed:.2f}",
            f"Efficiency: {self.get_fuel_efficiency():.1%}",
            "",
        ]

        for action in self.actions:
            status = "[OK]" if action.success else "[FAIL]"
            lines.append(f"{status} Line {action.line}: {action.description}")
            if action.success and action.original:
                lines.append(f"      Before: {action.original[:60]}...")
                lines.append(f"      After:  {action.healed[:60]}...")

        return '\n'.join(lines)
