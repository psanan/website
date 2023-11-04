Creating and Maintaining Documentation
======================================

Docs should be:

* easy to edit
* easy to build, including locally
* as short as possible
* directly linked to the codebase, tests, and test reference output
* easy to find on the web

(longer:)

Creating and Maintaining Documentation
======================================

Guiding principles and consequences:

Docs should be easy to edit
---------------------------
Documentation can always be improved, and there will typically be errors
that are obvious to readers other than the writer. This includes readers
more expert than the writer, but also complete beginners, who will expose
unexplained assumptions, minor typos and inconsistencies,  and non-trivial
logical leaps. Thus, strive to make it simple for these readers to contribute,
and encourage them to do so, for example by taking advantage of increasing
general familiarity with tools like GitHub/Bitbucket/GitLab/ReadTheDocs.
Ensure that the docs can easily be (re)built locally.

Shorter docs are often better
------------------------------
No documentation is far better to incorrect documentation, and usually better
than confusing documentation. The less documentation there is, the easier it
is to maintain and improve. Most people don't read long documentation.
Thus, be proactive about removing or condensing documentation when possible,
and try to write as concisely as possible. This is doubly true for developer
documentation, as these readers tend to value technical precision and consistency
more than long explanations and motivations.

Strive for Documentation that cannot be out of sync with the code
-----------------------------------------------------------------
Follow the usual guideline of not duplicating information. Thus,

* Include code directly from source files
* Include expected output directly from testing reference output

