My website is split into two largely-independent sections.
These are distinguished in terms of who might want to read the content and/or
subscribe to the feeds.

"Professional" : This is the website you'd provide for professional purposes.
It's intended for a wide audience, including people who have never met me
or people who might want to employ me in the future.

"Personal" : This is my "blog," for people who know me personally or share
one of my non-job interests like trailrunning or making music (for the pure
art of it - I hope to have some audio stuff on the professional site at
some point in my life!)

The top-level domain should just be the professional site.

# For each sub-site 

Uses pelican: see https://docs.getpelican.com/en/stable/quickstart.html

I used `pelican-quickstart`, using rsync/ssh to send to the `public_html` dir
on the server.

Relies on submodules for the theme and plugins:

    git submodule update --init --recursive

To build the website:

    make html

To see locally:

    pelican --listen
    # navigate to localhost:8000 in web browser
    # But note that by defaults links will be the the web versions of the pages

To push to server:

    make rsync_upload

## SSL / HTTPS / .htaccess

Note that you have to somehow enable https, or a web browser will mark as "not secure".
Blindly following instructions from Bluehost, it works to copy the file `htaccess` here
to `public_html/.htaccess` on the server.

## Desired Improvements

Finish consolidating my old "personal" websites (thenoblesunfish.wordpress.com and windfarmmusic.wordpress.com). It's possible to export from the WordPress admin interface and [import into Pelican](https://docs.getpelican.com/en/4.2.0/importer.html>).
(Getting the text seems totally fine - the images may need more effort, as the links still point to wordprss (which actually works))
