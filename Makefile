all:

# Dependency-order sorted list of directories to build
DIRS+=src/compiler
DIRS+=test/unittest

# General commands
#

# General build rule
#
# Note: This rule runs after other rules, so all cannot depend on test 
# since the test won't be built first.
.PHONY: all clean cleaner cleanest
all clean cleaner cleanest:
	$(foreach dir,$(DIRS),$(MAKE) --directory $(dir) $@ && ) true

# Documentation building
PDFS+= docs/Primer.pdf
PDFS+= docs/Reference_Manual.pdf
PDFS+= docs/Standard_Library_Reference.pdf
PDFS+= docs/User_Manual.pdf

.PHONY: docs
docs: $(PDFS)
	doxygen dox/doxyfile
	cp dox/index.html  docs/index.html  # So docs/ is *all* temporary files
	cp dox/_config.yml docs/_config.yml # So docs/ is *all* temporary files

.PHONY: FORCE
FORCE:

TMP_DIR=/tmp/bill
TMP_DIR:
	if [ !-e $(TMP_DIR) ] ; then ; mkdir /tmp/bill ; fi

docs/%.pdf: FORCE | $(TMP_DIR)
	doxygen $(@:docs/%.pdf=dox/books/%/doxyfile)
	cd $(@:docs/%.pdf=$(TMP_DIR)/%/latex) && make
	cp $(@:docs/%.pdf=$(TMP_DIR)/%/latex/refman.pdf) $@

# Running tests
.PHONY: test
test: all
	test/exampletest/bill_examples.sh dox "echo TODO: Compile "
	test/unittest/bill_test.exe
