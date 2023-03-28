# Patterns on Logistic Map: back to front

This repo is the official python implementation of the methods in: "[Patterns on Logistic Map: back to front](https://arxiv.org/abs/2212.01459)". 

## Getting Started
### Environment Requirements

First, please make sure you have installed Conda. Then, our environment can be installed by:
```
conda create -n digits python=3.6.9
conda activate digits
pip install -r requirements.txt
```

### Methods

- iteration(): This method iterates the logistic map through the dynamic iteration method for low positions.
  - Parameters: 
    - x0: initial condition
    - number_iterations: amount of iteration the logistic map will undergo
    - u: logistic map parameter control
    - accuracy: number of last decimal places that will be iterated
    
- fixed(): this method finds the existing fixed digits in the logistic map for a given mu.
  - Parameters:
    - u: logistic map parameter control
    - max_fixed_iteration: maximum number of iterations to find the fixed digits
    - iteration_compare: number of iteration to comparer the seed with the final iteration value
    
- period(): This method finds cycles of periodic digits
 - Parameters:
  - x0: initial condition
  - u: logistic map parameter control
  - accuracy: number of last decimal places that will be iterated
  - max_position: maximum decimal position that will be scanned

## Citing

If you find this repository useful for your work, please consider citing it as follows:

```bibtex
@article{valle2022patterns,
  title={Patterns on logistic map: back to front},
  author={Valle, Jo{\~a}o and Bruno, Odemir M},
  journal={arXiv preprint arXiv:2212.01459},
  year={2022}
}
```
