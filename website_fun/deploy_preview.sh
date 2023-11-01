#!/usr/bin/env sh

printf -- "Updating feed\n"
python scripts/feed_update.py

printf -- "Uploading\n"

# Requires an SSH alias "webhost"

# Images are big so don't update them
# If you want to wipe out some images to replace, do it manually for now, like
# ssh webhost  "rm -rf public_html/images/foo/"
rsync -r --progress --delete --exclude=images site/ webhost:public_html/preview/
rsync -r --progress --delete --ignore-existing site/images/ webhost:public_html/preview/images/

