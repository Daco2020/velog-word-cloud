#!/bin/bash

# pre-commit hook install from pip
pre-commit install

# symlink
ln -sf ../../commit-msg.py ./.git/hooks/commit-msg

# implement permission
chmod +x .git/hooks/commit-msg