# Source for patricksanan.org

This is a "fun" website, in the learning-to-code, web 1.0 sense.
It's non-scalable, to be sure, but in return, it's fun to work on with low-level. There aren't any levels of abstractioon top of HTML and CSS.

(And it's so simple, I have to believe it'll load quickly and work anywhere).

All HTML files live directly in `site/`. A single CSS stylesheet and other
resources are in subdirectories of `site/`.

`scripts/` contains a couple of Python scripts to automate some tedious
operations on the HTML files, like updating the headers and footers and
creating or updating HTML for images.

You don't have to build, run, or install anything beyond a web browser and a
text editor. Just `site/index.html` with your web browser. Edit the files in a
text editor and reload the current page in your browser.

To deploy, upload the contents of `site/` to the appropriate destination
(probably `public_html`) on your web server.

Working with this site should only require the basic information you can find
about CSS and HTML from https://developer.mozilla.org, along with some Python
scripting.
