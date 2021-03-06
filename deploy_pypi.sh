#!/bin/bash

# Updates the patch version of the package
bump

# TODO: Create git tag using the version from bump

# Remove the previous build
rm dist/*

# Create new build
python -m build

# Deploy build to testpypi
# twine upload --repository testpypi dist/*

# Deploy build to pypi
twine upload dist/*