import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import re
import magic  # pip install python-magic-bin
import os
import hashlib

# Function to get the file type based on magic signature
def get_file_type(filepath):
    try:
        return magic.from_file(filepath)
    except Exception as e:
        return f"Error: {str(e)}"

# Function to get MIME type of the file
def get_mime_type(filepath):
    try:
        return magic.Magic(mime=True).from_file(filepath)
    except Exception as e:
        return f"Error: {str(e)}"

# Function to get the file extension
def get_file_extension(filepath):
    ext = os.path.splitext(filepath)[1]
    return ext if ext else "No extension"

# Function to generate MD5 and SHA256 hashes of the file
def generate_hashes(filepath):
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()
    
    try:
        with open(filepath, "rb") as f:
            # Read file in chunks to avoid large file memory issues
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
                sha256_hash.update(byte_block)
                
        return md5_hash.hexdigest(), sha256_hash.hexdigest()
    
    except Exception as e:
        return f"Error generating hashes: {str(e)}"

# Function to extract ASCII strings from the file
def extract_ascii_strings(filepath):
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
            strings = re.findall(rb"[ -~]{4,}", data)
            return [s.decode(errors='ignore') for s in strings]
    except Exception as e:
        return [f"Error extracting strings: {str(e)}"]

# Function to detect suspicious strings in the file's content
def detect_suspicious_strings(strings):
    suspicious_keywords = [
        "http", "https", "powershell", "cmd.exe", "CreateProcess",
        "socket", "ftp", "regedit", "GetProcAddress", "filezilla", "token"
    ]
    
    suspicious = []
    for s in strings:
        for keyword in suspicious_keywords:
            if keyword.lower() in s.lower():
                suspicious.append(s)
                break
    return suspicious

# Main function for analyzing the file
def analyze_file():
    filepath = filedialog.askopenfilename(title="Select File", filetypes=[("All Files", "*.*")])
    if not filepath:
        return

    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, f"ðŸ“ Static Malware Analysis Report\n")
    result_text.insert(tk.END, f"{'-'*60}\n")
    result_text.insert(tk.END, f"ðŸ“‚ File Path        : {filepath}\n")
    result_text.insert(tk.END, f"ðŸ“„ File Name        : {os.path.basename(filepath)}\n")
    result_text.insert(tk.END, f"ðŸ“ File Extension   : {get_file_extension(filepath)}\n\n")

    # Get file type, MIME type, and hashes
    file_type = get_file_type(filepath)
    mime_type = get_mime_type(filepath)
    md5_hash, sha256_hash = generate_hashes(filepath)
    
    result_text.insert(tk.END, f"[+] Detected File Type : {file_type}\n")
    result_text.insert(tk.END, f"[+] MIME Type           : {mime_type}\n\n")
    result_text.insert(tk.END, f"[+] MD5 Hash            : {md5_hash}\n")
    result_text.insert(tk.END, f"[+] SHA256 Hash         : {sha256_hash}\n\n")

    # Extract embedded ASCII strings
    result_text.insert(tk.END, f"[+] Extracting Embedded ASCII Strings...\n")
    strings = extract_ascii_strings(filepath)
    result_text.insert(tk.END, f"    Total Strings Found: {len(strings)}\n\n")

    if strings:
        result_text.insert(tk.END, f"[+] First 20 Strings:\n")
        for s in strings[:20]:
            result_text.insert(tk.END, f"    {s}\n")
    else:
        result_text.insert(tk.END, "    No strings could be extracted.\n")

    # Detect suspicious strings
    suspicious = detect_suspicious_strings(strings)
    if suspicious:
        result_text.insert(tk.END, f"\n[+] Suspicious Strings Detected:\n")
        for s in suspicious:
            result_text.insert(tk.END, f"    {s}\n")
    else:
        result_text.insert(tk.END, "\n    No suspicious strings detected.\n")

    # Export the result to .txt file
    def export_results():
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if save_path:
            with open(save_path, 'w') as f:
                f.write(result_text.get('1.0', tk.END))
            messagebox.showinfo("Export Successful", f"Results saved to: {save_path}")
    
    export_button.config(state=tk.NORMAL, command=export_results)

# GUI Setup
root = tk.Tk()
root.title("Static Malware Analyzer (Professional Edition)")
root.geometry("1000x700")

frame = tk.Frame(root)
frame.pack(pady=10)

analyze_btn = tk.Button(
    frame, text="ðŸ” Select Malware File", command=analyze_file,
    font=("Arial", 12, "bold")
)
analyze_btn.pack(pady=5)

export_button = tk.Button(
    frame, text="ðŸ’¾ Export Results", state=tk.DISABLED,
    font=("Arial", 12, "bold")
)
export_button.pack(pady=5)

result_text = scrolledtext.ScrolledText(
    root, width=110, height=30, font=("Consolas", 10)
)
result_text.pack(pady=10)

root.mainloop()