## print Function
print('Hello World')            # displays output (argument: any type of data)
print('A Number:', 302)         # can display multiple items with commas (argument list: any type of data)
        
print('One', end=' ')           # End Manipulator changes the string attached at the end
print('Two')                    # default: end='\n'

print('One', 'Two', sep='*')    # Separator changes the string between multiple arguments
print('One', 'Two')             # default: sep=' '

print('One', 'Two', 'Three', sep='\t', end='\tdone!')
