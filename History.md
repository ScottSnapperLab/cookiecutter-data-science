
v2017.06.22.1
=============

  * Fixed how Snakefile path is determined
  * Snakefile now collects PRE list in rule: pre
  * Removed SAVE_RUN_CONFIG rule
  * Improved the way rule graphs are drawn
  * Changed Snakefile to use ruamel.yaml
  * Reworked how logging is organized and added load_csv with gzip to TOP level import
  * Reqs now include scipy and matplotlib
  * Configs: OUT_DIR ==> OUT_DIR_LOCATION
  * Makefile now uses '--no-chan-pri' when creating conda env
  * Added binary doc-type patterns and notebook/ to .gitignore

v2017.03.31.3
=============

  * completed improving logging setup and config


v2017.03.31.2
=============

  * fixed cookiecutter json delimiter problem

v2017.03.31.1
=============

  * Moved config processing to misc.py
  * Added todos.txt
  * Improved logging set up and configuration.
