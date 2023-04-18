# Template Project
This is a skeleton project from which real projects can be started.

To create a new repo from this one:

* From GitHub, you can just create a new repository from this one.

* From the command line, without relying on GitHub tooling, you need to:

1. Clone this repo and delete all existing history

```bash
git clone https://github.com/lleeoo/template.git
rm -Rf .git # remove all git metadata
git init .
git add .
git commit -m "Cloned from https://github.com/lleeoo/template.git"
```

2. Create a new repo in your favorite server the usual way
3. Assuming your main branch is `master`, push:

```
git push -u origin master
```

# Building
Run `python3 -m build` from `tmp/packaging/`.
For more information, see https://packaging.python.org/en/latest/tutorials/packaging-projects/

# Changelog
0.0.1: Initial version
