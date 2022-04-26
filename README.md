# documenting-your-code

This repo is a starting place for a tutorial/workshop about documenting your code.

The repo does _not_ contain all of the material from the tutorial. The tutorial is designed to be taught by an instructor. This repo contains code that is used as part of that instruction. In the future, I do hope to translate the material into a self-guided tutorial.

## Learner prerequisites

Learners will need a GitHub.com account and should be familiar with some foundational `git` workflow tasks: cloning a repo, making a branch, pushing to a remote repository.

Participants should also be comfortable with a virtual environment tool of their choice (`venv`, `conda`, etc.).

## Getting started

These steps should get you ready for the tutorial. Ideally all of these steps would be complete before the tutorial starts.

### Fork the repository

You should fork this repository to your GitHub account using the "Fork" icon in the top right of the page. ([Access more information about forking a repository.](https://docs.github.com/en/get-started/quickstart/fork-a-repo))

### Get your new repo locally

```bash
git clone git@github.com:<your-username-here>/documenting-your-code.git
cd documenting-your-code/
```

(This assumes you are using the SSH clone method. If you are not sure what to use, you can read [the GitHub documentation on cloning](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories).)

### Get Python 3.9 and create a virtual environment

:warning: A virtual environment is not _strictly_ required for this tutorial, but it is strongly recommended.

If you are not familiar with virtual environments and want to be, I recommend `conda` as a good starting place. The [Introduction to Conda for (Data) Scientists](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists) lesson from The Carpentries is a good resource. Start with the [Setup instructions](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/setup/), then move on to the Episodes.

This tutorial assumes we are working with Python version 3.9. We also want to create a virtual environment where we can safely install dependencies.

Depending on which virtual environment tool you use, you might install Python 3.9 separately or you may do it as part of the virtual environment creation.

**Be sure to activate your new virtual environment!**

After you have an environment, you can use the `requirements.txt` in the repo to install all of the tools you will need.

```bash
python3 -m pip install -r requirements.txt
```

### Install `randomly` in developer mode

Now that we have our virtual environment, we can install our demo package, `randomly`, in "editable" (a.k.a. "develop") mode. From the root directory of the repo (i.e., `/path/to/documenting-your-code`), run:

```bash
python3 -m pip install -e .
```

This will ensure that any changes we make to the demo package will be automatically available to us in our virtual environment without reinstalling the `randomly` package.
