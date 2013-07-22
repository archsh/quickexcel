#### Makefile for generating files.
PYUIC4=python scripts/pyuic.py
PYRCC4=pyrcc4

UI_FILES = $(wildcard ui/*.ui)
UI_PYS := $(patsubst ui/%.ui,source/ui/base/%_ui.py,$(UI_FILES))
RC_FILES = $(wildcard ui/*.qrc)
RC_PYS := $(patsubst ui/%.qrc,source/ui/base/%_rc.py,$(RC_FILES))

UI_REMADE := $(patsubst source/ui/base/%_ui.py,source/ui/%.py,$(UI_PYS))

uis: $(UI_PYS) $(RC_PYS)

uiremade: $(UI_REMADE)

source/ui/%.py: source/ui/base/%_ui.py $(MAKEFILE)
	@echo "Generating UI remaded py ..."
	@echo "# -*- coding: utf-8 -*-" > $@
	@echo "" >> $@
	@echo "from PyQt4 import QtCore, QtGui" >> $@
	@echo "from .base.$(^:source/ui/base/%_ui.py=%_ui) import $(^:source/ui/base/%_ui.py=Ui_%)" >> $@
	@echo "" >> $@
	@echo "class $(@:source/ui/%.py=%)(QtGui.QWidget,$(^:source/ui/base/%_ui.py=Ui_%)):" >> $@
	@echo "    pass" >> $@
	@echo "" >> $@
	@unix2dos $@

source/ui/base/%_ui.py: ui/%.ui
	@echo "Compiling UI design file ..."
	@$(PYUIC4) -o $@ $^

source/ui/base/%_rc.py: ui/%.qrc
	@echo "Compiling UI res file ..."
	@$(PYRCC4) -o $@ $^