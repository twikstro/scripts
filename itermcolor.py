#!/usr/bin/env python
"""
Display tabs in iTerm2 in different colors based on target hostname

"""
import sys

USAGE = """
Usage: itermcolor.py [role]
e.g. itermcolor.py production

Usage in .ssh/config:
Add the following two lines for each host, changing the role parameter accordingly:

    PermitLocalCommand yes
    LocalCommand python ~/path/to/itermcolor.py jump

Customize role colors below
"""

def get_color_by_role(s):

    blue = (0, 0, 1)
    yellow = (0.8, 0.7, 0)
    orange = (0.9, 0.3, 0)
    green = (0, 1, 0)
    red = (1, 0, 0)
    white = (1, 1, 1)

    defaultColor = white

    colorTable = {
    'noncrit': green,
    'test': yellow,
    'infra': orange,
    'production': red,
    'jump': blue
    }

    return colorTable.setdefault(s, defaultColor)


def set_tab_color(color):

    r, g, b = color

    # iTerm 2
    # http://www.iterm2.com/#/section/documentation/escape_codes"
    sys.stdout.write("\033]6;1;bg;red;brightness;%d\a" % int(r * 255))
    sys.stdout.write("\033]6;1;bg;green;brightness;%d\a" % int(g * 255))
    sys.stdout.write("\033]6;1;bg;blue;brightness;%d\a" % int(b * 255))
    sys.stdout.flush()

def itermcolor(name):

    color = get_color_by_role(name)
    set_tab_color(color)

def main():

    if (len(sys.argv) != 2):
        sys.exit(USAGE)

    name = sys.argv[1]
    itermcolor(name)

if __name__ == "__main__":
    main()
