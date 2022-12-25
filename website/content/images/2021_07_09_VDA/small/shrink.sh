cp ../*.jpg .
mogrify -auto-orient -thumbnail 300x *.jpg

cp ../pano_*.jpg .
mogrify -auto-orient -thumbnail 800x pano*.jpg
