#!/usr/bin/env sh

printf -- "Updating feed\n"
python scripts/feed_update.py

printf -- "Updating non-image files\n"
# Images are big so don't update existing files in any "image" directories
# If you want to wipe out some images to update, do it manually for now, like
# ssh webhost  "rm -rf public_html/images/foo/"
rsync -r --progress --delete --exclude=images/ site/ webhost:public_html/

printf -- "Uploading new image files\n"
rsync -r --progress --delete --ignore-existing site/images/ webhost:public_html/images/
