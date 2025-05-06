# Zarhus Developer Meetup presentations

This repository contains presentations for Zarhus Developer Meetups.

## Usage

* Install npm manager e.g. [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script)
* Use lts version of npm:

```bash
npm install --lts
```

* Fix vulnerabilities if found during install:

```bash
npm audit fix
```

* Host presentations:

```bash
npm run dev -- -p 8000 --remote --force
```

* Open content in browser on <http://0.0.0.0:8000>

* To export presentations in .pdf:

```bash
npm i -D playwright-chromium
npx slidev export
```

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
