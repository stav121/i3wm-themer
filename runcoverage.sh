#!/bin/bash

coverage run -m pytest
coverage xml --include="i3wmthemer/*"
python-codacy-coverage -r coverage.xml
rm -rf 000.png
rm -rf coverage.xml
