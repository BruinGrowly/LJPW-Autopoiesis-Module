"""
Gap Detector - Identifies errors/issues in Python scripts

The Gap is the Fuel. Each detected issue represents potential energy
that can be converted into healing transformations.

From LJPW V7.9: "The gap from Anchor is the space Love creates for others to exist."
In code terms: The gap from perfect code is the opportunity for improvement.
"""

import ast
import re
import sys
import traceback
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple, Set
from pathlib import Path


@dataclass
class Gap:
    """
    Represents a detected issue (gap) in the code.

    The gap is fuel for the self-healing engine.
    """
    type: str
    message: str
    line: int
    column: int
    severity: float  # 0.0 to 1.0, higher = more severe
    dimension: str  # Primary LJPW dimension affected: L, J, P, or W
    fixable: bool = True
    suggested_fix: Optional[str] = None
    context: Optional[str] = None  # Code context around the issue

    def to_dict(self) -> Dict:
        """Convert to dictionary for harmony metrics."""
        return {
            'type': self.type,
            'message': self.message,
            'line': self.line,
            'severity': self.severity,
        }


class GapDetector:
    """
    Detects gaps (errors, issues) in Python source code.

    Like the LJPW tick engine sensing the gap from anchor,
    this detector identifies where code deviates from harmony.

    Gap types detected:
    - Syntax errors (P dimension - can't execute)
    - Name/Type errors (J dimension - incorrect)
    - Style issues (L dimension - unreadable)
    - Missing docs/handling (W dimension - unwise)
    """

    # Common Python built-in names
    BUILTINS: Set[str] = set(dir(__builtins__)) if isinstance(__builtins__, dict) else set(dir(__builtins__))

    # PEP8 style patterns
    NAMING_PATTERNS = {
        'class': re.compile(r'^[A-Z][a-zA-Z0-9]*$'),  # PascalCase
        'function': re.compile(r'^[a-z_][a-z0-9_]*$'),  # snake_case
        'variable': re.compile(r'^[a-z_][a-z0-9_]*$'),  # snake_case
        'constant': re.compile(r'^[A-Z][A-Z0-9_]*$'),  # UPPER_CASE
    }

    MAX_LINE_LENGTH = 100
    MAX_COMPLEXITY = 10

    def __init__(self):
        self.gaps: List[Gap] = []
        self.source_lines: List[str] = []
        self.defined_names: Set[str] = set()
        self.used_names: Set[str] = set()
        self.imported_names: Set[str] = set()

    def detect(self, source: str, filename: str = "<string>") -> List[Gap]:
        """
        Detect all gaps in the given source code.

        This is the primary sensing mechanism of the self-healing engine.
        """
        self.gaps = []
        self.source_lines = source.split('\n')
        self.defined_names = set()
        self.used_names = set()
        self.imported_names = set()

        # Phase 1: Syntax check (P dimension)
        tree = self._check_syntax(source, filename)
        if tree is None:
            # Syntax error found - critical gap
            return self.gaps

        # Phase 2: AST analysis
        self._analyze_ast(tree)

        # Phase 3: Style analysis (L dimension)
        self._check_style()

        # Phase 4: Name analysis (J dimension)
        self._check_names()

        # Phase 5: Documentation analysis (W dimension)
        self._check_documentation(tree)

        return self.gaps

    def _check_syntax(self, source: str, filename: str) -> Optional[ast.AST]:
        """
        Check for syntax errors - P dimension gaps.

        Syntax errors are critical: code cannot run.
        """
        try:
            tree = ast.parse(source, filename=filename)
            return tree
        except SyntaxError as e:
            self.gaps.append(Gap(
                type='syntax_error',
                message=str(e.msg) if e.msg else "Invalid syntax",
                line=e.lineno or 1,
                column=e.offset or 0,
                severity=1.0,  # Critical
                dimension='P',
                fixable=True,
                suggested_fix=self._suggest_syntax_fix(e, source),
                context=self._get_context(e.lineno or 1),
            ))
            return None
        except Exception as e:
            self.gaps.append(Gap(
                type='syntax_error',
                message=str(e),
                line=1,
                column=0,
                severity=1.0,
                dimension='P',
                fixable=False,
            ))
            return None

    def _analyze_ast(self, tree: ast.AST) -> None:
        """Analyze AST for various issues."""
        for node in ast.walk(tree):
            # Track definitions
            if isinstance(node, ast.FunctionDef):
                self.defined_names.add(node.name)
                self._check_function(node)
            elif isinstance(node, ast.AsyncFunctionDef):
                self.defined_names.add(node.name)
                self._check_function(node)
            elif isinstance(node, ast.ClassDef):
                self.defined_names.add(node.name)
                self._check_class(node)
            elif isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Store):
                    self.defined_names.add(node.id)
                elif isinstance(node.ctx, ast.Load):
                    self.used_names.add(node.id)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    name = alias.asname if alias.asname else alias.name.split('.')[0]
                    self.imported_names.add(name)
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    name = alias.asname if alias.asname else alias.name
                    self.imported_names.add(name)
            elif isinstance(node, ast.ExceptHandler):
                self._check_except_handler(node)

    def _check_function(self, node: ast.FunctionDef) -> None:
        """Check function for issues."""
        # Check naming convention
        if not node.name.startswith('_'):
            if not self.NAMING_PATTERNS['function'].match(node.name):
                self.gaps.append(Gap(
                    type='naming_violation',
                    message=f"Function '{node.name}' should use snake_case",
                    line=node.lineno,
                    column=node.col_offset,
                    severity=0.3,
                    dimension='L',
                    fixable=True,
                    suggested_fix=self._to_snake_case(node.name),
                ))

        # Check complexity (simplified cyclomatic)
        complexity = self._estimate_complexity(node)
        if complexity > self.MAX_COMPLEXITY:
            self.gaps.append(Gap(
                type='complexity_high',
                message=f"Function '{node.name}' has complexity {complexity} (max {self.MAX_COMPLEXITY})",
                line=node.lineno,
                column=node.col_offset,
                severity=0.5,
                dimension='L',
                fixable=False,  # Requires refactoring
            ))

    def _check_class(self, node: ast.ClassDef) -> None:
        """Check class for issues."""
        if not self.NAMING_PATTERNS['class'].match(node.name):
            self.gaps.append(Gap(
                type='naming_violation',
                message=f"Class '{node.name}' should use PascalCase",
                line=node.lineno,
                column=node.col_offset,
                severity=0.3,
                dimension='L',
                fixable=True,
                suggested_fix=self._to_pascal_case(node.name),
            ))

    def _check_except_handler(self, node: ast.ExceptHandler) -> None:
        """Check exception handlers for bare except."""
        if node.type is None:
            self.gaps.append(Gap(
                type='bare_except',
                message="Bare 'except:' clause catches all exceptions including KeyboardInterrupt",
                line=node.lineno,
                column=node.col_offset,
                severity=0.7,
                dimension='W',
                fixable=True,
                suggested_fix="except Exception:",
            ))

    def _check_style(self) -> None:
        """Check style issues - L dimension gaps."""
        for i, line in enumerate(self.source_lines, 1):
            # Line length
            if len(line) > self.MAX_LINE_LENGTH:
                self.gaps.append(Gap(
                    type='long_line',
                    message=f"Line too long ({len(line)} > {self.MAX_LINE_LENGTH})",
                    line=i,
                    column=self.MAX_LINE_LENGTH,
                    severity=0.2,
                    dimension='L',
                    fixable=True,
                ))

            # Trailing whitespace
            if line.rstrip() != line and line.strip():
                self.gaps.append(Gap(
                    type='style_violation',
                    message="Trailing whitespace",
                    line=i,
                    column=len(line.rstrip()),
                    severity=0.1,
                    dimension='L',
                    fixable=True,
                    suggested_fix=line.rstrip(),
                ))

            # Mixed tabs and spaces
            if '\t' in line and '    ' in line:
                self.gaps.append(Gap(
                    type='style_violation',
                    message="Mixed tabs and spaces in indentation",
                    line=i,
                    column=0,
                    severity=0.4,
                    dimension='L',
                    fixable=True,
                ))

    def _check_names(self) -> None:
        """Check for undefined and unused names - J dimension gaps."""
        # Undefined names (excluding builtins and imports)
        known_names = self.defined_names | self.imported_names | self.BUILTINS
        for name in self.used_names:
            if name not in known_names and not name.startswith('_'):
                # Could be a forward reference or from *-import
                self.gaps.append(Gap(
                    type='name_error',
                    message=f"Name '{name}' may be undefined",
                    line=1,  # Would need more tracking to get exact line
                    column=0,
                    severity=0.6,
                    dimension='J',
                    fixable=False,
                ))

        # Unused imports
        for name in self.imported_names:
            if name not in self.used_names and name not in {'__future__'}:
                self.gaps.append(Gap(
                    type='unused_import',
                    message=f"Import '{name}' appears unused",
                    line=1,
                    column=0,
                    severity=0.3,
                    dimension='L',
                    fixable=True,
                ))

    def _check_documentation(self, tree: ast.AST) -> None:
        """Check documentation - W dimension gaps."""
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                # Check for docstring
                if not ast.get_docstring(node):
                    node_type = 'Class' if isinstance(node, ast.ClassDef) else 'Function'
                    self.gaps.append(Gap(
                        type='missing_docstring',
                        message=f"{node_type} '{node.name}' has no docstring",
                        line=node.lineno,
                        column=node.col_offset,
                        severity=0.4,
                        dimension='W',
                        fixable=True,
                    ))

    def _suggest_syntax_fix(self, error: SyntaxError, source: str) -> Optional[str]:
        """Attempt to suggest a fix for syntax errors."""
        if not error.lineno:
            return None

        lines = source.split('\n')
        if error.lineno > len(lines):
            return None

        line = lines[error.lineno - 1]
        msg = str(error.msg).lower() if error.msg else ""

        # Common syntax error patterns
        if "expected ':'" in msg or "invalid syntax" in msg:
            # Missing colon
            if line.rstrip().endswith(')') and any(kw in line for kw in ['def ', 'class ', 'if ', 'for ', 'while ', 'with ', 'try', 'except', 'elif ', 'else']):
                return line.rstrip() + ':'

        if "unexpected indent" in msg:
            return line.lstrip()

        if "unmatched ')'" in msg or "unmatched ']'" in msg or "unmatched '}'" in msg:
            # Count brackets
            opens = line.count('(') + line.count('[') + line.count('{')
            closes = line.count(')') + line.count(']') + line.count('}')
            if closes > opens:
                # Remove extra closing bracket
                for char in ')]}>':
                    if line.count(char) > line.count({'(': ')', '[': ']', '{': '}', '<': '>'}[char] if char in ')]}>>' else ''):
                        return line.replace(char, '', 1)

        if "eol while scanning string" in msg:
            # Unclosed string
            if line.count('"') % 2 == 1:
                return line + '"'
            if line.count("'") % 2 == 1:
                return line + "'"

        return None

    def _estimate_complexity(self, node: ast.FunctionDef) -> int:
        """Estimate cyclomatic complexity of a function."""
        complexity = 1  # Base complexity

        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1
            elif isinstance(child, (ast.ListComp, ast.SetComp, ast.GeneratorExp, ast.DictComp)):
                complexity += 1

        return complexity

    def _get_context(self, line_num: int, context_lines: int = 2) -> str:
        """Get context around a line."""
        start = max(0, line_num - context_lines - 1)
        end = min(len(self.source_lines), line_num + context_lines)
        return '\n'.join(self.source_lines[start:end])

    def _to_snake_case(self, name: str) -> str:
        """Convert name to snake_case."""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def _to_pascal_case(self, name: str) -> str:
        """Convert name to PascalCase."""
        return ''.join(word.capitalize() for word in name.replace('_', ' ').split())

    def get_fuel_level(self) -> float:
        """
        Calculate total "fuel" from detected gaps.

        The fuel is the sum of all gap severities.
        More errors = more fuel for self-healing.
        """
        return sum(gap.severity for gap in self.gaps)

    def get_gaps_by_dimension(self) -> Dict[str, List[Gap]]:
        """Organize gaps by their primary LJPW dimension."""
        result: Dict[str, List[Gap]] = {'L': [], 'J': [], 'P': [], 'W': []}
        for gap in self.gaps:
            result[gap.dimension].append(gap)
        return result

    def report(self) -> str:
        """Generate a gap detection report."""
        if not self.gaps:
            return "No gaps detected - code is in harmony!"

        lines = [
            "GAP DETECTION REPORT",
            "=" * 50,
            f"Total gaps detected: {len(self.gaps)}",
            f"Total fuel available: {self.get_fuel_level():.2f}",
            "",
        ]

        by_dim = self.get_gaps_by_dimension()
        dim_names = {'L': 'Love/Coherence', 'J': 'Justice/Correctness',
                     'P': 'Power/Functionality', 'W': 'Wisdom/Knowledge'}

        for dim, gaps in by_dim.items():
            if gaps:
                lines.append(f"\n{dim_names[dim]} ({dim}) - {len(gaps)} gaps:")
                for gap in gaps:
                    lines.append(f"  Line {gap.line}: {gap.message}")
                    if gap.suggested_fix:
                        lines.append(f"    Suggested: {gap.suggested_fix}")

        return '\n'.join(lines)
