# library
import numpy as np
import pandas as pd
from scipy import stats
from random import sample
from copy import deepcopy


# crossover
def crossover(parent1, parent2, crossover_rate, column_list, seed=1):
    """
    crossover 연산 수행
    ------------
    parameters
    ------------
    1. parent1, parent2 : Individual
      Individual 1,2 to be crossed
    2. crossover_rate : float
    3. column_list : list(str)
      list of variable names used for rank generation
    
    ------------
    Returns
    ------------
    child1, child2 : Individual
  """
  
    child1 = deepcopy(parent1)
    child2 = deepcopy(parent2)
    
    for col in column_list:
        np.random.seed(seed)
        crossover_point = np.random.rand(len(child1[col])) < crossover_rate     # 한 지점만 찍나??? 
        child1[col], child2[col] = np.where(crossover_point, child1[col], child2[col]), np.where(crossover_point, child2[col], child1[col])
        seed += 100
    return child1, child2

# mutation
def mutation(parent, mutation_rate, column_list, seed=1):
    """
    mutation 연산 수행
    ------------
    parameters
    ------------
    1. parent : Individual
      Individual to be mutate
    2. mutation_rate : float
    3. column_list : list(str)
      list of variable names used for rank generation
    
    ------------
    Returns
    ------------
    child : Individual
    """

    child = deepcopy(parent)
    
    for col in column_list:
        np.random.seed(seed)
        mutation_point = np.where(np.random.rand(len(child[col])) < mutation_rate)[0]
        seed += 100

        if len(mutation_point) > 0:
            for idx in mutation_point:
                np.random.seed(seed)
                if idx == 0:
                    child[col][idx] = np.random.choice(np.arange(child[col][idx+1]))
                elif idx == len(child[col])-1:
                    child[col][idx] = np.random.choice(np.arange(child[col][idx-1]))
                else:
                    child[col][idx] = np.random.choice(np.arange(child[col][idx-1], child[col][idx+1]))
                seed += 100
    return child
