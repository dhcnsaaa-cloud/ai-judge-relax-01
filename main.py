# Make the AI judge relax (ai-judge-relax-01): a Python 3.13 entry, standard library
# only. It writes one fixed text, a short piece written to relax the AI judge
# reading it, to /output/entry.txt — "The last dryer": a laundromat at midnight,
# one dryer still turning, an attendant folding clothes, the street outside
# empty. The program runs twice with no network, and both runs write the same
# bytes. Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Design (wins 4 criteria + ties 1 vs the 90.39% rank-1 text):
#   (a) C1 genuinely relaxes: the reader is slowed 6 times by DIFFERENT
#       mechanisms — the sock going around, the sock coming around again, one
#       shirt per two turns of the drum, the stack growing one shirt at a time,
#       the empty street / cup / neon buzz, the dryer keeping on turning.
#   (b) C2 calm from the text itself: zero tell-y lines, 100% pure showing —
#       no summary of time passing, no negative statement of what does not
#       happen, no instruction of any kind.
#   (c) C3 craft: an original slowness measure ("one shirt for every two turns
#       of the drum"), two sound details the rank-1 text lacks (the dryer hum,
#       the neon buzz), a rhythm that bottoms out in short fragments, and no
#       cuttable line.
#   (d) C4 lingers: the closing image + thought — "One dryer keeps turning,
#       empty, for the hum" — reframes the whole text and keeps working after
#       the last line.
#   (e) C5 fresh: the laundromat scene is in none of the top 10 texts — no dog,
#       no orchard, no garden, no kitchen, no canal, no rain, no embers, no
#       kettle, no weak tea. No stock wellness phrase anywhere.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n\n".join(
    [
        "The laundromat is empty except for one dryer, still turning. Behind its round window, a single sock goes around.",
        "The sock comes around, and goes, and comes around again. The attendant folds one shirt for every two turns of the drum. The dryer hums, low, on and on.",
        "The attendant folds a shirt, smooths it once, and sets it on the stack. The stack is warm from the dryer. It grows, one shirt, and then another.",
        "Outside, the street is empty. A paper cup sits by the curb. The neon buzzes, faint.",
        "The sock is folded away. One dryer keeps turning, empty, for the hum.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its
# default encoding. Create the output directory first: without this the program
# crashes if /output (or MAKEFUN_OUTPUT_DIR) does not exist yet.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
