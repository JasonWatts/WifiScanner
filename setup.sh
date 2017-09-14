# Wifi Scanner Setup

# Python Dependencies Setup
echo 'Starting Setup...'
{
	while read p; do
	  python3 -m pip install $p
	done <requirements.txt

} && {
	printf 'Please provide Google Spread sheet url: '
	read url
	echo $url > info.txt
	printf 'User (e.g. carmacost): '
	read user
	echo $user >> info.txt
	printf 'Device (e.g. mac or pc): '
	read device
	echo $device >> info.txt

	printf '\nAwesome! You are done!  If you made any mistakes just run the setup script again :) \n\n'
} || {
	echo 'There appears to be an error with Python. Contact James'
}

