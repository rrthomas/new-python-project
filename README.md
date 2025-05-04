# Python project template

https://github.com/rrthomas/python-project-template  
© Reuben Thomas <rrt@sc3d.org>  

This is a simple Python project template which you can use to create a new
Python project. It uses the [Nancy](https://github.com/rrthomas/nancy/)
templating system.


## Installation

You will need to have Python and Nancy. Nancy can be installed from the
Python package index with:

```
pip install nancy
```

Then, clone the template’s git repository with:

```
git clone https://github.com/rrthomas/python-project-template
```


## Creating a new project

Run Nancy as follows, setting the variables appropriately:

```
env PROJECT_NAME="project-name" AUTHOR="My Name" EMAIL=my@email.org DESCRIPTION="Description of my new project" nancy --process-hidden /path/to/python-project-template/template /path/to/new-project
```

You can run your new program:

```
cd /path/to/new-project
make build
PYTHONPATH=. python -m project_name
```

The project is set up with a `pyproject.toml` and Makefile to build, test
and publish it, and basic command-line handling.


## Copyright and Disclaimer

python-project-template is copyright Reuben Thomas, and is free software,
licensed under the GNU Public License version 3, or, at your option, any
later version. See the file COPYING.
