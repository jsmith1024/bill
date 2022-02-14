all:

compiler := src/compiler

DIRS+=$(compiler)

TARGETS = all clean cleaner cleanest
.PHONY: $(TARGETS) $(DIRS)
$(TARGETS): $(DIRS)

$(DIRS):
	+$(MAKE) --directory $@ $(MAKECMDGOALS)

