# AirBnB clone
The **AirBnb Clone** project is one of the biggest project of the ALX SE Program.
The goal is to create a clone of a [Airbnb website](https://www.airbnb.com/).
The first step is to create a command interpreter or a console.
# The Console

## Objectives
- Creates data models(User, City,...)
- Manage those models with a console
- store the objects of the models to a JSON file

## Usage
It has two modes of execution:
+ Interactive mode

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
+ Non Interactive mode
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
### Usage in interactive mode
- Start the console: `./console.py`
- Seek The available commands: `help`
- Describe the command: `help 'command'`. For example `help create`
- Execute a command: `'command' 'Argmunets'`. For example `Create User`
- Exit the console: `quit` or `EOF`
