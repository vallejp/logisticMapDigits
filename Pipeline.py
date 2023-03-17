class AbstractPipelineClass:
    def __init__(self):
        raise NotImplementedError
    
    def iteration(self):
        raise NotImplementedError

    def fixed(self):
        raise NotImplementedError

    def period(self):
        raise NotImplementedError
    
    def frenquecy(self):
        raise NotImplementedError