#!/usr/bin/sh

if [ "$UID" = "0" ];
then

	echo "Downloading geckodriver..."
	wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
	echo "Unarchiving..."
	tar -xvzf geckodriver*
	chmod +x geckodriver
	echo "Moving geckodriver to /usr/local/bin..."
	mv geckodriver /usr/local/bin/
else
	echo "Run with sudo!"
fi
