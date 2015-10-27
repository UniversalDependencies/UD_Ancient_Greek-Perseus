# UD Ancient Greek

Ancient Greek Dependency Treebank (AGDT) from the Perseus Project
http://nlp.perseus.tufts.edu/syntax/treebank/

@incollection {grc,
  author      = {Bamman, David and Crane, Gregory},
  year        = {2011}
  affiliation = {Perseus Project, Tufts University, Medford/Somerville, USA},
  title       = {The {A}ncient {G}reek and {L}atin Dependency Treebanks},
  booktitle   = {Language Technology for Cultural Heritage},
  series      = {Theory and Applications of Natural Language Processing},
  publisher   = {Springer Berlin Heidelberg},
  isbn        = {978-3-642-20227-8},
  keyword     = {Computer Science},
  pages       = {79--98},
}

Creative Commons Attribution-NonCommercial-ShareAlike 2.5 License:
http://creativecommons.org/licenses/by-nc-sa/2.5

The first conversion of AGDT to Universal Dependencies was published in HamleDT 3.0
(http://ufal.mff.cuni.cz/hamledt/; http://hdl.handle.net/11234/1-1508), using
a procedure designed by Dan Zeman (zeman@ufal.mff.cuni.cz) and implemented in
the Treex framework (http://ufal.mff.cuni.cz/treex/).

The HamleDT conversion is based on AGDT version 1.2 (while the current version
at the Perseus Project is 1.7). The two smallest files were taken as
development and test data respectively:
dev .... 1999.01.0013.xml ... Aeschylus (Seven Against Thebes)
test ... 1999.01.0015.xml ... Aeschylus (Supplian Women)

Subsequently it appears in the UD 1.2 release; the conversion procedure has
been slightly improved since HamleDT 3.0, hence the data are not necessarily
identical.

=== Machine-readable metadata =================================================
Documentation status: partial
Data source: automatic
Data available since: UD v1.2
License: CC BY-NC-SA 2.5
Genre: fiction
Contributors: Celano, Giuseppe G. A.; Zeman, Daniel
===============================================================================

===============================================================================
From the README file of the legacy project:
===============================================================================

This is a README file for the Ancient Greek Dependency Treebank, version 1.2.


1. Preamble

	1.1 Source

		The Ancient Greek Dependency Treebank is available at:

		http://nlp.perseus.tufts.edu/syntax/treebank/


	1.2 License

		AGDT 1.2 is licensed under a Creative Commons Attribution-
		NonCommercial-ShareAlike 2.5 License:

		http://creativecommons.org/licenses/by-nc-sa/2.5


2. Documentation

	2.1 Data Format

		The data given in this treebank is provided as an XML document.  Each
		word contains six required attributes:

		id: This is a unique identifier, and corresponds to the word's linear
		position in the sentence.  The first word in a sentence is given
		id 1.

		cid: This is a canical identifier for the word within the larger corpus.

		form: The token form of the word, in Beta Code.

		lemma: The base lemma from which the word is derived, in Beta Code.

		head: The id of the word's parent.  If a word depends on the sentence
		root, its head is 0.

		relation: The syntactic relation between the word and its parent.  A
		catalogue of syntactic tags can be found in the syntactic guidelines
		described below.

		postag: The morphological analysis for the word.  This field is 9
		characters long, and corresponds to the following morphological
		features:

			1: 	part of speech

				n	noun
				v	verb
				t	participle
				a	adjective
				d	adverb
				l	article
				g	particle
				c	conjunction
				r	preposition
				p	pronoun
				m	numeral
				i	interjection
				e	exclamation
				u	punctuation

			2: 	person

				1	first person
				2	second person
				3	third person

			3: 	number

				s	singular
				p	plural
				d	dual

			4: 	tense

				p	present
				i	imperfect
				r	perfect
				l	pluperfect
				t	future perfect
				f	future
				a	aorist

			5: 	mood

				i	indicative
				s	subjunctive
				o	optative
				n	infinitive
				m	imperative
				p	participle
				d	gerund
				g	gerundive

			6: 	voice

				a	active
				p	passive
				m	middle
				e	medio-passive

			7:	gender

				m	masculine
				f	feminine
				n	neuter

			8: 	case

				n	nominative
				g	genitive
				d	dative
				a	accusative
				v	vocative
				l	locative

			9: 	degree

				c	comparative
				s	superlative

			---

			For example, the postag for the noun "a)/ndra" is "n-s---ma-",
			which corresponds to the following features:

			1: n	noun
			2: -
			3: s	singular
			4: -
			5: -
			6: -
			7: m	masculine
			8: a	accusative
			9: -



	2.2 Text

		AGDT 1.2 is comprised of 13 texts, in the following distribution:

		Hesiod, Shield of Heracles: 3,834 words
		Hesiod, Theogony: 8,106 words
		Hesiod, Works and Days: 8,106 words

		Homer, Iliad: 128,102 words
		Homer, Odyssey: 104,467 words

		Aeschylus, Agamemnon: 9,806 words
		Aeschylus, Eumenides: 6,380 words
		Aeschylus, Libation Bearers: 6,563 words
		Aeschylus, Persians: 6,223 words
		Aeschylus, Prometheus Bound: 7,045 words
		Aeschylus, Seven Against Thebes: 6,206 words
		Aeschylus, Suppliants: 5,949 words

		Sophocles, Ajax: 9,474 words

		The editions of these texts are as follows:

		Hesiod. The Homeric Hymns and Homerica with an English Translation by
		Hugh G. Evelyn-White. Works and Days. Cambridge, MA.,Harvard University
		Press; London, William Heinemann Ltd. 1914.

		Homer. The Odyssey with an English Translation by A. T. Murray.
		Cambridge, MA., Harvard University Press; London, William Heinemann,
		Ltd. 1919.

		Homer. Homeri Opera in five volumes. Oxford, Oxford University Press.
		1920.

		Aeschylus. Aeschylus, with an English translation by Herbert Weir Smyth,
		Ph. D. in two volumes. Cambridge. Cambridge, Mass., Harvard University
		Press; London, William Heinemann, Ltd. 1926.

		Sophocles. The Ajax of Sophocles. Edited with introduction and notes by
		Sir Richard Jebb. Sir Richard Jebb. Cambridge. Cambridge University
		Press. 1893.


		The following document_ids in the treebank correspond to the following
		works:

		Perseus:text:1999.01.0127	Hesiod (Shield of Heracles)
		Perseus:text:1999.01.0129	Hesiod (Theogony)
		Perseus:text:1999.01.0131	Hesiod (Works and Days)

		Perseus:text:1999.01.0133	Homer (Iliad)
		Perseus:text:1999.01.0135	Homer (Odyssey)

		Perseus:text:1999.01.0003	Aeschylus (Agamemnon)
		Perseus:text:1999.01.0005	Aeschylus (Eumenides)
		Perseus:text:1999.01.0007	Aeschylus (Libation Bearers)
		Perseus:text:1999.01.0009	Aeschylus (Prometheus Bound)
		Perseus:text:1999.01.0011	Aeschylus (Persians)
		Perseus:text:1999.01.0013	Aeschylus (Seven Against Thebes)
		Perseus:text:1999.01.0015	Aeschylus (Supplian Women)

		Perseus:text:1999.01.0183	Sophocles (Ajax)

	2.3 Annotation Standards

		This release of the treebank has been annotated according to the
		guidelines specified in version 1.1 of the "Guidelines for the Syntactic
		Annotation of the Ancient Greek Dependency Treebank (1.1)," found in
		docs/guidelines.pdf


	2.4 Authorship

		Aside from the scholarly treebanks of Aeschylus (ed., Francesco Mambrini)
		and Sophocles (ed., Dan Libatique), each sentence in the Ancient Greek
		Dependency Treebank is built from the efforts of two independent annotators
		(marked "primary" in the data) reconciled by a third (marked "secondary").
		We would like to recognize the contribution of the following individuals
		toward its creation and thank them for their commitment to the advancement
		of Classical scholarship:

		Jennifer Adams, James Artz, Jennifer Curtin, James C. D'Amico, W. B. Dolan,
		Calliopi Dourou, Scott J. Dube, C. Dan Earley, J. F. Gentile, Francis Hartel,
		Connor Hayden, Kenny Hickman, Tovah Keynton, Michael Kinney, Florin Leonte,
		Alex Lessie, Daniel Lim Libatique, Brian Livingston, Viet Luong, Meg Luthin,
		George Matthews, Molly Miller, Jack Mitchell, Skylar Neil, Robin Ngo, Jessica
		Nord, Anthony D. Yates, Sam Zukoff and the Tufts University LAT-181 class
		(Spring 2008).
