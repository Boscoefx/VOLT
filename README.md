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

- 🚀 **Automated vulnerability scanning** – Quickly identify security flawsd text displaying important legal warnings about:
  - Educational and authorized security testing only
  - Must have explicit permission to test
  - Unauthorized scanning may be illegal
  - Full responsibility acknowledgment
  - User accepts all risks and consequences
  - Software provided "AS IS" without warranty
  - Call to use responsibly and ethically

This is the **startup/welcome screen** that users see when they first run `python volt.py`. It establishes the tool's identity and critically displays the legal disclaimer before any scanning begins.

---

Now let me update your README.md with this actual screenshot:
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
- 🧪Perfect! Here's the description of **Image 1 - VOLT Terminal Startup Screen**:

## 📸 Image 1 Description:

This screenshot shows the **VOLT Web Vulnerability Scanner** application running in a terminal on macOS. Here's what's visible:

### 🔴 Key Elements:

1. **Terminal Header**
   - User: `kali@kali`
   - Location: `~/VOLT` directory
   - Command executed: `python volt.py`

2. **VOLT Banner** (Large Red ASCII Art)
   - Displays the project name "VOLT" in prominent red text
   - Creates an Scan type

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

*VOLT initializes with its signature ASCII logo and displays legal disclaimer on startup. Shows version information (v1.00), author credit ( impressive visual impact when the tool starts

3. **Tool Information**
   ```
   VOLT Web Vulnerability Scanner
   Version      : v1.00
   Author       : Bosco
   ```

4. **Legal Disclaimer Section** (Red Text)
   - `[!] LEGAL DISCLAIMER` header
   - Emphasizes that VOLT is for **EDUCATIONAL and AUTHORIZED SECURITY TESTING only**
   - Clear warnings about:
     - Only using on owned systems or with explicit permission
     - Unauthorized scanning being illegal
     - User accepts full responsibility
     - Risks and consequences on the user
     - Software provided "AS IS" without warranty
   - Final line: **"Use responsibly and ethically"**

### 💻 Visual Design:
- Dark terminal background (black)
- Red text for branding and warnings (high visibility)
- Clean, professional layout
- Important legal information displayed prominently on startup
- Repository structure visible in the tab bar showing: `config.py`, `core`, `modules`, `__pycache__`, `report.txt`, `requirements.txt`, `volt.py`

This is an **excellent startup screen** that immediately establishes the tool's purpose, shows professionalism, and ensures users are aware of legal and ethical requirements before using the scanner! 🔒

---

Would you like me to add this screenshot to your README.md with a proper description?
