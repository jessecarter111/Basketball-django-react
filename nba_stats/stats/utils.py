import unicodedata as ud
import re


def rmdiacritics(char):
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


def clean_name(name):
    regex = re.compile('[,\.!?\']')
    name = regex.sub('', name)
    for i in range(len(name)):
        name = name.replace(name[i], rmdiacritics(name[i]))
    return name


THREE_POINT_INCLUSION_YEAR = 1979
