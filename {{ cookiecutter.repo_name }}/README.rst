{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.repo_name | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
     :alt: Updates


{{cookiecutter.description}}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.repo_name | replace("_", "-") }}.readthedocs.io.
{% endif %}



Project Organization
------------
```
├── configs
├── data
│   ├── external           <- Data from third party sources
│   ├── interim            <- Intermediate data that has been transformed.
│   ├── processed          <- The final, canonical data sets for modeling.
│   └── raw                <- The original, immutable data dump.
├── docs                   <- A default Sphinx project; see sphinx-doc.org for details
├── github                 <- Contains a script for creating and pushing to github
├── LICENSE
├── Makefile               <- Makefile with commands to provision a Conda environment and register
│                             the environment's kernel with Jupyter
├── models                 <- Trained and serialized models, model predictions, or model summaries
├── notebooks              <- Jupyter notebooks. Naming convention is a date and title
│                             (`2016-07-28__initial_exploration.ipynb`)
├── README.md              <- The top-level README for developers using this project.
├── references             <- Data dictionaries, manuals, and all other explanatory materials.
├── reports                <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures            <- Generated graphics and figures to be used in reporting
├── requirements.txt       <- The requirements file for reproducing the analysis environment.
├── setup.py               <- Allows installing this project's python code for Notebook importation
├── Snakefile              <- Snakemake file for reproducing a full pipeline
├── src                    <- Source code for use in this project.
│   ├── {{cookiecutter.project_name}}
│   │   ├── data           <- Code to download or generate data
│   │   ├── features       <- Code to turn raw data into features for modeling
│   │   ├── models         <- Code to train models and then use trained models to make
│   │   ├── rules          <- Scripts meant to be plugged in as Snakemake Rules
│   │   └── visualization  <- Code to create exploratory and results oriented visualizations
│   └── R
│       └── rules          <- Scripts meant to be plugged in as Snakemake Rules
└── tox.ini
```
