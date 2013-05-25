"""
Humanstxt
==========

Humanstxt is a Python library for parsing vailed humans.txt
( like template in http://humanstxt.org/Standard.html)
"""

__author__ = "whtsky"
__version__ = '0.1'

import re
from collections import OrderedDict


split_informations = re.compile(r"(?:\n *)+\n").split

TITLE_FINDER = re.compile(r"^/\* *(.*[^ ]) *\*/$")


class HumanTxt(OrderedDict):
    def __str__(self):
        informations = []
        for k, v in self.items():
            if k != "description":
                lines = ["/* %s */" % k.upper()]
                for k, v in v.items():
                    lines.append("    %s: %s" % (k, v))
                informations.append("\n".join(lines))

            else:
                informations.append(v)
            informations.append("")  # Add a new line.
        return "\n".join(informations[:-1])

    def __unicode__(self):
        return str(self).decode('utf-8')


def find_title(line):
    results = TITLE_FINDER.findall(line)
    if results:
        return results[0].lower()


def parse(text):
    humans = HumanTxt()
    informations = split_informations(text)

    for information in informations:
        lines = information.splitlines()
        first_line = lines[0].strip()

        title = find_title(first_line)
        if title:
            lines.pop(0)
            infos = OrderedDict()

            for k, v in [line.strip().split(':', 1) for line in lines]:
                v = v.strip().replace(" [at] ", "@")
                infos[k.strip()] = v.strip()
            humans[title] = infos
        else:
            humans["description"] = information
    return humans

