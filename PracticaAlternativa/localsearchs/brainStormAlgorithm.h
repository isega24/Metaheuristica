#ifndef __ALGORITMO_H__

#define __ALGORITMO_H__

#include "problem.h"
#include "random.h"

namespace realea {

class Algoritmo {
  public:
    unsigned apply(tChromosomeReal &sol, tFitness &fitness, unsigned itera);

    void setProblem(Problem *problem) {
      m_problem = problem;
      setEval(problem);
    }

    void setRandom(Random *random) {
       m_random = random;
    }

    void setEval(IEval *eval) {
      m_eval = eval;
    }


  protected:
    Random *m_random; /**< The current randomgeneration numbers */
    IEval *m_eval; /** The current evaluation function */
    Problem *m_problem; /**< The current problem */
};

}
#endif
