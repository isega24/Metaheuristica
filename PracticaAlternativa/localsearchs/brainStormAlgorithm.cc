#ifndef __ALGORITMO_H__

#define __ALGORITMO_H__

#include "problem.h"
#include "random.h"
#include <vector>

namespace realea {


unsigned Algoritmo::apply(vector<tChromosomeReal> &sol, tFitness &fitness, unsigned itera){

}


}
#endif



using namespace realea;
int main(int argc, char const *argv[]) {
    int problemNumber = 0;
    if(argc < 2){
        exit();
    }
    else{

    }

    int seed = time(NULL);    // Esto solo se hará una vez
    SRandom * sr = new SRandom(seed);
    Random random(sr);    // Generador de números aleatorios usado en el problema
    ProblemCEC2014 cec2014(/* dimensión del problema aquí */);    // Clase con los problemas de CEC2014
    ProblemPtr problem = cec2014.get(/* número de la función (a partir de 1) aquí */);    // Problema con una función concreta
    DomainRealPtr domain = problem->getDomain();    // Dominio (rango de valores) del problema
    tChromosomeReal sol(dim);
    getInitRandom(&random, domain, sol);    // Esto inicializa sol a una solución aleatoria. Debe copiarse la función getInitRandom como está en example.cc (no se puede incluir porque tiene otra función main)

    Algoritmo * alg = new Algoritmo();    // Instancia del algoritmo
    alg->setRandom(&random);              // Importamos el RNG
    alg->setProblem(problem.get());       // Cargamos el problema (esto carga también la función de evaluación)

    tFitness fitness = /* evaluación de sol o flotante muy grande, según se desee usar el cromosoma inicial o no */;
    alg->apply(sol, fitness, tope);    // Ejecutamos el algoritmo hasta un máximo de tope pasos. En sol y fitness se almacenarán el mejor cromosoma y su evaluación
    return 0;
}
