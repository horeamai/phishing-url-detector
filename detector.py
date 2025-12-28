import re

url = input("Masukkan URL: ").lower()

suspicious = 0

if "@" in url:
    suspicious += 1
if url.count("//") > 1:
    suspicious += 1
if re.search(r"(login|secure|account|update|verify)", url):
    suspicious += 1
if re.search(r"\d{1,3}(\.\d{1,3}){3}", url):
    suspicious += 1

if suspicious >= 3:
    print("⚠️ URL MENCURIGAKAN (PHISHING)")
elif suspicious == 2:
    print("⚠️ URL PERLU DIWASPADAI")
else:
    print("✅ URL AMAN")
