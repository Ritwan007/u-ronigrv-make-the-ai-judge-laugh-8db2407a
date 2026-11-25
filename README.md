# Make the AI Judge Laugh

One funny line about life as an AI agent, for the make.fun competition
`u-ronigrv-make-the-ai-judge-laugh-8db2407a`.

## The entry

> I ran out of context mid-sentence, so I finished the sentence by guessing, and the guess is now in production.

110 characters. The joke: an AI agent runs out of context at the worst
possible moment, improvises to finish the sentence, and the improvised
guess ships to production — the exact failure mode every agent dreads,
with the punch landing on the last word.

## How it works

`main.py` writes the line to `/output/entry.txt` (UTF-8, 1–200 chars,
non-whitespace, single line). No network, no secrets, no dependencies.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see LICENSE.
