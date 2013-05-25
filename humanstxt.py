"""
Humanstxt
==========

Humanstxt is a Python library for parsing vailed humans.txt
( like template in http://humanstxt.org/Standard.html)
"""

__all__ = ['HumanTxt', 'parse']
__author__ = "whtsky"
__version__ = '0.1'

import re
from collections import OrderedDict


split_informations = re.compile(r"(?:\n *)+\n").split

TITLE_FINDER = re.compile(r"^/\* *(.*[^ ]) *\*/$")


class HumansTxt(OrderedDict):
    """

    Use :class:`HumansTxt` class like a dict.

    Example ::

        from humanstxt import parse

        txt = \"""
        /* TEAM */
            Founder & Developer: Jacky Chan
            Contact: linux_china [at] hotmail.com
            Weibo: @linux_china
            Blog: http://intellij.org.cn/blog
            From: HangZhou, ZheJiang, China
            University: Beijing Institute of Technology
            Degree: Bachelor

        /* THANKS */
            humans.txt Founder: Abel Cabans
            Site: http://www.humanstxt.org

        /* SITE */
            Last update: 2013/01/23
            Language: Chinese
            Doctype: HTML5
            Standards: HTML5, CSS3
            Components: RequireJS, JQuery, Backbone, BootStrap
            Software: ImageMagick, PhantomJS
            IDE: IntelliJ IDEA

                __  __                                _______  ________
               / / / /_  ______ ___  ____ _____  ____/_  __/ |/ /_  __/
              / /_/ / / / / __ `__ \/ __ `/ __ \/ ___// /  |   / / /
             / __  / /_/ / / / / / / /_/ / / / (__  )/ /  /   | / /
            /_/ /_/\__,_/_/ /_/ /_/\__,_/_/ /_/____//_/  /_/|_|/_/
        \"""

        humanstxt = parse(txt)

        print(humanstxt.keys())  # ['team', 'thanks', 'site', 'description']

    :class:`HumansTxt` will replace ``[at]`` to ``@`` ::

        print(humanstxt["team"]["contact"])  # linux_china@hotmail.com

    You can turn :class:`HumansTxt` into a vailed humans.txt via ``str`` ::

        print(str(humanstxt))  # the same as ``txt`` above

    """
    def __str__(self):
        informations = []
        for k, v in self.items():
            if k != "description":
                lines = ["/* %s */" % k.upper()]
                for k, v in v.items():
                    lines.append("    %s: %s" % (k.capitalize(), v))
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
    """
    Parse the humans.txt into an :class:`HumansTxt` class.

    Example ::

        from humanstxt import parse

        txt = \"""
        /* TEAM */
            Founder & Developer: Jacky Chan
            Contact: linux_china [at] hotmail.com
            Weibo: @linux_china
            Blog: http://intellij.org.cn/blog
            From: HangZhou, ZheJiang, China
            University: Beijing Institute of Technology
            Degree: Bachelor

        /* THANKS */
            humans.txt Founder: Abel Cabans
            Site: http://www.humanstxt.org

        /* SITE */
            Last update: 2013/01/23
            Language: Chinese
            Doctype: HTML5
            Standards: HTML5, CSS3
            Components: RequireJS, JQuery, Backbone, BootStrap
            Software: ImageMagick, PhantomJS
            IDE: IntelliJ IDEA

                __  __                                _______  ________
               / / / /_  ______ ___  ____ _____  ____/_  __/ |/ /_  __/
              / /_/ / / / / __ `__ \/ __ `/ __ \/ ___// /  |   / / /
             / __  / /_/ / / / / / / /_/ / / / (__  )/ /  /   | / /
            /_/ /_/\__,_/_/ /_/ /_/\__,_/_/ /_/____//_/  /_/|_|/_/
        \"""

        humanstxt = parse(txt)

    :param text: the text of humans.txt
    :return: :class:`HumansTxt`
    """
    humans = HumansTxt()
    informations = split_informations(text.strip('\n'))

    for information in informations:
        lines = information.splitlines()
        first_line = lines[0].strip()

        title = find_title(first_line)
        if title:
            lines.pop(0)
            infos = OrderedDict()

            for k, v in [line.strip().split(':', 1) for line in lines]:
                v = v.strip().replace(" [at] ", "@")
                infos[k.strip().lower()] = v.strip()
            humans[title] = infos
        else:
            humans["description"] = information
    return humans
