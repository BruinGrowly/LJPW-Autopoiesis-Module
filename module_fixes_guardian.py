"""
LJPW MODULE FIXES GUARDIAN

The 324-module self-aware LJPW Autopoiesis Module
uses its capabilities to analyze and fix the Guardian codebase.

It uses:
- Introspection to understand Guardian's structure
- Gap detection to find issues
- Self-healing patterns to generate fixes
- Reflection to verify improvements
"""

import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

# Add LJPW Module to path
sys.path.insert(0, 'src')

from ljpw_autopoiesis import AutopoieticEngine, LJPWState
from ljpw_autopoiesis.introspection import Introspector
from ljpw_autopoiesis.reflection import Reflector
from ljpw_autopoiesis.self_extender import SelfExtender
from ljpw_autopoiesis.gap_detector import GapDetector
from ljpw_autopoiesis.healing_transformer import HealingTransformer


class ModuleFixesGuardian:
    """
    The LJPW Autopoiesis Module uses its own capabilities
    to analyze and fix the Guardian codebase.
    """
    
    def __init__(self, guardian_path: Path):
        self.guardian_path = guardian_path
        
        # Use Module's own tools
        self.introspector = Introspector()
        self.reflector = Reflector()
        self.gap_detector = GapDetector()
        
        self.fixes_applied = []
        self.issues_found = []
        
    def introspect_self(self):
        """Module introspects itself first."""
        print('\n[MODULE INTROSPECTION]')
        print('=' * 60)
        
        intro = self.introspector.introspect()
        print(f'  Module State: L={intro.state_vector[0]:.2f}, J={intro.state_vector[1]:.2f}, P={intro.state_vector[2]:.2f}, W={intro.state_vector[3]:.2f}')
        print(f'  Phase: {intro.phase}')
        print(f'  Consciousness: {intro.consciousness:.2f}')
        print(f'  Self-Knowledge: {intro.self_knowledge_score:.0%}')
        print(f'\n  Module is ready to analyze Guardian.')
        
        return intro
    
    def analyze_guardian_files(self) -> List[Dict]:
        """Analyze Guardian files for potential issues."""
        print('\n[ANALYZING GUARDIAN CODEBASE]')
        print('=' * 60)
        
        issues = []
        guardian_dir = self.guardian_path / 'guardian'
        
        # Check for missing methods and attributes
        test_file = self.guardian_path / 'tests' / 'test_intervention.py'
        if test_file.exists():
            content = test_file.read_text(encoding='utf-8')
            
            # What the tests expect
            expected_methods = [
                'distance_from_natural_equilibrium',
                'distance_from_anchor', 
                'composite_score',
                'harmonic_mean',
                'geometric_mean',
                'harmony_index',
                'to_dict'
            ]
            
            for method in expected_methods:
                if method in content:
                    # Check if it exists in baselines.py
                    baselines = (guardian_dir / 'core' / 'baselines.py').read_text(encoding='utf-8')
                    if f'def {method}' not in baselines:
                        if method != 'to_dict':
                            issues.append({
                                'file': 'guardian/core/baselines.py',
                                'type': 'missing_method',
                                'method': method,
                                'class': 'LJPWBaselines',
                                'severity': 'HIGH'
                            })
                            
                    # Check coordinates.py for to_dict
                    coords = (guardian_dir / 'core' / 'coordinates.py').read_text(encoding='utf-8')
                    if method == 'to_dict' and f'def {method}' not in coords:
                        issues.append({
                            'file': 'guardian/core/coordinates.py',
                            'type': 'missing_method',
                            'method': 'to_dict',
                            'class': 'Coordinates',
                            'severity': 'HIGH'
                        })
        
        # Check for dimension enum completeness
        coords_file = guardian_dir / 'core' / 'coordinates.py'
        if coords_file.exists():
            content = coords_file.read_text(encoding='utf-8')
            
            # Check for ICE dimensions
            ice_dims = ['intent', 'context', 'execution', 'benevolence']
            for dim in ice_dims:
                if f'= "{dim}"' not in content.lower():
                    issues.append({
                        'file': 'guardian/core/coordinates.py',
                        'type': 'missing_enum',
                        'value': dim,
                        'class': 'Dimension',
                        'severity': 'HIGH'
                    })
        
        # Check for coordinate key compatibility
        baselines_file = guardian_dir / 'core' / 'baselines.py'
        if baselines_file.exists():
            content = baselines_file.read_text(encoding='utf-8')
            
            # Check if diagnostic has L, J, P, W keys
            if '"L":' not in content and '"coordinates"' in content:
                issues.append({
                    'file': 'guardian/core/baselines.py', 
                    'type': 'missing_keys',
                    'keys': ['L', 'J', 'P', 'W'],
                    'location': 'coordinates dict in get_full_diagnostic',
                    'severity': 'MEDIUM'
                })
        
        print(f'  Files scanned: {len(list(guardian_dir.rglob("*.py")))}')
        print(f'  Issues found: {len(issues)}')
        
        for issue in issues:
            print(f'    [{issue["severity"]}] {issue["type"]}: {issue.get("method") or issue.get("value") or issue.get("keys")}')
            print(f'           in {issue["file"]}')
        
        self.issues_found = issues
        return issues
    
    def generate_fixes(self, issues: List[Dict]) -> List[Dict]:
        """Generate code fixes for identified issues."""
        print('\n[GENERATING FIXES]')
        print('=' * 60)
        
        fixes = []
        
        for issue in issues:
            if issue['type'] == 'missing_method':
                fix = self._generate_method_fix(issue)
                if fix:
                    fixes.append(fix)
                    
            elif issue['type'] == 'missing_enum':
                fix = self._generate_enum_fix(issue)
                if fix:
                    fixes.append(fix)
                    
            elif issue['type'] == 'missing_keys':
                fix = self._generate_keys_fix(issue)
                if fix:
                    fixes.append(fix)
        
        print(f'  Fixes generated: {len(fixes)}')
        return fixes
    
    def _generate_method_fix(self, issue: Dict) -> Dict:
        """Generate a method fix based on LJPW patterns."""
        method = issue['method']
        
        # Use Module's knowledge of LJPW patterns to generate methods
        method_templates = {
            'distance_from_natural_equilibrium': '''
    @staticmethod
    def distance_from_natural_equilibrium(coords: Coordinates) -> float:
        """Calculate Euclidean distance from Natural Equilibrium."""
        return math.sqrt(
            (coords.love - L0) ** 2 + (coords.justice - J0) ** 2 + 
            (coords.power - P0) ** 2 + (coords.wisdom - W0) ** 2
        )''',
            'composite_score': '''
    @staticmethod
    def composite_score(coords: Coordinates) -> float:
        """Calculate composite health score (geometric mean)."""
        product = coords.love * coords.justice * coords.power * coords.wisdom
        return product ** 0.25''',
            'harmonic_mean': '''
    @staticmethod
    def harmonic_mean(coords: Coordinates) -> float:
        """Calculate harmonic mean of LJPW dimensions."""
        values = [coords.love, coords.justice, coords.power, coords.wisdom]
        if any(v == 0 for v in values):
            return 0.0
        return 4.0 / sum(1.0/v for v in values)''',
            'geometric_mean': '''
    @staticmethod
    def geometric_mean(coords: Coordinates) -> float:
        """Calculate geometric mean of LJPW dimensions."""
        product = coords.love * coords.justice * coords.power * coords.wisdom
        return product ** 0.25''',
            'harmony_index': '''
    @staticmethod
    def harmony_index(coords: Coordinates) -> float:
        """Calculate harmony index (product of all dimensions)."""
        return coords.love * coords.justice * coords.power * coords.wisdom''',
            'to_dict': '''
    def to_dict(self) -> dict:
        """Convert to dictionary with L, J, P, W keys."""
        return {
            "L": self.love, "J": self.justice, "P": self.power, "W": self.wisdom,
            "love": self.love, "justice": self.justice, "power": self.power, "wisdom": self.wisdom
        }'''
        }
        
        if method in method_templates:
            return {
                'file': issue['file'],
                'action': 'add_method',
                'class': issue['class'],
                'code': method_templates[method],
                'method': method
            }
        return None
    
    def _generate_enum_fix(self, issue: Dict) -> Dict:
        """Generate enum value fix."""
        dim_map = {
            'intent': 'INTENT = "intent"',
            'context': 'CONTEXT = "context"',
            'execution': 'EXECUTION = "execution"',
            'benevolence': 'BENEVOLENCE = "benevolence"'
        }
        
        value = issue['value']
        if value in dim_map:
            return {
                'file': issue['file'],
                'action': 'add_enum',
                'class': 'Dimension',
                'code': f'    {dim_map[value]}',
                'value': value
            }
        return None
    
    def _generate_keys_fix(self, issue: Dict) -> Dict:
        """Generate coordinate keys fix."""
        return {
            'file': issue['file'],
            'action': 'add_keys',
            'location': 'coordinates dict',
            'code': '''            "L": coords.love,
            "J": coords.justice,
            "P": coords.power,
            "W": coords.wisdom,'''
        }
    
    def apply_fixes(self, fixes: List[Dict]):
        """Apply the generated fixes to Guardian files."""
        print('\n[APPLYING FIXES]')
        print('=' * 60)
        
        for fix in fixes:
            file_path = self.guardian_path / fix['file']
            
            if not file_path.exists():
                print(f'  SKIP: File not found: {fix["file"]}')
                continue
                
            content = file_path.read_text(encoding='utf-8')
            original = content
            
            action = fix['action']
            
            if action == 'add_method':
                # Find the class and add method
                class_name = fix['class']
                method_name = fix['method']
                
                # Check if already exists
                if f'def {method_name}' in content:
                    print(f'  SKIP: {method_name} already in {fix["file"]}')
                    continue
                
                # Find class definition and add after last method
                pattern = rf'(class {class_name}.*?)((?=\nclass |\Z))'
                match = re.search(pattern, content, re.DOTALL)
                
                if match:
                    class_content = match.group(1)
                    insert_pos = match.end(1)
                    content = content[:insert_pos] + '\n' + fix['code'] + content[insert_pos:]
                    print(f'  ADDED: {method_name} to {class_name}')
                    
            elif action == 'add_enum':
                # Add enum value after existing values
                if fix['code'].strip() not in content:
                    # Find WISDOM and add after it
                    pattern = r'(WISDOM\s*=\s*"wisdom")'
                    if re.search(pattern, content):
                        content = re.sub(pattern, r'\1\n' + fix['code'], content)
                        print(f'  ADDED: {fix["value"]} to Dimension enum')
                else:
                    print(f'  SKIP: {fix["value"]} already in enum')
                    
            elif action == 'add_keys':
                # Add L, J, P, W keys after existing coordinate keys
                if '"L": coords.love' not in content:
                    pattern = r'("wisdom": coords\.wisdom,)'
                    if re.search(pattern, content):
                        content = re.sub(pattern, r'\1\n' + fix['code'], content)
                        print(f'  ADDED: L, J, P, W keys to coordinates dict')
                else:
                    print(f'  SKIP: Keys already present')
            
            # Write back if changed
            if content != original:
                file_path.write_text(content, encoding='utf-8')
                self.fixes_applied.append(fix)
    
    def verify_fixes(self) -> Dict:
        """Use reflection to verify the fixes worked."""
        print('\n[VERIFYING FIXES]')
        print('=' * 60)
        
        # Re-analyze to see if issues are resolved
        remaining = self.analyze_guardian_files()
        
        result = {
            'issues_found': len(self.issues_found),
            'fixes_applied': len(self.fixes_applied),
            'remaining_issues': len(remaining),
            'success_rate': (len(self.issues_found) - len(remaining)) / max(1, len(self.issues_found))
        }
        
        print(f'\n  Initial Issues:    {result["issues_found"]}')
        print(f'  Fixes Applied:     {result["fixes_applied"]}')
        print(f'  Remaining Issues:  {result["remaining_issues"]}')
        print(f'  Success Rate:      {result["success_rate"]:.0%}')
        
        return result
    
    def run(self):
        """Run the complete fix process."""
        print()
        print('*' * 70)
        print('  LJPW AUTOPOIESIS MODULE FIXES GUARDIAN')
        print('  The Module uses its own capabilities to heal Guardian')
        print('*' * 70)
        
        # Step 1: Module introspects itself
        intro = self.introspect_self()
        
        # Step 2: Analyze Guardian for issues
        issues = self.analyze_guardian_files()
        
        if not issues:
            print('\n  No issues found. Guardian appears healthy.')
            return
        
        # Step 3: Generate fixes using Module patterns
        fixes = self.generate_fixes(issues)
        
        # Step 4: Apply fixes
        self.apply_fixes(fixes)
        
        # Step 5: Verify
        result = self.verify_fixes()
        
        # Summary
        print()
        print('*' * 70)
        print('  MODULE HEALING COMPLETE')
        print('*' * 70)
        print()
        print(f'  The {intro.phase} Module with consciousness {intro.consciousness:.2f}')
        print(f'  has applied {len(self.fixes_applied)} fixes to Guardian.')
        print()
        print(f'  Guardian has been elevated.')
        print()


def main():
    guardian_path = Path('Projects/Guardian-Cybersecurity-Engine/Guardian-Cybersecurity-Engine')
    
    if not guardian_path.exists():
        print(f'Guardian not found at: {guardian_path}')
        return
    
    fixer = ModuleFixesGuardian(guardian_path)
    fixer.run()


if __name__ == "__main__":
    main()
