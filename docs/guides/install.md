# Installation

The steps to install `randomly` are:

1. Clone the GitHub repository.
2. Create a new virtual environment.
3. Install `randomly` in the new environment.

## Get this repo locally

```bash
git clone git@github.com:deppen8/documenting-your-code.git
cd documenting-your-code/
```

(This assumes you are using the SSH clone method. If you are not sure what to use, you can read [the GitHub documentation on cloning](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories).)

## Get Python 3.9 and create a virtual environment

This tutorial assumes we are working with Python version 3.9. We also want to create a virtual environment where we can safely install dependencies.

Depending on which virtual environment tool you use, you might install Python 3.9 separately or you may do it as part of the virtual environment creation.

In any case, you can use the `requirements.txt` in the repo to install all of the tools you will need.

**Be sure to activate your new virtual environment!**

## Install `randomly` in the environment

Now that we have our virtual environment, we can install our demo package, `randomly`, in "editable" (a.k.a. "develop") mode. From the root directory of the repo (i.e., `/path/to/documenting-your-code`), run:

```bash
python3 -m pip install -e .
```

This will ensure that any changes we make to the demo package will be automatically available to us in our virtual environment without reinstalling the `randomly` package.
