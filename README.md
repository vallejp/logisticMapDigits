# Patterns on Logistic Map: back to front

This repo is the official python implementation of the methods in: "[Dynamics and patterns of the least significant digits of the infinite-arithmetic precision logistic map orbits](https://www.sciencedirect.com/science/article/abs/pii/S0960077924000390)". A brief tutorial can be found on the website: [here](https://scg.ifsc.usp.br/lmdigits/).

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
    
- fixed(): This method finds the existing fixed digits in the logistic map for a given mu.
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

- frenquecy(): This method analyzes the frequency of the numbers present in the cycles of the periodic digits (to run this method you need to run the period() first)
  - Parameters:
    - u: logistic map parameter control
    - s_f: number of decimal places the fixed digit occupies
    - max_position: maximum decimal position that will be scanned

- attraction(): This method finds the seeds that are attracted to a certain fixed digit
  - Parameters:
    - u: logistic map parameter control
    - iteration_compare: number of iteration to comparer the seed with the final iteration value
    - xfixed: the fixed digit value

## Citing

If you find this repository useful for your work, please consider citing it as follows:

```bibtex
@article{valle2024dynamics,
  title={Dynamics and patterns of the least significant digits of the infinite-arithmetic precision logistic map orbits},
  author={Valle, Jo{\~a}o and Bruno, Odemir M},
  journal={Chaos, Solitons \& Fractals},
  volume={180},
  pages={114488},
  year={2024},
  publisher={Elsevier}
}
```
