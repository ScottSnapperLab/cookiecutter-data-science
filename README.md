# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage](https://github.com/ScottSnapperLab/cookiecutter-data-science)

- Forked from http://drivendata.github.io/cookiecutter-data-science/


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/drivendata/cookiecutter-data-science


[![asciicast](https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02.png)](https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02)


### The resulting directory structure
------------

The directory structure of your new project looks like this:

```
├── LICENSE
├── Makefile                 <- Makefile with commands like `make data` or `make train`
├── README.md                <- The top-level README for developers using this project.
├── setup.py                 <- Allow the `src` directory to be pip installed and called
│                               from the jupyter notebooks.
├── Snakefile                <- Template Snakefile for using the project like a pipeline.
├── configs
│   ├── factory_resets
│   ├── logging.yaml
│   ├── main.yaml
│   └── README.txt
│
├── data
│   ├── external             <- Data from third party sources.
│   ├── interim              <- Intermediate data that has been transformed.
│   ├── processed            <- The final, canonical data sets for modeling.
│   └── raw                  <- The original, immutable data dump.
│
├── docs                     <- A default Sphinx project; see sphinx-doc.org for details
│
├── notebooks                <- Jupyter notebooks. Naming convention is a number (for ordering),
│                               the creator's initials, and a short `-` delimited description, e.g.
│                               `1.0-jqp-initial-data-exploration`.
│
├── github                   <- Allows `make github_remote` to create and push this project to github.
│   └── push_to_new_remote.sh
│
│
├── references
│
├── reports                  <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures              <- Generated graphics and figures to be used in reporting
│
├── requirements.txt         <- The requirements file for reproducing the analysis environment, e.g.
│                               generated with `pip freeze > requirements.txt`
│
├── src                      <- Source code for use in this project.
│   └── project_name         <- Allow the `src` directory to be pip installed and called
│       │                       from the jupyter notebooks via `from project_name.models import train_model`.
│       ├── __init__.py      <- Makes project_name a Python module
│       ├── cli              <- Defines the skeleton of a command line interface to `src`
│       │   ├── config.py
│       │   └── main.py
│       │
│       ├── errors.py
│       ├── features         <- Scripts to turn raw data into features for modeling
│       │   └── build_features.py
│       │
│       ├── logging.py
│       ├── misc.py
│       ├── models           <- Scripts to train models and then use trained models to make
│       │   │                   predictions
│       │   ├── predict_model.py
│       │   └── train_model.py
│       │
│       ├── rules
│       │   └── template_python_script.py
│       │
│       ├── todos.txt
│       └── visualize         <- Scripts to create exploratory and results oriented visualizations
│           └── visualize.py
│
├── test_environment.py
└── tox.ini
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
