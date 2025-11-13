# Exercice 3 notes:
## Reference vs Value:
- It's passed by reference: The function has access to the original value and can change it.
- It's passed by value: The function only has access to a copy. Changes to the copy within the function don't affect the original.

### Types passed by reference:
- Lists
- Dicts
- Sets

### Types passed by value:
- Integers
- Floats
- Strings
- Booleans
- Tuples

#### Example passing by reference
```python
    def modify_list(inner_lst):
        inner_lst.append(4)
        # the original "outer_lst" is updated
        # because inner_lst is a reference to the original

    outer_lst = [1, 2, 3]
    modify_list(outer_lst)
    # outer_lst = [1, 2, 3, 4]
```

#### Example passing by value
```python
    def attempt_to_modify(inner_num):
        inner_num += 1
        # the original "outer_num" is not updated
        # because inner_num is a copy of the original

    outer_num = 1
    attempt_to_modify(outer_num)
    # outer_num = 1
```