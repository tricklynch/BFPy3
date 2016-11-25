Zed Shaw, author of Learn Python the Hard Way, made the claim that Python 3 is not Turing complete[1]. This is blatantly false. If you can use a language, referred to as a host language, to implement a Turing complete language, you can then use the Turing complete language to compute anything that is computable. Since this is all running in the host language, that shows that the host language is also Turing complete.

The default values are meant to force portability, in accordance with [2], in writing your brainfuck, but there will be command line flags to set up the machine however you want.

[1] https://learnpythonthehardway.org/book/nopython3.html 
[2] http://www.muppetlabs.com/~breadbox/bf/standards.html
