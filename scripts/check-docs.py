#!/usr/bin/env python3
"""Documentation integrity and public-repo boundary check.

Run manually or in CI:  python3 scripts/check-docs.py

Checks tracked files only. Exits non-zero on any failure. Not a git hook.

1. Relative markdown links resolve to a tracked file or directory.
2. Decision-log headings (D-###, R-###, C-###) are unique.
3. Public-repo boundary (decision D-010): no email addresses, Google Forms or
   Sheets links, phone numbers, or image files are tracked.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
EMAIL_ALLOWED = {"noreply@anthropic.com"}
EMAIL_ALLOWED_DOMAINS = {"example.com", "example.org"}
GOOGLE = re.compile(r"docs\.google\.com/(forms|spreadsheets)|forms\.gle/")
PHONE = re.compile(r"(?<![\w.])\+\d{1,3}[ -]?\d{2,4}[ -]?\d{3,4}[ -]?\d{3,4}\b")
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic", ".bmp", ".tiff"}
LOG = Path("docs/01-decisions/DECISION-LOG.md")
LOG_HEADING = re.compile(r"^###\s+([DRC]-\d{3})\b")


def tracked_files():
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    return [Path(p) for p in out.splitlines() if (ROOT / p).is_file()]


def read_text(path):
    try:
        return (ROOT / path).read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def strip_code_fences(text):
    return re.sub(r"```.*?```", "", text, flags=re.S)


def main():
    files = tracked_files()
    failures = []

    for path in files:
        if path.suffix.lower() in IMAGE_EXT:
            failures.append(f"{path}: image file tracked (public-repo boundary, D-010)")

    for path in files:
        text = read_text(path)
        if text is None:
            continue

        if path.suffix == ".md":
            for target in LINK.findall(strip_code_fences(text)):
                if re.match(r"^(https?:|mailto:|#)", target):
                    continue
                rel = target.split("#", 1)[0]
                if not rel:
                    continue
                dest = (ROOT / path.parent / rel).resolve()
                if not dest.exists():
                    failures.append(f"{path}: broken link -> {target}")

        for m in EMAIL.finditer(text):
            addr = m.group(0)
            if addr in EMAIL_ALLOWED or addr.split("@")[1].lower() in EMAIL_ALLOWED_DOMAINS:
                continue
            failures.append(f"{path}: email address present (D-010)")
            break
        if GOOGLE.search(text):
            failures.append(f"{path}: Google Forms/Sheets link present (D-010)")
        if PHONE.search(text):
            failures.append(f"{path}: phone-number-like string present (D-010)")

    log_text = read_text(LOG)
    if log_text is None:
        failures.append(f"{LOG}: missing")
    else:
        seen = {}
        for i, line in enumerate(log_text.splitlines(), 1):
            m = LOG_HEADING.match(line)
            if m:
                if m.group(1) in seen:
                    failures.append(
                        f"{LOG}:{i}: duplicate heading {m.group(1)} (first at line {seen[m.group(1)]})"
                    )
                seen[m.group(1)] = i

    if failures:
        print("FAIL")
        for f in failures:
            print("  -", f)
        return 1
    print(f"OK: {len(files)} tracked files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
