When defining a class, don't forget the 
```
class [name]:
	def __init__(self,args*):
		self.[class_attributes] = whatever
```

def init ;)

--------

Functions inside a class can use staticmethod if they don't rely on the class attributes but should belong inside the class structurally i.e 

```
class [name]:
	def __init__(self,stuff):
		attribute definitions

	@staticmethod
	def unrelated(args*):
		logic that doesn't care about any of the [self.] class attributes

	def related(self,args*):
		logic that does care about the [self.] attributes
```

------------

To import classes, it's as simple as 

```
from [foldername].[filename] import [classname]


name = [classname]()

function_return = name.[function_in_class](args*)
```

alongside a setup.py in the base dir with 

```
from setuptools import setup, find_packages
setup(
    name='qr_proj',
    version='0.1',
    packages=find_packages(),
)
```

and run in the terminal pip install -e .

