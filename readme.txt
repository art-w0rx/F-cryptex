The program is designed to encrypt files of various formats (archives, text documents, tables, music, and so on)
The program requires Python version 3 and higher, as well as libraries (pycryptodome, simple-script), 
which can be installed using pip via the console.
The program works on Linux and also on Android via PyDroid everything works fine. 
Initially, the stdiomask library was used to hide the input of password characters, 
but later began to use the standard getpass library, since PyDroid did not work with stdiomask.
