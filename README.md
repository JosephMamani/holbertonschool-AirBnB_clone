First step towards the AirBnb clone project.
# AirBnB clone - The console
### First step: Write a command interpreter to manage your AirBnB objects
This is the first step towards our final project: a copy of the AirBnb website. The command interpreter will:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc.
- Do operations on objects (count, compute stats, etc)
- Update attributes of an object.
- Destroy an object.

### Learning Objectives
- How to create a Python package.
- How to create a command interpreter in Python using the cmd module.
- What is Unit testing and how to implement it in a large project.
- How to serialize and deserialize a Class.
- How to write and read a JSON file.
- How to manage `datetime`
- What is an `UUID`
- What is `*args` and `**kwargs` and how to use it.
- How to handle named arguments in a function.

### Execution
The command interpreter should work like this in interactive mode:
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Files
| File | Description |
| ------------- | ------------- |
| console.py  | The command interpreter  |
| models  | Contains all the classes  |
| tests   | Unitest files   |

### How to use the console
With `./console.py` you will enter the command interpreter:

```
$ ./console.py
(hbnb)
(hbnb) 
(hbnb) quit 
```

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220704%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220704T193438Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2ce8ccb25df8e174d7e62b8a8b5975b321fa4d9e89cd4e74fbc9a752bea1f43a)
