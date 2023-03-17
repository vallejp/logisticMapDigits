from mpmath import *
from Pipeline import AbstractPipelineClass
from Methods import save_iteration, cycles, fixed, frequency_experiment

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
                 ):
        self.u = u
        self.x0 = x0
        self.accuracy = accuracy
        self.number_iterations = number_iterations
        self.max_position = max_position
        self.max_fixed_iteration = max_fixed_iteration
        self.iteration_compare = iteration_compare
        self.s_f = s_f
    
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
    
if __name__ == '__main__':
    u = mpf('3.98')
    x0 = mpf('0.6')
    accuracy = 10
    number_iterations = 10
    max_position = 3
    max_fixed_iteration = 20
    iteration_compare = 1
    s_f = 1

    pipe = DigitsPipeline(
        u=u,
        x0=x0,
        accuracy=accuracy,
        number_iterations=number_iterations,
        max_position=max_position,
        max_fixed_iteration=max_fixed_iteration,
        iteration_compare=iteration_compare,
        s_f=s_f,
    )

    pipe.iteration()
    pipe.period()
    pipe.fixed()
    pipe.frenquecy()