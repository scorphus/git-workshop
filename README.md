# Git Workshop

Repository used for my Git workshops.

## Presentation

Mail me for the Keynote/PDF :wink:

## Bisecting

1. Look manually for misspelled `eightty` commit
2. Use the following to find the *titlize* commit

```fish
git bisect start --term-bad=new --term-good=old master works
git bisect run ./magic.sh
```

### `magic.sh`

```fish
#!/bin/sh

word=$(./spell-number.py 88)

if [[ "$word" == "eighty eight" ]]; then
    exit 0
elif [[ "$word" == "eightty eight" ]]; then
    exit 0
else
    exit 1
fi
```

## License

[MIT](http://opensource.org/licenses/MIT) © [scorphus](https://github.com/scorphus)
