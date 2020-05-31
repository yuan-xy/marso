from marso import load_grammar


def test_load_grammar():
    grammar = load_grammar(language="demo")._pgen_grammar
    assert grammar.start_nonterminal == 'grammar'
    nonterminals = {'grammar', 'rule', 'rhs', 'items', 'item', 'atom'}
    assert nonterminals == {x for x in grammar.nonterminal_to_dfas.keys()}
    reserved = {':', '|', '[', '*', '+', ']', '(', ')'}
    assert reserved == {x for x in grammar.reserved_syntax_strings.keys()}

def test_parse_demo_language():
    code = "abc : def + 'ss'\n"
    grammar = load_grammar(language="demo")
    root = grammar.parse(code)
    assert root.start_pos == (1, 0)
    assert root.end_pos == (2, 0)
    assert root.parent is None
    assert root.type == "grammar"
    assert root.children.__len__() == 2
    assert root.children[0].type == "rule"
    assert root.children[1].type == "endmarker"

    rule = root.children[0]
    assert rule.parent == root
    assert rule.children.__len__() == 4
    assert rule.children[0].type == "name"
    assert rule.children[0].value == "abc"

    assert rule.children[1].type == "operator"
    assert rule.children[1].value == ":"
    assert rule.children[1].start_pos == (1, 4)
    assert rule.children[1].prefix == " "

    assert rule.children[2].type == "items"
    assert rule.children[3].type == "newline"
    assert rule.children[3].value == "\n"

    items = rule.children[2]
    assert items.parent == rule
    assert items.children.__len__() == 2
    assert items.children[0].type == "item"
    assert items.children[1].type == "string"
    assert items.children[1].value == "'ss'"

    item = items.children[0]
    assert item.children[0].type == "name"
    assert item.children[0].value == "def"
    assert item.children[1].type == "operator"
    assert item.children[1].value == "+"