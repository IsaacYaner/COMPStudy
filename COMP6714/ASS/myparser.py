import regex
class ParseError(Exception):
    def __init__(self, pos, msg, *args):
        self.pos = pos
        self.msg = msg
        self.args = args

    def __str__(self):
        return '%s at position %s' % (self.msg % self.args, self.pos)

class TokenParser:
    def __init__(self):
        self.cache = {}

    def parse(self, token):
        self.tokens = token
        self.pos = -1
        self.len = len(token) - 1
        rv = self.start()
        self.assert_end()
        return rv

    def assert_end(self):
        if self.pos < self.len:
            raise ParseError(
                self.pos + 1,
                'Expected end of string but got %s',
                self.tokens[self.pos + 1]
            )

    def keyword(self, *keywords):
        if self.pos >= self.len:
            raise ParseError(
                self.pos + 1,
                'Expected %s but got end of string',
                ','.join(keywords)
            )

        for keyword in keywords:
            if regex.match(keyword, self.tokens[self.pos+1]) is not None:
                return self.next()

        raise ParseError(
            self.pos + 1,
            'Expected %s but got %s',
            ','.join(keywords),
            self.tokens[self.pos + 1],
        )

    def match(self, *rules):
        last_error_pos = -1
        last_exception = None
        last_error_rules = []

        for rule in rules:
            initial_pos = self.pos
            try:
                rv = self.terms[rule]()
                return rv
            except ParseError as e:
                self.pos = initial_pos

                if e.pos > last_error_pos:
                    last_exception = e
                    last_error_pos = e.pos
                    last_error_rules.clear()
                    last_error_rules.append(rule)
                elif e.pos == last_error_pos:
                    last_error_rules.append(rule)

        if len(last_error_rules) == 1:
            raise last_exception
        else:
            raise ParseError(last_error_pos, 'Expected %s but got %s', ','.join(last_error_rules), self.text[last_error_pos])

    def maybe_keyword(self, *keywords):
        try:
            return self.keyword(*keywords)
        except ParseError:
            return None

class SimpleBooleanParser(TokenParser):
    def dive(self, term):
        if len(self.terms[term]) == 1:
            return self.terms[term][0]()
        return self.default(self.terms[term][1], *self.terms[term][2:])

    def next_term(self, term):
        return self.term_names[self.term_names.index(term)+1]

    def start(self):
        self.default = self.perform
        # token_list = ['&', ['/s', '/d'], r'\+s', r'/[0-9]+', r'\+[0-9]+', r'\|']
        self.terms = {
            'expression':       ['&'],
            'in_sentence':      ['/s', '/d'],
            'after_sentence':   [r'\+s'],
            'in_n':             [r'/[0-9]+'],
            'after_n':          [r'\+[0-9]+'],
            'term':             [r'\|'],
            'factor':           [self.factor],
            'word':             [self.next],
            }
        self.term_names = ['expression','in_sentence','after_sentence','in_n','after_n','term','factor','word']
        return self.default(self.terms['expression'][1], *self.terms['expression'][2:])
    
    # Write each operator below
    # () > | > +n > /n > +s > /s > &
    def factor(self):
        if self.maybe_keyword(r'\('):
            rv = self.match('expression')
            self.keyword(r'\)')
            return rv
        return self.match('word')
    def word(self):
        return self.next()
    def next(self):
        self.pos += 1
        return self.tokens[self.pos]

    def match(self, *rules):
        for rule in rules:
            rv = self.dive(rule)
            return rv        

    def perform(self, next_level, *operator):
        # print("Perform: ", next_level, operator, self.tokens[self.pos+1])
        rv = self.match(next_level)
        while True:
            op = self.maybe_keyword(*operator)
            if op is None:
                break
            term = self.match(next_level)
            rv = self.operate(rv, term, op)
        return rv


    def operate(self, dest, src, op):
        result = '(' + dest + op + '' + src + ')'
        if op == '|':
            dest = result
        if regex.match(r'\+[0-9]+', op):
            dest = result
        if regex.match(r'/[0-9]+', op):
            dest = result
        if regex.match(r'\+s', op):
            dest = result
        if regex.match(r'/s', op):
            dest = result
        if regex.match(r'/d', op):
            dest = result
        if regex.match(r'&', op):
            dest = result
        return dest

from sys import stdin
if __name__ == '__main__':
    parser = SimpleBooleanParser()
    for line in stdin:
        # Get rid of end of line
        query = line[:-1]           
        # Decouple "" into (+1)
        subset = [x.group() for x in regex.finditer(r'"(\w+ )*(\w+ ?)?"', query)]
        post = [regex.sub(r'(?<=\w+) +(?=\w+)', '+1', x) for x in subset]
        for i in range(len(subset)):
            query = regex.sub(subset[i], "("+post[i][1:-1]+")", query, count=1)
        query = regex.sub(r'([()])', r" \1 ", query)
        query = regex.sub(r'(?<=(\n| |^)[^+/]\w+) +(?=\w+)', ' | ', query)
        query = query.split()
        print(query)
        print(parser.parse(query))
