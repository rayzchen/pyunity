@ECHO OFF

py -m unittest tests.py
py -m autopep8 -i -r --ignore E301,E302 pyunity setup.py prepare.py cli.py
py prepare.py
py -3.6 setup.py build -c mingw32 bdist_wheel -d dist\0.4.0\
py -3.7 setup.py build -c mingw32 bdist_wheel -d dist\0.4.0\
py -3.8 setup.py build -c mingw32 bdist_wheel -d dist\0.4.0\
py setup.py build -c mingw32 bdist_wheel -d dist\0.4.0\ sdist -d dist\0.4.0\
RMDIR /S /Q docs\en\
DEL docs\source\pyunity*
set SPHINX_APIDOC_OPTIONS=members,inherited-members,show-inheritance
sphinx-apidoc -e -F -M -o docs\source pyunity pyunity\config.py pyunity\examples\*
sphinx-build -T -E -b html docs\source docs\en
RMDIR /S /Q build\ pyunity.egg-info\
IF NOT [%1] == [] (
git add .
git commit -m %1
git push
)
start py -3.6 -m pip install -U dist\0.4.0\pyunity-0.4.0-cp36-cp36m-win32.whl
start py -3.7 -m pip install -U dist\0.4.0\pyunity-0.4.0-cp37-cp37m-win32.whl
start py -3.8 -m pip install -U dist\0.4.0\pyunity-0.4.0-cp38-cp38-win32.whl
py -m pip install -U dist\0.4.0\pyunity-0.4.0-cp39-cp39-win32.whl