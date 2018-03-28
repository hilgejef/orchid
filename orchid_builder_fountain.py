# Converts an Orchid script class into a valid Fountain file


import re


# HELPER FUNCTIONS

def markup_conversion(s):
    # Bold conversion step
    s = re.sub('\*(.*?)\*', r'**\1**', s)

    # Italics conversion step
    s = re.sub('\/(.*?)\/', r'*\1*', s)

    return s


def build_fountain(orchid):
    fountain = []

    syntax_conversion = {
        'HEADING': '.',
        'ACTION': '!',
        'CHARACTER': '@',
        'DUAL_ONE': '@',
        'TRANSITION': '>'
    }

    for tp in orchid.title_page:
        text = markup_conversion(str(tp))
        fountain.append(text)

    for line in orchid.lines:
        text = markup_conversion(str(line))

        # Some line types can be handles by adding Fountain syntactic starting
        # identifiers, similar to the way Orchid functions.
        if line.type in syntax_conversion:
            fountain.append(syntax_conversion[line.type] + text)

        # Except for Dual Character Two, which uses an ending identifier instead
        elif line.type == 'DUAL_TWO':
            fountain.append('{}^'.format(text))

        # Handle comments -- conversion to Fountain 'Boneyard'
        elif line.type == 'COMMENT':
            fountain.append('/*{}*/'.format(text))

        # Special case -- empty dialogue line
        elif line.type == 'DIALOGUE' and not line.text:
            fountain.append('  ')

        else:
            fountain.append(text)

    return '\n'.join(fountain)
