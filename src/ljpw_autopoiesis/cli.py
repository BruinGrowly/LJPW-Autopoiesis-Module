"""
CLI for LJPW Autopoiesis Self-Healing Module.

Usage:
    ljpw-heal <file>           Heal a Python file
    ljpw-heal --diagnose <file>  Diagnose without healing
    ljpw-heal --stdin          Read from stdin
"""

import argparse
import sys
from pathlib import Path

from .engine import SelfHealingEngine, diagnose


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="LJPW Autopoiesis Self-Healing Module",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ljpw-heal script.py              # Heal script.py in place
  ljpw-heal script.py -o fixed.py  # Heal and save to fixed.py
  ljpw-heal --diagnose script.py   # Diagnose without healing
  ljpw-heal --stdin < script.py    # Heal from stdin

Based on LJPW Framework V7.9: "The gap is the fuel."
Errors are metabolized to bring code back into harmony.
        """,
    )

    parser.add_argument(
        "file",
        nargs="?",
        help="Python file to heal",
    )

    parser.add_argument(
        "-o", "--output",
        help="Output file (default: overwrite input)",
    )

    parser.add_argument(
        "--diagnose",
        action="store_true",
        help="Diagnose only, don't heal",
    )

    parser.add_argument(
        "--stdin",
        action="store_true",
        help="Read source from stdin",
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output",
    )

    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Don't create backup when overwriting",
    )

    parser.add_argument(
        "--max-ticks",
        type=int,
        default=20,
        help="Maximum tick cycles (default: 20)",
    )

    parser.add_argument(
        "--report",
        action="store_true",
        help="Show detailed report after healing",
    )

    args = parser.parse_args()

    # Get source
    if args.stdin:
        source = sys.stdin.read()
        filename = "<stdin>"
    elif args.file:
        path = Path(args.file)
        if not path.exists():
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        source = path.read_text(encoding="utf-8")
        filename = args.file
    else:
        parser.print_help()
        sys.exit(1)

    # Diagnose mode
    if args.diagnose:
        report = diagnose(source)
        print(report)
        sys.exit(0)

    # Heal mode
    engine = SelfHealingEngine(
        max_ticks=args.max_ticks,
        verbose=args.verbose,
    )

    result = engine.heal_source(source, filename=filename)

    # Output
    if args.stdin:
        # Write to stdout
        print(result.healed_source)
    elif args.output:
        # Write to specified file
        Path(args.output).write_text(result.healed_source, encoding="utf-8")
        print(f"Healed code written to: {args.output}")
    else:
        # Overwrite input file
        if result.source_changed:
            path = Path(args.file)
            if not args.no_backup:
                backup_path = path.with_suffix(path.suffix + ".bak")
                backup_path.write_text(source, encoding="utf-8")
                print(f"Backup saved to: {backup_path}")
            path.write_text(result.healed_source, encoding="utf-8")
            print(f"Healed: {args.file}")
        else:
            print(f"No changes needed: {args.file}")

    # Report
    if args.report:
        print("\n" + "=" * 60)
        print(engine.report())

    # Summary
    if not args.stdin:
        print(f"\nSummary:")
        print(f"  Ticks: {result.total_ticks}")
        print(f"  Gaps found: {result.total_gaps_found}")
        print(f"  Gaps healed: {result.total_gaps_healed}")
        print(f"  Initial harmony: {result.initial_harmony.harmony():.3f}")
        print(f"  Final harmony: {result.final_harmony.harmony():.3f}")
        print(f"  Phase: {result.final_harmony.phase()}")


if __name__ == "__main__":
    main()
