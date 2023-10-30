# Source for patricksanan.org

This is a "fun" website, in the learning-to-code, web 1.0 sense.

It tries to avoid layers of abstraction and complication beyond
[basic HTML and CSS](https://developer.mozilla.org).

It's very non-scalable: it will only stay fun if it stays small and simple,
and it uses my own conventions so will likely be much less fun for
someone else.

All HTML files live directly in `site/`. A single CSS stylesheet and other
resources are in subdirectories of `site/`.

Python scripts (with only standard modules) help with some tedious operations
on the HTML files, like updating headers and footers and creating or
updating HTML for images.

Nothing needs to be built, run, or installed beyond a web browser and text
editor (assuming your system has a relatively recent Python). Open
`site/index.html` with your web browser. Edit the files in a text editor and
reload the browser page.

To deploy, upload the contents of `site/` (including hidden files) to the
appropriate destination (probably `public_html`) on your web server.
