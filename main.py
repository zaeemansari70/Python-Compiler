from lexer import Lexer
from parser import Parser
# from codegen import CodeGen

sample_input = """
x = 3 - 4
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(sample_input)
# codegen = CodeGen()

pg = Parser()
pg.parse()
parser = pg.get_parser()
print(parser.parse(tokens))

# codegen.create_ir()
# codegen.save_ir("output.ll")
