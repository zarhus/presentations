# Zarhus Developer Meetup presentations

This repository contains presentations for Zarhus Developer Meetups.

## Installation

Install the `slidev-template` submodule:

```bash
git submodule update --init --remote slidev-template
```

## Usage

### Start presentation

Start the desired presentation:

```bash
./scripts/local-preview.sh ../pages/ram-wipe.md
```

Then open content in browser on <http://localhost:8000>

## Contribution

Please feel free to create issues for improvement ideas and bugs, as well as
pull requests to fix any issues. If you intend to provide code improvements,
please install all dependencies by running:

```bash
pip install -r requirements.txt
```

Before pushing code for review, ensure that `pre-commit run --all-files` does
not return any issues.
