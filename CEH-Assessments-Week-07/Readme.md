
# 🧪 CEH v13 – Week 07: System Hacking Techniques & Password Cracking with John the Ripper

This week's focus was on understanding core system hacking techniques and applying **John the Ripper (JtR)** to crack SHA-256 hashed passwords using different modes.

---

## 🔐 Part 1: Conceptual Summary

### 🔸 Techniques for System Hacking:

| Technique                | Description |
|--------------------------|-------------|
| **Password Cracking**   | Gaining unauthorized access by recovering passwords via brute force, dictionary attacks, or rainbow tables. |
| **Vulnerability Exploitation** | Exploiting system/software flaws using automated tools to gain control or escalate privileges. |
| **Payload Usage**        | Injecting code (e.g., Meterpreter) to establish backdoors or manipulate systems post-exploit. |

### 🔸 Tools & Their Specializations:

| Tool          | Focus Area                                | Cracking Methods                       |
|---------------|--------------------------------------------|----------------------------------------|
| **John the Ripper** | Offline hash cracking                  | Brute force, dictionary, rule-based     |
| **Hydra**           | Network login brute-forcing            | Protocol-based (SSH, FTP, HTTP, etc.)  |
| **Hashcat**         | GPU-accelerated hash cracking          | Brute force, hybrid, dictionary attacks |

---

## 💻 Part 2: Practical Lab – John the Ripper (JtR)

### 🔹 Mode A: Single Crack Mode
- Uses known user information for intelligent guesses.

```bash
# Generate SHA-256 of password
echo -n 'Topgun' | sha256sum

# Save username:hash to file
echo -n 'topgun:4558ce5abe3b1e70bbadc3b95f2ff84f54d0a5c30fb524ceebfd401f8233fda7' > simple.txt

# Run JtR
john --single --format=raw-sha256 simple.txt
```

---

### 🔹 Mode B: Wordlist Mode
- Tests against common passwords from a wordlist like `rockyou.txt`.

```bash
# Generate hash
echo -n 'password1234' | sha256sum

# Save to file
echo user01:b9c950640e1b3740e98acb93e669c65766f6670dd1609ba91ff41052ba48c6f3 >> crack.txt

# Run JtR with wordlist (unzip rockyou.txt if needed)
john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha256 crack.txt
```

---

### 🔹 Mode C: Incremental Mode
- Performs full brute-force on all character combinations.

```bash
# Generate hash
echo -n 'passw0rd' | sha256sum

# Save to file
echo user02:8f0e2f76e22b43e2855189877e7dc1e1e7d98c226c95db247cd1d547928334a9 >> inc.txt

# Run JtR incrementally
john --incremental --format=raw-sha256 inc.txt
```

---

## 📌 Key Takeaways

- **John the Ripper** supports versatile modes for password cracking.
- Understanding hash algorithms (like SHA-256) is key to offline attacks.
- Each attack mode targets different use cases—single mode for targeted attacks, wordlist for real-world guesses, and incremental for full brute-force.

---

## 📂 Resources

All lab screenshots, hash outputs, and result logs are available in this folder:  
📁 [`CEH-Assessments-Week-07/`](./)

---

## ⚠️ Disclaimer

This project is created **strictly for educational purposes** under the CEH v13 training curriculum.  
All usernames, passwords, and targets used are simulated or lab-based.  
**Do not apply these techniques on unauthorized systems.**
