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
![ARP Scan](screenshots/arp-scan.png)

- **UDP Ping Scan**  
![UDP Scan](screenshots/udp-scan.png)

- **ICMP Echo Ping Sweep**  
![ICMP Scan](screenshots/icmp-scan.png)

---

### ✅ Q4: Port Scanning (with Host Discovery Disabled)

- **Metasploitable Linux – Port + Version Scan**  
![Linux Ports](screenshots/metasploitable-portscan.png)

- **Windows 10 – Port + Version Scan**  
![Windows Ports](screenshots/windows10-portscan.png)

---

## 📌 Tools Used:
- **Nmap**: For scanning hosts, ports, and services.
- **VirtualBox / VMware**: Lab simulation with Kali, Metasploitable, Windows 10.

> 🔐 This content is for **educational purposes only**.
