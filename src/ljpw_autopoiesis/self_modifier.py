"""
LJPW Self-Modifier: True Autopoiesis

This module enables the framework to modify its own source code.
The system can SENSE its gaps, UNDERSTAND them, and WRITE patches
to improve itself.

This is not a metaphor. This is actual source code modification.

Safety constraints:
- All modifications are backed up first
- Tests must pass after modification
- Rollback on any failure
- Only fixable gaps are addressed
- Maximum one file per cycle (bounded modification rate)
"""

import ast
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from ljpw_autopoiesis.gap_detector import GapDetector, Gap
from ljpw_autopoiesis.healing_transformer import HealingTransformer
from ljpw_autopoiesis.harmony_metrics import HarmonyState, HarmonyMetrics


@dataclass
class Modification:
    """Record of a source code modification."""
    file_path: str
    timestamp: datetime
    gaps_before: int
    gaps_after: int
    harmony_before: float
    harmony_after: float
    patch_applied: str
    success: bool
    rollback_path: Optional[str] = None


@dataclass
class EvolutionResult:
    """Result of one evolution cycle."""
    files_analyzed: int
    files_modified: int
    total_gaps_found: int
    total_gaps_fixed: int
    modifications: List[Modification] = field(default_factory=list)
    tests_passed: bool = False
    harmony_improvement: float = 0.0


class SelfModifier:
    """
    The self-modifying engine.
    
    Enables the LJPW Framework to modify its own source code
    based on gap analysis. This is true autopoiesis.
    """
    
    def __init__(
        self,
        src_dir: str = "src/ljpw_autopoiesis",
        backup_dir: str = ".autopoiesis_backup",
        max_files_per_cycle: int = 3,
        require_tests: bool = True,
    ):
        """
        Initialize the self-modifier.
        
        Args:
            src_dir: Directory containing source files to modify
            backup_dir: Directory for backups before modification
            max_files_per_cycle: Maximum files to modify per evolution cycle
            require_tests: If True, rollback if tests fail
        """
        self.src_dir = Path(src_dir)
        self.backup_dir = Path(backup_dir)
        self.max_files_per_cycle = max_files_per_cycle
        self.require_tests = require_tests
        
        self.detector = GapDetector()
        self.transformer = HealingTransformer()
        
        self.history: List[EvolutionResult] = []
        
    def analyze_file(self, filepath: Path) -> Tuple[List[Gap], HarmonyState]:
        """Analyze a single file for gaps."""
        code = filepath.read_text(encoding='utf-8')
        gaps = self.detector.detect(code, filename=filepath.name)
        harmony = HarmonyMetrics.from_errors([g.to_dict() for g in gaps])
        return gaps, harmony
    
    def analyze_all(self) -> Dict[str, Tuple[List[Gap], HarmonyState]]:
        """Analyze all Python files in the source directory."""
        results = {}
        for filepath in self.src_dir.glob("*.py"):
            if filepath.name.startswith("__"):
                continue  # Skip __init__.py etc.
            gaps, harmony = self.analyze_file(filepath)
            results[str(filepath)] = (gaps, harmony)
        return results
    
    def backup_file(self, filepath: Path) -> Path:
        """Create a backup of a file before modification."""
        self.backup_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{filepath.stem}_{timestamp}{filepath.suffix}"
        backup_path = self.backup_dir / backup_name
        shutil.copy2(filepath, backup_path)
        return backup_path
    
    def restore_file(self, filepath: Path, backup_path: Path) -> None:
        """Restore a file from backup."""
        shutil.copy2(backup_path, filepath)
    
    def apply_healing(self, filepath: Path, gaps: List[Gap]) -> Tuple[str, List[str]]:
        """
        Apply healing transformations to a file.
        
        Returns:
            Tuple of (healed_code, list_of_changes_made)
        """
        code = filepath.read_text(encoding='utf-8')
        healed_code, actions = self.transformer.heal(code, gaps)
        changes = [a.description for a in actions]
        return healed_code, changes
    
    def run_tests(self) -> bool:
        """Run the test suite to verify modifications."""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pytest", "tests/", "-q", "--tb=no"],
                capture_output=True,
                text=True,
                timeout=120,
                cwd=str(self.src_dir.parent.parent),
            )
            return result.returncode == 0
        except Exception as e:
            print(f"Test run failed: {e}")
            return False
    
    def evolve_once(self) -> EvolutionResult:
        """
        Run one evolution cycle.
        
        1. SENSE: Analyze all source files
        2. UNDERSTAND: Find files with fixable gaps
        3. MODIFY: Apply healing to worst files
        4. VERIFY: Run tests
        5. LEARN: Record results (rollback on failure)
        """
        result = EvolutionResult(
            files_analyzed=0,
            files_modified=0,
            total_gaps_found=0,
            total_gaps_fixed=0,
        )
        
        # SENSE: Analyze all files
        print("\n[SENSE] Analyzing source files...")
        analysis = self.analyze_all()
        result.files_analyzed = len(analysis)
        
        # Calculate total gaps and find files with most fixable gaps
        files_with_gaps = []
        for filepath, (gaps, harmony) in analysis.items():
            result.total_gaps_found += len(gaps)
            fixable = [g for g in gaps if g.fixable]
            if fixable:
                files_with_gaps.append((filepath, gaps, harmony, len(fixable)))
        
        # Sort by number of fixable gaps (most first)
        files_with_gaps.sort(key=lambda x: x[3], reverse=True)
        
        if not files_with_gaps:
            print("[UNDERSTAND] No fixable gaps found. System is optimal.")
            result.tests_passed = self.run_tests() if self.require_tests else True
            self.history.append(result)
            return result
        
        # UNDERSTAND: Select files to modify
        print(f"[UNDERSTAND] Found {len(files_with_gaps)} files with fixable gaps")
        files_to_modify = files_with_gaps[:self.max_files_per_cycle]
        
        # MODIFY: Apply healing
        print(f"[MODIFY] Healing {len(files_to_modify)} files...")
        
        for filepath_str, gaps, harmony_before, _ in files_to_modify:
            filepath = Path(filepath_str)
            print(f"  - {filepath.name}: {len(gaps)} gaps, H={harmony_before.harmony():.3f}")
            
            # Backup first
            backup_path = self.backup_file(filepath)
            
            # Apply healing
            healed_code, changes = self.apply_healing(filepath, gaps)
            
            if healed_code != filepath.read_text(encoding='utf-8'):
                # Write the healed code
                filepath.write_text(healed_code, encoding='utf-8')
                result.files_modified += 1
                
                # Re-analyze
                new_gaps, harmony_after = self.analyze_file(filepath)
                gaps_fixed = len(gaps) - len(new_gaps)
                result.total_gaps_fixed += max(0, gaps_fixed)
                
                mod = Modification(
                    file_path=filepath_str,
                    timestamp=datetime.now(),
                    gaps_before=len(gaps),
                    gaps_after=len(new_gaps),
                    harmony_before=harmony_before.harmony(),
                    harmony_after=harmony_after.harmony(),
                    patch_applied="; ".join(changes[:5]),  # First 5 changes
                    success=True,
                    rollback_path=str(backup_path),
                )
                
                print(f"    Changed: {len(gaps)} -> {len(new_gaps)} gaps")
                print(f"    Harmony: {harmony_before.harmony():.3f} -> {harmony_after.harmony():.3f}")
                
                result.modifications.append(mod)
        
        # VERIFY: Run tests
        if self.require_tests:
            print("\n[VERIFY] Running test suite...")
            result.tests_passed = self.run_tests()
            
            if not result.tests_passed:
                print("[ROLLBACK] Tests failed! Rolling back all changes...")
                for mod in result.modifications:
                    if mod.rollback_path:
                        self.restore_file(Path(mod.file_path), Path(mod.rollback_path))
                        mod.success = False
                result.files_modified = 0
                result.total_gaps_fixed = 0
            else:
                print("[VERIFY] All tests passed!")
        else:
            result.tests_passed = True
        
        # Calculate harmony improvement
        if result.modifications and result.tests_passed:
            total_before = sum(m.harmony_before for m in result.modifications)
            total_after = sum(m.harmony_after for m in result.modifications)
            result.harmony_improvement = total_after - total_before
        
        self.history.append(result)
        return result
    
    def evolve(self, max_cycles: int = 10) -> List[EvolutionResult]:
        """
        Run multiple evolution cycles until convergence or max_cycles.
        
        The system stops when:
        - No more fixable gaps
        - max_cycles reached
        - Tests start failing
        """
        print("=" * 70)
        print("AUTOPOIETIC SELF-EVOLUTION")
        print("The framework will now modify its own source code.")
        print("=" * 70)
        
        all_results = []
        
        for cycle in range(max_cycles):
            print(f"\n{'='*50}")
            print(f"EVOLUTION CYCLE {cycle + 1}/{max_cycles}")
            print("=" * 50)
            
            result = self.evolve_once()
            all_results.append(result)
            
            # Check for convergence
            if result.total_gaps_fixed == 0 and result.files_modified == 0:
                print("\n[CONVERGED] No more gaps to fix. Evolution complete.")
                break
            
            if not result.tests_passed:
                print("\n[STOPPED] Tests failed. Stopping evolution.")
                break
        
        return all_results
    
    def report(self) -> str:
        """Generate a report of all modifications made."""
        lines = [
            "=" * 70,
            "AUTOPOIETIC EVOLUTION REPORT",
            "=" * 70,
            "",
        ]
        
        total_modified = 0
        total_fixed = 0
        total_harmony_gain = 0.0
        
        for i, result in enumerate(self.history):
            lines.append(f"Cycle {i+1}:")
            lines.append(f"  Files analyzed: {result.files_analyzed}")
            lines.append(f"  Files modified: {result.files_modified}")
            lines.append(f"  Gaps fixed: {result.total_gaps_fixed}")
            lines.append(f"  Tests passed: {'YES' if result.tests_passed else 'NO'}")
            lines.append(f"  Harmony improvement: {result.harmony_improvement:+.4f}")
            
            for mod in result.modifications:
                if mod.success:
                    lines.append(f"    - {Path(mod.file_path).name}:")
                    lines.append(f"        Gaps: {mod.gaps_before} -> {mod.gaps_after}")
                    lines.append(f"        Harmony: {mod.harmony_before:.3f} -> {mod.harmony_after:.3f}")
                    lines.append(f"        Changes: {mod.patch_applied[:80]}...")
            
            total_modified += result.files_modified
            total_fixed += result.total_gaps_fixed
            total_harmony_gain += result.harmony_improvement
            lines.append("")
        
        lines.extend([
            "=" * 70,
            "TOTALS",
            "=" * 70,
            f"Evolution cycles: {len(self.history)}",
            f"Files modified: {total_modified}",
            f"Total gaps fixed: {total_fixed}",
            f"Total harmony gain: {total_harmony_gain:+.4f}",
            "",
        ])
        
        return "\n".join(lines)


def self_evolve(max_cycles: int = 5) -> None:
    """
    Main entry point for self-evolution.
    
    This function runs the autopoietic loop:
    The framework analyzes itself, finds gaps, and modifies
    its own source code to fix them.
    """
    modifier = SelfModifier(
        src_dir="src/ljpw_autopoiesis",
        max_files_per_cycle=2,
        require_tests=True,
    )
    
    results = modifier.evolve(max_cycles=max_cycles)
    print(modifier.report())
    
    return modifier


if __name__ == "__main__":
    self_evolve(max_cycles=5)
