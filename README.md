# Loading Screen Gold: A Tip in 200 Characters

Entry for the make.fun bounty
[u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270).

`main.py` (pure Python standard library, no network) writes one
loading-screen tip of at most 200 characters to `/output/entry.txt`:

> Tip: your agent already rewrote this file twice. Breathe, read the diff, and approve nothing it wrote after midnight.

Run it locally with `OUTPUT_DIR` set to a scratch directory:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

Two runs produce byte-identical output.
