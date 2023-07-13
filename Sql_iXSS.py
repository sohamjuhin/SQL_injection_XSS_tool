import requests

# Function to check for XSS vulnerability
def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url + payload)
    if payload in response.text:
        print("XSS vulnerability detected!")
    else:
        print("No XSS vulnerability found.")

# Function to check for SQL injection vulnerability
def check_sql_injection(url):
    payload = "1' OR '1'='1"
    response = requests.get(url + "?id=" + payload)
    if "error" in response.text:
        print("SQL injection vulnerability detected!")
    else:
        print("No SQL injection vulnerability found.")

# Main function to perform vulnerability scan
def vulnerability_scan(url):
    print("Scanning", url, "for vulnerabilities...")
    check_xss(url)
    check_sql_injection(url)
    print("Scan complete.")

# Usage example
target_url = "http://example.com"
vulnerability_scan(target_url)
