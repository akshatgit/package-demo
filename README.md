# Python Package Example

A simple tutorial for an end to end packaging of python applications.

## Structure

```shell
/project/
    /package/
        __init__.py
        module.py
    setup.py
```

## Requirements

```shell
python3.7 -m pip install --user --upgrade setuptools wheel
```

## Build

```shell
python3.7 setup.py sdist bdist_wheel
```

## Testing

Activate Virtualenv:

```shell
source venv/bin/activate
```

Install Wheel Package:

```shell
pip install dist/package-0.1-py3-none-any.whl
```

```shell
(venv) ➜ pip3.7 freeze | grep -i package
package==0.1
```

**Note: Change package version accordingly.

```python
import package
a = package.module.Module
print(a.greeting(a))
```

output: `Hello World`

## References

- [Official Tutorial](https://packaging.python.org/tutorials/packaging-projects/)

- [Communit Article by Geoff Boeing](https://gist.github.com/gboeing/dcfaf5e13fad16fc500717a3a324ec17)
