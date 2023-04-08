import argparse
import os

import book.content as CONTENT
import book.book as BOOK

def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project",
        dest="project",
        type=str,
        help="the root directory of markdown files",
    )
    parser.add_argument(
        "--content",
        dest="content",
        default="_sidebar.md",
        type=str,
        help="content file name",
    )
    parser.add_argument(
        "--author",
        dest="author",
        default="someone",
        type=str,
        help="author",
    )
    parser.add_argument(
        "--title",
        dest="title",
        type=str,
        help="title",
    )
    parser.add_argument(
        "--language",
        dest="language",
        default="zh",
        type=str,
        help="language",
    )
    parser.add_argument(
        "--identifier",
        dest="identifier",
        type=str,
        help="identifier",
    )
    parser.add_argument(
        "--output",
        dest="output",
        type=str,
        help="output",
    )
    return parser.parse_args()


def main():
    options = parse_arg()
    if not os.path.isdir(options.project):
        print(f"Error: project {options.project} does not exist.")
        exit(1)

    content_file_name = os.path.join(options.project, options.content)
    if not os.path.isfile(content_file_name):
        print(f"Error: content file {content_file_name} does not exist.")
        exit(1)

    content = CONTENT.parse_content(content_file_name)
    BOOK.convert_to_epub(content, options)


if __name__ == "__main__":
    main()
