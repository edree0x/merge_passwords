import csv
import json
import os
import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet

# إنشاء مفتاح التشفير
KEY_FILE = "encryption.key"
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as kf:
        kf.write(key)
else:
    with open(KEY_FILE, 'rb') as kf:
        key = kf.read()
cipher = Fernet(key)

def encrypt_data(data):
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(data):
    return cipher.decrypt(data.encode()).decode()

def read_csv(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames

def read_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data, list(data[0].keys()) if data else []

def read_txt(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    data = [{"Account": line.strip()} for line in lines]
    return data, ["Account"]

def merge_files(file_list, output_file):
    all_data = []
    header_set = set()
    seen_accounts = set()

    for file_name in file_list:
        ext = file_name.split('.')[-1].lower()
        if ext == "csv":
            data, headers = read_csv(file_name)
        elif ext == "json":
            data, headers = read_json(file_name)
        elif ext == "txt":
            data, headers = read_txt(file_name)
        else:
            print(f"Unsupported file type: {file_name}")
            continue

        header_set.update(headers)

        for row in data:
            key_field = row.get("Email") or row.get("Username") or row.get("Account", "")
            if key_field and key_field not in seen_accounts:
                seen_accounts.add(key_field)
                all_data.append(row)

    headers = list(header_set)

    # كتابة البيانات مع التعامل مع الفراغات
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in all_data:
            writer.writerow({k: encrypt_data(row.get(k, "N/A")) for k in headers})

    print(f"File merged and encrypted: {output_file}")

# واجهة رسومية لاختيار الملفات
def select_files():
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(title="Select password files", filetypes=[("CSV files", "*.csv"), ("JSON files", "*.json"), ("TXT files", "*.txt")])
    if files:
        output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if output_file:
            merge_files(files, output_file)

if __name__ == '__main__':
    select_files()
