# Source for patricksanan.org

This is a "fun" website, in the learning-to-code, web 1.0 sense.

It tries to avoid layers of abstraction above HTML and CSS.

It's very non-scalable: it will only stay fun if it stays small and simple.

All HTML files live directly in `site/`. A single CSS stylesheet and other
resources are in subdirectories of `site/`.

Python scripts help with some tedious operations on the HTML files, like
updating the headers and footers and creating or updating HTML for images.

Nothing needs to be built, run, or installed anything beyond a web browser and a
text editor. Open `site/index.html` with your web browser. Edit the files in a
text editor and reload the current page in your browser.

To deploy, upload the contents of `site/` to the appropriate destination
(probably `public_html`) on your web server.

Working with this site should only require the basic information you can find
about CSS and HTML from https://developer.mozilla.org, along with some Python
scripting.
