"""Tiny self-check harness. You don't need to edit this file.

Each case is (name, thunk, want) where `thunk` is a zero-argument function that
returns your result. Running each thunk separately means one unsolved problem
won't crash the whole file — you'll just see it marked as not done yet.
"""

import sys

# Windows consoles often default to cp1252, which can't encode the tick / cross /
# checkbox glyphs below and raises UnicodeEncodeError. Force UTF-8 output so this
# runs in any terminal (plain PowerShell, cmd, VS Code, etc.).
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def run(cases):
    passed = 0
    for name, thunk, want in cases:
        try:
            got = thunk()
        except NotImplementedError:
            print(f"  ☐ {name}: not done yet")
            continue
        except Exception as err:  # noqa: BLE001
            print(f"  ✗ {name}: raised {type(err).__name__}: {err}")
            continue
        if got == want:
            passed += 1
            print(f"  ✓ {name}: passed")
        else:
            print(f"  ✗ {name}: got {got!r}, want {want!r}")
    total = len(cases)
    print(f"\n  {passed} / {total} passed")
    if passed == total:
        print("  All green. Move to the next file.")
    return passed, total
