# sublime-halftheory-minifier
## A Javascript and CSS Minifier for Sublime Text

The plugin supports [Google Closure Compiler](https://developers.google.com/closure/compiler/) for Javascript minification and [cssminifier](https://www.cssminifier.com/) for CSS minification.

This module was forked from [Sublime-Minifier](https://github.com/bistory/Sublime-Minifier) which was forked from [JsMinifier](https://github.com/cgutierrez/JsMinifier).

## Install
```
cd ~/Library/Application\ Support/Sublime\ Text/Packages
git clone https://github.com/halftheory/sublime-halftheory-minifier Minifier
# open SublimeText > Package Control: Satify Dependencies
```
Usage
-----

__Windows__ / __Linux__ default key binding:    
`ctrl + alt + m` - attempts to minify the current buffer and replaces the buffers content    
`ctrl + alt + shift + m` - attempts to minify the current buffer and saves the output to a separate file.

__MacOSX__ default key binding:    
`⌘ + alt + m` - attempts to minify the current buffer and replaces the buffers content    
`⌘ + alt + shift + m` - attempts to minify the current buffer and saves the output to a separate file.


Installation
------------
**Without Git:** Download the latest source from [GitHub](https://github.com/halftheory/sublime-halftheory-minifier) and copy the whole directory into the Packages directory. Make sure folder name is "Minifier".

**With Git:** Clone the repository in your Sublime Text 2 or 3 Packages directory, located somewhere in user's "Home" directory:

    `git clone git://github.com/halftheory/sublime-halftheory-minifier.git Minifier`

The "Packages" packages directory is located at:

* OS X:

ST2 : `~/Library/Application Support/Sublime Text 2/Packages/`
ST3: `~/Library/Application Support/Sublime Text 3/Packages/`
ST4: `~/Library/Application Support/Sublime Text/Packages/`

* Linux:

ST2 : `~/.Sublime Text 2/Packages/`
ST3 : `~/.Sublime Text 3/Packages/`
ST4 : `~/.Sublime Text/Packages/`

* Windows:

ST2 : `%APPDATA%/Sublime Text 2/Packages/`
ST3 : `%APPDATA%/Sublime Text 3/Packages/`
ST4 : `%APPDATA%/Sublime Text/Packages/`
