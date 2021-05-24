import unicodedata as ud
import re

THREE_POINT_INCLUSION_YEAR = 1979


def removediacritics(char: str) -> str:
    '''
    Return the base character of char, by "removing" any
    diacritics like accents or curls and strokes and the like.
    '''
    desc = ud.name(char)
    cutoff = desc.find(' WITH ')
    if cutoff != -1:
        desc = desc[:cutoff]
        try:
            char = ud.lookup(desc)
        except KeyError:
            pass  # removing "WITH ..." produced an invalid name
    return char


def clean_name(name: str) -> str:
    regex = re.compile('[,\.!?\']')
    name = regex.sub('', name)
    for i in range(len(name)):
        name = name.replace(name[i], removediacritics(name[i]))
    return name.lower()