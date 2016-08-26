PIP = /usr/bin/pip
PY = /usr/bin/python3
PYI = /usr/bin/pyinstaller
RM = rm -r
APP = txth

run:
	$(PY) $(APP).py

compile:
	$(PYI) -F --path /usr/lib/python3.5/site-packages/textile $(APP).py
	$(RM) build __pycache__ $(APP).spec

depends:
	$(PIP) install textile pyinstaller

