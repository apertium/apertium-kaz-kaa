#!/bin/bash

# Assuming that you have the whole apertium tree in your source dir and you are in kaz-kaa directory.

# You have to compile apertium-kaz and apertium-kaa first.

cp ../../languages/apertium-kaz/kaz.automorf.att.gz apertium-kaz-kaa.kaz-kaa.LR.att.gz
cp ../../languages/apertium-kaz/kaz.autogen.att.gz apertium-kaz-kaa.kaa-kaz.RL.att.gz
cp ../../incubator/apertium-kaa/kaa.automorf.att.gz apertium-kaz-kaa.kaa-kaz.LR.att.gz
cp ../../incubator/apertium-kaa/kaa.autogen.att.gz apertium-kaz-kaa.kaz-kaa.RL.att.gz

DIFF=$(diff ../../languages/apertium-kaz/apertium-kaz.kaz.rlx apertium-kaz-kaa.kaz-kaa.rlx)
if [ "$DIFF" != "" ]; then
        cp ../../languages/apertium-kaz/apertium-kaz.kaz.rlx apertium-kaz-kaa.kaz-kaa.rlx
fi;

DIFF=$(diff ../../incubator/apertium-kaa/apertium-kaa.kaa.rlx apertium-kaz-kaa.kaa-kaz.rlx)
if [ "$DIFF" != "" ]; then
        cp ../../incubator/apertium-kaa/apertium-kaa.kaa.rlx apertium-kaz-kaa.kaa-kaz.rlx
fi;

exit 0


