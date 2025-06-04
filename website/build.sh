# chmod +x build.sh
# PUSH WEBSITE TO GU DOMAINS    

printf 'Push to GU domains? (y/n)? '
read answer 
if [ "$answer" != "${answer#[Yy]}" ] ;then
    rsync -alvr --delete _site/ nandinik@gtown3.reclaimhosting.com:/home/nandinik/public_html/data_viz

else
    echo NOT PUSHNG TO GU DOMAINS!
fi
