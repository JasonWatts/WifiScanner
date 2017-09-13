# Wifi Scanner Setup

# Python Dependencies Setup
while read p; do
  python3 -m pip install $p
done <requirements.txt

printf 'Please provide Google Spread sheet url:'
read url
echo $url > url.txt
