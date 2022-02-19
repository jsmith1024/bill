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
.PHONY: docs
docs:
	./doxy

# Running tests
.PHONY: test
test: all
	test/unittest/bill_test.exe


