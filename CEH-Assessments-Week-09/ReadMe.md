
# CEH v13 – Assessment #9: Steganography Lab

This repository contains my Week 9 Cybersecurity assessment focused on **Steganography techniques** used to hide and extract secret data from different media formats.

![Steganography](https://th.bing.com/th/id/R.0c5997f4e7175af8642b7859cbd04f43?rik=qrMrTY8qHrIYKg&pid=ImgRaw&r=0)

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

#### Kali Linux Steghide Tool
![Kali Linux Steghide Tool.png](https://github.com/SkillDevloper/CEH-Assessments/blob/main/CEH-Assessments-Week-09/screenshots/Kali%20Linux%20(Steghide%20Tool).png?raw=true)

#### unhide massage.txt file in video audio using DeepSound or OpenPuff
![unhide massage.txt file in video audio using DeepSound or OpenPuff](https://github.com/SkillDevloper/CEH-Assessments/blob/main/CEH-Assessments-Week-09/screenshots/Windows%20(unhide%20massage.txt%20file%20in%20video%20audio%20using%20DeepSound%20or%20OpenPuff).png?raw=true)
