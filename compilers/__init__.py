import sublime

if sublime.version() < '3':
    from googleclosurecall import GoogleClosureCall
    from cssminifiercall import CssminifierCall
else:
    from Minifier.compilers.googleclosurecall import GoogleClosureCall
    from Minifier.compilers.cssminifiercall import CssminifierCall