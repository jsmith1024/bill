all:

PROG = bill

CXXFLAGS+= -Wall
CXXFLAGS+= -Werror
CXXFLAGS+= -O3
#CXXFLAGS+= -lboost_unit_test_framework		# these lines required for test
#LIBS+= boost/test/included/unit_test.hpp
#LIBS+= boost_unit_test

#unit_test.o: unit_test.hpp
#	g++ -o unit_test.o -c boost/test/unit_test.hpp ${CXXFLAGS}


OBJECTS+= src/compiler/repl/REPL.o

PROG_OBJECTS+= src/compiler/main.o
# PROG_OBJECTS+= src/docuprep/main.o		# to be added later

TEST_OBJECTS+= test/test.o
TEST_OBJECTS+= test/test_REPL.o

REPL.o: REPL.h

all: $(OBJECTS) $(PROG_OBJECTS)
	g++ -o $@ $^ ${CXXFLAGS} ${LIBS}

test: $(OBJECTS) $(TEST_OBJECTS)
	g++ -o $@ $^ ${CXXFLAGS} ${LIBS}

%.o: %.cpp
	g++ -o $@ -c $< ${CXXFLAGS}

clean:
	-rm ${OBJECTS} $(TEST_OBJECTS) $(PROG_OBJECTS)
