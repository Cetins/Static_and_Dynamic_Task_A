### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame: #Class hasn't been initialised

  def check_for_ace(self, card):
    if card.value = 1:  # this line is not checking a condition but reassigns the value >> if card.value == 1:
      return True
    else  # missing :   also we don't need and else condition we can return false as default
      return False
   

  dif highest_card(self, card1 card2):  # Typo dif >> def also there should be a comma after card1
  if card1.value > card2.value: #indentation error lines 27 to 30 should be indented 1 tab
    return card # Undefined variable <card> it should be <card1>
  else:
    return card2
  


def cards_total(self, cards): # indentation error whole funtction is out of class scope, no need to use cards as a parameter
                              # class has cards property
  total # total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total  # indentation error should be indented back 1 tab
    
    # return (f"You have a total of {total}")
  
```
