# 🚀 VOLT – Web Vulnerability Assessment Tool

## 🔎 Automated Web Security Scanner

VOLT is a fast, lightweight, and easy-to-use web vulnerability assessment tool built for security testers and ethical hackers to quickly analyze websites for common security issues.

---

## 📌 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Reports](#-reports)
- [Technologies Used](#-technologies-used)
- [Future Enhancements](#-future-enhancements)
- [Disclaimer](#-legal-disclaimer)
- [Author](#-author)
- [Support](#-support)

---

## 🔍 Features

- 🚀 **Automated vulnerability scanning** – Quickly identify security flaws
- 🎯 **Multiple scan modes** – Full, limited, and fast scanning options
- 🖥 **Interactive and CLI support** – Use via terminal or interactive mode
- 📊 **HTML and text reports** – Detailed scan results in multiple formats
- 🛡 **Security recommendations** – Get actionable fixes for vulnerabilities
- ⚡ **Lightweight and fast** – Minimal resource usage, quick scans
- 🌐 **Cross-platform compatible** – Works on Windows, macOS, and Linux

---

## 🛠 Installation

### 📥 Clone the Repository

```bash
git clone https://github.com/Boscoefx/VOLT.git
cd VOLT
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📌 Usage

Run VOLT directly from your terminal using Python.

### 🖱 Interactive Mode

Start the scanner without arguments:

```bash
python volt.py
```

You will be prompted for:
- 🌐 Target URL
- 🧪 Scan type

### 💻 Command Line Mode

#### 🔎 Full Scan

```bash
python volt.py -u http://example.com
```

#### 🎚 Limited Scan

```bash
python volt.py -u http://example.com -l 20
```

#### ⚡ Fast Scan

```bash
python volt.py -u http://example.com -f
```

#### ❓ Display Help

```bash
python volt.py --help
```

### 🧾 Command Line Help Menu

```
Usage:
  python volt.py [options]

Options:
  -u, --url        Target URL to scan
  -l, --limit      Limited scan mode with custom depth
  -f, --fast       Perform fast scan
  -h, --help       Show help menu

Examples:
  python volt.py -u http://example.com
  python volt.py -u http://example.com -l 20
  python volt.py -u http://example.com -f
```

---

## 🖼 Screenshots

### 🔴 VOLT Startup with Legal Disclaimer

![VOLT Terminal Startup](images/volt_startup.png)

*VOLT initializes with its signature ASCII logo and displays legal disclaimer on startup. Shows version information (v1.00), author credit (Bosco), and important security warnings.*

**Key Information Displayed:**
- ✅ Tool name and version
- ✅ Author attribution
- ✅ Legal disclaimer
- ✅ Usage restrictions
- ✅ Liability notice
- ✅ Ethical usage reminder

### 🔴 Interactive Mode Prompts

![VOLT Interactive Mode](images/volt_interactive.png)

*User-friendly interactive mode prompting for target URL and scan type selection.*

### 🔴 Scan Results Summary

![VOLT Scan Results](images/volt_results.png)

*Real-time vulnerability detection with severity levels and vulnerability counts.*

### 🔴 HTML Report Output

![VOLT HTML Report](images/volt_report.png)

*Professional HTML report with detailed vulnerability analysis, recommendations, and remediation steps.*

---

## 🗂 Reports

After each scan, VOLT automatically generates comprehensive reports:

| Format | Location | Description |
|--------|----------|-------------|
| 📝 HTML Report | `reports/report.html` | Interactive web-based report with full details |
| 📜 Text Report | `reports/report.txt` | Plain text format for logging and archiving |

### 📊 Reports Include

- 📈 **Severity overview** – High, medium, and low-risk vulnerabilities
- 🔬 **Vulnerability details** – In-depth information on each issue
- 🛠 **Fix recommendations** – Step-by-step solutions and remediation
- 🧾 **Clean layout** – Easy-to-read formatting and organization
- ⏱ **Scan duration** – Time taken to complete the scan
- 📅 **Scan timestamp** – When the scan was performed
- 🔗 **Affected URLs** – Links to vulnerable endpoints

### 👁 View Report

```bash
# View HTML report in your default browser
firefox reports/report.html
```

or

```bash
# View text report in terminal
cat reports/report.txt
```

---

## 🧩 Technologies Used

- 🐍 **Python 3.8+** – Core programming language
- 🌐 **Requests** – HTTP library for web requests
- 🥣 **BeautifulSoup4** – HTML/XML parsing and analysis
- 🎨 **Colorama** – Terminal color output for better visibility
- 📄 **HTML/CSS** – Professional report generation
- 🔒 **SSL/TLS** – Secure HTTPS connections

---

## 🔮 Future Enhancements

- 📑 **PDF export** – Generate PDF reports
- 📊 **Advanced analytics** – Charts and graphs for vulnerability trends
- 🧮 **CVSS scoring** – Industry-standard severity ratings
- ⚙ **Multi-threading** – Parallel scanning for faster results
- 🖼 **GUI interface** – Graphical user interface option
- 🔌 **REST API** – API integration support
- 🌍 **Proxy support** – Route scans through proxies
- 🔐 **Authentication** – Support for authenticated scanning
- 📱 **Mobile reporting** – Responsive report design

---

## ⚠ Legal Disclaimer

### 🚨 IMPORTANT – READ BEFORE USING

**VOLT is intended only for EDUCATIONAL and AUTHORIZED SECURITY TESTING.**

#### ✅ Allowed Uses

- Security testing on systems you own
- Authorized penetration testing with written permission
- Educational purposes in controlled environments
- Personal security research

#### 🚫 Prohibited Uses

- Unauthorized scanning or testing of third-party websites
- Illegal hacking or unauthorized access attempts
- Circumventing security measures without permission
- Using VOLT for malicious purposes

### ⚖ Legal Responsibility

- ✅ **You are fully responsible** for obeying all applicable cyber laws
- ✅ **Obtain written permission** before testing any system you don't own
- ✅ **Comply with** local, state, and federal regulations
- ✅ **Understand the consequences** of unauthorized testing

### ❗ Liability Disclaimer

The author and contributors are NOT responsible for:

- ❌ Illegal usage or misuse of this tool
- ❌ Data loss or corruption
- ❌ System damage or disruption
- ❌ Service interruption or downtime
- ❌ Legal consequences or prosecution
- ❌ Financial losses

🧠 **This tool is provided "AS IS" with no warranty, express or implied.**

🛡 **By using VOLT, you acknowledge and accept full responsibility for your actions and agree to act ethically and legally.**

---

## 👨‍💻 Author

**Bosco**

- 🐙 GitHub: [Boscoefx](https://github.com/Boscoefx)
- 💼 LinkedIn: [Naseeb Kanjirakkadan](https://www.linkedin.com/in/naseeb-kanjirakkadan)
- 📧 Email: [Contact via GitHub](https://github.com/Boscoefx)

---

## ⭐ Support & Contribution

### Show Your Support

If you find this project helpful:

- ⭐ **Star the repository** – Show your appreciation
- 🤝 **Contribute** – Submit pull requests with improvements
- 🐛 **Report bugs** – Open issues for any problems found
- 💡 **Suggest features** – Share your ideas for enhancement
- 📢 **Spread the word** – Tell others about VOLT

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Reporting Issues

When reporting bugs, please include:
- Description of the issue
- Steps to reproduce
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)

---

## 📝 Additional Resources

- 📖 [Documentation](https://github.com/Boscoefx/VOLT/wiki)
- 🆘 [FAQ](https://github.com/Boscoefx/VOLT/discussions)
- 🐛 [Report Issues](https://github.com/Boscoefx/VOLT/issues)
- 💬 [Discussions](https://github.com/Boscoefx/VOLT/discussions)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Thank You for Using VOLT!

**Happy scanning and stay secure! 🔒**

*Together, let's make the web a safer place.*

---

*Last Updated: February 8, 2026*

*Version: 1.0.0*
