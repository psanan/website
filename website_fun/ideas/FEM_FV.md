The FEM Is usually motivated in a certain way:

1. Start with a PDE (pointwise, "strong form")
2. Multiple by a test function
3. Integrate over a domain
4. Apply integration by parts
5. Pick finitie-dimensional function spaces for the solution and test functions
6. Write a linear system in terms of bases for these finite-dimensional spaces

However, the first 4 steps aren't very satisfying. Is this just a mathematical trick? How do we get away with using functions which have less derivates than are required for the strong form, and aren't even continuous??

Usually one just hand waves.

Contrast this with the Finite Volume method. There, we start with the "real" physics, conservation laws. The numerical method rests upon enforcing these physics in control volumes. (Things get uglier once you start needing to talk about pointwise values and derivatives, though)

Let's back up and think about what the "real" physics are. Typically, these are understood as

a. Conservation laws
b. Symmetries / invariances
c. Optimalities, or variational forms (https://www.encyclopediaofmath.org/index.php/Variational_principles_of_classical_mechanics)

I'll skip straight to an example of the third type, which is hopefully quite intuitive.

Consider a series of linear springs, connecting "nodes" (handles). One fixes some of these nodes in various places, and applies forces to some of them, and we ask what the equilibirum state of the system is.

One can find this state by writing down the potential (elastic) energy of the system. If there are only fixed nodes, one simply minimizes this - take a derivative in each "dof", set to zero, and solve!

If there are forces, then we are looking for a stationary point - the energy gradient (the force) must look like the applied forces.

Now let's move to an apparently-different system: viscous flow. 
One usually understand this in terms of conservation laws, so the FV method makes a lot of intuitive sense, but FEM? Not so much. 

However, we can also pose this as an optimality problem!

DO THIS (Steady state heat equation? Stokes?)


