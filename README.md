# 🔍 VOLT – Web Vulnerability Scanner

VOLT is an automated web vulnerability scanner built in Python.  
It is designed to help security researchers, students, and penetration testers identify common security flaws in web applications and generate structured, professional reports.

---

## 🚀 Overview

VOLT performs automated scanning of web applications to detect vulnerabilities such as:

- SQL Injection  
- Cross-Site Scripting (XSS)  
- CSRF Issues  
- Open Redirects  
- Insecure HTTP Headers  
- Sensitive File Exposure  
- Directory Listing  
- IDOR (Insecure Direct Object References)  

The tool generates a detailed HTML report with severity classifications and remediation recommendations, similar to professional scanners like Nessus and Burp Suite.

---

## ✨ Key Features

✔ Automated website crawling  
✔ Detection of multiple vulnerability types  
✔ Severity-based classification  
✔ Professional HTML and text reports  
✔ Clear remediation guidance  
✔ Command-line interface  
✔ Fast and full scan modes  
✔ Beginner-friendly usage  

---

## 🛠 Installation

### Clone the repository

```bash
git clone https://github.com/Boscoefx/VOLT.git
cd VOLT


Install Dependencies
pip install -r requirements.txt

📌 Usage
Interactive Mode

Run the tool without arguments:

python volt.py


You will be prompted to enter:

Target URL

Scan mode (Full / Limited)

Command Line Mode

Full Scan

python volt.py -u http://example.com


Limited Scan

python volt.py -u http://example.com -l 20


Fast Scan

python volt.py -u http://example.com -f


Display Help Menu

python volt.py --help

📄 Reports

After each scan, VOLT automatically generates two reports:

reports/report.html – Professional formatted security report

reports/report.txt – Plain text findings

Report Includes

Severity overview table

Detailed findings list

Remediation recommendations

Clean structured layout

Clickable author credits

To view the report:

firefox reports/report.html

⚠ Legal Disclaimer

This tool is intended strictly for EDUCATIONAL and AUTHORIZED SECURITY TESTING purposes only.

Use this tool ONLY on systems and websites you own or have explicit permission to test.

Unauthorized scanning or testing may be illegal in your region.

The author and contributors are not responsible for any misuse, damage, or legal consequences caused by this tool.

Use ethically and responsibly.

👨‍💻 Author

Bosco

GitHub:
https://github.com/Boscoefx

LinkedIn:
https://www.linkedin.com/in/naseeb-kanjirakkadan

🧩 Technologies Used

Python

Requests

BeautifulSoup

Colorama

HTML / CSS Reporting

🔮 Future Enhancements

Planned upgrades for upcoming versions:

PDF export support

Pie chart analytics

CVSS scoring

Multi-threaded scanning

GUI interface

API integration

⭐ Support the Project

If you found this tool useful:

*Give the repository a ⭐ on GitHub

*Share it with others

*Contribute improvements

*Thank you for using VOLT!
