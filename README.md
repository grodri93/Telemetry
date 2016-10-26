# Telemetry
The project currently parses a string, seperating and organizing all the sensor data.
## Getting Started
The programs here use Python 2.7.12. These instructions should work for Linux and Windows machine.
### Prerequisites
#### Linux:
Python should already be built in linux. In terminal type to test:
```
python
```
If succesful, the python version should print out. It should look similar:
```
Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
#### Windows:
Since Windows doesn't have terminal you will have to use Windows PowerShell. It's already installed in Windows.
Install python from http://python.org/download. Open up PowerShell and type in
```
python
```
If it does not work type this in PowerShell
```
[ENVIRONMENT]::SETENVIRONMENTVARIABLE("PATH", "$ENV:PATH;C:\PYTHON27", "USER")
```
Restart PowerShell and try again. If it does not work, try restarting computer.
### Using parsedata.py
To use the functions from here, type this line in the beggining of program. 

NOTE: parsedata is where the function is and parse is the function name.
```
from parsedata import parse
```
Currently parsedata only contains parse function. The function takes in a string and parses the string by looking for ';' and seperating the string. Then it organizes and returns a dictionary with all the info.
#### Example:
```
sensor = parse("123;456;789")
```
The sensor variable should contain all the values organized and converted to numbers. Look at test_parsedata.py to see the full example. To run type,
```
python test_parsedata.py
