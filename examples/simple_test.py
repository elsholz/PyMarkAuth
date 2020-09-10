from pymarkauth import MarkDown

with MarkDown('simple_test.md') as doc:
    sec = doc.section("This is the title")

    sec.text(
        "This is some text. ",
        "This text is appended in the same line.",
        doc.newline(),
        "This is is a new line in the markdown file, but will be rendered on the same line.",
        doc.paragraphs(
            "This is a paragraph.",
            doc.italics("This is another paragraph in italics.")
        )
    )

    subsec = sec.section("That's a subsection")

    subsec.text(doc.bold("This is bold."))

    subsec = sec.section("This Subsection has some lists.")
    subsec.unordered_list([
        'Item 1',
        'Item 2',
        'Item 3',
        ['sub item 1', 'sub item 2'],
        'another item',
        doc.ordered_list([
            'ordered sublist item 1',
            doc.unordered_list(['subsubitem unordered 1', 'subsubitem unordered 2']),
            'ordered sublist item 2',
            doc.unordered_list(['subsubitem unordered 1', 'subsubitem unordered 2', 'subsubitem unordered 3'])
        ])
    ])

    sec = doc.section('Another H1 Section')
    subsec = sec.section("That's an H2 subsection")
    subsec = subsec.section("That's an H3 subsection")
    subsec = subsec.section("That's an H4 subsection")
    subsec = subsec.section("That's an H5 subsection")
    subsec = subsec.section("That's an H6 subsection")

    # to print the contents use
    # print(doc)
