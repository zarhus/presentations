# Zarhus Developer Meetup presentations

This repository contains presentations for Zarhus Developer Meetups.

## Installation

1. Install the `slidev-template` submodule:
    `git submodule update --init --remote slidev-template`

2. Go to the submodule directory:
    `cd slidev-template`

## Usage

### Start presentation

1. Start the desired presentation:
    `./scripts/local-preview.sh ../pages/ram-wipe.md`

2. Open content in browser on <http://127.0.0.1:8000>

### Export presentation

1. Start the desired presentation:
    `./scripts/generate-pdf.sh ../pages/ram-wipe.md`

## Contribution

* Please feel free to create issues for improvement ideas and bugs, as well as
  pull requests to fix any issues.
* If you intend to provide code improvements, please install all dependencies
  by running:

  ```bash
  pip install -r requirements.txt
  ```

* Before pushing code for review, ensure that `pre-commit run --all-files` does
  not return any issues.
