import re

# Daftar kata kunci mencurigakan
SUSPICIOUS_KEYWORDS = [
    "login", "secure", "account", "update", "verify", "bank", "payment"
]

# Daftar domain resmi populer (contoh sederhana)
TRUSTED_DOMAINS = [
    "google.com", "facebook.com", "github.com", "twitter.com", "linkedin.com"
]

def is_url_valid(url):
    """Cek format URL"""
    regex = re.compile(
        r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*$'
    )
    return re.match(regex, url)

def check_suspicious_keywords(url):
    """Cek keyword mencurigakan di URL"""
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword.lower() in url.lower():
            return True
    return False

def check_trusted_domains(url):
    """Cek apakah URL termasuk domain terpercaya"""
    for domain in TRUSTED_DOMAINS:
        if domain in url:
            return True
    return False

def main():
    url = input("Masukkan URL: ").strip()

    if not is_url_valid(url):
        print("❌ URL TIDAK VALID")
        return

    if check_trusted_domains(url):
        print("✅ URL AMAN (trusted domain)")
    elif check_suspicious_keywords(url):
        print("⚠️ URL MENCURIGAKAN")
    else:
        print("⚠️ URL PERLU DIAWASI")

if __name__ == "__main__":
    main()
