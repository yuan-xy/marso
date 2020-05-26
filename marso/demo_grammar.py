from marso.grammar import Grammar
from marso.python.errors import ErrorFinderConfig
from marso.python.parser import Parser as PythonParser
from tokenize import tokenize, generate_tokens
import token

class DemoGrammar(Grammar):
    _error_normalizer_config = ErrorFinderConfig()
    _token_namespace = token
    _start_nonterminal = 'grammar'

    def __init__(self, bnf_text):
        super(DemoGrammar, self).__init__(
            bnf_text,
            tokenizer=generate_tokens,
            parser=PythonParser,
            # diff_parser=DiffParser
        )


    def _tokenize(self, code):
        # Used by Jedi.
        return tokenize(code)
