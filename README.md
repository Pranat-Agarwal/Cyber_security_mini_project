# EWB Phishing URL Awareness Checker

## Overview

Phishing is a type of cyberattack where attackers use deceptive links or messages to trick people into revealing sensitive information such as passwords or account details. This project is an educational Python tool that checks the visible text of a URL for common phishing warning signs.

The tool works locally and does not open, visit, scan, or send URLs to any website.

## Features

- Detects an `@` symbol in the URL
- Flags unusually long URLs (over 100 characters)
- Flags IP-address hostnames
- Flags many hostname segments (5 or more)
- Flags punycode-style hostnames (`xn--`)
- Flags the HTTP scheme
- Allows checking several URLs without restarting
- Provides a clear **"REVIEW CAREFULLY"** summary when warnings are found
- Handles malformed URL input clearly without crashing
- Explains each warning in simple words

## Requirements

Python 3.14.5. No extra packages.

## How to Run

Windows:

python phishing_checker.py
then type URL and enter
to exit enter q

## Example Output

python phishing_checker.py

=================================================================
       EWB PHISHING URL AWARENESS CHECKER
=================================================================
Text checks only - this program does not open URLs.
Enter a sample URL to inspect.
Type 'q', 'quit', or 'exit' to close the program.

-----------------------------------------------------------------
Enter a sample URL (or type q to quit): https://www.example.com/login

=================================================================
RESULT
=================================================================
URL: https://www.example.com/login

Findings:

1. No listed warning signs found. This does NOT prove safety.

-----------------------------------------------------------------
No listed warning signs detected.
This does NOT prove that the URL is safe.
-----------------------------------------------------------------

Never enter passwords from unexpected links.

-----------------------------------------------------------------
Enter a sample URL (or type q to quit): q

Goodbye! Stay alert online.


## Test Results

Python version used: 3.14.5   |   Operating system: Windows   |   Date: 29 Oct 2026
| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | https://www.example.com/login | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | Uses an IP address instead of a familiar domain. | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | Contains an @ symbol; inspect carefully. | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Contains many hostname segments/subdomains. | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Contains a punycode-style hostname. | PASS |


## Screenshots

![Sample run](screenshots/sample_run.png)

![Test results](screenshots/test_results.png)

## Improvements

## Improvements

1. **Loop with Quit Command** - Changed the program to check multiple URLs without restarting. Added a quit command to exit the program. Tested it by entering multiple sample URLs and typing `q` to exit.

2. **Review Carefully Summary** - Added a clear warning summary that displays the number of warning signs found. Tested it using sample URLs containing an IP address and HTTP scheme.

3. **Malformed Input Handling** - Added exception handling for invalid URL formats to prevent crashes. Tested it with malformed input such as `http://[bad`.

4. **Warning Explanations** - Added simple explanations for each warning sign, including the `@` symbol, long URLs, IP addresses, multiple hostname segments, punycode, and HTTP. Tested the explanations using sample URLs for each warning type.

5. **Improved Output Formatting** - Added numbered findings, clear headings, consistent spacing, separators, and quit instructions to make the results easier to read. Tested the output with URLs that trigger different warnings and URLs with no listed warning signs.


## Limitations

This is an educational tool. It only reads URL text. It does not visit URLs, scan for malware or prove that a URL is safe. No warning signs found does NOT mean a URL is safe.

## Ethical Use

Use sample strings only. Do not collect credentials. Do not use this project to deceive anyone or to test websites without permission.

## Author

Pranat Agarwal, 2022–2026 Batch, EWB Courses