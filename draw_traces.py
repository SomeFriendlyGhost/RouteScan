#!/usr/bin/env python3

import csv
import argparse
from graphviz import Digraph
import math
from pygraphviz import *

def read_trace_file(filename: str = 'routeScan.txt'):
    with open(filename) as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        read_csv.__next__()
        for row in read_csv:
            yield row

def parse_trace(trace):
    ret_dict ={}
    
    try:
        for colnumber in range(1,31):
            if colnumber == 1:
                tup = (trace[0], trace[2])
            else:
                tup = (trace[colnumber], trace[colnumber+1])
            
            if tup in ret_dict.keys():
                ret_dict[tup] = ret_duct[tup] + 1
            else:
                ret_dict[tup] = 1
    except IndexError:
        pass
        
    return ret_dict

def get_trace_tupples(trace):
    try:
        for colnumber in range(1,31):
            if colnumber == 1:
                tup = (trace[0].strip(), trace[2].strip())
            else:
                tup = (trace[colnumber].strip(), trace[colnumber+1].strip())
            
            if '*' in tup:
                continue
            if '' in tup:
                continue
            
            
            yield tup
            
    except IndexError:
        pass

        
def Draw_it(Dictionary, g, min_count=1):
    for (src, dst) in SourceDestDictionary.keys():
        if SourceDestDictionary[(src,dst)] >= min_count:
            g.node(src.replace(':', '-'), src)

    for (src, dst) in sorted(SourceDestDictionary.keys()):
        if SourceDestDictionary[(src,dst)] >= min_count:
            occ = SourceDestDictionary[(src, dst)]
            g.edge(src.replace(':', '-'),
               dst.replace(':', '-'),
               penwidth=str(2 + math.log(occ)), tooltip="count: {}".format(occ))
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    SourceDestDictionary = {}
    #g = AGraph(strict=False, directed=True)
    g = Digraph('G', filename='file.dot')
    colonnPointer1 = 0
    colonnPointer2 = 1

    for trace in read_trace_file(args.filename):
        for tup in get_trace_tupples(trace):
            if tup in SourceDestDictionary.keys():
                SourceDestDictionary[tup] = SourceDestDictionary[tup] + 1
            else:
                SourceDestDictionary[tup] = 1
    Draw_it(SourceDestDictionary, g, 10)
  
    for t in SourceDestDictionary:
        print( SourceDestDictionary[t], t )

    g.view()
    g.graph_attr.update(overlap='false', ranksep='0.1', rankdir='LR')
    g.save('file.dot')
    g.render('file.png')
