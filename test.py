#!/usr/bin/python3
import shlex

string = 'Destroy User asadasad-dsdsd-sf43e3e3-e3 \'{"lol": 13.2, "gre": "hello"}\''
print(shlex.split(string))