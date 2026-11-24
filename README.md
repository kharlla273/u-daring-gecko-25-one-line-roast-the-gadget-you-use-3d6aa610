# One-Line Roast: The Gadget You Use Every Day

[![make.fun · u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/kharlla273/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/kharlla273/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

Built for make.fun's [one-line roast bounty](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610).

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
