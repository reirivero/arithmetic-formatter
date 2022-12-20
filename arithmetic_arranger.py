def arithmetic_arranger(lst, displayed=False):
    if len(lst) <= 5:
      results, min, sus = list(), list(), list()
      for problem in lst:
        opt = problem.split()
        try:
          if len(opt[0]) > 4 or len(opt[2]) > 4: 
            return 'Error: Numbers cannot be more than four digits.'
          elif '+' in opt: 
            results.append(int(opt[0]) + int(opt[2]))
          elif '-' in opt: 
            results.append(int(opt[0]) - int(opt[2]))
          else:
            return "Error: Operator must be '+' or '-'." 
        except ValueError:
          return 'Error: Numbers must only contain digits.'

          
        min.append(opt[0])
        space = ' ' 
        if len(opt[0]) > len(opt[2]):
          space = space * ((len(opt[0]) - len(opt[2])) + 1)
          sus.append(space.join([opt[1],opt[2]]))   
        else:
          sus.append(space.join([opt[1],opt[2]])) 
  
      problems = list(zip(min,sus))
      
      i, j, arranged_problems = 0, 0, ''
      
      while j < len(problems[i]):
        if i == 0:
          arranged_problems += problems[i][j].rjust(len(problems[i][1]))
          i += 1
        elif i > 0 and i < len(problems) -1 :
          arranged_problems += problems[i][j].rjust(len(problems[i][1]) + 4)
          i += 1
        elif i == len(problems) -1:
          arranged_problems += problems[i][j].rjust(len(problems[i][1]) + 4)
          arranged_problems += '\n'
          i = 0
          j += 1       
  
      for i in range(len(problems)):
        if i == 0:
          arranged_problems += ('-'*len(problems[i][1])).rjust(len(problems[i][1]))
        else: 
          arranged_problems += ('-'*len(problems[i][1])).rjust(len(problems[i][1]) + 4)
      
      if displayed == True:
        arranged_problems += '\n'
        for i in range(len(results)):
          if i == 0:
            arranged_problems += str(results[i]).rjust(len(problems[i][1])) 
          else:
            arranged_problems += str(results[i]).rjust(len(problems[i][1]) + 4) 
      
       
    else:
      return "Error: Too many problems."

    return arranged_problems