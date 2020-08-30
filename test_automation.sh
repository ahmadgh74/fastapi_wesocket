#!/bin/bash

coverage run --omit 'venv/*' -m unittest test && coverage html