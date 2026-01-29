# pictowhack - whack annoying pictograms 

_Removes bot pics from your files and logs statements_
 
This is a simple python script to remove pictograms (emoji, 
symbols, and Unicode pictographic characters) from text files.
It assumes you have python3 (v3.6+) installed and command `python3`.

## Files

- `pictowhack.py` - Python script
- `test/test-pictograms.txt` - Test file with 135 pictograms
- `test/test-pictograms.txt` - Backup used to replace whack'd test file
- `test/restore-test.sh` - shell script to restore whack'd test file

## Usage

### Python Script (Recommended Usage)

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
- No additional dependencies (imports are standard python libs)

## Recommended
- *Backup or --dry-run* - This script makes irreversible text file changes, so always backup files in the pathspec, or preview the results in `--dry-run` mode until satisfied.  
- *Check your Pathspec* - This is designed for text files, but it will 'pictowhack' any file - including binary files - in the pathspec!  Check all the files impacted, to ensure NO unexpected files are mistakenly targeted by your pathspec !
- *Check Results* - The script only removes, and does not replace pictograms.  If you have files logging a lone pictogram for any reason (e.g. ```log.success(`✅`)```), you should consider adapting script to replace, rather than remove, certain chars.

