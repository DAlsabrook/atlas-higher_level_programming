#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find("obj"): str.find("lang")]\
	  + str[str.find("wi"):str.find("very")]\
		  + str[:str.find("is")]
print(str)
