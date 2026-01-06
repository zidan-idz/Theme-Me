#!/usr/bin/env python3
"""
Run all Theme-Me tests and generate a summary report.
"""

import unittest
import sys
from pathlib import Path

# Add project root to sys.path so we can import core modules
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT))

def run_tests():
    """Run all test suites and print results."""
    
    # Test files (relative to testing/ directory)
    test_files = [
        'test_themes.py',
        'test_fonts.py',
        'test_backgrounds.py'
    ]
    
    print("=" * 70)
    print("Theme-Me - Automated Test Suite")
    print("=" * 70)
    print()
    
    total_tests = 0
    total_passed = 0
    total_failed = 0
    
    for test_file in test_files:
        test_path = Path(__file__).parent / test_file
        if not test_path.exists():
            print(f"[ERROR] Test file not found: {test_file}")
            continue
        
        print(f"Running: {test_file}")
        print("-" * 70)
        
        # Load and run the test
        # We need to load from the 'testing' module context
        loader = unittest.TestLoader()
        # Since we are inside testing/, we can import directly if we are careful,
        # but better to load by file path or module name relative to root
        
        # Using discovery is often easier, but let's stick to the explicit list
        # We can load by name 'testing.test_themes' since we added root to path
        module_name = f"testing.{test_file.replace('.py', '')}"
        
        try:
            suite = loader.loadTestsFromName(module_name)
        except Exception as e:
            print(f"[ERROR] Failed to load {module_name}: {e}")
            total_failed += 1
            continue
        
        # Run tests with a custom result
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        # Update counters
        tests_run = result.testsRun
        failures = len(result.failures)
        errors = len(result.errors)
        passed = tests_run - failures - errors
        
        total_tests += tests_run
        total_passed += passed
        total_failed += failures + errors
        
        print()
    
    # Print summary
    print("=" * 70)
    print("Test Summary")
    print("=" * 70)
    print(f"Total Tests:  {total_tests}")
    print(f"[PASS] Passed:    {total_passed}")
    print(f"[FAIL] Failed:    {total_failed}")
    print()
    
    if total_failed == 0:
        print("[SUCCESS] All tests passed! Project is ready for deployment.")
        return 0
    else:
        print("[WARNING] Some tests failed. Please review the output above.")
        return 1

if __name__ == '__main__':
    sys.exit(run_tests())
