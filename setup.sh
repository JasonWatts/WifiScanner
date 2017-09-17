# Wifi Scanner Setup

# Python Dependencies Setup
echo 'Starting Setup...'
{
	while read p; do
	  pip3 install --user $p
	done <requirements.txt

} && {
	printf 'Please provide Google Spread sheet url: '
	read url
	printf 'User (e.g. carmacost): '
	read user
	printf 'Device (e.g. Mac or Pc): '
	read device
	printf '{\n"url": "%s",\n"user": "%s",\n"device": "%s"\n}' "$url" "$user" "$device" > info.json

	printf '\nAwesome! You are done!  If you made any mistakes just run the setup script again :) \n\n'
} || {
	echo 'There appears to be an error with Python. Contact James'
}

