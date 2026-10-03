"""Screen OCR Region — Select a screen region, read the text, and copy it to the clipboard."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='screen_ocr_region',
        description='Select a screen region, read the text, and copy it to the clipboard.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Screen OCR Region')
    print('Grab text from a window when copy is disabled.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
