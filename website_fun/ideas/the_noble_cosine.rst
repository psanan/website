The Noble Cosine
################
:date: 2009-10-27 19:02
:author: windfarmmusic
:category: Analysis, Geometry, Mathematics
:tags: math
:slug: 29
:status: draft

My vision for this blog is, at this point, still a selfish one. Essentially, when I have an idea or question which I hope will be clarified by writing about it, I shall do so. With that in mind,

**The Noble Cosine.**

$latex \\cos x $

I've been seeing this expression for so long, but like many things, one doesn't always take the time to really understand what it means.

| I, like most people, first heard about and used the cosine in the context of right triangles, and then more generally in general triangles in Euclidean space.
| ...

This definition is of course tied to the pythagorean theorem, which in fact applies to much more than just right triangles and is a key to extending the idea of cosine...

Pretty soon, you're introduced to the idea that trigonometric functions can be expressed and even defined as power series.

$ latex \\cos x = 1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\cdots $

Cosine is now cast as an analytic function, which opens up a whole new world of things to do with it. It also shows that the cosine is just the real part of the complex-valued function $e^{ix}$ ...

The cosine can also be expressed as an infinite \*product*...

Sinusoids play key role in physics as well, being solutions to 2nd-order differential equations....

But, how is this a consistent extension of our triangle-measuring, and more to the point, what is the more general idea that both of these approaches are examples of?....

Clearly, ideas from complex analysis are important. The geometric interpretation of the complex plane (or more precisely, the 'canonical' isomorphism between $latex \\mathbb{C}$ and $latex \\mathbb{R}^2$) shows the connection between the 'right triangle' definitions and Euler's formula. Another question that might bother a lot of people is 'why complex numbers?'. Why is it so useful and natural to introduce a whole other dimension into our real number system? I'd say the answer is that the complex numbers are a \*splitting field*, whereas the real numbers are not. This means that we can completely factor a polynmial in $latex \\mathbb{C}$ though we might not be able to in $latex \\mathbb{R}$. This is how the concept of imaginary numbers likely arose. We saw above that sinusoids arise as solutions to differential equations. Our desire to be able to factor differential operators leads us to complex sinusoids just as our desire to factor polynomials lead us to complex numbers. $latex D^2 + 1$ can be factored  as $latex (D + i) (D - i)$ What's the solution to (D \\pm i)x = 0 ? e^{\pm ix}.

...

Going further off on this tangent, we examine  how the idea of complex numbers arises. A key point is that the complex numbers are in many ways simpler and more complete than the real numbers. Both names are misnomers. The real numbers are not as 'real' as one would think (in fact if we're talking about quantum dynamics then complex numbers are pretty real) and complex numbers not really more complex!

I think it's a fact that the complex numbers are the unique minimal extension of the reals to a splitting field....

...

The analytic function is the quintessential 'nice' function, and it is something which arises naturally in complex analysis. ...

...

| One also often sees cosines pop up when talking about inner product spaces:
| [latex] \\langle a,b \\rangle = \\cos(x,y)||x||||y|\| [\latex]
| This is a nice expression to think about because it encompasses our right triangle idea: the cosine gives a measure, between -1 and 1, of how correlated two vectors are, independent of their scalar magnitude. It quantifies 'how much in the same direction' two vectors are.

This idea can be further extended to apply only locally, as things like first fundamental forms on hypersurfaces or generally (Reimannian) metrics on (Reimannian) manifolds can be thought of as local inner products between tangent vectors.

...

It's nice to think of the cosine as a measure of correlation between two things, independent of their 'lengths', but why such a particular formulation? We can eliminate all others by stipulating that this measure of correlation be \*basis independent*. This is a very fundamental idea in physics and is intimately related the reasons for using the distance function d(x,y) = \|x-y|^2 in euclidean space. This is the only measure of distance that's invariant under  the sorts of transformations that our experience indicates physical reality is invariant under. ...
