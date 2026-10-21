def plenty_of_arguments(a, b, **kwargs):
    total =  a + b + sum(kwargs.values())
    return total > 100



plenty_of_arguments(20, 30) 