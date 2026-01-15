# Compiler
CC = gcc

# Compiler flags
# -fPIC is required to generate position-independent code for shared libraries
CFLAGS = -Wall -Wextra -std=c11 -fPIC

# Output shared library name (convention usually requires 'lib' prefix and .so extension)
TARGET = libmain.so

# Source files
SRCS = main.c cs50.c

# Build rule
$(TARGET): $(SRCS)
	$(CC) $(CFLAGS) -shared $(SRCS) -o $(TARGET)

# Clean up compiled files
clean:
	rm -f $(TARGET)

