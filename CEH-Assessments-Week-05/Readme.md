# 🛰️ CEH v13 – Week 05: SNMP Enumeration & EVE-NG Lab

This week's assessment involved network device enumeration using **SNMP** protocol. We simulated a realistic Cisco router network inside **EVE-NG**, configured SNMP, and performed enumeration from Kali Linux using `nmap`.

---

## 🧪 Lab Objectives:

- Setup **Cisco Router** in EVE-NG
- Enable **SNMP (v2c)** with default community strings
- Ping router from Kali
- Enumerate router info using Nmap scripts
- Brute force SNMP strings using `snmp-brute`

---

## 🔧 Tools Used:
- EVE-NG (with Cisco IOL images)
- Kali Linux
- Nmap
- WinSCP (for IOL uploads)
- VMware (for local lab environment)

---

### ✅ `SNMP_Enumeration_Lab.md`  
> Nmap scans used:
```bash
nmap -sU -p 161 150.1.7.103
nmap -sU -p 161 --script=snmp-brute 150.1.7.103
