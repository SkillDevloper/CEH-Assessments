# Week 2 – OSINT & IoT Device Discovery

## 📘 Part 1: Conceptual

### Q1: Define following terminologies:

- **Confidentiality**: Ensuring that data is accessible only to authorized individuals and protected from unauthorized access.
- **Integrity**: Maintaining the accuracy and reliability of data by preventing unauthorized modifications or corruption.
- **Authentication**: The process of verifying the identity of users, devices, or systems before granting access.

---

### Q2: CEH Methodology Flow Diagram Explanation

This diagram represents the System Hacking Process in ethical hacking. It includes:

1. **Footprinting** – Gathering publicly available information
2. **Scanning** – Identifying vulnerabilities and open ports
3. **Enumeration** – Extracting system details (usernames, shares)
4. **Vulnerability Analysis** – Analyzing for possible exploitation

Then starts the system hacking process:

- **Gaining Access** – Exploit vulnerabilities
- **Privilege Escalation** – Gain root/admin rights
- **Maintaining Access** – Install backdoors
- **Clearing Logs** – Remove evidence

---

## 🧪 Part 2: Lab

### 🔍 OSINT Investigation on Tesla

| Category | Details | Tools |
|---|---|---|
| Company Name | Tesla, Inc. | WHOIS, Official site |
| Products | EVs (Model S, X, 3, Y), Energy, Software | Tech News |
| Scope | AI, Autopilot, Charging Infra | Business reports |
| Website | www.tesla.com | nslookup, whois |
| IP | 23.195.108.48 | nslookup |
| Location | USA (37.7510, -97.8220) | ipinfo.io |
| Hosting | Akamai CDN (USA) | whois, Shodan |
| Tech Stack | AkamaiGHost, ReactJS, Cloudflare | Wappalyzer |
| WAF | Akamai, Cloudflare | wafw00f |
| Subdomains | shop.tesla.com, energy.tesla.com | Amass, crt.sh |

---

### 🛰️ Shodan Search Results (IoT Devices)

| Device Type | Shodan Query | Description |
|-------------|--------------|-------------|
| Yawcam | "Yawcam" country:US | Webcam feeds |
| HP Printers | "HP Printer" port:9100 | Exposed printer |
| Apple AirPlay | "AirPlay" port:7000 | Audio receivers |
| FTP Servers | "220 Anonymous FTP" | Public file servers |

🔧 **Tools Used**:
- WHOIS, nslookup
- ipinfo.io
- BuiltWith, Wappalyzer
- WAFW00F, Amass
- crt.sh
- Shodan.io, Censys.io

---

### 📸 Screenshots:

(Screenshots of Shodan queries are stored inside the `screenshots/` folder)

---

### 📌 Conclusion

- Tesla’s public digital footprint is secure but reveals a lot of tech stack & infrastructure data.
- Several IoT devices around the world are publicly accessible — webcams, printers, and smart home devices.
- OSINT + Shodan can reveal critical exposure which may be used in cyberattacks if not protected.

---

## ⚠️ Disclaimer

**This content is for educational purposes only.**  
All techniques shown are intended for ethical research and learning purposes only.
