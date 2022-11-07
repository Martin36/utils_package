#!/bin/bash

# Updates the patch version of the package
export VERSION=`bump`

# Create git tag using the version from bump
git tag v$VERSION
git push origin v$VERSION

# Remove the previous build
rm dist/*

# Create new build
python -m build

# Deploy build to testpypi
# twine upload --repository testpypi dist/*

# Deploy build to pypi
twine upload dist/*