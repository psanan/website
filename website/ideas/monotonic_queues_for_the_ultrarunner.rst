

When studying a programming interview, I came across a very interesting data structure: the monotonic queue.

You use this in situations where you have items which have a) some value which you'd like to maximize and b) some notion of age, which you'd like to constrain.

THe classic usage is in this type of problem:

   Given an array of numbers, compute the maximum value in a sliding window of width K.
   For example, given K=5 and array

      1, 2, 3, 5, 1, 4, 7, 1, 2, 0, 0, 0

   return

      5, 5, 7, 7, 7, 7, 7, 7, 2


The obvious way to do the computation is to look at each set of K=5 values, compute the maximum, and output it.

That works fine for small problems, but what if your list is millions of entries, and K is a few thousands?
Multiplying those numbers together is something big enough to matter. I'd like to solve this in linear time
with respect to the input size, meaning that I do the best that I should reasonable expect, asymptotically:
some constnat multiple of the size of the input - I have to at least read the whole input array here
(it's not obviously sorted or otherwise structured).

This means that you're looking at each entry of the array K times, which is a big hint to the
algorithm designer that you could do better.

With a monotonic queue, in fact you can do this!
The idea is to be clever enough that you can update the answer as you "slide" the window, adding one new entry
and evicting the old one. This makes some sense - when I slide the window, the new problem to be
solved (find the maximum) has almost the same data as the previous problem, so I should be
able to reuse what I've already computed, somehow.

The trick is to keep track of the maximum value in the window, but
also all other potential future maximum values: these are less than the current maximum value, but might
become the maximum once the window is moved over, ejecting the current maximum from the left. Thus, you keep
track of all entries which are bigger than all entries to their right in the window.
An entry can be useful both by being big and by being recent (closer to the right side of the window,
hence appearing in more to-be-checked windows).


A monotonic queue is a list of items that all have optimal values amongst the set of items
which are the same "age" or older. In the example above, "age" is the position in the input array.
The queue looks like this, as you slide the window over. (x,y) means value x which was in position y in the
input array.

    (1,1)
    (2,2)
    (3,3)
    (5,4)
    (5,4), (1,6)  # window is complete, output first value (5)
    (5,4), (4,7)
    (7,8)
    (7,8), (1,9)
    (7,8), (2,10)
    (7,8), (2,10)
    (7,8), (2,10)
    (2,10)        # last full window, finished by outputting last value (2)

You can see that at all points, the first values decrease and the second values increase.
This monotonicity in both "slots" gives the data structure its name.

This structure popped into my head while running, thinking about how competitions are
most fun when you have a change of winning, but aren't certain you will.
(John Kelly's Goldilocks zone goes into this a lot).

This motivates the idea of separating athletic competitions into categories by region, gender, age, or leagues
(either self-assigned or determined by performance, as in football).

Right now, I think I'm still improving, in absolute terms. But I assume that
no matter what I do, by some point before I'm about 50, this will reverse.

As I get older, I will certainly be looking at my age group results, but another fun
option occurs.

If age were considered to be the main determiner of performance, then
the baseline result should be that everyone in the "old" category should finish
roughly in order of age. Age of course is not the only determiner, but it's something
the athlete can't do anything about, so it's more fun if we can reduce its effect
on ranking people.

You can thus thinkg about defining "par" as finishing the race faster than everyone older than you.
That should remain attainable as long as you can finish the race, at all. At a certain point,
all you will need to do is finish, as you'll be the oldest one!

The monotonic queue in this case is the set of all "winners" of the race.
These are people who ran the fastest amongst all people their age or older.
It's a list of people which increasing in both age and finishing time.

The first entry in the list is the usual winner of the race - they ran the fastest.
If the oldest person won the race, the list ends there. However, in the likely event
that some older person also finished the race, then the second entry in the list is the fastest
such person. The third entry is the fastest person older than that,
and so on until the list ends with the oldest finisher.

A problem with this is that it's not clear when being older actually makes you slower.
Until you're about 30 or so, it seems likely that being older is an advantage (for ultras).
If an 18 year old wins the race and a 29  year old comes second, it doesn't make a lot of sense
to say that the 29 year old is also a generalized winner, when in fact they probably had
an advantage due to their age. Using the usual "masters" cutoff of 40 is probably the most practical
choice. Then again, you can argue that this is unnecessary, as if you are unhappy at being penalized
for being young, then all you have to do is wait and keep running, which is the behavior
that this metric is trying to incentivize in the first place!

I'd love for this to be a way that race results are reported. No need to define
different age divisions, and you get to see a fuller picture of what ultrarunning is - the absolute speedsters,
the "masters" people putting down amazing times well into their 50s, and the people running
the most ultra of ultras, which is continuing to finish races for decades.

It also makes explicit what I think is a goal of many multi-decade runner: I'm going to win
by being the oldest finisher. It also adds a continuum of ways to win before you become
quite that old.

An intersting question is how large these sets of winners typically are. As above,
if the oldest person wins, they are the only winner. Alternately, if the youngest
person wins and everyone else finishes in order of age, everyone is a winner!

Ages are often prominently reported with ultra results, so let's look at some data.
We'll learn about some beastly, older runners, and also get some data on how many generalized winners there are.
How does that number scale with the size of the race?


the 2021 WSER:
Women:
  (33) Beth Pascal 17:10
  (42) Ragna Debats 17:41
  (47) Magdalena Boulet 22:12
  (53) Selena Nordburg 27:28
  (56) Susan Kramer 28:32


Men:
  (31) Jim Walmsley: 14:46
  (35) Tyler Green: 16:11
  (36) Tim Tollefson 16:55
  [Women did very well this year and would start appearing here on an overall list!]
  (41) Cody Draper 21:51
  (51) Christopher McBride 21:53
  (52) Timothy Christoni 23:03
  (53) Steve Rowbury 23:05
  (55) Dan Barger 25:39
  (57) Joe Steinmetz 26:10
  (65) Steen Vagn 28:20
  (68) Kuni Yamagata 29:31


Another way to interpret all of this is to be able to calculate your rank
in the race, if you only consider those people older than you. I'm probably a little young
to actually be doing this. I think it's reasonable to expect that I am going to continue to improve
for a couple more years, at least. Still, for fun, let's examine the `2019 SwissAlps 100k <https://www.swissalps100.com/results.asp?iY=2019&iD=100>`__, since their
results have ages stated. I definitely felt I underperformed in this race. I didn't eat enough and
ran out of energy and had to sit at an aid station for a long time to recover, and I did an extra 8-10k
by taking a wrong turn and having to backtrack (up a hill).

My ranking was 41/96, but if I only consider the competition to be me and older people, I was 29/65 (all genders).
One encouraging thing about this race is how well the older runners did! The winner (by over an hour) was 45 and places 12 and 13
were 57 and 60! A 66 year old came in 68th and a 69 year old in 78th. 
