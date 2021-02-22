## TODO

Consolidate from windfarmmusic.wordpress.com. It's possible to export from the WordPress admin interface and [import into Pelican](https://docs.getpelican.com/en/4.2.0/importer.html>).

## Patrick Sanan's Website(s)
My website is split into two largely-independent sections,
distinguished by who might want to read the content and/or
subscribe to the feeds.

"professional" : This is the website you'd provide for professional purposes.
It's intended for a wide audience, including people who have never met me
or people who might want to employ me in the future.

"personal" : This is my blog, for people who know me personally or share
one of my non-job interests.

The top-level domain holds the professional site, and the personal site
is in a sub-directory.

Note: if changing the names of the subdirectories, be careful, because the two sites
refer to each other. In particular, there is customization in the upload
command in the Makefile for the professional site to avoid deleting
the personal site.

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
It seems to work to copy the file `htaccess` here
to `public_html/.htaccess` on the server.

See $HOME/work/notes/tech/2019.07.02.md as well.
