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
            raise ParseError(self.pos + 1, 'Expected end of string but got %s', self.tokens[self.pos + 1])

    def keyword(self, *keywords):
        if self.pos >= self.len:
            raise ParseError(
                self.pos + 1,
                'Expected %s but got end of string',
                ','.join(keywords)
            )

        for keyword in keywords:
            if regex.match(keyword, self.tokens[self.pos+1]) is not None:
                return self.next(False)

        raise ParseError(self.pos + 1, 'Expected %s but got %s', ','.join(keywords), self.tokens[self.pos + 1],)

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
    def __init__(self, terms, operations, value=None):
        self.terms = terms
        self.term_names = list(self.terms.keys())
        # TODO use eval as basic expression
        self.operations = operations
        if value is not None:
            self.value = value
        else:
            self.value = lambda a : a

    def next_term(self, term):
        return self.term_names[self.term_names.index(term)+1]
    def next(self, to_value=True):
        self.pos += 1
        if to_value:
            return self.value(self.tokens[self.pos])
        return self.tokens[self.pos]
    # TODO add arguments
    def dive(self, term):
        if len(self.terms[term]) > 0 and callable(self.terms[term][0]):
            return self.terms[term][0]()
        try:
            return getattr(self, term)()
        except:
            return self.default(term)

    def start(self):
        self.default = self.perform
        return self.default(self.term_names[0])
    
    # TODO add more parenthesis for factors
    def factor(self):
        if self.maybe_keyword(r'\('):
            rv = self.match(self.term_names[0])
            self.keyword(r'\)')
            return rv
        return self.match(self.term_names[-1])
    def word(self):
        return self.next()


    def match(self, *rules):
        for rule in rules:
            rv = self.dive(rule)
            return rv        
    def perform(self, term):
        next_level = self.next_term(term)
        operator = self.terms[term]
        rv = self.match(next_level)
        while True:
            op = self.maybe_keyword(*operator)
            if op is None:
                break
            term = self.match(next_level)
            rv = self.operate(rv, term, op)
        return rv

    def operate(self, dest, src, op):
        for i in self.term_names:
            for ops in self.terms[i]:
                if regex.match(ops, op):
                    return self.operations[i](dest, src, op)

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
