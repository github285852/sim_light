
CC = gcc
FLAGS = -fPIC -shared
SRC = cct.c mymath.c
INCLUDE = ./
libcct.so:
	$(CC) $(SRC) $(FLAGS) -o libcct.so
# gcc cct.c mymath.c -fPIC -shared -o libcct.so

#cct.o: cct.c
#	$(CC) cct.c -o cct.o
#
#mymath.o: mymath.c
#	$(CC) -c mymath.c

.PHONY:clean
clean:
	-rm -rf *.o


