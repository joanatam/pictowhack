#!/usr/bin/env python3
"""
Remove Pictograms Utility

This script removes pictograms (emoji, symbols, and other Unicode pictographic characters)
from files specified by path patterns.

Usage:
    python pictowhack.py PATHSPEC [PATHSPEC ...]
    ./pictowhack.py "*.txt" "docs/*.md"

Examples:
    ./pictowhack.py *.txt
    ./pictowhack.py docs/*.md src/**/*.js
    ./pictowhack.py --dry-run *.txt
"""

import sys
import os
import glob
import unicodedata
import argparse
from pathlib import Path


def is_pictogram(char):
    """
    Determine if a character is a pictogram/emoji/symbol that should be removed.

    This includes:
    - Emoji characters (various Unicode blocks)
    - Other symbols (So category except 'box drawings')
    - Modifier symbols (Sk category)
    - Various symbol blocks
    """
    try:
        category = unicodedata.category(char)
        name = unicodedata.name(char, '').lower()

        if category in ['So']:  # Other Symbol, Modifier Symbol
            if len(name) > 11 and 'box drawings' in name:
                return False
            print(f"  Name {name}, Category {category}: {char}")
            return True

        # Change this condition to return True if
        # you want to remove emoji these characters:
        if any(keyword in name for keyword in [
            'emoji', 'pictogram', 'symbol', 'dingbat', 'arrow',
            'star', 'heart', 'face', 'hand', 'gesture', 'activity',
            'object', 'flag', 'sign', 'mark'
        ]):
            return False

        # Change this condition to return True if you want to
        # remove these specific Unicode blocks known for symbols/emoji:
        code = ord(char)
        if any(start <= code <= end for start, end in [
            (0x1F600, 0x1F64F),  # Emoticons
            (0x1F300, 0x1F5FF),  # Misc Symbols and Pictographs
            (0x1F680, 0x1F6FF),  # Transport and Map
            (0x1F1E0, 0x1F1FF),  # Regional indicator symbols
            (0x2600, 0x26FF),    # Misc symbols
            (0x2700, 0x27BF),    # Dingbats
            (0x1f926, 0x1f937),  # Gestures
            (0x1F918, 0x1F91F),  # Hand symbols
            (0x1F980, 0x1F9FF),  # Supplemental Symbols and Pictographs
            (0x2B00, 0x2BFF),    # Misc Symbols and Arrows
        ]):
            return False
            

        return False

    except (ValueError, TypeError):
        return False


def remove_pictograms_from_file(filepath, dry_run=False):
    """
    Remove pictograms from a single file.

    Args:
        filepath (str): Path to the file
        dry_run (bool): If True, only show what would be changed

    Returns:
        tuple: (modified, original_chars, cleaned_chars)
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        original_chars = len(content)
        cleaned_content = ''.join(char for char in content if not is_pictogram(char))
        cleaned_chars = len(cleaned_content)

        if original_chars != cleaned_chars:
            if dry_run:
                print(f"Would modify ^^^: {filepath} ({original_chars - cleaned_chars} pictograms removed)")
            else:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                print(f"Modified: {filepath} ({original_chars - cleaned_chars} pictograms removed)")
            return True, original_chars, cleaned_chars
        else:
            return False, original_chars, cleaned_chars

    except (IOError, OSError) as e:
        print(f"Error processing {filepath}: {e}")
        return False, 0, 0


def main():
    parser = argparse.ArgumentParser(
        description='Remove pictograms from file(s)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s *.txt
  %(prog)s docs/*.md src/**/*.js
  %(prog)s --dry-run *.txt
        """
    )
    parser.add_argument(
        'paths',
        nargs='+',
        help='File path patterns (supports wildcards)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed output'
    )

    args = parser.parse_args()

    total_files_processed = 0
    total_files_modified = 0
    total_chars_removed = 0

    for pattern in args.paths:
        # Expand glob patterns
        matches = glob.glob(pattern, recursive=True)

        if not matches:
            print(f"No files found matching: {pattern}")
            continue

        for filepath in matches:
            if os.path.isfile(filepath):
                total_files_processed += 1
                modified, original, cleaned = remove_pictograms_from_file(filepath, args.dry_run)

                if modified:
                    total_files_modified += 1
                    total_chars_removed += (original - cleaned)
                    print(f"{total_files_processed}. {original - cleaned} pictograms found in: {filepath}")
 
                if args.verbose and not modified:
                    print(f"{total_files_processed}. No pictograms found in: {filepath}")
            elif args.verbose:
                print(f"Skipping directory: {filepath}")

    # Summary
    print(f"\nSummary:")
    print(f"Files processed: {total_files_processed}")
    if not args.dry_run:
        print(f"Files modified: {total_files_modified}")
    else:
        print(f"Files that would be modified: {total_files_modified}")
    print(f"Pictograms removed: {total_chars_removed}")


if __name__ == '__main__':
    main()

