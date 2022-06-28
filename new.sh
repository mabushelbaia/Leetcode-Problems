#!/bin/sh

if [ "$#" -lt 2 ]; then echo "invalid args"; exit 0; fi
if ls -la | grep "$1" > /dev/null; then
	touch ./"$1"/main."$2"
else
	mkdir ./"$1"
	touch ./"$1"/main."$2"
fi
code ./"$1"/main.$2
