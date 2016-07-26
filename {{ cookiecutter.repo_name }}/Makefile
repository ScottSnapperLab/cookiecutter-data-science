.PHONY: clean data lint requirements sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

BUCKET = {{ cookiecutter.s3_bucket }}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

environment:
	conda create -n {{ cookiecutter.conda_env_name }} --file requirements.txt

data: environment
	python src/python/data/make_dataset.py

clean:
	find . -name "*.pyc" -exec rm {} \;

lint:
	flake8 --exclude=lib/,bin/ .

sync_data_to_s3:
	aws s3 sync data/ s3://$(BUCKET)/data/

sync_data_from_s3:
	aws s3 sync s3://$(BUCKET)/data/ data/
