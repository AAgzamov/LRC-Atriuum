#!/usr/bin/bash

if [ "$UID" = "0" ];
then
	if [ -e /usr/local/bin/geckodriver ];
	then
		echo "geckodriver is already installed."
		chmod +x /usr/local/bin/geckodriver

	else
		echo "Downloading geckodriver..."
		wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
		echo "Unarchiving..."
		tar -xvzf geckodriver*
		chmod +x geckodriver
		echo "Moving geckodriver to /usr/local/bin..."
		mv geckodriver /usr/local/bin/
	fi
	pip3 install -r requirements.txt
else
	echo "Run with sudo!"
fi
