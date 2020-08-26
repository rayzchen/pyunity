python setup.py bdist_wheel sdist install
rm -rf build/ pyunity.egg-info/ docs/build/html/
sphinx-apidoc -e -F -M -o docs/source pyunity pyunity/config.py pyunity/examples/*
sphinx-build -T -E -b html docs/source docs/build/html
git add .
git commit -m %1
git push