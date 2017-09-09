# Wifi Scanner Setup

# Python Dependencies Setup
while read p; do
  pip install $p
done <dependencies.txt

echo "Dependencies Installed"
