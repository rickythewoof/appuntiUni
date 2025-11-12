the choice for ReLU for hidden units has been shown that on average it's a good function.
### Cost Function
Model implicitly defines a conditional function $p(t | x, \theta)$. We want to maximize the probability to reach a certain output given an input, and we can oly choose $\theta$ parameters.
- Cost function: Maximum likelihood principle (**cross-entropy**)
	- $\displaystyle J(\theta) = E_{x,t}[-\ln(p(t|x, \theta))]$
	- With $\ln ...$ being the data set
	- and $E$ being the cross-entropy, which is an estimation. If we assuyme that error is gaussian noise we have exactly Mean Square Error
Example:
## Binary classification
Sigmoid unit
- Sigmoid activation function $\sigma(x) = \frac1{1+e^{-x}}$ , useful becase of its range $y\in(0,1)$ 
- $y=\sigma(\alpha)$, with $\alpha = w^Th+b$ 

Sigmoid saturates only on correct answers!
In general , in this case we have the likelihood, since it's a binary classification we have Bernoully distribution
- $p(t|x,\theta)=\sigma(\alpha)^t(1-\sigma(\alpha))^{1-t}$ 
	- this means the probability of having the actual value given x and $\theta$, which is a combination of $\sigma(\alpha)$ if $t=1$ and $1-\sigma(\alpha)$ if $t=0$

To calculate now the cost function over the average of the outputs:
-  $J(\theta) = \frac1{|D|} \sum_{(x,t)\in D} - \ln p(t, x, \theta)$ (assuming that $J(\theta)$ approximates the **cross-entropy**)
- $- \ln p(t, x, \theta) = -\ln \sigma(\alpha)^t(1-\sigma(\alpha))^{1-t} = -\ln((2t-1)\alpha)= \text{softplus}((1-2t)\alpha)$ 
This is called the **binary cross-entropy**.

## Multiclass classification
In this case the output will have $k$ units, since every unit will classify the probability of an element being in that specific domain (so that $\sigma(\alpha_i)=p(t_{i}| x, \sigma)$)
We'll use **softmax** function, which computes the exponential of the probability over the sum of all of the others. We normalize the outpus, so that the sum of all values are equal to 1.
- $\displaystyle softmax_i(\alpha) = \frac{e^{\alpha_i}}{\sum_j e^{\alpha_j}}$ 
We don't need a sigmoid at the last output anymore, since they are already being normalized between 0 and 1 with softmax.
The likelihood corresponds to Multinomial distribution (*one-hot encoding*):
- $\displaystyle p(t|x, \sigma) = \prod_{j}(softmax_j(\alpha))^{t_j}$  which means that the probability of success is the probability returned by the softmax on the correct classification.
- The cost function is the same thing, as always
## Summary
- **Regression**: Linear output unit, mean squared error loss function
- **Binary classification**: Sigmoid output unit, binary cross-entropy
- **Multi-class classification**: Softmax output unit, categorical cross-entropy
Generally, all hidden layers use ReLU as their output function
# Gradient Computation
It's basically the same as the gradient descend in the linear regression, with the difference of having multiple layers to do the gradient. **not being linear, it means that the gradient function is not convex** => we use **Stochastic Gradient Descend**.
To train our network we need to compute the gradientrs with respect to the network parameters $\theta$. The **backpropagation** algorithm is used to propagate the gradient computation from the cost through the whole network.
- We just need it to be *differentiable*, so that we can do the partial derivative over every parameter and use that to update the parameter values

Computing the derivative over the loss function over ALL the parameters is incredibly difficult, and it's a bottleneck. We use the chain-rule: we differentiate a composition of functions.
### Chain rule
let $y = g(x)$ and $z = f(g(x)) = f(y)$ \[derivate of a composite function]
by applying the chain rule we have:
- $\displaystyle \frac{dz}{dx} =  \frac{dz}{dy} \frac{dy}{dx}$ 
In the case of vector functions, $g : \mathbb{R}^m \rightarrow \mathbb{R}^n$ and $f: \mathbb{R}^n \rightarrow \mathbb{R}$ 
- $\displaystyle \frac{\partial z}{\partial x_{i}} = \sum_{j} \frac{\partial z}{\partial y_{j}}\frac{\partial y_{j}}{\partial x_{i}}$
 
This means that we can calculate the derivative for every node of the layer to calculate the entire derivative. backpropagation reuses a lot. In the forward pass we keep stored both  the function output and also the linear combination of it.