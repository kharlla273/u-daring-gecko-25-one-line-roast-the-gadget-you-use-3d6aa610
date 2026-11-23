# One-Line Roast: The Gadget You Use Every Day

A tiny deterministic program that writes one original roast line about the
phone — the gadget used every day — to `/output/entry.txt`.

## The line

> Every Sunday my phone sends me a screen-time report like a disappointed
> parent — then tries to sell me cloud storage for the evidence.

(134 characters, well inside the 200-character gate.)

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

No dependencies, no network, no randomness: the same line, byte for byte,
on every run.

## How it works

`main.py` holds the roast as a single constant, validates it against the
gate (1–200 characters, not only whitespace), creates `/output` if needed,
and writes the line plus a trailing newline as UTF-8.
