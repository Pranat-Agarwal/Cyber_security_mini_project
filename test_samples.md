# Test Results
Python version used: 3.14.5   |   Operating system: Windows   |   Date: 29 Oct 2026
| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | https://www.example.com/login | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | Uses an IP address instead of a familiar domain. | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | Contains an @ symbol; inspect carefully. | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Contains many hostname segments/subdomains. | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Contains a punycode-style hostname. | PASS |
## Notes
Write 2 or 3 lines: what you learned, and what surprised you

I learned how to identify common phishing URL warning signs using Python.

I understood the importance of checking hostnames, IP addresses, HTTP schemes, and suspicious symbols.

I was surprised that a URL with no warning signs can still be unsafe.