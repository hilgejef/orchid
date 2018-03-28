# Orchid parser
# Expects a file formatted in the Orchid screenwriting markup language
# Outputs a Script class containing "blocks" of screenwriting text elements


import re


# CLASS DEFINITIONS

class Script:
    def __init__(self):
        self.title_page = []
        self.lines = []

    def __repr__(self):
        title_page = '\n'.join(['\t'.join([line.type, str(line)]) for line in self.title_page])
        return title_page + '\n'.join(['\t'.join([line.type, str(line)]) for line in self.lines])

    def add_line(self, line):
        self.lines.append(line)

    def add_to_title_page(self, line):
        self.title_page.append(line)


class Line:
    def __init__(self, line_type=None, text=''):
        self.type = line_type
        self.text = text

    def __repr__(self):
        return self.text


# REGEX DEFINITIONS

r_heading = re.compile('@\s*(.+)')
r_action = re.compile('\+\s*(.+)')
r_character = re.compile('&\s*(.+)')
r_dual_one = re.compile('>\s*(.+)')
r_dual_two = re.compile('<\s*(.+)')
r_dialogue = re.compile('\$\s*(.+)')
r_parenthetical = re.compile('\(\s*(.+)')
r_transition = re.compile('~\s*(.+)')
r_comment = re.compile('#\s*(.+)')
r_title_page = re.compile('%\s*(.+)')


# REGEX MAPPING

regexs = {
    '@': ('HEADING', r_heading),
    '+': ('ACTION', r_action),
    '&': ('CHARACTER', r_character),
    '>': ('DUAL_ONE', r_dual_one),
    '<': ('DUAL_TWO', r_dual_two),
    '$': ('DIALOGUE', r_dialogue),
    '(': ('PARENTHETICAL', r_parenthetical),
    '~': ('TRANSITION', r_transition),
    '#': ('COMMENT', r_comment),
    '%': ('TITLE_PAGE', r_title_page),
}


# PARSER

def parse(filename):
    script = Script()

    with open(filename) as bouquet:
        for flower in bouquet:
            flower = flower.strip()

            # In case of line being empty, add a line break to script and continue
            if not flower:
                script.add_line(Line('LINE_BREAK', flower))
                continue

            identifier = flower[0]

            # If not a valid identifier, then consider this an action line
            if identifier not in regexs:
                rtype, text = 'ACTION', flower
            else:
                rtype, regex = regexs[identifier]
                text = re.match(regex, flower)[1]

            line = Line(rtype, text)

            if rtype == 'TITLE_PAGE':
                script.add_to_title_page(line)
            else:
                script.add_line(line)

    return script
