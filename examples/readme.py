from pymarkauth import MarkDown

with MarkDown('../README.md') as doc:
    sec = doc.section("PyMarkAuth")
    sec.paragraphs(
        'With PyMarkAuth you can author markdown code simply from python code.'
        ' To view the source code that generated this readme, take a look at the examples directory!',
    )

    subsec = sec.section("Here's a list of features")
    subsec.unordered_list([
        'lines and paragraphs',
        'nested sections',
        'text styling',
        'links and images',
        'nested ordered lists and unordered lists',
        'code blocks',
        doc.italics('future features:'),
        doc.ordered_list([
            'Tables',
            'List of emojies (github specific)',
            'programming language enum'
        ])
    ])

    sec.newline()
    sec.newline()
    sec.text('Heres some code:')
    sec.newline()
    sec.code(
        'for x in range(10):',
        '    print(f"Hello, World! {x}")',
        language='python'
    )

    subsec = sec.section('You can also add images and links')
    subsec.image(source='logo/logo.svg')
    subsec.newline()
    subsec.text('You can go to python.org from ')
    subsec.link(target='https://python.org', display_text='here.')

