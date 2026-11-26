#!/usr/bin/env python3
"""make.fun bounty entry: Fortune Cookie Wisdom for Developers.

Crack open the cookie. The fortune inside is the entire
deployment strategy, and it is one line long.
"""

FORTUNE = (
    "You will ship on Friday, and nothing will break — "
    "because you finally wrote the test first. "
    "Lucky numbers: 200, 201, 404."
)


def fortune():
    """Return the developer fortune cookie wisdom."""
    return FORTUNE


def main():
    print(fortune())


if __name__ == "__main__":
    main()
