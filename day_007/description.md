## Palindrome problem
The palindrom problem was super easy not gonna document much. One key takeaway though is: 
```
def digest(self, s):
        s = s.lower()
        for letter in s:
            if letter not in self.valid_letters:
                letter = ''
        return s
```
is wrong because we're setting the local variable letter to an empty string, but this doesn't modify the original string s. Strings in Python are immutable, so you need to build a new string. Instead we need to do this:
```
def digest(self, s):
    s = s.lower()
    result = ''
    for letter in s:
        if letter in self.valid_letters:
            result += letter
    return result
```