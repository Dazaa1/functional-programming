# Exerice 1 notes

- Functional programming is a parogramming paradigm, it is about declaring what you want to happen instead of how you want it to happen.


## Difference between imperative code and functional code:

#### Imperative code:
```python
    car = create_car()
    car.add_gas(10)
    car.clean_windows()
```

#### Functiona code:
```python
    return clean_windows(add_gas(create_car()))
```