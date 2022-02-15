all:

compiler := src/compiler
DIRS+=$(compiler)

unittest := test/unittest
DIRS+=$(unittest)
$(unittest): $(compiler)

TARGETS = all clean cleaner cleanest
.PHONY: $(TARGETS) $(DIRS)
$(TARGETS): $(DIRS)

$(DIRS):
	+$(MAKE) --directory $@ $(MAKECMDGOALS)
