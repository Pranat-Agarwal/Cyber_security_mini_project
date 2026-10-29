
import re
from urllib.parse import urlparse

REASONS = {
    "@ symbol": (
        "Text before @ can be misleading because the actual "
        "hostname appears after the @ symbol."
    ),
    "long URL": (
        "A very long URL can hide the important part of the "
        "destination among many characters."
    ),
    "IP address": (
        "An IP address is less recognizable than a normal "
        "domain name and deserves extra attention."
    ),
    "many segments": (
        "Many hostname segments or subdomains can make a URL "
        "look complicated or misleading."
    ),
    "punycode": (
        "Punycode can represent special characters in domain "
        "names that may visually resemble other letters."
    ),
    "http": (
        "HTTP does not provide encrypted communication. "
        "HTTPS is preferred, but HTTPS alone does not prove "
        "that a website is trustworthy."
    )
}

INFO_MESSAGES = (
    "No URL entered.",
    "Could not identify",
    "This text is not a valid URL format.",
    "No listed warning signs found."
)


def has_warnings(findings):
    if not findings:
        return False

    return not findings[0].startswith(INFO_MESSAGES)


def inspect_url(raw_url):
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append(
            "Contains an @ symbol; inspect carefully."
        )

    if len(url) > 100:
        findings.append(
            "Unusually long URL (over 100 characters)."
        )

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    if "xn--" in host:
        findings.append(
            "Contains a punycode-style hostname."
        )

    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    if not findings:
        findings.append(
            "No listed warning signs found. "
            "This does NOT prove safety."
        )

    return findings


def get_warning_reason(warning):
    if "@ symbol" in warning:
        return REASONS["@ symbol"]

    if "Unusually long URL" in warning:
        return REASONS["long URL"]

    if "IP address" in warning:
        return REASONS["IP address"]

    if "many hostname segments" in warning:
        return REASONS["many segments"]

    if "punycode" in warning:
        return REASONS["punycode"]

    if "Uses HTTP" in warning:
        return REASONS["http"]

    return ""


def display_result(raw_url):
    findings = inspect_url(raw_url)

    print("\n" + "=" * 65)
    print("RESULT")
    print("=" * 65)
    print(f"URL: {raw_url.strip()}")
    print("\nFindings:")

    for number, item in enumerate(findings, start=1):
        print(f"\n{number}. {item}")

        reason = get_warning_reason(item)

        if reason:
            print(f"   Why it matters: {reason}")

    if has_warnings(findings):
        print("\n" + "-" * 65)
        print("REVIEW CAREFULLY")
        print(f"{len(findings)} warning sign(s) found.")
        print("These are clues, not proof that the URL is malicious.")
        print("-" * 65)
    else:
        print("\n" + "-" * 65)
        print("No listed warning signs detected.")
        print("This does NOT prove that the URL is safe.")
        print("-" * 65)

    print("\nNever enter passwords from unexpected links.")


def main():
    print("\n" + "=" * 65)
    print("       EWB PHISHING URL AWARENESS CHECKER")
    print("=" * 65)
    print("Text checks only - this program does not open URLs.")
    print("Enter a sample URL to inspect.")
    print("Type 'q', 'quit', or 'exit' to close the program.")

    while True:
        print("\n" + "-" * 65)

        raw_url = input(
            "Enter a sample URL (or type q to quit): "
        )

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("\nGoodbye! Stay alert online.")
            break

        display_result(raw_url)


if __name__ == "__main__":
    main()
