# Debugging and Modules
Use this as a resource to get your head around the debugger by using it to learn how modules in python work.

## Why Debug
The debugger is a program you can use to inspect your program in python.
When programming it is necessary to understand how your functions, logic and variables are interacting.
You could try very hard to make up a mental picture of how the computer will reason about your code.
Since your computer is already doing that by running the program, just ask it to tell you. A debugger is how you do that.

## Instructions

1. Open Visual Studio code
1. Open your **folder**
    1. File > "Open Folder"
    2. Choose the folder your work is **in**
1. Install the Python Extension
    1. "View > Extensions" or the last icon on the left
    1. Search for "Python" get the one from author "Don Jayamanne"
    1. Install, wait
    1. Enable
1. View your code. The top left icon is the files View
1. On one of your code file press F5 to start the debugger
1. This will create a `launch.json` file that VS code uses to learn how to run your work. You can ignore this.
1. Since our program requests user input, it will hang in the background when VS Code runs it. Change the to the External debug option to get user input.

Currently you will have to install that plugin every time you log on.

## This Demo

### Part 1
1. Open this folder in visual studio.
1. Follow the instructions to get VS set up correctly
1. Open `myModule.py` and place a breakpoint at line 4
1. Have a look around the variables and "step over" the code
1. Remove your breakpoints when finished

### Part 2
1. Open main.py and place a breakpoint at line 7
1. See the module "example" is available from the file `myModule` we just looked at
1. "step into" the function `demonstration` from `example` and you'll see the same function from part 1

## Advanced `launch.json` Options

Now your happy with using the debugger, you can tell it to do some more work for you.
Open that `launch.json` file again because we want to add another run option.

1. Copy the object with the name "External Terminal/Console" to a new one.
1. Give it a new name in the field `name`
1. When we git F5 we know we just want to run the program, tell VS code to do that too in `stopOnEntry`
1. Our code always uses a start file to enter the menu. Tell VS code to always run that and not our currently open file with `program`

Have a look at the example settings below.

```json
{
    "name": "My Project Settings",
    "type": "python",
    "request": "launch",
    "stopOnEntry": false,
    "pythonPath": "${config.python.pythonPath}",
    "program": "${workspaceRoot}/main.py",
    "console": "externalTerminal",
    "debugOptions": [
        "WaitOnAbnormalExit",
        "WaitOnNormalExit"
    ]
}
```
