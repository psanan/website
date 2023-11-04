
Here, we focus on "tutorial" types of documentation - those that attempt to inform the reader in a way that more mechanical (yet still very important documentation), such as an API reference or the source itself, cannot do. This sort of documentation says a lot more about why you would use software, and typically relies on some instructive example cases.

Writing good documentation is hard, because writing is hard.

Writing good technical documentation is even harder, for a couple of reasons:

1. Most people are not in a position to write the most valuable kind of documentation: that which takes someone from not understanding to understanding. This is because people who already understand cannot see what's missing (and get bored), and people who don't understand, don't understand what they're writing about. The best time seems to be as you're learning (or relearning) something.

2. Software is forever changing, and so documentation is often out of date. Wrong or bad documentation is worse than no documentation, so what was once beneficial is now detrimental and might as well be deleted.


Here, we are concerned with the second point.

First, we take a concept that will be familiar to anyone who's worked with software or engineering for very long. The less "stuff" the better. The best code is no code, and the best docs are often no docs. Better to have nothing, if you can't have something good, and realize that whatever you build needs to be maintained.

Of course, both code and docs are tools which do something very useful (obviously, since we're bothering with them at all).

Code, like docs, goes out of date, but practices have been developed to mitigate this. The most important ones are the extensive use of tests, and the automatic execution of those tests (CI).

Can we bring that success to tutorial-style software documentation? I argue yes, in two ways:

1. We go back to our old, great analogy of the Bonsai Tree. A bonsai tree is designed for display. It's small and you can make each little twig they way you want it. Tutorials should also be for display, meaning people need to be able to use it and give you feedback. There's no better way to debug a tutorial than to give it to someone and see how they get confused. If that can continue to happen, you are in good shape.

2. Tutorials typically rely on example code. Small snippets to demonstrate key features of the API, and larger examples, often excerpted. These are code, and should be tested like any other code! This requires a little dedication to write tutorials in such a way that *they do not contain any literal code, input, or output*. Rather, they include snippets of code, input, and output which is included in the tests for the software. By doing this, in most cases the normal development workflow, which involves updating test information, also updates your tutorials.

This can have some interesting synergies with testing, itself. Graphical output is very important in tutorials, and and including the generation of such output with the test suite can add valuable coverage.
