# md2epub

Generate a epub book from Markdown files.

Like [docsify](https://github.com/docsifyjs/docsify) projects.

## feature

- support code block
- support define content

## Usage

```shell
git clone https://github.com/spike014/md2epub.git
```

```shell
cd md2epub && pip install -r requirements.txt 
```

```shell
python3 md2epub.py --project {docsify project root}
```

more (help):

```shell
python3 md2epub.py --help
```
```
usage: md2epub.py [-h] [--project PROJECT] [--content CONTENT] [--author AUTHOR] [--title TITLE] [--language LANGUAGE] [--identifier IDENTIFIER] [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --project PROJECT     the root directory of markdown files
  --content CONTENT     content file name
  --author AUTHOR       author
  --title TITLE         title
  --language LANGUAGE   language
  --identifier IDENTIFIER
                        identifier
  --output OUTPUT       output
```

## TODO:

- using github.io address to input project
- handle image reference
- handle link reference

## License

MIT
