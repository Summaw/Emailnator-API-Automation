# Emailnator-API-Automation
Automate the creation and management of temporary email addresses using Emailnator with browser-level stealth and advanced inbox monitoring.
This Python toolkit leverages real browser fingerprinting (via `primp`) to bypass anti-bot protections, generate disposable emails, and fetch inbox messages—making it perfect for testing, automation, QA, and privacy-focused workflows.


🚀 Features
- Stealth Browser Emulation: Uses real browser fingerprints to avoid detection and bypass anti-bot systems.
- Automated Temp Mail Generation: Instantly create disposable email addresses for any use case.
- Inbox Monitoring: Programmatically fetch and process incoming messages.
- Colorful Console Output: All actions are logged with timestamps and color-coded status for easy monitoring.
- Modular & Extensible: Clean, reusable codebase for integration into your own projects.

📦 Installation

1) Clone the repository:
```bash
git clone https://github.com/Summaw/Emailnator-API-Automation.git
cd Emailnator-API-Automation/pypi
```

2) Install dependencies:
```bash
pip install -r requirements.txt
```


Your requirements.txt should include:
```text
requests
colorama
primp
```

🛠 Usage
Run the main script:
```bash
python main.py
```

# What happens:
- Fetches browser-like cookies from Emailnator.
- Generates a new temporary email address.
- Fetches messages for that email.
- Logs all steps to the console with color and timestamps.


🗂 Project Structure

```text
  GMAILNATOR/
  main.py
  modules/
    generateEmail.py
    getCookies.py
    getMessages.py
    write/
      write.py
```

📝 Example Output
```
[12:34:56] [INFO]    Starting...
[12:34:57] [SUCCESS] Cookies: eyJpdiI6IlZZMisrZWtFL0MzaVJzYTlaOG44cEE9PSIsInZhbHVl...
[12:34:58] [SUCCESS] Generated email: example.email@gmail.com
[12:34:59] [SUCCESS] Messages: [{'from': '...', 'subject': '...', ...}]
[12:35:00] [INFO]    Finished
```

💡 Extending
- Add new providers: Implement new modules for other temp mail services.
- Integrate with bots: Use the modular functions in your own automation scripts.

❓ Troubleshooting
- No cookies or errors?
- Make sure your network allows outbound HTTPS and you’re not being blocked by Cloudflare or similar services.
- primp not working?
- Ensure you’re using Python 3.8+ and the latest version of primp.

🙏 Credits
- primp for browser impersonation
- colorama for colored console output


### Get disposable emails. Beat anti-bot. Automate everything.
