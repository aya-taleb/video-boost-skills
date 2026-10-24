# Contributing

Thanks for helping. Fixes, better examples and new test cases are all welcome.

## Where to send a fix

Every skill in this repo has its home here, so fix it here. Some of my other repos share
skills between them; this one doesn't yet.

## How to make a change

1. Fork the repo and make your change on a branch.
2. If you changed a Python tool, run its tests:
   `python3 -m unittest discover -s tests -v`
3. Run the checks: `python3 scripts/validate.py`
4. If you changed how a skill behaves, add or update a test case in
   `skills/<skill>/evals/`. Each case is a folder with a prompt and a few checkable
   statements. Copy an existing case to start.
5. Open a pull request. Say what you changed and why, in a few lines.

## House rules for writing

- Plain words, short sentences. Write like a person.
- No em dashes.
- Skip the stock AI words listed in `scripts/validate.py`. The check will flag them.
- Never make up facts, numbers, quotes or sources in a skill or an example.

## Good first issues

Look for the `good first issue` label. A new test case, a fresh dated source for a
platform rule, or a fix to one of the Python tools (with a unit test) are all great
places to start.
