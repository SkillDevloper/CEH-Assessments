# 🛡️ CEH v13 – Week 08: Static Malware Analysis & File Type Identification

This week, I focused on **static malware analysis**, analyzing malicious file characteristics **without execution**, to safely understand file behavior, structure, and potential impact.

---

## 🔧 Tools & Techniques

### File Type Detection
- `file` (Linux)
- Hex editors (HxD)
- PEStudio (Windows)
- ExifTool, Binwalk

### Embedded String Extraction
- `strings` command
- Ghidra / CFF Explorer
- Floss (for obfuscated strings)
- Manual Hex inspection

---

## 🔍 File Signatures & Formats

| File Type                   | Hex Signature        |
|----------------------------|----------------------|
| Windows EXE/DLL/SYS (PE)   | `4D 5A (MZ)`         |
| PDF                        | `%PDF`               |
| ZIP / DOCX / PPTX / XLSX   | `PK.. (50 4B 03 04)` |
| RAR                        | `Rar! (52 61 72 21)` |
| JPEG                       | `FF D8 FF E0`        |
| PNG                        | `‰PNG (89 50 4E 47)` |
| ELF (Linux)                | `7F 45 4C 46`        |
| ISO                        | `CD001`              |

---

## 📄 Sample Analysis Results

- **Sample-Lab-3-1-6 (OBJ)**  
  Strings like `.drectve`, `Microsoft (R) Optimizing Compiler`, `C:\cygwin\home...`, `_printf`  

- **Sample-Lab-3-1-9 (DOCX)**  
  Strings in XML metadata: `[Content_Types].xml`, `word/document.xml`, file paths  

- **Sample-Lab-3-1-8 (HTML)**  
  Clear text strings: `<html>`, `<h1>Hello Malwares</h1>`

- Excel & PowerPoint samples include `[Content_Types].xml` and `/ppt/slides/slide1.xml` components.

---

## 🚀 Takeaways

- Static analysis reveals malware fingerprints **without running dangerous code**  
- File signatures & embedded strings give clues about build tools, paths, and payload intent  
- A critical first stage before moving to dynamic or behavior-based analysis

---

## 📂 Resources

- `file` command, Hex editors (HxD)
- **Ghidra**, **CFF Explorer**, **Floss**
- **PEStudio**, **ExifTool**, **Binwalk**

---

## 🧰 Tools Used

| Tool          | Purpose                          |
|---------------|----------------------------------|
| `file`        | File type detection              |
| `strings`     | Extract readable strings         |
| **HxD**       | Manual hex + header analysis     |
| **PEStudio**  | PE structure + metadata review   |
| **Floss**     | Obfuscated string extraction     |
| **Ghidra**    | Deep binary dissection           |
| **CFF Explorer** | EXE/DLL static inspection     |

---

## ⚠️ Disclaimer

This analysis was performed in a **safe lab environment** for educational purposes as part of the CEH v13 curriculum.  
Do not apply these techniques to unknown or illegal malware samples.

