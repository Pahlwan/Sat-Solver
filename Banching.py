def branching_sat_solve_opti(clause_set,partial_assignment):   
    if(len(partial_assignment)!=0):
        
        res1 = True
        for clause in clause_set:
            res = False
            for c in clause:
                if(c in partial_assignment):
                    res = res or True
                    break
               
                elif(-c in partial_assignment):
                    res = res or False
                else:
                    res = None and res
                    break
             
            if(res == False):
                return False
            else:
                res1 = res1 and res
        if(res1):
            print(partial_assignment)
            return True
        
    x1 = 0
    for x in list(chain.from_iterable(clause_set)):
        if abs(x) not in map(abs,partial_assignment):
            x1 = x
            break
    if(x1!=0):
        if branching_sat_solve_opti(clause_set,partial_assignment+[x1]):
            return True
        if branching_sat_solve_opti(clause_set,partial_assignment+[-x1]):
            return True
    return False
