![This is a alt text.](https://user-images.githubusercontent.com/107968573/216862342-3bd995bb-a40c-4fcd-a66b-d0473af89352.png "hehe")

# :sparkles: 0x00. AirBnB clone - The console :sparkles:

## :bulb: Purpose (description of project)

This particular project is a small, but important piece of a large puzzle. We are writing a command interpreter to manage our upcoming AirBnB clone projects.

## :star: Description (of command interpreter)
The console is the command line interface which allows a user to create allowed classes, delete classes, and add attributes to classes. The console works in both interactive and non-interactive mode. 
To enter interactive mode:
```$ ./console.py```
After you've launched interactive mode you will be presented with a new prompt as shown:
```(hbnb) ```
It also works in non-interactive mode, and you enter it with:
```$ echo "create BaseModel" | ./console```
You'll have a list of commands you're able to use including:
```help, create, show, all, update, and quit```
To exit the console you use:
Ctrl+Z on the keyboard

### Information (how to start it, how to use it)
Objectives of the project are to:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### Example
```$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create
Creates new instance of BaseModel
(hbnb) help 
```
## :bulb: Contributors
###### This project was brought to you by the following contributors:

__*Teylor Chapman*__

![This is a alt text.](https://avatars.githubusercontent.com/u/111523192?v=4 "@teylorchapman")

__*Lindsey Thomas*__

![This is a alt text.](https://pbs.twimg.com/media/FghkAgdXEAAX0BV?format=jpg&name=medium "@timidgeek")

###### *Thank you for  your time.* :sparkles:
