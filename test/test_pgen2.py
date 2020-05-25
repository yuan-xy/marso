from textwrap import dedent

import pytest

from marso import load_grammar
from marso import ParserSyntaxError
from marso.pgen2 import generate_grammar
from marso.python import tokenize


def _parse(code, version=None):
    code = dedent(code) + "\n\n"
    grammar = load_grammar(version=version)
    return grammar.parse(code, error_recovery=False)


def _invalid_syntax(code, version=None, **kwargs):
    with pytest.raises(ParserSyntaxError):
        module = _parse(code, version=version, **kwargs)
        # For debugging
        print(module.children)


def test_formfeed(each_version):
    s = u"foo\n\x0c\nfoo\n"
    t = _parse(s, each_version)
    assert t.children[0].children[0].type == 'name'
    assert t.children[1].children[0].type == 'name'
    s = u"1\n\x0c\x0c\n2\n"
    t = _parse(s, each_version)

    with pytest.raises(ParserSyntaxError):
        s = u"\n\x0c2\n"
        _parse(s, each_version)


def test_matrix_multiplication_operator(works_ge_py35):
    works_ge_py35.parse("a @ b")
    works_ge_py35.parse("a @= b")


def test_yield_from(works_ge_py3, each_version):
    works_ge_py3.parse("yield from x")
    works_ge_py3.parse("(yield from x) + y")
    _invalid_syntax("yield from", each_version)


def test_left_recursion():
    with pytest.raises(ValueError, match='left recursion'):
        generate_grammar('foo: foo NAME\n', tokenize.PythonTokenTypes)


@pytest.mark.parametrize(
    'grammar, error_match', [
        ['foo: bar | baz\nbar: NAME\nbaz: NAME\n',
         r"foo is ambiguous.*given a TokenType\(NAME\).*bar or baz"],
        ['''foo: bar | baz\nbar: 'x'\nbaz: "x"\n''',
         r"foo is ambiguous.*given a ReservedString\(x\).*bar or baz"],
        ['''foo: bar | 'x'\nbar: 'x'\n''',
         r"foo is ambiguous.*given a ReservedString\(x\).*bar or foo"],
        # An ambiguity with the second (not the first) child of a production
        ['outer: "a" [inner] "b" "c"\ninner: "b" "c" [inner]\n',
         r"outer is ambiguous.*given a ReservedString\(b\).*inner or outer"],
        # An ambiguity hidden by a level of indirection (middle)
        ['outer: "a" [middle] "b" "c"\nmiddle: inner\ninner: "b" "c" [inner]\n',
         r"outer is ambiguous.*given a ReservedString\(b\).*middle or outer"],
    ]
)
def test_ambiguities(grammar, error_match):
    with pytest.raises(ValueError, match=error_match):
        generate_grammar(grammar, tokenize.PythonTokenTypes)
