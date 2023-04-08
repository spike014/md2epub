from ebooklib import epub
import os

import book.chapter as CHAPTER

def convert_to_epub(content, options):
    project_paths = options.project.split("/")
    if not options.identifier:
        options.identifier = project_paths[len(project_paths)-1]
    if not options.title:
        options.title = project_paths[len(project_paths)-1]
    if not options.output:
        options.output = f"{options.title}-{options.identifier}.epub"

    book = epub.EpubBook()
    book.set_identifier(options.identifier)
    book.set_title(options.title)
    book.set_language(options.language)
    book.add_author(options.author)

    book.spine = ["nav"]
    book.toc = []
    book.toc.append(
            epub.Link(options.identifier, options.title, options.identifier)
    )
    book.add_item(epub.EpubNav())
    
    CHAPTER.add_itemsV2(book, content, options, 0)

    epub.write_epub(options.output, book, {})
