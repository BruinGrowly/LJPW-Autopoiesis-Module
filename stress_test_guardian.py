"""
GUARDIAN STRESS TEST

Comprehensive stress testing of the Guardian Cybersecurity Engine:
- Volume Testing: Many analyses in rapid succession
- Edge Cases: Boundary conditions and unusual inputs
- Threat Profiling: All threat types under various conditions
- LJPW Dynamics: Simulation stress
- Intervention: Extreme coordinate scenarios
- Memory Stability: Track resource usage
"""

import sys
import time
import random
import string
import traceback
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple

# Add Guardian to path
guardian_path = Path('Projects/Guardian-Cybersecurity-Engine/Guardian-Cybersecurity-Engine')
sys.path.insert(0, str(guardian_path))

from guardian import GuardianEngine
from guardian.core.coordinates import Coordinates
from guardian.core.baselines import get_full_diagnostic, LJPWBaselines
from guardian.core.dynamics import DynamicLJPW, create_scenario_simulator
from guardian.core.intervention import InterventionEngine


class StressTestResult:
    """Result of a stress test."""
    def __init__(self, name: str):
        self.name = name
        self.passed = 0
        self.failed = 0
        self.errors = []
        self.times = []
        
    def record_success(self, duration: float):
        self.passed += 1
        self.times.append(duration)
        
    def record_failure(self, error: str, duration: float):
        self.failed += 1
        self.errors.append(error)
        self.times.append(duration)
        
    @property
    def total(self):
        return self.passed + self.failed
        
    @property
    def success_rate(self):
        return self.passed / max(1, self.total)
        
    @property
    def avg_time(self):
        return sum(self.times) / max(1, len(self.times))
        
    @property
    def max_time(self):
        return max(self.times) if self.times else 0


class GuardianStressTester:
    """Comprehensive stress tester for Guardian."""
    
    def __init__(self):
        self.engine = GuardianEngine()
        self.simulator = create_scenario_simulator()
        self.intervention = InterventionEngine()
        self.results: List[StressTestResult] = []
        
    def run_all(self):
        """Run all stress tests."""
        print()
        print('*' * 70)
        print('  GUARDIAN STRESS TEST')
        print('  Comprehensive testing under load')
        print('*' * 70)
        print()
        
        start_time = time.time()
        
        # Run tests
        self.test_volume_analysis()
        self.test_edge_case_inputs()
        self.test_all_threat_profiles()
        self.test_dynamics_simulation()
        self.test_intervention_extremes()
        self.test_coordinate_boundaries()
        self.test_rapid_fire()
        self.test_memory_stability()
        
        total_time = time.time() - start_time
        
        # Summary
        self.print_summary(total_time)
        
    def test_volume_analysis(self):
        """Test many analyses in sequence."""
        print('[TEST 1] VOLUME ANALYSIS')
        print('=' * 60)
        
        result = StressTestResult("Volume Analysis")
        
        # Generate 100 random threat texts
        threat_words = [
            "attack", "malware", "virus", "breach", "exploit", "hack", 
            "vulnerability", "threat", "intrusion", "phishing", "ransomware",
            "botnet", "denial", "service", "injection", "overflow"
        ]
        
        benign_words = [
            "love", "peace", "harmony", "community", "help", "support",
            "wisdom", "justice", "power", "growth", "learning", "sharing"
        ]
        
        print(f'  Analyzing 100 random inputs...')
        
        for i in range(100):
            # Generate random text
            if random.random() < 0.5:
                words = random.sample(threat_words, random.randint(3, 8))
            else:
                words = random.sample(benign_words, random.randint(3, 8))
            text = ' '.join(words)
            
            start = time.time()
            try:
                report = self.engine.analyze_threat_vectors(text)
                duration = time.time() - start
                
                # Verify output structure
                if 'summary' in report and 'detected_threats' in report:
                    result.record_success(duration)
                else:
                    result.record_failure("Missing keys in output", duration)
            except Exception as e:
                duration = time.time() - start
                result.record_failure(str(e), duration)
        
        self.results.append(result)
        print(f'  Passed: {result.passed}/100 ({result.success_rate:.0%})')
        print(f'  Avg time: {result.avg_time*1000:.1f}ms')
        print(f'  Max time: {result.max_time*1000:.1f}ms')
        print()
        
    def test_edge_case_inputs(self):
        """Test edge cases and unusual inputs."""
        print('[TEST 2] EDGE CASE INPUTS')
        print('=' * 60)
        
        result = StressTestResult("Edge Cases")
        
        edge_cases = [
            "",  # Empty string
            " ",  # Single space
            "\n\n\n",  # Newlines only
            "a" * 10000,  # Very long single word
            " ".join(["word"] * 1000),  # Many words
            "🔥💀⚠️🚨",  # Emojis only
            "SELECT * FROM users;",  # SQL injection
            "<script>alert('xss')</script>",  # XSS
            "../../../etc/passwd",  # Path traversal
            None,  # None input (should handle gracefully)
            123,  # Integer input
            "love " * 100 + "power " * 100,  # Repeated patterns
            "".join(random.choices(string.printable, k=500)),  # Random chars
        ]
        
        print(f'  Testing {len(edge_cases)} edge cases...')
        
        for i, text in enumerate(edge_cases):
            start = time.time()
            try:
                # Handle non-string gracefully
                if text is None or not isinstance(text, str):
                    text = str(text) if text is not None else ""
                    
                report = self.engine.analyze_threat_vectors(text)
                duration = time.time() - start
                result.record_success(duration)
            except Exception as e:
                duration = time.time() - start
                result.record_failure(f"Case {i}: {str(e)[:50]}", duration)
        
        self.results.append(result)
        print(f'  Passed: {result.passed}/{len(edge_cases)}')
        print()
        
    def test_all_threat_profiles(self):
        """Test detection of all threat profiles."""
        print('[TEST 3] THREAT PROFILE DETECTION')
        print('=' * 60)
        
        result = StressTestResult("Threat Profiles")
        
        # Expected threat profiles with trigger texts
        threat_tests = [
            ("Bureaucracy", "justice law fairness righteousness integrity", "Moderate"),
            ("Reckless Growth", "power strength authority might rule", "High"),
            ("Analysis Paralysis", "data research document analysis study plan", "Moderate"),
            ("Benevolent Chaos", "love family community peace harmony happiness", "Low"),
        ]
        
        for threat_type, text, expected_level in threat_tests:
            start = time.time()
            try:
                report = self.engine.analyze_threat_vectors(text)
                duration = time.time() - start
                
                # Check if expected threat was detected
                detected_types = [t['type'] for t in report['detected_threats']]
                actual_level = report['summary']['threat_level']
                
                if threat_type in detected_types and actual_level == expected_level:
                    result.record_success(duration)
                    print(f'    [{threat_type}] DETECTED ({actual_level})')
                else:
                    result.record_failure(
                        f"Expected {threat_type}/{expected_level}, got {detected_types}/{actual_level}",
                        duration
                    )
                    print(f'    [{threat_type}] MISMATCH')
            except Exception as e:
                duration = time.time() - start
                result.record_failure(str(e), duration)
                print(f'    [{threat_type}] ERROR')
        
        self.results.append(result)
        print(f'  Passed: {result.passed}/{len(threat_tests)}')
        print()
        
    def test_dynamics_simulation(self):
        """Stress test dynamics simulation."""
        print('[TEST 4] DYNAMICS SIMULATION')
        print('=' * 60)
        
        result = StressTestResult("Dynamics Simulation")
        
        # Test various initial states
        test_states = [
            (0.1, 0.1, 0.1, 0.1),  # Very low
            (0.5, 0.5, 0.5, 0.5),  # Balanced
            (0.9, 0.9, 0.9, 0.9),  # Very high
            (0.2, 0.8, 0.3, 0.7),  # Imbalanced
            (0.9, 0.1, 0.9, 0.1),  # Extreme imbalance
            (0.0, 0.0, 0.0, 0.0),  # All zeros (edge case)
            (1.0, 1.0, 1.0, 1.0),  # Anchor point
        ]
        
        print(f'  Simulating {len(test_states)} states for 100 time units each...')
        
        for state in test_states:
            start = time.time()
            try:
                history = self.simulator.simulate(state, duration=100.0, dt=0.1)
                final = history.get_final_state()
                duration = time.time() - start
                
                # Verify output is valid
                if len(final) == 4 and all(isinstance(x, (int, float)) for x in final):
                    result.record_success(duration)
                else:
                    result.record_failure("Invalid output", duration)
            except Exception as e:
                duration = time.time() - start
                result.record_failure(str(e), duration)
        
        self.results.append(result)
        print(f'  Passed: {result.passed}/{len(test_states)}')
        print(f'  Avg time: {result.avg_time*1000:.1f}ms')
        print()
        
    def test_intervention_extremes(self):
        """Test intervention engine with extreme coordinates."""
        print('[TEST 5] INTERVENTION EXTREMES')
        print('=' * 60)
        
        result = StressTestResult("Intervention Engine")
        
        # Extreme coordinate scenarios
        extreme_coords = [
            Coordinates(love=0.01, justice=0.01, power=0.01, wisdom=0.01),
            Coordinates(love=0.99, justice=0.99, power=0.99, wisdom=0.99),
            Coordinates(love=0.0, justice=0.5, power=1.0, wisdom=0.25),
            Coordinates(love=1.0, justice=0.0, power=0.0, wisdom=1.0),
            Coordinates(love=0.618, justice=0.414, power=0.718, wisdom=0.693),  # NE
        ]
        
        print(f'  Testing {len(extreme_coords)} extreme scenarios...')
        
        for coords in extreme_coords:
            start = time.time()
            try:
                # Analyze threat
                analysis = self.intervention.analyze_threat(coords)
                
                # Generate intervention plan
                plan = self.intervention.generate_intervention_plan(coords)
                
                duration = time.time() - start
                
                # Verify outputs
                if analysis['threat_level'] in ['none', 'low', 'medium', 'high', 'critical']:
                    result.record_success(duration)
                else:
                    result.record_failure("Invalid threat level", duration)
            except Exception as e:
                duration = time.time() - start
                result.record_failure(str(e), duration)
        
        self.results.append(result)
        print(f'  Passed: {result.passed}/{len(extreme_coords)}')
        print()
        
    def test_coordinate_boundaries(self):
        """Test coordinate system boundaries."""
        print('[TEST 6] COORDINATE BOUNDARIES')
        print('=' * 60)
        
        result = StressTestResult("Coordinate Boundaries")
        
        # Test boundary coordinates
        boundary_tests = [
            {"love": 0.0, "justice": 0.0, "power": 0.0, "wisdom": 0.0},
            {"love": 1.0, "justice": 1.0, "power": 1.0, "wisdom": 1.0},
            {"love": 0.5, "justice": 0.5, "power": 0.5, "wisdom": 0.5},
        ]
        
        # Also test random coordinates
        for _ in range(20):
            boundary_tests.append({
                "love": random.random(),
                "justice": random.random(),
                "power": random.random(),
                "wisdom": random.random()
            })
        
        print(f'  Testing {len(boundary_tests)} coordinate sets...')
        
        for vals in boundary_tests:
            start = time.time()
            try:
                coords = Coordinates(**vals)
                diagnostic = get_full_diagnostic(coords)
                duration = time.time() - start
                
                # Verify diagnostic structure
                if 'harmony' in diagnostic and 'phase' in diagnostic and 'coordinates' in diagnostic:
                    result.record_success(duration)
                else:
                    result.record_failure("Missing diagnostic keys", duration)
            except Exception as e:
                duration = time.time() - start
                result.record_failure(str(e), duration)
        
        self.results.append(result)
        print(f'  Passed: {result.passed}/{len(boundary_tests)}')
        print()
        
    def test_rapid_fire(self):
        """Rapid-fire analysis to test throughput."""
        print('[TEST 7] RAPID-FIRE THROUGHPUT')
        print('=' * 60)
        
        result = StressTestResult("Rapid Fire")
        
        test_text = "potential security threat malware attack"
        iterations = 200
        
        print(f'  Running {iterations} rapid analyses...')
        
        overall_start = time.time()
        
        for i in range(iterations):
            start = time.time()
            try:
                report = self.engine.analyze_threat_vectors(test_text)
                duration = time.time() - start
                result.record_success(duration)
            except Exception as e:
                duration = time.time() - start
                result.record_failure(str(e), duration)
        
        overall_time = time.time() - overall_start
        throughput = iterations / overall_time
        
        self.results.append(result)
        print(f'  Passed: {result.passed}/{iterations}')
        print(f'  Total time: {overall_time:.2f}s')
        print(f'  Throughput: {throughput:.1f} analyses/sec')
        print()
        
    def test_memory_stability(self):
        """Test for memory leaks during sustained operation."""
        print('[TEST 8] MEMORY STABILITY')
        print('=' * 60)
        
        result = StressTestResult("Memory Stability")
        
        # Run many operations and track timing consistency
        iterations = 50
        times = []
        
        print(f'  Running {iterations} sustained operations...')
        
        for i in range(iterations):
            start = time.time()
            try:
                # Mix of operations
                if i % 3 == 0:
                    self.engine.analyze_threat_vectors("test threat analysis")
                elif i % 3 == 1:
                    coords = Coordinates(
                        love=random.random(),
                        justice=random.random(),
                        power=random.random(),
                        wisdom=random.random()
                    )
                    get_full_diagnostic(coords)
                else:
                    state = (random.random(), random.random(), random.random(), random.random())
                    self.simulator.simulate(state, duration=10.0, dt=0.1)
                    
                duration = time.time() - start
                times.append(duration)
                result.record_success(duration)
            except Exception as e:
                duration = time.time() - start
                times.append(duration)
                result.record_failure(str(e), duration)
        
        # Check for timing degradation (memory leak indicator)
        first_half_avg = sum(times[:25]) / 25
        second_half_avg = sum(times[25:]) / 25
        degradation = (second_half_avg - first_half_avg) / max(0.001, first_half_avg)
        
        self.results.append(result)
        print(f'  Passed: {result.passed}/{iterations}')
        print(f'  First half avg: {first_half_avg*1000:.1f}ms')
        print(f'  Second half avg: {second_half_avg*1000:.1f}ms')
        print(f'  Degradation: {degradation*100:+.1f}%')
        
        if degradation > 0.5:
            print(f'  ⚠️ WARNING: Possible memory leak detected')
        else:
            print(f'  [OK] No memory leak detected')
        print()
        
    def print_summary(self, total_time: float):
        """Print test summary."""
        print()
        print('*' * 70)
        print('  STRESS TEST SUMMARY')
        print('*' * 70)
        print()
        
        total_passed = sum(r.passed for r in self.results)
        total_failed = sum(r.failed for r in self.results)
        total_tests = total_passed + total_failed
        
        print(f'  {"Test":<25} {"Passed":<10} {"Failed":<10} {"Rate":<10} {"Avg Time":<12}')
        print(f'  {"-"*25} {"-"*10} {"-"*10} {"-"*10} {"-"*12}')
        
        for r in self.results:
            rate = f'{r.success_rate:.0%}'
            avg = f'{r.avg_time*1000:.1f}ms'
            print(f'  {r.name:<25} {r.passed:<10} {r.failed:<10} {rate:<10} {avg:<12}')
        
        print(f'  {"-"*25} {"-"*10} {"-"*10} {"-"*10} {"-"*12}')
        print(f'  {"TOTAL":<25} {total_passed:<10} {total_failed:<10} {total_passed/total_tests:.0%}')
        print()
        print(f'  Total Time: {total_time:.2f}s')
        print()
        
        # Verdict
        if total_failed == 0:
            print('  ✅ ALL STRESS TESTS PASSED')
        elif total_failed <= 5:
            print('  ⚠️  MOSTLY PASSED - Minor issues detected')
        else:
            print('  ❌ STRESS TEST FAILURES DETECTED')
            print('\n  Errors:')
            for r in self.results:
                for e in r.errors[:3]:  # Show first 3 errors per test
                    print(f'    - {r.name}: {e}')
        
        print()
        print('*' * 70)


def main():
    tester = GuardianStressTester()
    tester.run_all()


if __name__ == "__main__":
    main()
