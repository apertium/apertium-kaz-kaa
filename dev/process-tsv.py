import sys;

def proc_word(s): #{

	o = s;
	o = o.replace('% ', '<b/>');
	o = o.replace('%-', '-');

	return o;
#}

pos_list = ['cnjcoo', 'cnjsub', 'post', 'pron', 'det', 'num', 'n', 'adj', 'adv', 'vt', 'vi'];

pos_name = {
	'post': 'Postpositions',
	'pron': 'Pronouns',
	'det': 'Determiners',
	'num': 'Numerals',
	'cnjcoo': 'Conjunctions',
	'n': 'Nouns',
	'adj': 'Adjectives',
	'adv': 'Adverbs',
	'vt': 'Verbs',
}

pos_sym = {
	'post': '<s n="post"/>',
	'cnjcoo': '<s n="cnjcoo"/>',
	'cnjsub': '<s n="cnjsub"/>',
	'pron': '<s n="prn"/>',
	'det': '<s n="det"/>',
	'num': '<s n="num"/>',
	'n': '<s n="n"/>',
	'adj': '<s n="adj"/>',
	'adv': '<s n="adv"/>',
	'vt': '<s n="v"/><s n="tv"/>',
	'vi': '<s n="v"/><s n="iv"/>'
};

pos_word = {};

for line in sys.stdin.readlines(): #{

	if line.count('Kazakh') > 0: #{

		continue;
	#}

	if line.strip() == '': #{
		continue;
	#}

	row = line.split('\t');

	if row[3] == 'x': #{
		if row[1] not in pos_word: #{
			pos_word[row[1]] = [];
		#}
		if (row[0], row[2]) not in pos_word[row[1]]: #{
			pos_word[row[1]].append((row[0], row[2]));
		#}
		#print(row[0], row[1], row[2], row[1]);
	else: #{
		continue;
	#}
#}

for pos in pos_list: #{
	if pos in pos_name: #{
		print('    <!-- SECTION: ', pos_name[pos], ' -->');
	#}
	if pos not in pos_word: #{
		continue;
	#}
	for w in pos_word[pos]: #{
		
		print('    <e><p><l>%s%s</l><r>%s%s</r></p></e>' % (proc_word(w[0]), pos_sym[pos], proc_word(w[1]), pos_sym[pos]));
		
	#}
	print('');
#}
