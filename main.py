import argparse
import re

parser = argparse.ArgumentParser(
    description="Replace commas, parentheses, colons, and semicolons with em dashes."
)

parser.add_argument("input_file", help="Path to the input text file")
parser.add_argument("output_file", help="Path to save the modified text file")

args = parser.parse_args()

with open(args.input_file, "r", encoding="utf-8") as f:
    text = f.read()

# If a closing parenthesis comes at the end of a sentence,
# remove it instead of turning it into an em dash.
text = re.sub(r"\s*\)(?=[.!?])", "", text)

# Replace remaining commas, parentheses, colons, and semicolons,
# along with surrounding spaces, with a single em dash.
text = re.sub(r"\s*[,():;]+\s*", "—", text)

with open(args.output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Saved modified file to: {args.output_file}")
