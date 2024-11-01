# Bing Searches Automation Tool

![Made with Python](https://forthebadge.com/images/badges/made-with-python.svg)
![MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)

### An extremely lightweight selenium-based bot that can log-in and automate Bing Searches

### ⚠️ **Disclaimer**

This content is provided for **educational and testing purposes only**. Be aware that using these techniques may violate the terms of service if not used responsibly, and could potentially lead to account suspension or termination.

**Use responsibly and at your own risk**.  
*The author is not responsible for any consequences arising from misuse.*

## Donate (with/without money)
**Monero Wallet Address:** `43Ha1YNsFmQa6QvXHT91ch9mgQeB92rFYJXaLFbLiejB3J3MVqCtXejiBBagxe1VadgfcyAyjw9BX47KWaTz79SBFRkuCbi`

---

### Donations without money (CPU-Friendly and Free)

Interested in donating Monero (XMR) without spending your own money? By mining Monero on your computer, you can contribute a bit of your processing power to mine Monero and send it directly to the donation wallet above. Here's how:

### 🔽 1. Download & Install XMRig

1. **Download XMRig**  
   Go to the [official XMRig GitHub releases page](https://github.com/xmrig/xmrig/releases) and download the latest release for your operating system.  
   - For **Windows**: Download the `.zip` file (e.g., `xmrig-6.22.1-win64.zip`).
   - For **Linux**: Download the `.tar.gz` file (e.g., `xmrig-6.22.1-linux-x64.tar.gz`).

2. **Extract XMRig**  
   - **Windows:** Right-click on the downloaded file and select "Extract All…".
   - **Linux:** Use the following command: (Asuuming you downloaded `xmrig-6.22.1-linux-x64.tar.gz`)
     ```bash
     tar -xvf xmrig-6.22.1-linux-x64.tar.gz
     ```
    - Locate the folder with the extracted files.

3. **Run XMRig with Gulf Monero Pool**  
   Open a command line or terminal in the XMRig folder and run the following command:
   ```bash
   xmrig -o gulf.moneroocean.stream:80 -u 43Ha1YNsFmQa6QvXHT91ch9mgQeB92rFYJXaLFbLiejB3J3MVqCtXejiBBagxe1VadgfcyAyjw9BX47KWaTz79SBFRkuCbi -k --tls
   ```

   You can change the mining pool `gulf.moneroocean.stream:80` to any other pool of your choice.


Of course, you are welcome to donate directly using XMR if you want :)

---

## Installation

1. **Ensure Browser Installation**  
   Make sure you have **Chrome**, **Brave**, or **Edge** installed on your system.

2. **Install ChromeDriver (Optional)**  
   As of **Selenium 4.10.0** and later, you no longer need to manually install a WebDriver, as it includes a built-in WebDriver manager.  
   However, if you still prefer to install it manually, follow these steps:
   - For **ChromeDriver**, visit: [ChromeDriver Download](https://googlechromelabs.github.io/chrome-for-testing/)  
   - For **EdgeDriver**, visit (*Open in Microsoft Edge*): [EdgeDriver Download](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver?form=MA13LH&ch=1#downloads)

3. **Clone the Repository**  
   You can clone the repository using Git:  
   ```bash
   git clone https://github.com/RoyCoding8/BingSearcher.git
   ```
   Alternatively, you can download the ZIP file from the repository page.

4. **Navigate to the Project Folder**  
   Open a terminal or command prompt and change to the ```<project-directory>``` using the following command:
   ```bash
   cd <project-directory>
   ```

5. Run the script:
    ```bash
   python main.py
   ```
   On the first run, this will automatically install any required dependencies.

## Features
- Multi-account support
- Mobile searches support

## Future Features

- GUI
