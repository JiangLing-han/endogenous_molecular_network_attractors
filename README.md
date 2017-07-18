# endogenous_molecular_network_attractors
Working scripts of [Chu X-Y, Jiang L-H, Zhou X-H, Cui Z-J, Zhang H-Y. Evolutionary Origins of Cancer Driver Genes and Implications for Cancer Prognosis. ***Genes***. 2017; 8(7):182.](http://www.mdpi.com/2073-4425/8/7/182), for calculating endogenous molecular network's attractors.
  
Basic Usage:
---
Before compute attrators, please confirm requirments below:
- python2.7, other 2.x may also work, python3.x are not supported because `exec` changed in python3.x
- scipy

###  - **Without start input**

  ```shell
  $ python attractors.py -net ./network_origion.xlsx
  ```      
  `-net` indicate the path of network file, attracors will be saved in `./Attractors` by default.
  
###  - **Without start input**

  ```shell
  $ python attractors.py -net ./network_origion.xlsx --start_list_path ./Input_file.txt
  ```      
  `--start_list_path` indicate the path of initial relative activities/concentrations for all the nodes in the network.
  
  The inputfile should be like the following format:
  >
        1	0.0
        2	0.0
        3	0.0
        ...
        11	0.0
        12	0.0
        13	0.0
        
   left is the nodes number, it should **start from 1**;
   right is its value which should be float, use `\t` to sepreate them.
   
More parameters setting, type this:

```shell
$ python attractors.py -h
```

Results:
---
  The attractors are something like follows:
  >

    691	['0.0000', '0.0000', '1.0000', '0.0000', '0.0000', '0.9543', '0.9306', '0.9306', '0.0000', '0.8402', '0.0000', '0.8259', '0.8184', '0.9170', '0.8694', '0.9405', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '1.0000', '0.0000', '1.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000']
    128	['0.0000', '0.0000', '1.0000', '0.0000', '0.0000', '0.9543', '0.9306', '0.9306', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '1.0000', '0.0000', '1.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000']   

  first column is the size of attractor, list is attractor.
  


