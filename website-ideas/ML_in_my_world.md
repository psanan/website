ML in my world (blog post):

Should do some more backgroudn - watch the rest of those lectures, look for the canonical textbook or two and read those.
Make sure that stuff is safely in notes.

Then, you shoulld be able to understand what Tensorflow does.

Then, you can make a quick example to understant the basics.

Then, what's the simplest audio-based thing you can do with it?

This is a post about things interesting to me, wrt ML

1. Lagrangian NNs (paper, and there was a great blog post)
2. SampleRNN (paper, and there was a great blog post)
3. multiscale modelling (PT):

https://github.com/tiwarylab/RAVE
PT nature paper
https://keras.io/
https://arxiv.org/abs/2002.06099


---------------

Learning: book (once finished, but into notes)
  Aggarwal2018
Learning : https://developers.google.com/machine-learning/crash-course [I should complete this before my interview..]
Google Colab: https://colab.research.google.com/notebooks/intro.ipynb#scrollTo=-Rh3-Vt9Nev9
Nsynth: https://aihub.cloud.google.com/p/products%2Fcddd17cf-5f86-4ce7-b6b6-03c5e52ee0fb

Google "Looking to Listen" project looks interesting.

---------------


What‘s the simplest audio I can make with tensorflow? (See PRiSM SampleRNN, NSynth, perhaps WaveNet examples..)


Basic question from watching lectures:
Real brains work in a time-depdendent manner. Neural nets are static. How does that huge simplificiation affect what these things can be used for? Are, e.g. vision and aural perception systems basically model-able by static NNs?


So from lecture 12a, seems like the idea is that to compute the gradient of a misfit function from our function-predictor neural network, with respect to a (large number) of weights, this gradient can be computed by reusing a bunch of derivatives. This is because of the layered structure of the network. Are these maybe arranged into a tensor stucture, hence TensorFlow?
