# Patrick Sanan's Website

A simple, low-maintenance, static website.

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

I would like to consolidate my old "personal" websites (thenoblesunfish.wordpress.com and windfarmmusic.wordpress.com). Maybe it's possible to export from the WordPress admin interface and [import into Pelican](https://docs.getpelican.com/en/4.2.0/importer.html>).
(Getting the text seems totally fine - the images may need more effort, as the links still point to wordprss (which actually works))

The main idea is to keep things very simple, but one feature I would like is slightly
better figures, which can

1. Have a caption inside a border
2. Have text flow around them

Both  of these seem to be possible as in this blog post: http://duncanlock.net/blog/2013/05/29/better-figures-images-plugin-for-pelican/
(Note that the post is about improving the figures, but I'd be happy with the
base state as presented there!)

