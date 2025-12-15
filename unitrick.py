#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
# ]
# ///
from pathlib import Path
from functools import partial
import argparse
import random
import sys
import time


whitelist = set()

def tricky_monkey_generator(instr: str, insert_invisible: bool):
    known_empty_chars: list[str] = [
        "\u200b",  # ZERO WIDTH SPACE
        "\u200c",  # ZERO WIDTH NON-JOINER
        "\u200d",  # ZERO WIDTH JOINER
        "\u2060",  # WORD JOINER
        "\u2061",  # FUNCTION APPLICATION
        "\u2062",  # INVISIBLE TIMES
        "\u2063",  # INVISIBLE SEPARATOR
        "\u2064",  # INVISIBLE PLUS
        "\ufeff",  # ZERO WIDTH NO-BREAK SPACE (BOM)
    ]

    for i, c in enumerate(instr):
        try:
            if i < len(instr) - 1:
                empty_strs: str = "".join(random.choices(known_empty_chars, k=random.randint(50, 100)))
            else:
                empty_strs: str = ""

            yield c + empty_strs

        except Exception:
            yield c


def tricky_monkey(instr: str, insert_invisible: bool) -> str:
    return "".join(
        tricky_monkey_generator(
            instr,
            insert_invisible=insert_invisible,
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Insert random invisible unicode characters after each character of an input text.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  {sys.argv[0]} -i input_file.txt -n
  {sys.argv[0]} -s "The quick brown fox jumps over the lazy dog." -n

  {sys.argv[0]} -i input_file.txt -n -o output_file.txt
  {sys.argv[0]} -s "The quick brown fox jumps over the lazy dog." -n -o output_file.txt
        """,
    )

    encoding_group = parser.add_argument_group("Encoding Arguments")
    encoding_group.add_argument("-i", "--input-file", type=Path, help="Path to file containing the text.")
    encoding_group.add_argument("-s", "--input-text", type=str, help="Direct input of the text.")
    encoding_group.add_argument(
        "-n",
        "--invisible",
        action="store_true",
        help="Insert invisible chars.",
    )

    output_group = parser.add_argument_group("Output Arguments (what to display)")
    output_group.add_argument("-o", "--output-text", type=Path, help="Write result to file at output path.")

    args = parser.parse_args()

    inv: bool = args.invisible

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if args.input_file and args.output_text:
        with (
            open(args.input_file.resolve(), "rt") as infd,
            open(args.output_text.resolve(), "wt") as outfd,
        ):
            for line in infd:
                outfd.write(
                    tricky_monkey(
                        instr=line,
                        insert_invisible=inv,
                    )
                )
    elif args.input_file:
        with open(args.input_file.resolve(), "rt") as infd:
            for line in infd:
                print(
                    tricky_monkey(
                        instr=line,
                        insert_invisible=inv,
                    )
                )
    elif args.input_text and args.output_text:
        with open(args.output_text.resolve(), "wt") as outfd:
            outfd.write(
                tricky_monkey(
                    instr=args.input_text,
                    insert_invisible=inv,
                )
            )
    elif args.input_text:
        print(
            tricky_monkey(
                instr=args.input_text,
                insert_invisible=inv,
            )
        )
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
