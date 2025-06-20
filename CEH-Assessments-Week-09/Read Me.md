
# CEH v13 – Assessment #9: Steganography Lab

This repository contains my Week 9 Cybersecurity assessment focused on **Steganography techniques** used to hide and extract secret data from different media formats.

![Steganography](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Steganography_illustration.png/800px-Steganography_illustration.png)

---

## 🔍 Part 1: Hiding Text in Images using Steghide & Stegosuite

### ✅ Steghide (Linux/Windows)
- Embed text:
  ```bash
  steghide embed -cf image.jpg -ef secret.txt
  ```
- Extract text:
  ```bash
  steghide extract -sf image.jpg
  ```

### ✅ Stegosuite (GUI Tool)
- Load image → Add secret text → Set passphrase → Save image
- Open same image → Enter passphrase → Extract text

---

## 💡 Part 2: WinRAR Steganography (Windows)

### 🔒 Hide secret text file
- Compress `secret.txt` to `secret.rar`
- Append to image:
  ```cmd
  copy /b image.jpg + secret.rar output.jpg
  ```
- To extract, rename `output.jpg` → `output.rar`

### ⚙️ Hide `.bat` file in image
- Compress `.bat` to `script.rar`
- Append to image → execute using `start output.jpg`

---

## 🎧 Part 3: Audio/Video Steganography

### 🟢 DeepSound (MP3 Audio)
- Embed secret into MP3 → Set encryption + password
- To extract, reopen in DeepSound and enter password

### 🔵 OpenPuff (MP4 Video)
- Select video carrier + secret files + passwords
- Save stego file → Reopen with same credentials to extract

---

## ⚠️ Disclaimer

**This lab is strictly for educational purposes.** Never use steganographic techniques for unauthorized or malicious activities.

---
