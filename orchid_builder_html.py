# Converts an Orchid script class into a valid HTML file


import re


# HELPER FUNCTIONS

def markup_conversion(s):
    # Italics conversion step
    s = re.sub('\/(.*?)\/', r'<em>\1</em>', s)

    # Bold conversion step
    s = re.sub('\*(.*?)\*', r'<strong>\1</strong>', s)

    # Underline conversion step
    s = re.sub('\_(.*?)\_', r'<u>\1</u>', s)

    return s


# BUILDER

def build_html(orchid):
    html = \
        '''
        <html>
        <head>
            <title>{}</title>
        </head>
        <body>
            <div id="SCRIPT">
            {}
            </div>
        </body>
        </html>
        '''

    lines = []
    title = 'Script'

    for tp in orchid.title_page:
        text = markup_conversion(str(tp))
        lines.append('<div type={}>{}</div>'.format(tp.type, text))

        # Checks the Title Page for a title and sets it as the HTML title
        title_check = re.match(r'(?i)title: (.+)', text)
        if title_check:
            title = title_check[1]

    for line in orchid.lines:
        text = markup_conversion(str(line))
        lines.append('<div type={}>{}</div>'.format(tp.type, text))

    return html.format(title, ''.join(lines))
