SHTML="python3 $HOME/scripts/strip-html.py"
unzip -p $1 content.xml  | sed 's/<\/table:table-cell><table:table-cell/<\/table:table-cell>@<table:table-cell/g'  | xmllint --format - | $SHTML  | sed 's/^ *//g' | sed 's/@/\t/g' | grep -v '^$' 
#| sed 's/$/\t\t/g' | sed 's/\t\t\t\t/\t\t/g' | sed 's/\t\t\t/\t\t/g' | sed 's/\tx\t\t$/\tx\t/g' 
