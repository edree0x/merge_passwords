# merge_passwords
# Password Manager Merger

## Overview
This Python script merges password files from different platforms (e.g., LastPass, Samsung Pass) into a single encrypted CSV file. It supports CSV, JSON, and TXT formats and removes duplicate entries.

## Features
- **Supports multiple file formats**: CSV, JSON, and TXT.
- **Removes duplicate accounts** based on email, username, or account name.
- **Encrypts the merged file** using `cryptography` for added security.
- **User-friendly interface**: Uses `Tkinter` for easy file selection.
- **Handles missing data** by filling empty fields with "N/A".

## Requirements
- Python 3.x
- Required libraries: `csv`, `json`, `tkinter`, `cryptography`
- Install dependencies using:
  ```sh
  pip install cryptography
  ```

## How to Use
1. Run the script:
   ```sh
   python merge_passwords.py
   ```
2. A file selection window will appear. Choose the password files to merge.
3. Select the output file location.
4. The merged and encrypted CSV file will be saved.

## Decrypting Data
The script generates an encryption key stored in `encryption.key`. Use the same key to decrypt data when needed.

## Future Improvements
- Add support for XML format.
- Implement a CLI version with arguments for automation.
- Include an option for exporting data in JSON format.

## Disclaimer
This script is for personal use only. Ensure you store your encryption key securely, as losing it will make decryption impossible.

