<!--
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
 -->

# Compare 2 TXT Files

A Python script to compare multiple text files in an `input` directory against a master `source/source.txt` file and collect all unique missing lines into a single `output/output.txt`.

## Table of Contents

- [Compare 2 TXT Files](#compare-2-txt-files)
  - [Table of Contents](#table-of-contents)
  - [What is this script?](#what-is-this-script)
  - [Why use it?](#why-use-it)
  - [How it works](#how-it-works)
  - [How to use it](#how-to-use-it)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Project Structure](#project-structure)
    - [Execution](#execution)
    - [Example](#example)
  - [Use Case: VSCode Extension Comparison](#use-case-vscode-extension-comparison)

## What is this script?

This tool is a specialized text processor designed for line-by-line comparison across multiple files. It identifies "delta" content—lines that appear in your new input files but are missing from your established source reference.

## Why use it?

- **Data Deduplication:** Identify new entries in logs or lists that haven't been recorded yet.
- **Incremental Updates:** Easily find what has changed or been added across dozens of files without manual searching.
- **Clean Output:** Automatically strips whitespace and ignores empty lines to ensure the output contains only high-quality data.

## How it works

1. **Reference Loading:** The script reads `./source/source.txt` and loads every unique line into a high-performance memory set.
2. **Input Scanning:** it scans the `./input/` directory for any file ending in `.txt`.
3. **Line-by-Line Comparison:** For every file found, it checks each line:
    - If the line (after trimming whitespace) does not exist in the source set, it is marked as "new".
4. **Consolidated Output:** All "new" lines are written sequentially into `./output/output.txt`.

## How to use it

### Prerequisites

- Python 3.x installed on your system.
- [uv](https://github.com/astral-sh/uv) installed on your system.

### Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   uv venv
   uv sync
   ```

### Project Structure

Ensure your folders are set up as follows:

```text
.
├── input/          # Place your new .txt files here
├── output/         # The results will be generated here
├── source/         # Contains source.txt (the master reference)
└── main.py         # The script
```

### Execution

1. Place your reference file in `source/source.txt`.
2. Place one or more text files you want to check in the `input/` folder.
3. Run the script from your terminal:

    ```bash
    ./start
    ```

4. Check `output/output.txt` for the results.

### Example

If `source.txt` contains:

```text
abc
def
```

And `input/1.txt` contains:

```text
abc
xyz
```

The resulting `output/output.txt` will contain:

```text
xyz
```

## Use Case: VSCode Extension Comparison

A great use case for this script is to compare Visual Studio Code extensions between different profiles. You can easily find out which extensions are installed in one profile but not in your default profile.

1. **Generate the default extension list:**

    ```bash
    code --profile "Default" --list-extensions > ./source/source.txt
    ```

2. **Generate the extension list for your other profile:**

    ```bash
    code --profile "Profile Name" --list-extensions > ./input/profile_name.extensions.txt
    ```

3. **Run the script:**

    ```bash
    ./start
    ```

4. The `output/output.txt` file will now contain a list of extensions that are in "Profile Name" but not in your "Default" profile.
