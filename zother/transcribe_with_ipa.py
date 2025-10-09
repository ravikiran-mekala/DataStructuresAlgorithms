#!/usr/bin/env python3
# Usage:
#   python transcribe_with_ipa.py /path/to/audio_or_video.(m4a|mp3|wav|mp4|mov|avi|mkv)
#
# Requirements (the script will try to install if missing):
#   - Python 3.8+
#   - ffmpeg (install via your OS package manager if needed)
#   - pip install openai-whisper pronouncing
#
# Output:
#   Prints two lines:
#     1) Text transcription
#     2) Broad IPA transcription (approx., from CMUdict; not a narrow, detailed phonetic record)

import sys
import subprocess
import shutil
import re
import os
import time


def ensure_package(pkg):
    try:
        __import__(pkg)
        return True
    except Exception:
        print(f"Installing {pkg} ...", file=sys.stderr)
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", pkg])
        __import__(pkg)
        return True


def pip_install(spec):
    print(f"Installing {spec} ...", file=sys.stderr)
    subprocess.check_call([sys.executable, "-m", "pip",
                          "install", "--upgrade", spec])


def ensure_import(import_name, pip_name=None):
    """Import a module; if it fails, install pip_name (or import_name) and retry."""
    try:
        __import__(import_name)
        return True
    except Exception:
        pip_install(pip_name or import_name)
        __import__(import_name)
        return True


def main():
    if len(sys.argv) < 2:
        print("Please provide an input file path.\nExample:\n  python transcribe_with_ipa.py input.m4a", file=sys.stderr)
        sys.exit(1)

    inpath = sys.argv[1]
    if not shutil.which("ffmpeg"):
        print(
            "ERROR: ffmpeg not found. Please install ffmpeg and try again.", file=sys.stderr)
        print("  macOS: brew install ffmpeg", file=sys.stderr)
        print("  Ubuntu/Debian: sudo apt-get install ffmpeg", file=sys.stderr)
        print("  Windows (choco): choco install ffmpeg", file=sys.stderr)
        sys.exit(2)

    # Ensure dependencies
    print("-> Ensuring dependencies...", file=sys.stderr, flush=True)
    # Ensure setuptools for pkg_resources used by pronouncing
    try:
        import pkg_resources  # noqa: F401
    except Exception:
        ensure_package("setuptools")
    # Pre-flight NumPy compatibility: downgrade to <2 if 2.x detected
    try:
        import numpy as _np  # noqa: F401
        _major = int(_np.__version__.split(".")[0])
        if _major >= 2:
            print("-> Detected NumPy >=2; installing numpy<2 for torch/whisper compatibility...",
                  file=sys.stderr, flush=True)
            pip_install("numpy<2")
            import importlib as _importlib
            _importlib.reload(_np)
    except Exception:
        # If numpy isn't present, whisper install will bring it in
        pass
    # Ensure whisper (pip package is openai-whisper)
    ensure_import("whisper", pip_name="openai-whisper")
    # Ensure pronouncing
    ensure_package("pronouncing")

    import whisper
    import pronouncing

    # Load a reasonable model
    print("-> Loading Whisper model 'base' (fallback to 'tiny.en' if unavailable)...",
          file=sys.stderr, flush=True)
    t0 = time.time()
    try:
        model = whisper.load_model("base")
    except Exception:
        model = whisper.load_model("tiny.en")
    print(f"-> Model loaded in {time.time() - t0:.1f}s",
          file=sys.stderr, flush=True)

    # Transcribe
    print("-> Transcribing (this may take a while)...",
          file=sys.stderr, flush=True)
    t1 = time.time()
    result = model.transcribe(inpath, language="en")
    text = (result.get("text") or "").strip()
    if not text:
        print("Transcription failed or returned empty text.", file=sys.stderr)
        sys.exit(3)
    print(
        f"-> Transcription complete in {time.time() - t1:.1f}s ({len(text.split())} words)", file=sys.stderr, flush=True)

    # ARPABET -> IPA mapping
    ARPABET_TO_IPA = {
        "AA": "ɑ", "AE": "æ", "AH": "ʌ", "AO": "ɔ", "AW": "aʊ", "AY": "aɪ",
        "B": "b", "CH": "tʃ", "D": "d", "DH": "ð", "EH": "ɛ", "ER": "ɝ", "EY": "eɪ",
        "F": "f", "G": "ɡ", "HH": "h", "IH": "ɪ", "IY": "i", "JH": "dʒ", "K": "k",
        "L": "l", "M": "m", "N": "n", "NG": "ŋ", "OW": "oʊ", "OY": "ɔɪ", "P": "p",
        "R": "ɹ", "S": "s", "SH": "ʃ", "T": "t", "TH": "θ", "UH": "ʊ", "UW": "u",
        "V": "v", "W": "w", "Y": "j", "Z": "z", "ZH": "ʒ"
    }

    def arpabet_seq_to_ipa(arpabet_seq):
        ipa = ""
        for token in arpabet_seq:
            base = ''.join([c for c in token if not c.isdigit()])
            stress_digits = ''.join([c for c in token if c.isdigit()])
            ipa_sym = ARPABET_TO_IPA.get(base, base.lower())
            if base == "ER" and stress_digits == "0":
                ipa_sym = "ɚ"
            if stress_digits == "1":
                ipa += "ˈ" + ipa_sym
            elif stress_digits == "2":
                ipa += "ˌ" + ipa_sym
            else:
                ipa += ipa_sym
        return ipa

    def text_to_ipa(s):
        words = re.findall(r"\w+('\w+)?|[^\w\s]", s, flags=re.UNICODE)
        ipa_tokens = []
        for w in words:
            if not re.match(r"[A-Za-z']+$", w):
                ipa_tokens.append(w)
                continue
            w_clean = w.lower()
            prons = pronouncing.phones_for_word(w_clean)
            if prons:
                arp = prons[0].split()
                ipa_tokens.append(arpabet_seq_to_ipa(arp))
            else:
                ipa_tokens.append(w_clean)
        return " ".join(ipa_tokens)

    print("-> Converting transcription to IPA...", file=sys.stderr, flush=True)
    ipa_line = text_to_ipa(text)

    # Write outputs to a text file
    try:
        outpath = sys.argv[2] if len(
            sys.argv) >= 3 else os.path.splitext(inpath)[0] + ".txt"
        print(f"-> Writing outputs to: {outpath}", file=sys.stderr, flush=True)
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(text + "\n")
            f.write(ipa_line + "\n")
    except Exception as e:
        print(f"Warning: failed to write output file: {e}", file=sys.stderr)

    # Output per your requested format:
    print(text)
    print(ipa_line)
    print("-> Done.", file=sys.stderr, flush=True)


if __name__ == "__main__":
    main()
