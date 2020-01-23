# Makefile created with Create Makefile.sh 13/12/2011

ifeq ($(shell uname), Darwin)  # If macOS
OpenMP=-Xpreprocessor -fopenmp
LOpenMP=-lomp
else
OpenMP=-fopenmp
LOpenMP=-lgomp
endif
COPT      = -O3
CFLAGS    = $(COPT) $(OpenMP)
CSTRICT   = -Wall -Wextra -ansi
CXXOPT    = -O3
CXXFLAGS  = $(CXXOPT) $(OpenMP) -fPIC
CXXSTRICT = -Wall -Wextra -ansi
LDFLAGS   = -lpng -lm -lfftw3f -lfftw3f_threads $(LOpenMP)
EXEC      = ponomarenko
LIB       = libpono.so

default: $(EXEC)
all: $(EXEC)
lib: $(LIB)

# ------- C files -------
# ------- C++ files -------
./framework/CFramework.o: ./framework/CFramework.cpp ./framework/CFramework.h
	$(CXX) $(CXXFLAGS) -c ./framework/CFramework.cpp -o ./framework/CFramework.o

./framework/libparser.o: ./framework/libparser.cpp ./framework/libparser.h
	$(CXX) $(CXXFLAGS) -c ./framework/libparser.cpp -o ./framework/libparser.o

./framework/CHistogram.o: ./framework/CHistogram.cpp
	$(CXX) $(CXXFLAGS) -c ./framework/CHistogram.cpp -o ./framework/CHistogram.o

./framework/CImage.o: ./framework/CImage.cpp ./framework/CImage.h
	$(CXX) $(CXXFLAGS) -c ./framework/CImage.cpp -o ./framework/CImage.o

./framework/CInspector.o: ./framework/CInspector.cpp ./framework/CInspector.h
	$(CXX) $(CXXFLAGS) -c ./framework/CInspector.cpp -o ./framework/CInspector.o

./framework/framework.o: ./framework/framework.cpp
	$(CXX) $(CXXFLAGS) -c ./framework/framework.cpp -o ./framework/framework.o

./framework/operations.o: ./framework/operations.cpp
	$(CXX) $(CXXFLAGS) -c ./framework/operations.cpp -o ./framework/operations.o

./curve_filter.o: ./curve_filter.cpp ./curve_filter.h
	$(CXX) $(CXXFLAGS) -c ./curve_filter.cpp -o ./curve_filter.o

./algo.o: ./algo.cpp ./algo.h
	$(CXX) $(CXXFLAGS) -c ./algo.cpp -o ./algo.o

# ------- Main -------
$(EXEC):  ./framework/CFramework.o ./framework/libparser.o ./framework/CHistogram.o ./framework/CImage.o ./framework/CInspector.o ./framework/framework.o ./framework/operations.o ./curve_filter.o ./algo.o
	$(CXX)  ./framework/CFramework.o ./framework/libparser.o ./framework/CHistogram.o ./framework/CImage.o ./framework/CInspector.o ./framework/framework.o ./framework/operations.o ./curve_filter.o ./algo.o $(LDFLAGS) -o $(EXEC)

$(LIB):  ./framework/CFramework.o ./framework/libparser.o ./framework/CHistogram.o ./framework/CImage.o ./framework/CInspector.o ./framework/operations.o ./curve_filter.o ./algo.o
	$(CXX) $^ $(LDFLAGS) -o $(LIB) -fPIC -shared

lint:
	$(MAKE) CFLAGS="$(CFLAGS) $(CSTRICT)" CXXFLAGS="$(CXXFLAGS) $(CXXSTRICT)"

clean:
	rm -f *.o *.so framework/*.o

distclean: clean
	rm -f $(EXEC)

