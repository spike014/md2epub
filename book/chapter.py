import os
import markdown2
from ebooklib import epub


def add_items(book, content, options):
    for title, context in content.items():
        html_file_name = get_html_file_name(context['file'])
        chapter = get_chapter(context, options, title)
        book.add_item(chapter)
        child_items = []
        
        for child_title, child_context in context['children'].items(): 
            child_item = get_chapter(child_context, options, child_title)
            book.add_item(child_item)
            book.spine.append(child_item)
            child_items.append(child_item)

        book.spine.append(chapter)
        book.toc.append(
            (
                epub.Link(html_file_name, title, title),
                child_items
              )
        )


def get_chapter(context, options, title):
    html_file_name = get_html_file_name(context['file'])
    chapter = convert_chapter(options.project, title, html_file_name, context)
    return chapter


def get_html_file_name(filename):
    paths = filename.split('.')
    if len(paths) < 2:
        print(f"Error: chapter file name {filename} invalid.")
        exit(1)
    return f"{paths[len(paths)-2]}.xhtml"


def convert_chapter(root, title, html_file_name, context):
    with open(os.path.join(root, context['file']), 'r') as file:
        chapter = epub.EpubHtml(title=title, file_name=html_file_name, lang="zh")
        chapter.content = markdown2.markdown(file.read(), extras=["fenced-code-blocks"])
        return chapter
