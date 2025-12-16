# # Compiler
# CC = gcc

# # Compiler flags
# CFLAGS = -Wall -Wextra -std=c11

# # Output executable name
# TARGET = main

# # Source files
# SRCS = hello.c cs50.c gb.c

# all: $(TARGET)

# # Build rule
# $(TARGET): $(SRCS)
# 	$(CC) $(CFLAGS) $(SRCS) -o $(TARGET)

# # Run the program
# run: $(TARGET)
# 	./$(TARGET)

# # Clean up compiled files
# clean:
# 	rm -f $(TARGET)

# ci: all run clean

# .PHONY: run clean












# Compiler
CC = gcc

# Compiler flags
# -fPIC is required to generate position-independent code for shared libraries
CFLAGS = -Wall -Wextra -std=c11 -fPIC

# Output shared library name (convention usually requires 'lib' prefix and .so extension)
TARGET = libmain.so

# Source files
SRCS = hello.c cs50.c gb.c

# Build rule
$(TARGET): $(SRCS)
	$(CC) $(CFLAGS) -shared $(SRCS) -o $(TARGET)

# Clean up compiled files
clean:
	rm -f $(TARGET)

