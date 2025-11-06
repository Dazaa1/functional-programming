# Exercice 2 notes:

## Immutability:
- In functional programming we strive for immutability once a value is created it cannot be changed.
- Generally speaking, immutability means fewer bugs and more maintainable code.

## Tuples vs Lists:
- They are both ordered collections of values, but lists are mutable and tuples are not.

### Lists:
```python
    ages = [16, 21, 30]
    # 'ages' is being changed in place
    ages.append(80)
    # [16, 21, 30, 80]
```

### Tuples:
```python
    ages = (16, 21, 30)
    more_ages = (80,) # note the comma! It's required for a single-element tuple
    # 'all_ages' is a brand new tuple
    all_ages = ages + more_ages
    # (16, 21, 30, 80)

    # or we can even reassign the same variable to point to a new tuple:
    ages = ages + more_ages
    # (16, 21, 30, 80)
```