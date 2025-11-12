# Exercice 8 notes:
## Zip
- Takes to iterable as paramters and return tuples with elements combined from the two iterables.

```python
a = [1, 2, 3]
b = [4, 5, 6]

c = list(zip(a, b))
print(c)
# [(1, 4), (2, 5), (3, 6)]
```