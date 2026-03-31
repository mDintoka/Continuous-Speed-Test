# Continuous-Speed-Test

Continuous internet speed monitoring tool to detect real-world fluctuations and inconsistencies that typical speed tests often hide

# 🚀 Continuous Speed Test Tool

## 📌 Overview

This project is a **continuous internet speed testing tool** built to solve a common problem:

> Traditional speed tests often show **ideal speeds**, but real-world performance fluctuates.

This tool continuously monitors your internet speed over time, helping you detect:

* Speed drops
* Network instability
* Sudden fluctuations (jitter-like behavior)

For example:

* 1 minute → 20 Mbps
* Next minute → 10 Mbps

---

## ❗ Problem It Solves

Many online speed tests only measure performance for a few seconds, which can:

* Hide unstable connections
* Misrepresent actual usage experience

This tool provides a **more realistic picture** of your network performance.

---

## ⚙️ Features

* 🔄 Continuous speed testing
* 📉 Detects fluctuations over time
* 🧪 Useful for debugging unstable internet
* 💾 Automatically saves speed data

---

## 🛠️ Requirements

Make sure you have:

* Python installed
* `curl` (for downloading the script)

---

## 📥 Installation (Using curl in CMD)

### Step 1: Download the script

```bash
curl -O https://github.com/mDintoka/Continuous-Speed-Test.git
```

### Step 2: Run the script

```bash
python speed_test.py
```

---

## ▶️ Usage

Once you run the script, it will:

* Continuously test your internet speed
* Display results over time
* Help you observe fluctuations
* Save the results into files

---

## 💾 Data Storage

The tool automatically saves your speed results into two files:

* **speed_data_Mbps** → stores speed in Mbps
* **speed_data_kbps** → stores speed in Kbps

This allows you to:

* Analyze performance later
* Track speed changes over time
* Use the data for graphs or reports

---

## 📌 Example Output

```
[00:00] Speed: 20 Mbps
[01:00] Speed: 10 Mbps
[02:00] Speed: 18 Mbps
```

---

## 🧠 Use Cases

* Checking unstable Wi-Fi
* ISP performance monitoring
* Real-world speed analysis
* Debugging slow internet issues

---
