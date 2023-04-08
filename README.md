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
  --content CONTENT     content file name, use `_sidebar.md` as default
  --author AUTHOR       author, use `someone` as default
  --title TITLE         title
  --language LANGUAGE   language, use `zh` as default
  --identifier IDENTIFIER
                        identifier
  --output OUTPUT       output
```

## example

1. clone a docsify project to `./ddia`

```
git clone https://github.com/spike014/ddia.git
```

2. run script

```
python3 md2epub.py --project ./ddia
```

3. check out the epub file in `pwd` path

```
ddia-ddia.epub
```

## TODO:

- using github.io address to input project
- handle image reference
- handle link reference

## License

MIT
