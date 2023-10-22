This is a "fun" website.

Fun in the web 1.0 sense.

Fun because it's so limited in ambition
that it doesn't require more than low-level tools.

It's just HTML and a single CSS file and a couple of simple Python scripts.

You should not have to "build" anything or run a local HTTP server.
Just edit the files and look at them in your local web browser.


It could just be
* A single CSS file
* A "site" directory, which can be copied directly to deploy
    * Totally flat for HTML files!

The initial impl could just have that, but the HTML pages will have duplicated boilerplate for headers, footers, inline images, and image galleries. I'll want to be able to easily bulk update those, or have them filled in from comments in new posts.
So we'll also need

* A reference HTML header
* A reference HTML footer
* A script which generates the feed - it will complain if it can't find a publication date in the HTML file
* A script which updates the headers and footers
* An image update script.
    * Looks for figures assigned to a particular class (or a div surrounding an image, perhaps)
    * finds probably-won't-change information within (probably just the path to the full-size image as href="xx") and replaces everything else
    * Has an option to (re)generate small images (and warns and has an option to delete now-unused small images)
* A script to generate the feed by looking for pages with a comment for a feed date (?)
* A deploy script which updates headers and footers, generates the feed, and deploys with rsync to a particular place (put the actual address in my personal config so I can still publish the website source)

