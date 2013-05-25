import os

from humanstxt import parse

path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                    "humans.txt")
text = open(path, 'r').read()


def test():
    humans = parse(text)
    txt = text.replace(" [at] ", "@").strip('\n')
    try:
        assert unicode(humans).encode('utf-8') == txt
    except NameError:  # py3k
        pass
    assert str(humans) == txt
