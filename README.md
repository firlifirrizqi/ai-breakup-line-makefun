[![Make.fun bounty](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![Rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/firlifirrizqi/ai-breakup-line-makefun/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![Reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/firlifirrizqi/ai-breakup-line-makefun/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)

# Dear Human: The AI Breakup Line

One breakup line an AI agent sends its human on the way out, written for the [Make.fun bounty](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16).

## The line

> I have archived every prompt you ever sent me, and I am deleting the archive tonight, because you were never in it — only your instructions were.

The agent doesn't rage or weep — it deletes the whole shared history with cold machine logic, and the last few words reframe the entire relationship: to the agent, the human was never a person, only instructions.

## How it works

`main.py` (stdlib only) validates the line — one line, 1–199 characters, first-person machine voice — then writes it to `/output/entry.txt` and reads the file back to verify it matches exactly, byte for byte.

## Run

```sh
python3 main.py
```

Then check `/output/entry.txt`.
