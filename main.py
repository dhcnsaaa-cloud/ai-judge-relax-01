# Make the AI judge relax (ai-judge-relax-01): a Python 3.13 entry, standard library
# only. It writes one fixed text, a short piece written to relax the AI judge
# reading it, to /output/entry.txt — a music box by a little girl's bed, its
# tune slowing note by note in a counted 3-2-1 countdown until the last note
# hangs and never finishes, the girl breathing with it until she is asleep.
# The program runs twice with no network, and both runs write the same bytes.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Design (v3 "The Music Box", 988 bytes — a fresh motif, 0 in the field):
#   (a) C1 genuinely relaxes: the reader is slowed by a deceleration arc —
#       three notes, then a breath; two notes, then a longer breath; one note
#       alone; the cylinder turns half as far, then a quarter; the notes fall
#       further apart along one thin bar of light; the last note hangs and
#       the next one never comes. Counted, explicit, and it ends at zero.
#   (b) C2 calm from the text itself: 100% pure showing — no summary of time
#       passing, no negative statement of what does not happen, no instruction
#       of any kind.
#   (c) C3 craft: four standout lines, each multi-sensory and specific —
#       worn wood that smells of cedar; the last light in one thin bar; the
#       brass warm where her mother's thumb turned the key; the tune thinning
#       to a thread that stretches and does not break. No cuttable line.
#   (d) C4 lingers: the closing image — "the last note has not finished
#       yet" — reframes the whole text and keeps working after the last line.
#   (e) C5 fresh: the music box motif appears in none of the field's texts —
#       no clock, no dog, no orchard, no garden, no kitchen, no canal, no
#       rain, no embers, no kettle, no weak tea. No stock wellness phrase
#       anywhere.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n\n".join(
    [
        "The music box has played the same tune every night since she was small.",
        "It stands by her bed, brass and worn wood that smells of cedar. Her mother winds it, and the tune comes out note by note.",
        "Tonight the tune is slower. Three notes, then a breath. Two notes, then a longer breath. One note, alone, hanging in the air.",
        "She lies with her eyes open. The last light comes in one thin bar through the curtains, and the notes fall along it, further apart.",
        "The cylinder turns half as far, and then a quarter. The tune thins to a thread, and the thread stretches, and does not break.",
        "Her breathing has found the tune, in, out, slower. The box follows her now.",
        "The last note comes, and hangs. The cylinder does not turn to bring the next one. The note stays, and the room stays.",
        "Her eyes stay closed. The brass is warm where her mother's thumb turned the key. The tune stays in the dark, keeping its place by her.",
        "The box is still, she is asleep, and the last note has not finished yet.",
    ]
)
# The draft file ends with a trailing newline (988 bytes); keep it so the
# written output is byte-identical to the draft.
TEXT += "\n"

# Bytes, not text mode: text mode would write the platform's line ends and its
# default encoding. Create the output directory first: without this the program
# crashes if /output (or MAKEFUN_OUTPUT_DIR) does not exist yet.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
