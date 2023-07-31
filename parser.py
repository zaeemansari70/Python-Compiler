from rply import ParserGenerator
from ast import *


class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NAME', 'NUMBER', 'SUM', 'SUB', 'EQUALS']
        )

    def parse(self):
        @self.pg.production('program : assign')
        def program(p):
            return Program(p[0])

        @self.pg.production('assign : name EQUALS expression')
        def assign(p):
            left = p[0]
            right = p[2]
            return Assign(left, right)

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.production('name : NAME')
        def name(p):
            return Name(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
