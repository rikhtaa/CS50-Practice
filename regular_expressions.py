import re

email = input("What's your email? ").strip()

# Walrus operator (:=)
# Assigns and tests a value in one line.
# Example:
# if match := re.search(...):

if match := re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# Regex Cheat Sheet

# .        Any single character
# *        Zero or more of the previous pattern (greedy)
# +        One or more of the previous pattern
# ?        Optional (0 or 1 occurrence)
# *?       Lazy match (match as little as possible)

# ^        Start of string
# $        End of string

# \d       Digit (0-9)
# \w       Letter, digit, or underscore
# \s       Whitespace
# \.       Literal dot (.)

# []       Character class
# [abc]    a, b, or c
# [^"]     Any character except "

# ()       Capturing group
# (?:...)  Non-capturing group

# Example:
# r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'
#
# (?:www\.)?  -> Optional "www." (not captured)
# ([^"]+)     -> Capture everything until the next double quote


# Match Object

# re.search() returns a Match object or None.

# match.group(0) -> Entire match
# match.group(1) -> First captured group
# match.group(2) -> Second captured group
#
# Optional capturing groups return None if they don't match.
# Group numbers do NOT change.


# re Functions

# re.search()      Find first match anywhere in the string
# re.match()       Match only at the beginning
# re.fullmatch()  Entire string must match
# re.findall()     Return all matches as a list
# re.sub()         Replace matched text
# re.split()      Split a string using a regex


# Common Flags

# re.IGNORECASE
# Ignore uppercase/lowercase differences.
