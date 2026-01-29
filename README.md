# pictowhack - Remove Pictograms Utility

Get those annoying little pics OUT of your files and logs statements ... ; )
 
This directory contains a python utility for removing pictograms (emoji, symbols, and Unicode pictographic characters) from files:

## Files

- `pictowhack.py` - Python script (recommended)
- `test-pictograms.txt` - Test file with 135 pictograms
- `test-pictograms.txt` - Backup used to replace whack'd test file
- `restore-test.sh` - shell script to restore whack'd test file

## Usage

### Python Script (Recommended)

```bash
# Make executable (first time only)
chmod +x pictowhack.py

# Always do 'verbose' dry run to see will be changed
python3 pictowhack.py -v --dry-run "*.txt"

# Display verbose output 
python3 pictowhack.py --verbose "*.txt"

# Use a path spec, to remove pictograms in specified path
python3 pictowhack.py "*.txt" "docs/*.md"

```

## Results

The Python script is char-code, unicode accurate:
- Uses `unicodedata` module for precise Unicode character classification
- Checks Unicode categories (So, Sk) and names containing keywords
- Covers specific Unicode blocks for emoji and symbols
- Conservative and accurate detection which can be viewed before changing
- Supports wildcards and recursive patterns

## Examples

```bash
# Remove pictograms from all text files
python3 pictowhack.py "*.txt"

# Remove from markdown files in docs/
python3 pictowhack.py "docs/*.md"

# Remove from nested directories
python3 pictowhack.py "src/**/*.js"

# Dry run first to see what would change
python3 pictowhack.py --dry-run "*.txt"
```

## Requirements

### Python Script
- Python 3.6+
- imports should be part of standard python libs
- No additional dependencies

## Recommended
- This script makes irreversible text file changes, so always backup files or preview execute in `--dry-run` mode until satisfied.  
- Check all the files impacted, to ensure NO unexpected files can be mistakenly targeted by your pathspec !
- The script only removes, and does not replace pictograms.  If you have files logging a lone pictogram for any reason (e.g. log.success(`✅`)), you should consider adapting this script to replace certain chars.
