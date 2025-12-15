# Insert invisible unicode characters after each letter in an input text

This tool inserts random invisible unicode characters after each character of an input text.

## Usage

```python
usage: unitrick.py [-h] [-i INPUT_FILE] [-s INPUT_TEXT] [-n] [-o OUTPUT_TEXT]

Insert random invisible unicode characters after each character of an input text.

options:
  -h, --help            show this help message and exit

Encoding Arguments:
  -i, --input-file INPUT_FILE
                        Path to file containing the text.
  -s, --input-text INPUT_TEXT
                        Direct input of the text.
  -n, --invisible       Insert invisible chars.

Output Arguments (what to display):
  -o, --output-text OUTPUT_TEXT
                        Write result to file at output path.

Examples:
  ./unitrick.py -i input_file.txt -n
  ./unitrick.py -s "The quick brown fox jumps over the lazy dog." -n

  ./unitrick.py -i input_file.txt -n -o output_file.txt
  ./unitrick.py -s "The quick brown fox jumps over the lazy dog." -n -o output_file.txt
  ```
