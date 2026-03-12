## Valid Parenthesis:
Mostly easy problem just one important line of code in here
```
if stack.top()==self.opening_parenthesis[self.closing_parenthesis.index(parenthesis)]:
```
basically this is checking if the parenthesis is of closing parenthesis type then does it correspond to opening parenthesis on top or not by equating with the parenthesis at the same index as the closing parenthesis

## Remove Consecutive Characters:
super simple problem, i just maintained a previous character variable and compared every character to that previous character