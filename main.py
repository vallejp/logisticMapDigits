from mpmath import *
from Pipeline import AbstractPipelineClass
from Methods import save_iteration, cycles, fixed, frequency_experiment, attraction

class DigitsPipeline(AbstractPipelineClass):
    def __init__(self,
                 u,
                 x0,
                 accuracy,
                 number_iterations,
                 max_position,
                 max_fixed_iteration,
                 iteration_compare,
                 s_f,
                 xfixed,
                 ):
        self.u = u
        self.x0 = x0
        self.accuracy = accuracy
        self.number_iterations = number_iterations
        self.max_position = max_position
        self.max_fixed_iteration = max_fixed_iteration
        self.iteration_compare = iteration_compare
        self.s_f = s_f
        self.xfixed = xfixed
    
    def iteration(self):
        print(f"\nGenerating {self.number_iterations} iteration of logistic map with x0 = {self.x0} and u = {self.u}...")
        save_iteration(self.x0, self.number_iterations, self.u, self.accuracy)
        print("Finished")

    def fixed(self):
        print(f"\nExplorando os dígitos fixos com u = {self.u}...")
        fixed(self.u, self.max_fixed_iteration, self.iteration_compare)
        print("Finished")

    def period(self):
        print(f"\nExploring the cycles of {self.max_position} position of logistic map with x0 = {self.x0} and u = {self.u}...")
        cycles(self.x0, self.u, self.accuracy, self.max_position)
        print("Finished")

    def frenquecy(self):
        print(f"\nFrenquecy experiment...")
        frequency_experiment(self.u, self.s_f, self.max_position)
        print("Finished")

    def attraction(self):
        print(f"Attraction experiment...")
        attraction(self.u, self.iteration_compare, self.xfixed)
        print("Finished")
    
if __name__ == '__main__':
    u = mpf('4.0')
    x0 = mpf('0.07')
    accuracy = 10
    number_iterations = 10
    max_position = 1
    max_fixed_iteration = 15
    iteration_compare = 2
    s_f = 1
    xfixed = mpf('0.56')

    pipe = DigitsPipeline(
        u=u,
        x0=x0,
        accuracy=accuracy,
        number_iterations=number_iterations,
        max_position=max_position,
        max_fixed_iteration=max_fixed_iteration,
        iteration_compare=iteration_compare,
        s_f=s_f,
        xfixed=xfixed,
    )

    pipe.iteration()
    pipe.period()
    pipe.fixed()
    pipe.frenquecy()
    pipe.attraction()
