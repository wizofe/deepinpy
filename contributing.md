# Contributing to deepinpy

Welcome and thanks for taking time to contribute! This is a list of guidelines but feel free to use them as recommendation, rather than rules. Use your best judgement and feel free to propose new changes in this document with a pull request.

#### Table of contents

[How to contribute](#how-to-contribute)

    * [Reporting bugs](#reporting-bugs)
    * [Contributing to code](#contributing-to-code)
    * [Git Workflow](#git-workflow)

## How to contribute

### Reporting bugs
This section guides you through submitting a bug report for deepinpy. Following these guidelines help maintainers and the community understand your report, reproduce the behavior and find related reports.

Before creating those reports ensure that one is needed. When creating a new report include as many details as possible. Fill out the required issue template (TODO) as the information included will help the maintainers resolve the issue faster.

#### How do I submit a bug report?

Bugs are tracked in the [official issue tracker](https://github.com/utcsilab/deepinpy/issues) where you can create a new one and provide the information by filling the issue template.

### Contributing to code

#### Picking an issue

> **Note:** If you are a first time contributor, and are looking for an issue to take on, you might want to look for [Good 
First Issue](https://github.com/utcsilab/deepinpy/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
> labelled issues. We do our best to label such issues, however we might fall behind at times. So, ask us.

#### Local development

You will first need to clone the repository using `git` and then enter this directory:

```bash
$ git clone git@github.com:utscsilab/deepinpy.git
$ cd deepinpy
```

> **Note:** A personal form is recommended for this step [fork](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) for this step. If you are new to GitHub collaboration,
> you can refer to the [Forking Projects Guide](https://guides.github.com/activities/forking/).

Now, you will need to install the required dependencies, create a new conda environment and ensure that the current tests are passing on your machine:
```bash
$ conda env update -n deepinpy --file env.yml
$ pytest
```

Deepinpy uses the [black](https://github.com/psf/black) coding style and you should take care that the submitted code follows it. The CI will fail any Pull Request not abiding and it will not be merged.

Similarly, the import statements are sorted with [isort](https://github.com/timothycrosley/isort)
and special care must be taken to respect it. If you don't, the CI will fail as well.

To make sure that you don't accidentally commit code that does not follow the coding style, you can
install a pre-commit hook that will check that everything is in order:

```bash
$ pre-commit install
```

You can also run it anytime using:

```bash
$ run pre-commit run --all-files
```

It is important that tests need to be together with the code otherwise the code won't be merged.

#### Pull requests

The following steps are strongly recommended, so that the project has a consistent codebase. If you have any suggestions feel free to send a PR nevertheless (including one for this guide).

* Fill in [the required template](https://github.com/utcsilab/deepinpy/blob/master/.github/PULL_REQUEST_TEMPLATE.md)
* Be sure that your pull request contains tests that cover the changed or added code.
* If your changes warrant a documentation change, the pull request must also update the documentation.

> **Note:** Make sure your branch is [rebased](https://docs.github.com/en/free-pro-team@latest/github/using-git/about-git-r
ebase) against the latest main branch. A maintainer might ask you to ensure the branch is up-to-date prior to merging your Pull Request if changes have conflicts.

All pull requests, unless otherwise instructed, need to be first accepted into the main branch (`master`).
