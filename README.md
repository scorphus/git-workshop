# Git Workshop

Repository used for my Git workshops/talks

## Presentation

Mail me for the Keynote/PDF :wink:

## Bisecting

Bisect helps you identify a commit that introduced a bug or a new functionality.

### Bisect manually and identify a commit that introduced a bug

The bug we have is the misspelled `eightty`. Let's find it:

```
git bisect start buggy working
./spell-number.py 88
git bisect good/bad  # good or bad depending on output
./spell-number.py 88
git bisect good/bad  # good or bad depending on output
# ... repeat until you get the commit that introduces the bug
```

### Automate it with a script:

This can be automated with a simple Bash script:

```
git bisect start buggy working
git bisect run ./script_spelling.sh
```

#### `script_spelling.sh`
```bash
#!/bin/sh

# Delete Python bytecodes
find . -name "*.pyc" -delete

word=$(./spell-number.py 88 | tr /A-Z/ /a-z/)

if [[ "$word" == "eightty eight" ]]; then
    exit 1
fi
```

### Bisect manually and identify a commit that introduced an unexpected feature

The unexpected feature we have is capitalization. For cases like this – when you
need to find a *good* commit – it's better to use old/new terms. Let's do it:

```
git bisect start --term-bad=new --term-good=old master working
./spell-number.py 359
git bisect old/new  # old or new depending on output
./spell-number.py 359
git bisect old/new  # old or new depending on output
# ... repeat until you get the commit that introduces the feature
```

### Automate it with a script
```
git bisect start master working
git bisect run ./script_capital.sh
```

#### `script_capital.sh`
```bash
#!/bin/sh

# Delete Python bytecodes
find . -name "*.pyc" -delete

word=$(./spell-number.py 359)

if [[ "$word" == "Three Hundred and Fifty Nine" ]]; then
    exit 1
fi
```

## License

[MIT](http://opensource.org/licenses/MIT) © [scorphus](https://github.com/scorphus)
