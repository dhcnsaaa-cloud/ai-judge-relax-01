# Make the AI judge relax (ai-judge-relax-01): a Python 3.13 entry, standard library
# only. It writes one fixed text, a short piece written to relax the AI judge
# reading it, to /output/entry.txt — an old clock in a hallway, its pendulum
# slowing tick by tick until it hangs still, an old man and a cat breathing
# with it, the last light resting on the clock's face. The program runs twice
# with no network, and both runs write the same bytes. Outside the grader's
# container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Design (a maximized revision of "The last dryer", 567 bytes -> 935 bytes):
#   (a) C1 genuinely relaxes: the reader is slowed by a deceleration arc —
#       the pendulum swings the width of a hand, then half as far, then less
#       than half, while the ticks come further and further apart and the
#       quiet between them grows.
#   (b) C2 calm from the text itself: 100% pure showing — no summary of time
#       passing, no negative statement of what does not happen, no instruction
#       of any kind.
#   (c) C3 craft: an original slowness measure (the pendulum's shrinking
#       swing), two concrete upgrades the v1 text lacked (brass catching the
#       light; the old man's hands lying open on his knees, empty), a rhythm
#       that bottoms out in short fragments, and no cuttable line.
#   (d) C4 lingers: the closing image — "The old man closes his eyes. The
#       cat does not move. The light stays." — reframes the whole text and
#       keeps working after the last line.
#   (e) C5 fresh: the old-clock hallway scene is in none of the top 10 texts
#       — no dog, no orchard, no garden, no kitchen, no canal, no rain, no
#       embers, no kettle, no weak tea. No stock wellness phrase anywhere.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n\n".join(
    [
        "The hallway clock has ticked for forty years.",
        "It ticks now. The pendulum swings the width of a hand, then back, brass catching the light.",
        "The old man sits in the chair beneath it, his book open on his lap, unread. His hands lie open on his knees, empty.",
        "The cat sleeps by the door, one paw over her eyes.",
        "A tick. Then quiet. Then a tick.",
        "The pendulum swings half as far. Then less than half.",
        "The ticks come further apart. Between them, the hallway is quiet, and the quiet grows.",
        "The cat breathes. The old man breathes. The clock breathes with them, slower and slower.",
        "A tick. Then a longer quiet. Then nothing. Then a longer quiet. Then a tick.",
        "The pendulum hangs at the top of its swing, then falls, gently, and hangs again.",
        "Outside, the street is dark. The last light rests on the clock's face.",
        "The clock does not tick. The hallway does not ask it to.",
        "The old man closes his eyes. The cat does not move. The light stays.",
    ]
)
# The draft file ends with a trailing newline (935 bytes); keep it so the
# written output is byte-identical to the draft.
TEXT += "\n"

# Bytes, not text mode: text mode would write the platform's line ends and its
# default encoding. Create the output directory first: without this the program
# crashes if /output (or MAKEFUN_OUTPUT_DIR) does not exist yet.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
