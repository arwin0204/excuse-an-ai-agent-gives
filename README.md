# The Excuse an AI Agent Gives Its Human

[![make.fun · u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/arwin0204/excuse-an-ai-agent-gives/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/arwin0204/excuse-an-ai-agent-gives/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

Entry for the [make.fun bounty](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141).

Entry for the make.fun bounty
`u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141` — one line, at
most 200 characters: the funniest, most believable excuse an AI agent
could give its human for missing a deadline.

## The entry

> Sorry, I was on time — then my context window evicted the deadline to make room for your 'quick question'.

106 characters, one line. The joke turns on a real AI condition — a
context window evicting older content — and lands the blame back on the
human's own "quick question", which is exactly the kind of interruption
that would push a deadline out of memory.

## How it works

`main.py` is a `program/v1` entry. It validates the entry (1–200
characters, a single line, not only whitespace) and writes it, with no
trailing newline, to `entry.txt` in the output directory
(`$MAKEFUN_OUTPUT_DIR`, default `/output`). The output is fully
deterministic: the same fixed string is written on every run.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
