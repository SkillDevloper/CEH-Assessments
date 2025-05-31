# 🧪 Week 03 – Network Scanning & Nmap Lab (CEH v13)

## 📘 Conceptual Learning:

### 🔹 Q1. Terminologies
- **Socket:** IP + Port combo (e.g., 192.168.1.1:80), endpoint of communication.
- **Port:** Logical number identifying service (e.g., 80 for HTTP).
- **Protocol:** Rules of communication like TCP, UDP, HTTP, FTP.

### 🔹 Q2. Objectives of Network Scanning:
1. Discover Live Hosts
2. Detect Open Ports
3. Identify Running Services
4. OS Fingerprinting
5. Find Vulnerabilities
6. Build Network Map

---

## 🔬 Lab Work:

### ✅ Q3: Host Discovery using Nmap (`150.1.7.0/24`)
- **ARP Ping Scan**  
![ARP Scan](https://github.com/SkillDevloper/CEH-Assessments/blob/main/CEH-Assessments-Week-03/screenshots/Screenshot%202025-04-06%20122706.png?raw=true)

- **UDP Ping Scan**  
![UDP Scan](https://github.com/SkillDevloper/CEH-Assessments/blob/main/CEH-Assessments-Week-03/screenshots/Screenshot%202025-04-06%20123119.png?raw=true)

- **ICMP Echo Ping Sweep**  
![ICMP Scan](https://github.com/SkillDevloper/CEH-Assessments/blob/main/CEH-Assessments-Week-03/screenshots/Screenshot%202025-04-06%20123500.png?raw=true)

---

### ✅ Q4: Port Scanning (with Host Discovery Disabled)

- **Metasploitable Linux – Port + Version Scan**  
![Linux Ports](https://github.com/SkillDevloper/CEH-Assessments/blob/main/CEH-Assessments-Week-03/screenshots/Screenshot%202025-04-06%20125445.png?raw=true)

- **Windows 10 – Port + Version Scan**  
![Windows Ports](https://github.com/SkillDevloper/CEH-Assessments/blob/main/CEH-Assessments-Week-03/screenshots/Screenshot%202025-04-06%20134416.png?raw=true)

---

## 📌 Tools Used:
- **Nmap**: For scanning hosts, ports, and services.
- **VirtualBox / VMware**: Lab simulation with Kali, Metasploitable, Windows 10.

> 🔐 This content is for **educational purposes only**.
