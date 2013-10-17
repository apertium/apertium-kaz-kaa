import sys;

def proc_word(s): #{

	o = s;
	o = o.replace('% ', '<b/>');
	o = o.replace('%-', '-');

	return o;
#}

sec_copula = '''
    <!-- SECTION: Copula -->

    <e><p><l>е<s n="cop"/></l><r>e<s n="cop"/></r></p></e>

''';

sec_punctuation = '''

    <!-- SECTION: Punctuation -->
    
    <e><p><l>,<s n="cm"/></l><r>,<s n="cm"/></r></p></e>
    <e><p><l>(<s n="lpar"/></l><r>(<s n="lpar"/></r></p></e>
    <e><p><l>)<s n="rpar"/></l><r>)<s n="rpar"/></r></p></e>
    <e><p><l>[<s n="lpar"/></l><r>[<s n="lpar"/></r></p></e>
    <e><p><l>]<s n="rpar"/></l><r>]<s n="rpar"/></r></p></e>
    <e><p><l>«<s n="lquot"/></l><r>«<s n="lquot"/></r></p></e>
    <e><p><l>»<s n="rquot"/></l><r>»<s n="rquot"/></r></p></e>
    <e><p><l>“<s n="lquot"/></l><r>“<s n="lquot"/></r></p></e>
    <e><p><l>”<s n="rquot"/></l><r>”<s n="rquot"/></r></p></e>
    <e><p><l>-<s n="guio"/></l><r>-<s n="guio"/></r></p></e>
    <e><p><l>—<s n="guio"/></l><r>—<s n="guio"/></r></p></e>
    <e><p><l>'<s n="apos"/></l><r>'<s n="apos"/></r></p></e>
    <e><re>[.\?;:!"]+</re><p><l><s n="sent"/></l><r><s n="sent"/></r></p></e>
    <e><re>[№%]?[0-9]+([.,][0-9]+)*[.,]*</re><p><l><s n="num"/></l><r><s n="num"/></r></p></e> 

''';

sec_proper_nouns = ''.join(open('proper-nouns.dix').readlines());

pos_list = ['cnjcoo', 'cnjsub', 'post', 'pron', 'det', 'num', 'n', 'np', 'adj', 'adv', 'vt', 'vi'];

pos_name = {
	'post': 'Postpositions',
	'pron': 'Pronouns',
	'det': 'Determiners',
	'num': 'Numerals',
	'cnjcoo': 'Conjunctions',
	'n': 'Nouns',
	'np': 'Proper nouns',
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

sym_list = ['post', 'cop', 'cnjcoo', 'cnjsub', 'prn', 'det', 'num', 'n', 'np', 'adj', 'adv', 'v', 'tv', 'iv', 'sent', 'lpar', 'rpar', 'guio', 'cm', 'apos', 'lquot', 'rquot'];


print('<dictionary>');
print('  <alphabet/>');
print('  <sdefs>');
for sym in sym_list: #{
	print('    <sdef n="%s"/>' % sym);
#}
print('  </sdefs>');
print('  <section id="main" type="standard">');

print(sec_copula);

num_entries = 0;
num_checked = 0;

pos_word = {};

for line in sys.stdin.readlines(): #{

	if line.count('Kazakh') > 0: #{

		continue;
	#}

	if line.strip() == '': #{
		continue;
	#}

	num_entries = num_entries + 1;

	row = line.split('\t');

	if row[3] == 'x': #{
		if row[1] not in pos_word: #{
			pos_word[row[1]] = [];
		#}
		if (row[0], row[2]) not in pos_word[row[1]]: #{
			pos_word[row[1]].append((row[0], row[2]));
		#}
		num_checked = num_checked + 1;
		#print(row[0], row[1], row[2], row[1]);
	else: #{
		continue;
	#}

#}

for pos in pos_list: #{
	if pos == 'np': #{
		print(sec_proper_nouns);
		continue;
	#}
	if pos in pos_name: #{
		print('    <!-- SECTION:', pos_name[pos], '-->');
	#}
	if pos not in pos_word: #{
		continue;
	#}
	for w in pos_word[pos]: #{
		
		print('    <e><p><l>%s%s</l><r>%s%s</r></p></e>' % (proc_word(w[0]), pos_sym[pos], proc_word(w[1]), pos_sym[pos]));
		
	#}
	print('');
#}

print(sec_punctuation);

print('  </section>');
print('</dictionary>');

print(num_entries, num_checked, file=sys.stderr);
