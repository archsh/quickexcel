#### Makefile for generating files.
PYUIC4=python scripts/pyuic.py
PYRCC4=pyrcc4

UI_FILES = $(wildcard ui/*.ui)
UI_PYS := $(patsubst ui/%.ui,source/ui/%_ui.py,$(UI_FILES))
RC_FILES = $(wildcard ui/*.qrc)
RC_PYS := $(patsubst ui/%.qrc,source/ui/%_rc.py,$(RC_FILES))

uis: $(UI_PYS) $(RC_PYS)

source/ui/%_ui.py: ui/%.ui
	@echo "Compiling UI design file ..."
	@$(PYUIC4) -o $@ $^

source/ui/%_rc.py: ui/%.qrc
	@echo "Compiling UI res file ..."
	@$(PYRCC4) -o $@ $^