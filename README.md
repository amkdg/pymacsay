# pymacsay
pymacsay is a wrapper for the command-line tool `say` in macOS

`say` is a command-line tool that converts text to audible speech.

### How to use pymacsay
Use `pip install pymacsay` to install pymacsay

### Quick Example
```python
# Import the Say class from the pymacsay module
from pymacsay import Say

# Obtain an instance of `Say`. To create an instance, you need to provide the path to `say`.
# It should be pre-installed and is located in /usr/bin/say by default.
say = Say('/usr/bin/say')

# Now try it!
say.say("Hi!")

# Optionally, you can change the voice using the `voice=` argument. The argument accepts a string with the name of the voice
# Here are some of the available voices: 'victoria', 'samantha', 'fred', 'alex'
say.say("Hello.", voice='victoria')

# Another optional argument is `rate=`. It simply changes the speaking rate.
# The argument accepts an Integer. The rate is measured in words per minute.
say.say('Helllooooo!', voice='fred', rate=20)
```

