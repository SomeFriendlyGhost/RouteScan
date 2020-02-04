#!/usr/bin/python

import subprocess as sub

option = raw_input("type 0 if you have a TargetList file, 1 if you want to make a targetList from a nmap scan, 2 if you want to read from a file you made youself\n")

def trace(trace_option):
	print(trace_option)
	with open(trace_option) as target_list_file:
        	target_list = target_list_file.readlines()
	print(target_list)
	for target in target_list:
		print(target)
        	if len(target.strip()) > 0:
                	sub.call(['./routeScanCmd', target.strip() ])
def zero():
	print("Zero")
	target_path = "TargetList.txt"
	trace(target_path)

def one():
	print("one")
	targetRange = raw_input("type the path to the file you want to extract")
	sub.call(['./ipExtract',targetRange])
	trace("TargetList.txt")

def two():
	print("two")
	target_path = raw_input("type path to the list of targets\n")
	trace(target_path)


def switch_method(argument):
	switcher={
		0:zero,
		1:one,
		2:two
		}
	switcher[int(argument)]()
	#if argument == "0":
	#	zero()
	#elif argument == "1":
	#	one()
	#elif argument == "2":
	#	two()
	#else:
	#	print("you done goofed")

switch_method(option)
