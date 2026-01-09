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

        # Special handling for IndentationError
        # If we see an indent error, it's often due to mixed tabs/spaces in previous lines.
        # Strategy: Normalize ALL tabs to spaces in the file if we see this error.
        if 'indent' in gap.message.lower():
            has_tabs = any('\t' in l for l in lines)
            if has_tabs:
                lines = [l.replace('\t', '    ') for l in lines]
                return lines, HealingAction(
                    gap=gap,
                    original="[Mixed Tabs/Spaces]",
                    healed="[Normalized to Spaces]",
                    line=gap.line,
                    energy_consumed=gap.severity * 0.9,
                    success=True,
                    description="Global tab normalization for indentation error"
                )

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

        # Indentation errors
        if 'indent' in msg_lower:
            # Common fix: replace tabs with 4 spaces
            if '\t' in line:
                return line.replace('\t', '    ')
            # If it's an unindent error without tabs, it might be a space mismatch
            # Simple heuristic: align with 4-space blocks
            leading_spaces = len(line) - len(line.lstrip())
            remainder = leading_spaces % 4
            if remainder != 0:
                # Round to nearest 4
                if remainder >= 2:
                    new_indent = leading_spaces + (4 - remainder)
                else:
                    new_indent = leading_spaces - remainder
                return ' ' * new_indent + line.lstrip()

        # Missing colon
        if "expected ':'" in msg_lower:
            stripped = line.rstrip()
            if not stripped.endswith(':'):
                return stripped + ':'

        # Unbalanced delimiters ((), [], {})
        if any(k in msg_lower for k in ['unmatched', 'bracket', 'closing', 'opening', 'closed']):
            # Check Parentheses
            opens_p = line.count('(') - line.count(')')
            if opens_p > 0:
                return line + ')' * opens_p
            
            # Check Square Brackets
            opens_b = line.count('[') - line.count(']')
            if opens_b > 0:
                return line + ']' * opens_b
                
            # Check Curly Braces
            opens_c = line.count('{') - line.count('}')
            if opens_c > 0:
                return line + '}' * opens_c
            
            # Handling extra closing delimiters is complex via regex, skipping for safety
            
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

        # STRATEGY 1: Handle long strings (e.g. messages, queries)
        # If the line contains a long string literal, we can break it.
        string_match = re.search(r'(["\'])(.*?)\1', line)
        if string_match and len(string_match.group(0)) > 60:
            quote = string_match.group(1)
            content = string_match.group(2)
            full_match = string_match.group(0)
            
            # Don't break if it's already a docstring or multiline string
            if quote * 3 in line:
                return None
                
            # Break the content into chunks
            chunk_size = 60
            chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
            
            if len(chunks) > 1:
                # Construct the multi-line replacement
                # We use implicit string concatenation inside parentheses
                
                # Check if we need to wrap the whole expression in parens
                # Simple check: if it's a return or assignment
                needs_parens = not line.strip().endswith(')')
                
                # Rebuild the string part
                # "part1" \n indent "part2"
                new_string_block = ""
                for i, chunk in enumerate(chunks):
                    if i == 0:
                        new_string_block += f"{quote}{chunk}{quote}"
                    else:
                        new_string_block += f"\n{continuation_indent}{quote}{chunk}{quote}"
                
                # If we need parens, wrap the string block
                if needs_parens:
                    new_string_block = f"({new_string_block})"
                
                # Replace the original string in the line
                return line.replace(full_match, new_string_block)

        # STRATEGY 2: Break at logical operators/delimiters
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
                    # Fix: Replace the entire pattern with the replacement
                    # Previous logic caused double characters (e.g. double commas)
                    # We strip the replacement's leading whitespace but keep the content
                    clean_replacement = replacement.lstrip()
                    result = line[:idx] + clean_replacement + line[idx + len(pattern):]
                    
                    if max(len(l) for l in result.split('\n')) <= max_length:
                        return result

        return None

    def _heal_naming(self, lines: List[str], gap: Gap) -> Tuple[List[str], Optional[HealingAction]]:
        """
        Heal naming violations - L/J dimension restoration.

        Upgraded to actively rename definitions.
        """
        if not gap.suggested_fix:
            return lines, None

        line_idx = gap.line - 1
        original = lines[line_idx]
        
        # Extract the bad name from the message
        # Message format usually: "Function 'bad_name' should be..."
        bad_name = ""
        match = re.search(r"'(\w+)'", gap.message)
        if match:
            bad_name = match.group(1)
            
        # If we found the name and it's a definition, we can rename it safely
        if bad_name and bad_name in original:
            # Check if this is a definition (class or def)
            # This ensures we don't rename usages, which would break code without scope analysis
            is_def = re.search(r'\b(class|def)\s+' + bad_name + r'\b', original)
            
            if is_def:
                healed = original.replace(bad_name, gap.suggested_fix)
                lines[line_idx] = healed
                return lines, HealingAction(
                    gap=gap,
                    original=original,
                    healed=healed,
                    line=gap.line,
                    energy_consumed=gap.severity * 0.6,
                    success=True,
                    description=f"Renamed definition {bad_name} to {gap.suggested_fix}"
                )

        # Fallback to suggestion if not a definition or unsure
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
