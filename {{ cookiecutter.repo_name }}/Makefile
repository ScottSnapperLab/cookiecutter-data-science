.PHONY: clean clean_env data lint environment serve_nb sync_data_to_s3 sync_data_from_s3 github_remote

#################################################################################
# GLOBALS                                                                       #
#################################################################################
SHELL := /bin/bash

BUCKET = {{ cookiecutter.s3_bucket }}
CONDA_ENV_NAME = {{ cookiecutter.conda_env_name }}
CONDA_ROOT = $(shell conda info --root)
CONDA_ENV_DIR = $(CONDA_ROOT)/envs/$(CONDA_ENV_NAME)
CONDA_ENV_PY = $(CONDA_ENV_DIR)/bin/python

ifeq (,$(shell which conda))
HAS_CONDA=False
else
HAS_CONDA=True
endif

#################################################################################
# COMMANDS                                                                      #
#################################################################################

serve_nb:
	source activate $(CONDA_ENV_NAME); \
	jupyter notebook --notebook-dir notebooks

install:
	conda create -n $(CONDA_ENV_NAME) --no-chan-pri --file requirements.txt --yes ; \
	source activate $(CONDA_ENV_NAME); \
	ipython kernel install --user --name $(CONDA_ENV_NAME) --display-name "$(CONDA_ENV_NAME)"; \
	pip install -e .

uninstall:
	source activate $(CONDA_ENV_NAME); \
	rm -rf $$(jupyter --data-dir)/kernels/$(CONDA_ENV_NAME); \
	rm -rf $(CONDA_ENV_DIR)

github_remote:
	bash github/push_to_new_remote.sh

data:
	source activate $(CONDA_ENV_NAME); \
	python src/python/data/make_dataset.py

clean_bytecode:
	find . -name "__pycache__" -type d -exec rm -r {} \; ; \
	find . -name "*.pyc" -exec rm {} \;

## Lint using flake8
lint:
	flake8 --exclude=lib/,bin/,docs/conf.py .

## Upload Data to S3
sync_data_to_s3:
	aws s3 sync data/ s3://$(BUCKET)/data/

## Download Data from S3
sync_data_from_s3:
	aws s3 sync s3://$(BUCKET)/data/ data/
