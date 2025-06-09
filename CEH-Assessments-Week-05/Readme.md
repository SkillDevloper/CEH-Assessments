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
```
---
## Screenshorts:
### VMware Setting to Install Eve ISO
![VMware Setting to Install Eve ISO.png](https://github.com/SkillDevloper/CEH-Assessments/blob/main/CEH-Assessments-Week-05/screenshots/VMware%20Setting%20to%20Install%20Eve%20ISO.png?raw=true)

### Assign IP or Subnet to VM network adapter IPV4
![Assign IP or Subnet to VM network adapter IPV4.png](https://github.com/SkillDevloper/CEH-Assessments/blob/main/CEH-Assessments-Week-05/screenshots/Assign%20IP%20or%20Subnet%20to%20VM%20network%20adapter%20IPV4.png?raw=true)

### Adding Paths in Winscp
![Adding Paths in Winscp.png](https://github.com/SkillDevloper/CEH-Assessments/blob/main/CEH-Assessments-Week-05/screenshots/Adding%20Paths%20in%20Winscp.png?raw=true)

### Lab Structure
![Structure.png](https://github.com/SkillDevloper/CEH-Assessments/blob/main/CEH-Assessments-Week-05/screenshots/Structure.png?raw=true)

#### You can see more images by going to the [Screenshots folder](https://github.com/SkillDevloper/CEH-Assessments/tree/main/CEH-Assessments-Week-05/screenshots).
