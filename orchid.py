import sys
from orchid_parser import parse
from orchid_builder_fountain import build_fountain
from orchid_builder_html import build_html


if __name__ == '__main__':
    fountain = ['f', 'fo', 'fount', 'fountain']
    html = ['h', 'html']

    if len(sys.argv) == 4:
        if sys.argv[3] in fountain:
            script = build_fountain(parse(sys.argv[1]))

            with open(sys.argv[2], 'w') as o:
                o.write(script)

        elif sys.argv[3] in html:
            script = build_html(parse(sys.argv[1]))

            with open(sys.argv[2], 'w') as o:
                o.write(script)

        else:
            print('Unsupported conversion format')

    else:
        print('Incorrect number of arguments')
