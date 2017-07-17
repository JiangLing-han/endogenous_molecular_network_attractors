# endogenous_molecular_network_attractors
Working scripts of [Chu, X.-Y.; Jiang, L.-H.; Zhou, X.-H.; Cui, Z.-J.; Zhang, H.-Y.	Evolutionary Origins of Cancer Driver Genes and Implications for Cancer Prognosis. ***Genes*** 2017, 8, 182.](http://www.mdpi.com/2073-4425/8/7/182), for calculating endogenous molecular network 's attractors.
  
Usage:
------
1 . Delete nodes

Run 'network_rewiring.py' and add the number of nodes you want to delete, for example:
```shell
$ python network_rewiring.py 1
```
If you just want to calculate attractors, skip this step. This step will create the folder and files needed in the next step.
  
2 . Calculate attractors


* Without start input

  Run script 'attractors_without_nodes.py' and add the number of nodes you want to delete,the total number of network 
  for example:
  ```shell
  $ python attractors_without_nodes.py 1 42
  ```      
  '1' means you want to delete 1 node, '42' means the origion network contains 42 nodes.
  This step will calculate the attractors and put them into the folder named as the number of nodes you input,for example:
  ```shell
  $ '/../network_without_nodes/2'
  ```
  The attractors are something like follows:
  ```
  691	['0.0000', '0.0000', '1.0000', '0.0000', '0.0000', '0.9543', '0.9306', '0.9306', '0.0000', '0.8402', '0.0000', '0.8259', '0.8184', '0.9170', '0.8694', '0.9405', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '1.0000', '0.0000', '1.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000']
  128	['0.0000', '0.0000', '1.0000', '0.0000', '0.0000', '0.9543', '0.9306', '0.9306', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '1.0000', '0.0000', '1.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000']   
  ```
  first column is the size of attractor, second column is the attractor.
  
* With start input
  Make sure inputfile exist in your working directory.
  Run script `attractors_without_nodes.py` and add the number of nodes you want to delete,the total number of network and the inputfilename, just like:
  ```shell
  $ python attractors_without_nodes.py 1 42 Input_file.txt
  ```
  '1' means you want to delete 1 node, '42' means the origion network contains 42 nodes, `Input_file.txt` is the name of your input.
  The inputfile should be like the following format:
  >
        1	0.0
        2	0.0
        3	0.0
        4	0.0
        5	0.0
        6	0.0
        ...
        33	0.0
        34	0.0
        35	0.0
        36	0.0
        37	0.0
        38	0.0
        39	0.0
        40	0.0
        41	0.0
        42	0.0
        
   left is the nodes number, it should start from 1;
   right is its value which should be float, using space to sepreate them.
   Others are the same as `Without start input`.
