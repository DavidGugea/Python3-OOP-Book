def format_string(string, formatter=None):
    '''Format a string using the formatter object, which is expected to have a format() method that accepts a string.'''
    class DefaultFormatter:
        '''Format a string in title case.'''
        def format(self, input_string):
            return str(input_string).title()

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)

hello_string = "hello world"
print("input : {0}".format(hello_string))
print("output: {0}".format(format_string(hello_string)))