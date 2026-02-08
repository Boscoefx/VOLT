import os
from datetime import datetime


class Report:

    def __init__(self):
        os.makedirs("reports", exist_ok=True)

        self.txt = open("reports/report.txt", "w", encoding="utf-8")
        self.html = open("reports/report.html", "w", encoding="utf-8")

        self.findings = []

        self.counts = {
            "CRITICAL": 0,
            "HIGH": 0,
            "MEDIUM": 0,
            "LOW": 0,
            "INFO": 0
        }

        self._init_html()

    # ---------- HEADER ----------
    def _init_html(self):
        self.html.write(f"""
<html>
<head>
<title>VOLT Professional Security Report</title>

<style>
body {{
    font-family: Arial, Helvetica, sans-serif;
    margin: 30px;
    background-color: #f4f6f9;
}}

.header {{
    background: #1e3a8a;
    color: white;
    padding: 20px;
    border-radius: 8px;
}}

.section {{
    background: white;
    padding: 15px;
    margin-top: 15px;
    border-radius: 8px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
}}

th, td {{
    padding: 10px;
    border: 1px solid #ccc;
}}

th {{
    background: #2563eb;
    color: white;
}}

.badge {{
    padding: 5px 10px;
    border-radius: 5px;
    color: white;
}}

.badge-critical {{ background: darkred; }}
.badge-high {{ background: red; }}
.badge-medium {{ background: orange; }}
.badge-low {{ background: green; }}
.badge-info {{ background: blue; }}

.footer {{
    margin-top: 20px;
    padding: 15px;
    background: white;
    border-radius: 8px;
    text-align: center;
}}

.social-icons img {{
    width: 32px;
    margin: 10px;
}}

</style>

</head>

<body>

<div class="header">
    <h1>VOLT Security Assessment Report</h1>
    <p>Scan Date: {datetime.now()}</p>
</div>

<div class="section">
<h2>Severity Overview</h2>

<table>
<tr>
    <th>Severity</th>
    <th>Count</th>
</tr>
""")

    # ---------- WRITE FINDINGS ----------
    def write(self, message):

        self.txt.write(message + "\n")
        self.txt.flush()

        severity = "INFO"

        if "[CRITICAL]" in message:
            severity = "CRITICAL"
            self.counts["CRITICAL"] += 1

        elif "[HIGH]" in message:
            severity = "HIGH"
            self.counts["HIGH"] += 1

        elif "[MEDIUM]" in message:
            severity = "MEDIUM"
            self.counts["MEDIUM"] += 1

        elif "[LOW]" in message:
            severity = "LOW"
            self.counts["LOW"] += 1

        elif "[INFO]" in message:
            severity = "INFO"
            self.counts["INFO"] += 1

        print(message)

        self.findings.append((severity, message))

    # ---------- CLOSE REPORT ----------
    def close(self):

        # Severity Summary
        self.html.write(f"""
<tr><td>CRITICAL</td><td>{self.counts["CRITICAL"]}</td></tr>
<tr><td>HIGH</td><td>{self.counts["HIGH"]}</td></tr>
<tr><td>MEDIUM</td><td>{self.counts["MEDIUM"]}</td></tr>
<tr><td>LOW</td><td>{self.counts["LOW"]}</td></tr>
<tr><td>INFO</td><td>{self.counts["INFO"]}</td></tr>
</table>
</div>

<div class="section">
<h2>Detailed Findings</h2>

<table>
<tr>
    <th>Severity</th>
    <th>Description</th>
    <th>Recommendation</th>
</tr>
""")

        for severity, message in self.findings:

            css = severity.lower()

            recommendation = "Review and remediate according to OWASP best practices."

            if severity == "CRITICAL":
                recommendation = "Immediate action required. Critical security risk."

            if severity == "HIGH":
                recommendation = "Urgent fix recommended to prevent exploitation."

            if severity == "MEDIUM":
                recommendation = "Investigate and apply security improvements."

            if severity == "LOW":
                recommendation = "Configuration improvement recommended."

            if severity == "INFO":
                recommendation = "Informational only."

            self.html.write(f"""
<tr>
    <td><span class="badge badge-{css}">{severity}</span></td>
    <td>{message}</td>
    <td>{recommendation}</td>
</tr>
""")

        # ---------- FOOTER WITH LOGOS ----------
        self.html.write(f"""
</table>
</div>

<div class="footer">
    <h3>Developed By: Bosco</h3>

    <div class="social-icons">

        <a href="https://github.com/Boscoefx" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
        </a>

        <a href="https://www.linkedin.com/in/naseeb-kanjirakkadan?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
        </a>

    </div>

    <p>VOLT Scanner v1.00 | Report Generated: {datetime.now()}</p>

    <p style="font-size:12px;color:gray;">
    This report is generated automatically and should be manually verified
    by a security professional before remediation actions are taken.
    </p>

</div>

</body>
</html>
""")

        self.txt.close()
        self.html.close()

