"""
Copyright (C) 2026 BitsVital LLC

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os


def main():
    source_file = os.path.join("source", "source.txt")
    input_dir = "input"
    output_file = os.path.join("output", "output.txt")

    # Load source lines into a set for efficient lookup
    source_lines = set()
    if os.path.exists(source_file):
        with open(source_file, "r", encoding="utf-8") as f:
            for line in f:
                source_lines.add(line.strip())
    else:
        print(f"Warning: Source file {source_file} not found.")

    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    # Open output file for writing
    with open(output_file, "w", encoding="utf-8") as out_f:
        # Iterate through files in the input directory
        if os.path.exists(input_dir):
            # Sort files to process them in a consistent order
            files = sorted(os.listdir(input_dir))
            for filename in files:
                if filename.endswith(".txt"):
                    file_path = os.path.join(input_dir, filename)
                    with open(file_path, "r", encoding="utf-8") as in_f:
                        for line in in_f:
                            stripped_line = line.strip()
                            if stripped_line and stripped_line not in source_lines:
                                out_f.write(stripped_line + "\n")
        else:
            print(f"Warning: Input directory {input_dir} not found.")

    print("Processing complete. Check output/output.txt for results.")


if __name__ == "__main__":
    main()
