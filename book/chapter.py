import os
import markdown2
from ebooklib import epub


def convert_chapter(root, title, html_file_name, context):
    with open(os.path.join(root, context['file']), 'r') as file:
        chapter = epub.EpubHtml(title=title, file_name=html_file_name, lang="zh")
        chapter.content = markdown2.markdown(file.read(), extras=["fenced-code-blocks", "latex"])
        return chapter

def add_items(book, content, options):
    for title, context in content.items(): 
        paths = context['file'].split('.')
        if len(paths) < 2:
            print(f"Error: chapter file name {context['file']} invalid.")
            exit(1)
        html_file_name = paths[len(paths)-2] + ".xhtml"
        chapter = convert_chapter(options.project, title, html_file_name, context)
        book.add_item(chapter)
        child_items = []
        
        for child_title, child_context in context['children'].items(): 
            child_paths = child_context['file'].split('.')
            if len(child_paths) < 2:
                print(f"Error: chapter file name {child_context['file']} invalid.")
                exit(1)
            child_html_file_name = f"{child_paths[len(child_paths)-2]}.xhtml"
            child_item = convert_chapter(options.project, child_title, child_html_file_name, child_context)

            book.spine.append(child_item)
            child_items.append(child_item)

        book.spine.append(chapter)
        book.toc.append(
            (
                epub.Link(html_file_name, title, title),
                child_items
              )
        )
