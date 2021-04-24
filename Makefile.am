###############################################################################
## Makefile for Kazakh--Karakalpak
###############################################################################

LANG1=kaz
LANG2=kaa
PREFIX1=$(LANG1)-$(LANG2)
PREFIX2=$(LANG2)-$(LANG1)

BASENAME=apertium-$(PREFIX1)

TARGETS_COMMON = $(PREFIX1).autobil.bin $(PREFIX2).autobil.bin \
	$(PREFIX1).automorf.bin $(PREFIX1).autopgen.bin $(PREFIX1).autogen.bin $(PREFIX1).t1x.bin $(PREFIX1).t2x.bin \
	$(PREFIX2).automorf.bin $(PREFIX2).autopgen.bin $(PREFIX2).autogen.bin $(PREFIX2).t1x.bin $(PREFIX2).t2x.bin \
        $(PREFIX1).rlx.bin $(PREFIX2).rlx.bin \
        $(PREFIX1).lrx.bin $(PREFIX2).lrx.bin

# this defines goals for .deps, modes, and autobil.prefixes
@ap_include@

###############################################################################
## Kazakh→Karakalpak monolingual transducers
###############################################################################

$(PREFIX1).automorf.bin: $(AP_SRC1)/$(LANG1).automorf.att.gz .deps/$(PREFIX1).autobil.prefixes .deps/.d
	$(ZCAT) $< | hfst-txt2fst > .deps/$(LANG1).automorf.hfst
	hfst-compose-intersect -1 .deps/$(LANG1).automorf.hfst -2 .deps/$(PREFIX1).autobil.prefixes -o .deps/$(PREFIX1).automorf.trimmed
	hfst-fst2txt -i .deps/$(PREFIX1).automorf.trimmed -o .deps/$(PREFIX1).automorf.trimmed.att
	lt-comp lr .deps/$(PREFIX1).automorf.trimmed.att $@

$(PREFIX1).autogen.hfst: $(AP_SRC2)/$(LANG2).autogen.hfst
	cp $< $@

$(PREFIX1).autogen.bin: $(AP_SRC2)/$(LANG2).autogen.bin
	cp $< $@

###############################################################################
## Karakalpak→Kazakh monolingual transducers
###############################################################################

$(PREFIX2).automorf.bin: $(AP_SRC2)/$(LANG2).automorf.att.gz .deps/$(PREFIX2).autobil.prefixes .deps/.d
	$(ZCAT) $< | hfst-txt2fst > .deps/$(LANG2).automorf.hfst
	hfst-compose-intersect -1 .deps/$(LANG2).automorf.hfst -2 .deps/$(PREFIX2).autobil.prefixes -o .deps/$(PREFIX2).automorf.trimmed
	hfst-fst2txt -i .deps/$(PREFIX2).automorf.trimmed -o .deps/$(PREFIX2).automorf.trimmed.att
	lt-comp lr .deps/$(PREFIX2).automorf.trimmed.att $@

$(PREFIX2).autogen.hfst: $(AP_SRC1)/$(LANG1).autogen.hfst
	cp $< $@

$(PREFIX2).autogen.bin: $(AP_SRC1)/$(LANG1).autogen.bin
	cp $< $@

###############################################################################
## Bilingual dictionaries
###############################################################################

$(PREFIX1).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $<
	lt-comp lr $< $@

$(PREFIX2).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $< 
	lt-comp rl $< $@

###############################################################################
## Disambiguation rules 
###############################################################################

$(PREFIX1).rlx.bin: $(AP_SRC1)/apertium-$(LANG1).$(LANG1).rlx
	cg-comp $< $@

$(PREFIX2).rlx.bin: $(AP_SRC2)/apertium-$(LANG2).$(LANG2).rlx
	cg-comp $< $@


###############################################################################
## Lexical selection rules
###############################################################################

$(PREFIX1).lrx.bin: $(BASENAME).$(PREFIX1).lrx
	lrx-comp $< $@

$(PREFIX2).lrx.bin: $(BASENAME).$(PREFIX2).lrx
	lrx-comp $< $@

###############################################################################
## Structural transfer rules
###############################################################################

$(PREFIX1).t1x.bin: $(BASENAME).$(PREFIX1).t1x
	apertium-validate-transfer $(BASENAME).$(PREFIX1).t1x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX1).t1x $@

$(PREFIX1).t2x.bin: $(BASENAME).$(PREFIX1).t2x
	apertium-validate-transfer $(BASENAME).$(PREFIX1).t2x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX1).t2x $@

$(PREFIX2).t1x.bin: $(BASENAME).$(PREFIX2).t1x
	apertium-validate-transfer $(BASENAME).$(PREFIX2).t1x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX2).t1x $@

$(PREFIX2).t2x.bin: $(BASENAME).$(PREFIX2).t2x
	apertium-validate-transfer $(BASENAME).$(PREFIX2).t2x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX2).t2x $@

###############################################################################
## Postgeneration dictionaries
###############################################################################

$(PREFIX1).autopgen.bin: $(BASENAME).post-$(LANG1).dix
	apertium-validate-dictionary $<
	lt-comp lr $< $@

$(PREFIX2).autopgen.bin: $(BASENAME).post-$(LANG2).dix
	apertium-validate-dictionary $< 
	lt-comp lr $< $@

EXTRA_DIST=$(BASENAME).$(PREFIX1).lrx \
           $(BASENAME).$(PREFIX1).dix \
           $(BASENAME).post-$(LANG1).dix \
           $(BASENAME).$(PREFIX2).lrx \
           $(BASENAME).post-$(LANG2).dix \
           $(BASENAME).$(PREFIX1).t1x \
           $(BASENAME).$(PREFIX1).t2x \
           $(BASENAME).$(PREFIX2).t1x \
           $(BASENAME).$(PREFIX2).t2x \
           modes.xml

#$(PREFIX1).prob $(PREFIX2).prob 

apertium_kaz_kaadir=$(prefix)/share/apertium/$(BASENAME)/

# $(PREFIX1).prob $(PREFIX2).prob 

apertium_kaz_kaa_DATA=$(TARGETS_COMMON) \
		    modes.xml \
			$(BASENAME).$(PREFIX1).t1x \
			$(BASENAME).$(PREFIX1).t2x \
			$(BASENAME).$(PREFIX2).t1x \
			$(BASENAME).$(PREFIX2).t2x

# All modes are created by the same goal, listing several will just give problems with make -j2
noinst_DATA=modes/$(PREFIX1).mode


install-data-local: install-modes

CLEANFILES = $(TARGETS_COMMON)
clean-local: 
	-rm -rf .deps
