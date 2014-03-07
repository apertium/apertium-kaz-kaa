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

sec_abbreviations = '''
    <!-- SECTION: Abbreviations -->

    <e><p><l>ж.<s n="abbr"/></l><r>j.<s n="abbr"/></r></p></e>
    <e><p><l>жж.<s n="abbr"/></l><r>jj.<s n="abbr"/></r></p></e>
    <e><p><l>т.б.<s n="abbr"/></l><r>t.b.<s n="abbr"/></r></p></e>
    <e><p><l>кг<s n="abbr"/></l><r>kg<s n="abbr"/></r></p></e>
    <e><p><l>км<s n="abbr"/></l><r>km<s n="abbr"/></r></p></e>
    <e><p><l>км²<s n="abbr"/></l><r>km²<s n="abbr"/></r></p></e>
    <e><p><l>км³<s n="abbr"/></l><r>km³<s n="abbr"/></r></p></e>

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

sym_list = ['post', 'cop', 'cnjcoo', 'cnjsub', 'prn', 'det', 'num', 'n', 'np', 'adj', 'adv', 'v', 'tv', 'iv', 'ant', 'top', 'pers', 'abbr', 'sent', 'lpar', 'rpar', 'guio', 'cm', 'apos', 'lquot', 'rquot'];

pos_static = {};
pos_static['pron'] = '''

    <e><p><l>мен<s n="prn"/><s n="pers"/></l><r>men<s n="prn"/><s n="pers"/></r></p></e>
    <e><p><l>сен<s n="prn"/><s n="pers"/></l><r>sen<s n="prn"/><s n="pers"/></r></p></e>
    <e><p><l>ол<s n="prn"/><s n="pers"/></l><r>ol<s n="prn"/><s n="pers"/></r></p></e>
    <e><p><l>біз<s n="prn"/><s n="pers"/></l><r>biz<s n="prn"/><s n="pers"/></r></p></e>
    <e><p><l>сіз<s n="prn"/><s n="pers"/></l><r>siz<s n="prn"/><s n="pers"/></r></p></e>
''';

pos_static['cnjcoo'] = '''

    <e><p><l>да<s n="cnjcoo"/></l><r>da<s n="cnjcoo"/></r></p></e>

''';

pos_static['num'] = '''
    <e><p><l>I<s n="num"/></l><r>I<s n="num"/></r></p></e>
    <e><p><l>II<s n="num"/></l><r>II<s n="num"/></r></p></e>
    <e><p><l>III<s n="num"/></l><r>III<s n="num"/></r></p></e>
    <e><p><l>IV<s n="num"/></l><r>IV<s n="num"/></r></p></e>
    <e><p><l>V<s n="num"/></l><r>V<s n="num"/></r></p></e>
    <e><p><l>VI<s n="num"/></l><r>VI<s n="num"/></r></p></e>
    <e><p><l>VII<s n="num"/></l><r>VII<s n="num"/></r></p></e>
    <e><p><l>VIII<s n="num"/></l><r>VIII<s n="num"/></r></p></e>
    <e><p><l>IX<s n="num"/></l><r>IX<s n="num"/></r></p></e>
    <e><p><l>X<s n="num"/></l><r>X<s n="num"/></r></p></e>
    <e><p><l>XI<s n="num"/></l><r>XI<s n="num"/></r></p></e>
    <e><p><l>XII<s n="num"/></l><r>XII<s n="num"/></r></p></e>
    <e><p><l>XIII<s n="num"/></l><r>XIII<s n="num"/></r></p></e>
    <e><p><l>XIV<s n="num"/></l><r>XIV<s n="num"/></r></p></e>
    <e><p><l>XV<s n="num"/></l><r>XV<s n="num"/></r></p></e>
    <e><p><l>XVI<s n="num"/></l><r>XVI<s n="num"/></r></p></e>
    <e><p><l>XVII<s n="num"/></l><r>XVII<s n="num"/></r></p></e>
    <e><p><l>XVIII<s n="num"/></l><r>XVIII<s n="num"/></r></p></e>
    <e><p><l>XIX<s n="num"/></l><r>XIX<s n="num"/></r></p></e>
    <e><p><l>XX<s n="num"/></l><r>XX<s n="num"/></r></p></e>
    <e><p><l>XXI<s n="num"/></l><r>XXI<s n="num"/></r></p></e>
''';

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

	line = line.strip();

	if line == '': #{
		continue;
	#}

	num_entries = num_entries + 1;

	row = line.split('\t');

	#print(line.count('\t'), len(row), row[0], row[1], row[2], row[1], file=sys.stderr);
	#print(line.count('\t'), row[2:], line.strip(), file=sys.stderr);
	if line.count('\t') >= 3: #{ 
		if row[3] == 'x' or row[3] == 'х': #{
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

#}

for pos in pos_list: #{
	if pos == 'np': #{
		print(sec_proper_nouns);
		continue;
	#}
	if pos in pos_name: #{
		print('    <!-- SECTION:', pos_name[pos], '-->');
	#}
	if pos in pos_static: #{
		print(pos_static[pos]);
	#}
	if pos not in pos_word: #{
		continue;
	#}
	for w in pos_word[pos]: #{
		
		print('    <e><p><l>%s%s</l><r>%s%s</r></p></e>' % (proc_word(w[0]), pos_sym[pos], proc_word(w[1]), pos_sym[pos]));
		
	#}
	print('');
#}

print(sec_abbreviations);

print(sec_punctuation);

print('  </section>');
print('</dictionary>');

print(num_entries, num_checked, "%.2f%%" % (float(num_checked)/float(num_entries)*100.0), file=sys.stderr);
