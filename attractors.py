# -*- coding:utf-8 -*-
"""
Author: Ling-Han Jiang
Date: 2017.6.9
Citing: Chu X-Y, Jiang L-H, Zhou X-H, Cui Z-J, Zhang H-Y. Evolutionary Origins of Cancer Driver Genes and Implications for Cancer Prognosis. Genes. 2017; 8(7):182.
Python: 2.7.12(not working for 3.x)
"""

import os, argparse, time, random
import pandas as pd
import numpy as np
from multiprocessing import Pool
from scipy.integrate import odeint


def function_producion(frame, n, k):
    function = []
    v1 = ''
    v2 = ''
    ep = 'def solve(w,t,n):'+'\n'
    for row in range(len(frame.index)):
        p1 = unicode(frame.iat[row,0])
        p2 = unicode(frame.iat[row,1])
        # p1 = str(frame.iat[row,0])
        # p2 = str(frame.iat[row,1])
        if p1!='nothing':
            if ',' in p1:
                p1 = p1.split(',')
    #            p1 = ['x' + str(dic[item.strip()]) for item in p1]
                p1 = ['x' + str(item.strip()) for item in p1]
                p1 = '+'.join([item+'**'+str(n) for item in p1])
                p1 = '(' + p1 + ')/(' + str(k) + '+(' + p1 + '))'
            else:
    #            p1 = 'x' + str(dic[p1.strip()])
                p1 = 'x' + str(p1.strip())
                p1 = '('+ p1 + '**' + str(n) + ')/(' + str(k) + '+(' + p1 + '**' + str(n) + '))'
        else:
            p1 = ''
        if p2!='nothing':
            if ',' in p2:
                p2 = p2.split(',')
    #            p2 = ['x' + str(dic[item.strip()]) for item in p2]
                p2 = ['x' + str(item.strip()) for item in p2]
                p2 = '+'.join([item+'**'+str(n) for item in p2])
                p2 = str(k) + '/(' + str(k) + '+(' + p2 + '))'
            else:
    #            p2 = 'x' + str(dic[p2.strip()])
                p2 = 'x' + str(p2.strip())            
                p2 = str(k) + '/(' + str(k) + '+(' + p2 + '**' + str(n) + '))'
        else:
            p2 = ''
    #    num = str(frame.index[row][1])
        num = str(frame.index[row])
        if p1!= '':
            if p2 != '':
                f = 'dx' + num + 'dt=' + p1 + '*' + p2 + '-x' + num
            else:
                f = 'dx' + num + 'dt=' + p1 + '-x' + num
        else:
            f = 'dx' + num + 'dt=' + p2 + '-x' + num
        v1 += 'x'+num+', '
        v2 += 'dx' + num + 'dt' +', '
        function.append('\t' + f + '\n')
    #    print f
    ep += '\t' + v1[:-2] + '= w' + '\n' + ''.join(function)
    ep += '\t' + 'return np.array(['+ v2[:-2] + '])' + '\n'
    # print(ep)
    exec(ep)# in locals(), globals()

    global solve2
    solve2 = solve
    
def attractor(frame,start_list):
    # Initial vector
    t = np.arange(0, FLAGS.time_step, 1)
    if start_list != []:
        start = tuple(start_list)
    else:
        start_range = len(frame[0].index)+1
        start = tuple([random.random() for i in range(1,start_range)]) 
    # Iteration
    track1 = odeint(solve2, start, t, args=(4,))    
    delta = track1[-1] - track1[-2]
    delta = np.abs(delta)
    # Judge if converge
    if (delta < np.array([FLAGS.delta]*len(delta))).all():
        pass
    else:
        print 'WRONG!!!'
    return [('%.4f' % abs(item))for item in track1[-1]]

def network_frame(
        outputfile,
        frame,
        start_list,
        round):
    # multiprocessing  
    time1 = time.time()
    PPP = Pool()
    result = []
    for i in range(round):
        r = PPP.apply_async(attractor,([frame],start_list))
        result.append(r)
    PPP.close()
    PPP.join()
    # Calculate attractors
    attractors = []
    attractors_dic = {}
    temp_lst = []
    for temp in result:
        temp = temp.get()
        if str(temp) not in temp_lst:
            attractors.append(temp)
            attractors_dic[str(temp)] = 0
            temp_lst.append(str(temp))
        else:
            attractors_dic[str(temp)] += 1
    # Save attractors
    f = open(os.path.join(os.getcwd(),outputfile+'.txt'),'w+')
    for i in attractors_dic:
        f.write(str(attractors_dic[i]) + '\t' + str(i) + '\n')
    f.close()
    time2 = time.time()
    print '%.2fs used ' %(time2 - time1)
    return len(attractors)
    
def Attractor_Calculation(
          input_path = 'network_without_0.xlsx',
          folder = '0', 
          outputfile='Attractors',
          round = 200,
          start_list = [],
          n = 3,
          k = 0.125):
    # Create folder
    folder_path = os.path.join(os.getcwd(), folder)
    try:
        os.makedirs(folder_path)
    except:
        pass
     # Read network  
    frame = pd.read_excel(input_path,sheetname='Sheet1')
    frame = frame.fillna('nothing')
    # Product function
    function_producion(frame,n,k)
    # Calculate attractors
    outputfile = os.path.join(folder,outputfile)
    # print(start_list)
    result = network_frame(outputfile,frame,start_list,round)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
          "--network_path","-net",
          type=str,
          default="network_origion.xlsx", 
          help="network file path"
        )
    parser.add_argument(
          "--round","-r",
          type=int,
          default=200,
          help="iteration number"
        )
    parser.add_argument(
           "--n","-n",
            type=int,
            default=3,
            help="Hill coeficient"
        )
    parser.add_argument(
            "--k","-k",
            type=float,
            default=0.125,
            help="parameter describing kinetic properties of x"
        )
    parser.add_argument(
           "--delta","-d",
            type=float,
            default=0.0001,
            help="convergence threshold"
        )
    parser.add_argument(
            "--start_list_path","-s",
            type=str,
            default="",
            help="path of file store initial relative activities/concentrations for all the nodes in the network"
        )    
    parser.add_argument(
            "--prefix","-p",
            type=str,
            default="Attractors",
            help="which will be the name of folder store the attractors, also the prefix of attractors file"
        )
    parser.add_argument(
           "--time_step","-t",
            type=int,
            default=100,
            help="times iteration will be"
        )
    FLAGS = parser.parse_args()
    if FLAGS.start_list_path != "":
        with  open(FLAGS.start_list_path, 'r') as f:
            start_input = [s.strip() for s in f.readlines()]
            start_input = filter(lambda x:len(x) > 2, start_input)
            len_start_list = len(start_input)
            # print start_input
            start_list = [random.random() for i in range(len_start_list)]
            for i in start_input:
                index = int(i.split('\t')[0])-1
                # print 'index is ',index
                start_list[index] = float(i.split('\t')[1])
    else:
        start_list = []
    # print(start_list)
    folder = FLAGS.prefix
    n = FLAGS.n
    k = FLAGS.k
    if FLAGS.network_path == 'network_origion.xlsx':
        input_path = os.path.join(os.getcwd(),FLAGS.network_path)
    else:
        input_path = FLAGS.network_path
    outputfile = '_'.join([folder,str(n),str(k)])
    Attractor_Calculation(
            input_path = input_path,
             folder = folder,
             outputfile =  outputfile,
             round = FLAGS.round,
             start_list = start_list,
             n = n,
             k = k)
