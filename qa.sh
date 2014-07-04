#!/bin/bash

# Takes the basename of the test scrpt in /test-scripts as an argument,
# an additional argument if the test requires it, and runs the test.
#
# Usage: ./qa.sh kaz-kaa-t1x
#        ./qa.sh kaz-kaa-testvoc reg
# If invoked without arguments ('./qa.sh'), will default to './qa.sh all'.

if [ $# -eq 0 ]
then
    testToRun=all.test
else
    testToRun=$1.test
fi

bash "test-scripts/$testToRun" "$2"
