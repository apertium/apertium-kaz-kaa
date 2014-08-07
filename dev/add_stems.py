import sys;

fordix = {
		'N1' : '<e><p><l>[1]<s n="n"/></l><r>[2]<s n="n"/></r></p></e>',
		'N5' : '<e><p><l>[1]<s n="n"/></l><r>[2]<s n="n"/></r></p></e>',
		'N6' : '<e><p><l>[1]<s n="n"/></l><r>[2]<s n="n"/></r></p></e>',
		'A1' : '<e><p><l>[1]<s n="adj"/></l><r>[2]<s n="adj"/></r></p></e>',
		'A2' : '<e><p><l>[1]<s n="adj"/></l><r>[2]<s n="adj"/></r></p></e>',
		'A3' : '<e><p><l>[1]<s n="adj"/></l><r>[2]<s n="adj"/></r></p></e>', 
		'A4' : '<e><p><l>[1]<s n="adj"/></l><r>[2]<s n="adj"/></r></p></e>',
		'ADV' : '<e><p><l>[1]<s n="adv"/></l><r>[2]<s n="adv"/></r></p></e>',
		'CA' : '<e><p><l>[1]<s n="cnjadv"/></l><r>[2]<s n="cnjadv"/></r></p></e>',
		'V-IV' : '<e><p><l>[1]<s n="v"/><s n="iv"/></l><r>[2]<s n="v"/><s n="iv"/></r></p></e>',
		'V-TV' : '<e><p><l>[1]<s n="v"/><s n="tv"/></l><r>[2]<s n="v"/><s n="tv"/></r></p></e>',
		'NP-TOP' : '<e><p><l>[1]<s n="np"/><s n="top"/></l><r>[2]<s n="np"/><s n="top"/></r></p></e>',
		'NP-ANT-M' : '<e><p><l>[1]<s n="np"/><s n="ant"/><s n="m"/></l><r>[2]<s n="np"/><s n="ant"/><s n="m"/></r></p></e>',
		'NP-COG-MF' : '<e><p><l>[1]<s n="np"/><s n="cog"/><s n="mf"/></l><r>[2]<s n="np"/><s n="cog"/><s n="mf"/></r></p></e>',
		'ABBR' : '<e><p><l>[1]<s n="abbr"/></l><r>[2]<s n="abbr"/></r></p></e>'
		}

def proc_lexc(s): #{

	o = s;
	o = o.replace('-', '%-');
	o = o.replace(' ', '% ');
	o = o.replace('\'', '%\'');
	o = o.replace('.', '%.');

	return o;
#}

def proc_dix(s): #{

	o = s;
	o = o.replace(' ', '<b/>');

	return o;
#}

# input_lexc = open("../../apertium-kaa/apertium-kaa.kaa.lexc", "r");
# input_dix = open("../apertium-kaz-kaa.kaz-kaa.dix", "r");

file_lexc = open('kaalexc.txt','w');
file_dix = open('kaadix.txt','w');
num_entries = 0; # number of stems added

for line in sys.stdin.readlines(): #{

	if ':' in line: #{
		file_lexc.write(line[:-2] + "\n");
		file_dix.write(line[:-2] + "\n");
		symbol = line[:-2];
		continue;
	#}

	line = line.strip();

	if line == '': #{
		file_lexc.write(line + "\n");
		file_dix.write(line + "\n");
		continue;
	#}

	num_entries = num_entries + 1;

	row = line.split(' ', 1); # row[0] - kaz, row[1] - kaa

	kaa_lexc = proc_lexc(row[1]);
	file_lexc.write(kaa_lexc + ":" + kaa_lexc + " " + symbol + " ; ! \"\"\n");
	# proc_line = kaa_lexc + ":" + kaa_lexc + " " + symbol + " ; ! \"\"\n";

	# inserted = False;
	# found = False;
	# for line0 in input_lexc:
	# 	if not inserted and " " + symbol + " ; ! " in line0:
	# 		found = True;
	# 		print("found " + proc_line);
	# 	if found:
	# 		file_lexc.write(proc_line);
	# 		inserted = True;
	# 		found = False;
	# 	file_lexc.write(line0);


	linedix = proc_dix(row[1]);
	file_dix.write(fordix[symbol].replace('[1]', row[0]).replace('[2]', linedix) + "\n");
	# proc_line = "\t" + fordix[symbol].replace('[1]', row[0]).replace('[2]', linedix) + "\n";

	# inserted = False;
	# found = False;
	# index1 = fordix[symbol].find(']');
	# index2 = fordix[symbol].find('[', index1);
	# for line0 in input_dix:
	# 	if not inserted and fordix[symbol][index1+1:index2] in line0:
	# 		found = True;
	# 	if found:
	# 		file_dix.write(proc_line);
	# 		inserted = True;
	# 		found = False;
	# 	file_dix.write(line0);


	# #print(line.count('\t'), len(row), row[0], row[1], row[2], row[1], file=sys.stderr);
	# #print(line.count('\t'), row[2:], line.strip(), file=sys.stderr);
	# if line.count(' ') >= 5: #{ 
	# 	if row[0] in open('wiki2.txt').read():
	# 		if row[0] not in open('kaa-pronouns.txt').read():
	# 			print(line);
	# 		# else:
	# 			# print("YES: " + line);
	# #}


	# input_lexc = open("kaalexc.txt", "r");
	# input_dix = open("kaadix.txt", "r");
#}

# input_lexc.close();
# input_dix.close();
file_dix.close();
file_lexc.close(); # you can omit in most cases as the destructor will call if

print(str(num_entries) + " stems successfully added!");