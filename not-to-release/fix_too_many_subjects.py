import os
import udapi

# Fix too-many-subjects errors in UD_Ancient_Greek-Perseus train split.
# Each entry: (sent_id, list_of_operations)
# Operations:
#   ('deprel', node_ord, new_deprel)          — change deprel of node
#   ('reparent', node_ord, new_head_ord, new_deprel) — change head and deprel of node

FIXES = {
    # ταῦτα (4) is the raised/outer subject of the embedded clause; Ὀδυσσεύς (8) is the matrix nsubj
    'tlg0012.tlg001.perseus-grc1.tb.xml@2282450': [
        ('deprel', 4, 'nsubj:outer'),
    ],

    # ἣ (1) is a relative pronoun subject of the relative clause; Ἥρη (7) is the antecedent.
    # Reparent Ἥρη to ἣ as apposition so ἣ remains the sole nsubj.
    'tlg0012.tlg001.perseus-grc1.tb.xml@2275814': [
        ('reparent', 7, 1, 'appos'),
    ],

    # Two relative pronoun αἳ: node 1 is the outer/topicalized subject, node 18 is the main nsubj.
    'tlg0013.tlg002.perseus-grc1.tb.xml@84': [
        ('deprel', 1, 'nsubj:outer'),
    ],

    # ὁρμή (11) and ἐπιχείρησις (24) both nsubj of same predicate.
    # ἐπιχείρησις is a conjoined/second topic → nsubj:outer
    'tlg0016.tlg001.perseus-grc1.1.tb.xml@86': [
        ('deprel', 24, 'nsubj:outer'),
    ],

    # ACI: βούλεσθαι (16) is the inf predicate; ἐμεωυτόν (23) is the accusative subject of the ACI → obj
    'tlg0016.tlg001.perseus-grc1.1.tb.xml@287': [
        ('deprel', 23, 'obj'),
    ],

    # ὅ (10) is a relative pronoun used as object, not subject; ἕκαστος (13) is the real nsubj
    'tlg0016.tlg001.perseus-grc1.1.tb.xml@324': [
        ('deprel', 10, 'obj'),
    ],

    # εὖρος (16) belongs to a different clause; reparent to node 18 as nsubj of that predicate
    'tlg0016.tlg001.perseus-grc1.1.tb.xml@683': [
        ('reparent', 16, 18, 'nsubj'),
    ],

    # Ἀστυάγης (19) is subject of the relative/embedded clause headed by node 22, not of περίοδος's clause
    'tlg0016.tlg001.perseus-grc1.1.tb.xml@779': [
        ('reparent', 19, 22, 'nsubj'),
    ],

    # τάδε (6) is the matrix nsubj; πόνοι (25) is outer/topicalized subject
    'tlg0016.tlg001.perseus-grc1.1.tb.xml@936': [
        ('deprel', 25, 'nsubj:outer'),
    ],

    # οἰκέοντας (32) is the subject of a subordinate participle clause headed by node 35
    'tlg0016.tlg001.perseus-grc1.1.tb.xml@989': [
        ('reparent', 32, 35, 'nsubj'),
    ],

    # δέ (2) is a discourse particle, not a subject; should be advmod
    'tlg0016.tlg001.perseus-grc1.1.tb.xml@1010': [
        ('deprel', 2, 'advmod'),
    ],

    # οὐδέν (24) is the subject of the embedded clause headed by node 23
    'tlg0016.tlg001.perseus-grc1.1.tb.xml@1041': [
        ('reparent', 24, 23, 'nsubj'),
    ],

    # οὗτοι (23) is the subject of the relative clause headed by node 26
    'tlg0016.tlg001.perseus-grc1.1.tb.xml@1203': [
        ('reparent', 23, 26, 'nsubj'),
    ],

    # αὐτός (47) is the outer/raised subject of an embedded predicate; Κῦρος (1) is the matrix nsubj
    'tlg0016.tlg001.perseus-grc1.1.tb.xml@1498': [
        ('deprel', 47, 'nsubj:outer'),
    ],

    # μηχανή (3) is the outer subject; ἐκεῖνον (11) is the main nsubj of the embedded clause
    'tlg0016.tlg001.perseus-grc1.1.tb.xml@1508': [
        ('deprel', 3, 'nsubj:outer'),
    ],

    # λεγόμενον (32) is the subject of a participle clause headed by node 28
    'tlg0060.tlg001.perseus-grc3.11.tb.xml@63': [
        ('reparent', 32, 28, 'nsubj'),
    ],

    # δημόσιον (5) is an oblique, not a subject (it's an adjective modifying an implied noun in obl position)
    'tlg0060.tlg001.perseus-grc3.11.tb.xml@292': [
        ('deprel', 5, 'obl'),
    ],

    # συντελεσθεῖσα (16) is an appositive participle modifying παρατάξεις (8); reparent as appos
    'tlg0060.tlg001.perseus-grc3.11.tb.xml@402': [
        ('reparent', 16, 8, 'appos'),
    ],

    # Κίμων (13) is the subject of the relative/embedded clause headed by node 28
    'tlg0060.tlg001.perseus-grc3.11.tb.xml@655': [
        ('reparent', 13, 28, 'nsubj'),
    ],

    # φθόγγος (12) is the outer/raised subject; εἰκάσαι (5) is the inf predicate
    'tlg0085.tlg001.perseus-grc2.tb.xml@2898040': [
        ('deprel', 12, 'nsubj:outer'),
    ],
}


def apply_fixes(doc, fixes):
    fixed = 0
    for bundle in doc.bundles:
        for tree in bundle.trees:
            sid = tree.sent_id
            if sid not in fixes:
                continue
            nodes = {n.ord: n for n in tree.descendants}
            for op in fixes[sid]:
                if op[0] == 'deprel':
                    _, nid, new_deprel = op
                    nodes[nid].deprel = new_deprel
                elif op[0] == 'reparent':
                    _, nid, new_head_id, new_deprel = op
                    nodes[nid].parent = nodes[new_head_id]
                    nodes[nid].deprel = new_deprel
            fixed += 1
    return fixed


if __name__ == '__main__':
    path = os.path.expanduser('grc_perseus-ud-train.conllu')
    doc = udapi.Document(path)
    n = apply_fixes(doc, FIXES)
    doc.store_conllu(path)
    print(f"Fixed {n} sentences in {path}")
