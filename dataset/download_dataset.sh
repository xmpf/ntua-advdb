#!/bin/bash -

URL="http://www.cslab.ntua.gr/courses/atds/yellow_trip_data.zip"

echo "Downloading dataset..."
wget "$URL" -O dataset.zip 2>/dev/null
unzip dataset.zip
rm -i ./dataset.zip
