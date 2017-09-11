# Wifi Scanner Setup

# Python Dependencies Setup
while read p; do
  sudo pip3 install $p
done <dependencies.txt

echo "Dependencies Installed!"
