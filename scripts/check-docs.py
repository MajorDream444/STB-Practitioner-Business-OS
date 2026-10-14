#!/usr/bin/env python3
"""Documentation integrity and public-repo boundary check.

Run manually or in CI:  python3 scripts/check-docs.py
Detector self-test:     python3 scripts/check-docs.py --self-test

Checks tracked files only. Exits non-zero on any failure. Not a git hook.

1. Relative markdown links resolve to a tracked file or directory (the git
   index, not merely the working tree, so a clean checkout cannot break).
2. Decision-log headings (D-###, R-###, C-###) are unique.
3. Every markdown file under docs/04-protocols/ carries an INACTIVE marker in
   its first lines (decision D-035: Human Context drafts must not read as live).
4. Public-repo boundary (decision D-010): no email addresses, Google Forms or
   Sheets links, phone numbers, or image files are tracked. This file alone is
   exempt from the content scans in (3), because its self-test holds fake
   phone-number fixtures; it is still checked for tracked images and links.
"""
import os
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
# Candidate phone numbers: start with +, 00 or 0 (international or domestic,
# including Dutch 06-..., 020 ..., +31 6 ..., 0031 ...), then digits with common
# separators. A candidate is flagged only if it holds 9-15 digits, which keeps
# dates, versions and short numbers out.
PHONE_CAND = re.compile(r"(?<![\w.,:/$-])(?:\+|00|0)\d[\d ().\-]{7,18}\d")
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic", ".bmp", ".tiff"}
SELF = Path("scripts/check-docs.py")
PROTOCOLS = "docs/04-protocols/"
LOG = Path("docs/01-decisions/DECISION-LOG.md")
LOG_HEADING = re.compile(r"^###\s+([DRC]-\d{3})\b")


def has_phone(text):
    for m in PHONE_CAND.finditer(text):
        if 9 <= len(re.sub(r"\D", "", m.group(0))) <= 15:
            return True
    return False


def self_test():
    positives = [
        "06-12345678", "06 12345678", "0612345678", "020 123 4567",
        "(020) 123 4567", "+31 6 1234 5678", "+31612345678", "0031 6 12345678",
        "+62 812 3456 7890", "call +44 20 7946 0958 now",
    ]
    negatives = [
        "2026-10-14", "2026-02-01", "v0.10.4", "0f803e1", "$0-$1,500",
        "1780274117711", "| 0 | 0 | 0 |", "sha 5933cdd770f5143336709683d7356f64",
        "09:00-17:30", "D-001 to D-023", "64/64 tests", "45 hrs, 60 hrs",
    ]
    bad = [t for t in positives if not has_phone(t)]
    bad += [t for t in negatives if has_phone(t)]
    if bad:
        print("SELF-TEST FAIL:", bad)
        return 1
    print(f"SELF-TEST OK: {len(positives)} positive, {len(negatives)} negative cases")
    return 0


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
    if "--self-test" in sys.argv:
        return self_test()
    files = tracked_files()
    failures = []
    tracked = {p.as_posix() for p in files}
    tracked_dirs = {d.as_posix() for p in files for d in p.parents if d.as_posix() != "."}

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
                dest = os.path.normpath((path.parent / rel).as_posix())
                if dest.startswith("..") or (dest not in tracked and dest not in tracked_dirs):
                    failures.append(f"{path}: broken or untracked link -> {target}")

        if path.as_posix().startswith(PROTOCOLS) and path.suffix == ".md":
            if "INACTIVE" not in "\n".join(text.splitlines()[:12]):
                failures.append(f"{path}: protocol draft lacks an INACTIVE marker (D-035)")

        if path == SELF:
            continue

        for m in EMAIL.finditer(text):
            addr = m.group(0)
            if addr in EMAIL_ALLOWED or addr.split("@")[1].lower() in EMAIL_ALLOWED_DOMAINS:
                continue
            failures.append(f"{path}: email address present (D-010)")
            break
        if GOOGLE.search(text):
            failures.append(f"{path}: Google Forms/Sheets link present (D-010)")
        if has_phone(text):
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
