import re


def parse_content(filename):
    """
    parse content file to dict.
    Currently, only one or two level directories are supported.
    TODO: support n+ level directories
    """
    content = {}
    with open(filename) as file:
        father = {}
        while line := file.readline():
            strs = line.split("\n")
            if strs[0]:
                line = strs[0]
            else:
                continue
            match = re.match(r"^(\s*)-\s*\[(.*)\]\((.*)\)\s*$", line)
            if match:
                level = len(match.group(1))/2+1
                title = match.group(2)
                chapter_file = match.group(3)
                if level == 1:
                    chapter = {
                        'file': chapter_file,
                        'children': {}
                    }
                    content[title] = chapter
                    father = chapter
                elif level == 2:
                    father['children'][title] = {
                        'file': chapter_file,
                        'children': {}
                    }
    return content
