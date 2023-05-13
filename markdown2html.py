#!/usr/bin/python3
"""
A script to interpret Markdown to HTML.
Markdown is awesome! All your README.md are made in Markdown,
but do you know how GitHub are rendering them?
It's time to code a Markdown to HTML!
"""


import sys
import os
import re


def markdownToHtml(markdownFile, outputFile):
    """
    Markdown file to HTML and writes the output to a file.
    arg:
        markdownFile: Name of the Markdown file
        outputFile: Output file name
    """
    # Check that the Markdown file exists and is a file
    # if it doesn't exist exit with code 1.
    if not (os.path.exists(markdownFile) and os.path.isfile(markdownFile)):
        print(f"Missing {markdownFile}", file=sys.stderr)
        sys.exit(1)

    # Open Markdown and interpret to HTML
    with open(markdownFile, encoding="utf-8") as f:
        html = []
        for line in f:
            # Markdown headings level <h1><h2>...
            # add interpreted lines to html list/array.
            # Use "re" as a regex to filter certain chars.
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                headingLevel = len(match.group(1))
                headingText = match.group(2)
                html.append(f"<h{headingLevel}>\
                            {headingText}</h{headingLevel}>")
            else:
                html.append(line.rstrip())

    # HTML Output
    with open(outputFile, "w", encoding="utf-8") as f:
        f.write("\n".join(html))


if __name__ == "__main__":
    # If the number of arguments is less than 2: print in STDERR
    # if it doesn't comply with the statement exit with code 1.
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    # Interpret the Markdown file to HTML
    markdownToHtml(sys.argv[1], sys.argv[2])
    sys.exit(0)
