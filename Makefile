#### Makefile for generating files.
PYUIC4=python scripts/pyuic.py
PYRCC4=pyrcc4
PYLUPDATE4=pylupdate4
LANGUAGES := zh-CN zh-TW en-US en-GB fr-FR es-SP

UI_FILES = $(wildcard ui/*.ui)
UI_PYS := $(patsubst ui/%.ui,source/quixcel/ui/base/%_ui.py,$(UI_FILES))
RC_FILES = $(wildcard ui/*.qrc)
RC_PYS := $(patsubst ui/%.qrc,source/quixcel/ui/base/%_rc.py,$(RC_FILES))
TS_FILES = $(LANGUAGES:%=source/locale/%.ts)
UI_REMADE := $(patsubst source/quixcel/ui/base/%_ui.py,source/quixcel/ui/%.py,$(UI_PYS))

uis: $(UI_PYS) $(RC_PYS)
ts: $(TS_FILES)
#uiremade: $(UI_REMADE)

source/quixcel/ui/%.py: source/quixcel/ui/base/%_ui.py $(MAKEFILE)
	@echo "Generating UI remaded py ..."
	@echo "# -*- coding: utf-8 -*-" > $@
	@echo "" >> $@
	@echo "from PyQt4 import QtCore, QtGui" >> $@
	@echo "from .base.$(^:source/quixcel/ui/base/%_ui.py=%_ui) import $(^:source/quixcel/ui/base/%_ui.py=Ui_%)" >> $@
	@echo "" >> $@
	@echo "class $(@:source/quixcel/ui/%.py=%)(QtGui.QWidget,$(^:source/quixcel/ui/base/%_ui.py=Ui_%)):" >> $@
	@echo "    pass" >> $@
	@echo "" >> $@
	@unix2dos $@

source/locale/%.ts: $(UI_PYS) $(UI_REMADE) source/main.pyw
	@echo "Generating $@ ..."
	@mkdir -p $(@D)
	@echo "$(PYLUPDATE4) $^ -ts $@"
	@$(PYLUPDATE4) $^ -ts $@

source/quixcel/ui/base/%_ui.py: ui/%.ui
	@echo "Compiling UI design file ..."
	@$(PYUIC4) -o $@ $^

source/quixcel/ui/base/%_rc.py: ui/%.qrc
	@echo "Compiling UI res file ..."
	@$(PYRCC4) -o $@ $^