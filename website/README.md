# Source for patricksanan.org

This is a "fun" website, in the web 1.0 sense.

It tries to avoid layers of abstraction and complication beyond
[basic HTML and CSS](https://developer.mozilla.org). It takes
any available option to be simpler.

It's non-scalable: it will stay "fun" iff it stays small and simple.
It's probably only directly useful to me (though ideally it encourages
you to do something similar and useful to you).

HTML files live directly in `site/`. A CSS stylesheet and other
resources are in subdirectories of `site/`.

There is no "build" - Open `site/index.html` with your web browser. Edit the
files in a text editor and reload the browser page.

To deploy, upload the contents of `site/` (including hidden files) to your
web server (probably to `$HOME/public_html`).

Python scripts in `scripts/`, (using only standard modules) help with some tedious operations
like updating/generating HTML for headers, footers, and images.

`deploy.sh`, for convenience, gives more hints.

Scripts use some command line tools:

* rsync to upload
* ImageMagick to shrink images

Other helpful tools:
* Git to track changes
* Shellcheck and Pylint to check style
* Yapf to format Python
