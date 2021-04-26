

# This file was *autogenerated* from the file checkEP.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)#from timing import log, endlog
from time import time, strftime, localtime
import numbers

def CheckModular(M,F1,F2):
    '''
    Takes as input the matroid and the flats 
    F1 and F2 where F1 is a hyperplane and F2 is a line.
    Checks that they form a modular pair.
    '''

    rF1 = M.rank(F1)
    #rF2 = M.rank(F2)
    rF12 = M.rank(F1.union(F2))
    rF1n2 = M.rank(F1.intersection(F2))
    if rF1 + _sage_const_2  == rF12 + rF1n2:
        return True
    return False

def GetHypsandLines(M):
    '''
    Obtains all hyperplanes and lines of the given matroid.
    '''

    hyps = [hyp for hyp in M.hyperplanes()]
    lines = [line for line in M.flats(_sage_const_2 )]

    return hyps, lines

def GetExtensions(M,hyp,line):
    '''
    Given a matroid and a pair of hyperplane and line,
    it returns all the extensions of the matroid in which 
    the corresponding modular cuts contain this pair.
    Output:   All extensions corresponding to hyp and line.
              i -- The new element.
    '''

    G = M.groundset()

    i = -_sage_const_1 
    
    while i in G:
        i -= _sage_const_1 
    return M.extensions(i,subsets=[hyp,line]), i

def CheckEP(M):
    '''
    Takes as input a matroid and checks if it is EP.
    If it is not EP, the function returns the boolean
    False, and the pair that breaks EP.
    '''

    hyps, lines = GetHypsandLines(M)

    for hyp in hyps:
        for line in lines:
            if CheckModular(M,hyp,line):
                continue
            if M.closure(set()) in M.modular_cut([hyp,line]):   
                return False, hyp, line
    return True, []

def RecursiveCheckEP2(M,depth):
    '''
    The recursive function.
    Takes as input the matroid to be checked
    and the depth at which EP is to be checked.
    Returns boolean indicating if the matroid is 
    EP at given depth.
    The print statements can be surpressed.

    input: M (matroid) sage Matroid object
           depth (int) greater than 0
    output: Boolean
    '''
    
    if not isinstance(depth,numbers.Integral) or depth <= _sage_const_0 :
        print('###### Depth has to be a positive integer ######')
        return None

    if depth == _sage_const_1 :
        ### We always check EP at depth 1. ###
        res = CheckEP(M) 
        if res[_sage_const_0 ]:
            return True
        else:
            #print('# hyperplane is {} and line is {} at depth 1'.format(res[1],res[2]))
            return False
    
    ### We start by generating all hyperplanes and lines of the matroid. ###
    hyps, lines = GetHypsandLines(M)
    
    for hyp in hyps:
        for line in lines:
            
            if CheckModular(M,hyp,line):
                ### We check modularity for each pair of hyperplane and line. ###
                continue    ### We only want nonmodular pairs. ###

            ### For a nonmodular pair, we generate all extensions corresponding to them. ###
            EPE, i = GetExtensions(M,hyp,line)
            
            EPmatroid = False  ### The indicator we use when we find an appropriate EP extension. ###
            for N in EPE:  

                hyp_line = [hyp,line]  
                if RecursiveCheckEP2(N,depth-_sage_const_1 ): 
                    ### Recursion takes place here. ###
                    
                    if N.rank([i]) != _sage_const_0 :
                        ### The moment we find a proper point extension that is EP, we break for that depth. ###
                        EPmatroid = True
                        break
            
            if not EPmatroid:
                #print('# hyperplane-line pair is {} at depth {}'.format(hyp_line,depth))
                return False
    return True

Mvam = Matroid(bases=['0124','0126','0125','0127','0234','0246','0245','0247','0236','0235','0237','0256','0267','0257',
'0134','0146','0147','0136','0135','0137','0156','0157','0346','0345','0347','0456','0467','0457',
'0356','0367','0357','0567','1234','1246','1245','1247','1236','1235','1237','1256','1267','1257',
'2346','2347','2456','2467','2457','2356','2367','2357','2567','1346','1345','1347','1456','1467',
'1457','1356','1367','1357','1567','3456','3467','3457','3567'])

cep = RecursiveCheckEP2(Mvam,_sage_const_1 )
print(cep)

