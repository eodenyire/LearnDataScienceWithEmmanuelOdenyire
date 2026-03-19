# Phase 4 Quiz: Deep Learning

**Instructions**: 25 questions. Open book.

---

## Section A: Neural Network Basics (1 point each)

**1.** What is the role of an activation function in a neural network?
- a) Normalize input data
- b) Introduce non-linearity to the network
- c) Reduce overfitting
- d) Speed up training

**2.** Which activation function is commonly used in the output layer for binary classification?
- a) ReLU
- b) Tanh
- c) Sigmoid
- d) Softmax

**3.** What does backpropagation compute?
- a) Forward pass predictions
- b) Gradients of the loss with respect to all weights
- c) Number of layers needed
- d) Optimal learning rate

**4.** Dropout regularization works by:
- a) Adding L2 penalty to weights
- b) Randomly setting neuron activations to zero during training
- c) Reducing the number of layers
- d) Increasing the learning rate

**5.** What is the vanishing gradient problem?
- a) Gradients explode to infinity in deep networks
- b) Gradients become very small in early layers, slowing learning
- c) The model forgets previous training data
- d) Loss function reaches a local minimum

---

## Section B: CNNs and RNNs (3 points each)

**6.** Explain what a convolutional layer does. What hyperparameters does it have?

**7.** What is pooling in CNNs? Compare MaxPooling vs. AvgPooling.

**8.** Why are RNNs better than feedforward networks for sequential data?

**9.** What problem do LSTMs solve that vanilla RNNs cannot?

**10.** Explain the attention mechanism in transformers in simple terms.

---

## Section C: Practical (5 points each)

**11.** Write a Keras CNN with: 2 Conv2D layers, BatchNorm, MaxPooling, Dropout, and Dense output for 10-class classification. Compile it appropriately.

**12.** You are training a deep learning model and observe: training loss decreasing, validation loss increasing after epoch 10. Describe 4 techniques to address this.

---

*Total: 25 points*
