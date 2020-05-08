% A grammar the covers most of the examples in COMP3411 lectures

:- dynamic(history/1).

sentence(VP) --> noun_phrase(Number, Actor), verb_phrase(Actor, Number, VP).

noun_phrase(plural, set(NP1, NP2)) --> np1(_, NP1), [and], noun_phrase(_, NP2).
noun_phrase(Number, NP1) --> np1(Number, NP1).

np1(Number, thing(Noun, Properties)) -->
	determiner(Number, _),
	adjp(Properties),
	noun(Number, Noun).
np1(Number, thing(Noun, [PP | Properties])) -->
	determiner(Number, _),
	adjp(Properties),
	noun(Number, Noun),
	pp(Number, PP).
np1(Number, thing(Name, [])) -->
	proper_noun(Number, _, Name).
np1(Number, personal(Pro)) -->
	pronoun(Number, _, Pro).
np1(Number1, possessive(Pos, thing(Noun, []))) -->
	possessive_pronoun(Number1, _, Pos), noun(_, Noun).
np1(Number, object(Noun)) -->
	num(Number), noun(Number, Noun).

adjp([prop(Adj)]) --> adjective(Adj).
adjp([]) --> [].

verb_phrase(Actor, Number, event(V, [actor(Actor) | Adv])) -->
	verb(Number, V),
	adverb(Adv).
verb_phrase(Actor, Number, event(V, [actor(Actor), object(NP) | Adv])) -->
	verb(Number, V),
	noun_phrase(_, NP),
	adverb(Adv).
verb_phrase(Actor, Number, event(V, [actor(Actor), object(NP), PP])) -->
	verb(Number, V),
	noun_phrase(_, NP),
	pp(Number, PP).
verb_phrase(Actor, Number, event(V, [actor(Actor), PP])) -->
	verb(Number, V),
	pp(_, PP).

pp(_, PP) --> prep(NP, PP), noun_phrase(_, NP).

% The next set of rules represent the lexicon

prep(NP, object(NP)) --> [of].
prep(NP, object(NP)) --> [to].
prep(NP, instrument(NP)) --> [with].
prep(NP, object(NP)) --> [in].
prep(NP, object(NP)) --> [for].

determiner(singular, det(a)) --> [a].
determiner(_, det(the)) --> [the].
determiner(plural, det(those)) --> [those].
determiner(_, _) --> [].

pronoun(singular, masculine, he) --> [he].
pronoun(singular, feminine, she) --> [she].
pronoun(_, neutral, what) --> [what].
pronoun(singular, neutral,Pro) --> [Pro], {member(Pro, [i, someone, it])}.
pronoun(plural, neutral, Pro) --> [Pro], {member(Pro, [they, some])}.

possessive_pronoun(singular, masculine, his) --> [his].
possessive_pronoun(singular, feminine, her) --> [her].

prep(of) --> [of].
prep(to) --> [to].
prep(with) --> [with].
prep(in) --> [in].
prep(for) --> [for].

num(singular) --> [one].
num(plural) --> [two];[three];[four];[five];[six];[seven];[eight];[nine];[ten].

noun(singular, Noun) --> [Noun], {thing(Noun, Props), member(number(singular), Props)}.
noun(plural, Noun) --> [Noun], {thing(Noun, Props), member(number(plural), Props)}.

proper_noun(singular, Gender, Name) -->
	[Name],
	{
		thing(Name, Props), member(isa(person), Props), member(gender(Gender), Props)
	}.
proper_noun(singular, neutral, france) --> [france].

adjective(adj(Adj)) --> [Adj], {member(Adj, [red,green,blue])}.

verb(_, Verb) --> [Verb], {member(Verb, [lost,found,did,gave,looked,saw,forgot,is])}.
verb(singular, Verb) --> [Verb], {member(Verb, [scares,hates])}.
verb(plural, Verb) --> [Verb], {member(Verb, [scare,hate])}.

adverb([adv(too)]) --> [too].
adverb([]) --> [].

% You may chose to use these items in the database to provide another way
% of capturing an objects properties.

thing(john, [isa(person), gender(masculine), number(singular)]).
thing(sam, [isa(person), gender(masculine), number(singular)]).
thing(bill, [isa(person), gender(masculine), number(singular)]).
thing(jack, [isa(person), gender(masculine), number(singular)]).
thing(monet, [isa(person), gender(masculine), number(singular)]).

thing(mary, [isa(person), gender(feminine), number(singular)]).
thing(annie, [isa(person), gender(feminine), number(singular)]).
thing(sue, [isa(person), gender(feminine), number(singular)]).
thing(jill, [isa(person), gender(feminine), number(singular)]).

thing(wallet, [isa(physical_object), gender(neutral), number(singular)]).
thing(car, [isa(physical_object), gender(neutral), number(singular)]).
thing(book, [isa(physical_object), gender(neutral), number(singular)]).
thing(telescope, [isa(physical_object), gender(neutral), number(singular)]).
thing(pen, [isa(physical_object), gender(neutral), number(singular)]).
thing(pencil, [isa(physical_object), gender(neutral), number(singular)]).
thing(cat, [isa(physical_object), gender(neutral), number(singular)]).
thing(mouse, [isa(physical_object), gender(neutral), number(singular)]).
thing(man, [isa(physical_object), gender(neutral), number(singular)]).
thing(bear, [isa(physical_object), gender(neutral), number(singular)]).

thing(cats, [isa(physical_object), gender(neutral), number(plural)]).
thing(mice, [isa(physical_object), gender(neutral), number(plural)]).
thing(men, [isa(physical_object), gender(neutral), number(plural)]).
thing(bears, [isa(physical_object), gender(neutral), number(plural)]).

thing(capital, [isa(abstract_object), gender(neutral), number(singular)]).

thing(france, [isa(place), gender(neutral), number(singular)]).

event(lost, [actor(_), object(_), tense(past)]).
event(found, [actor(_), object(_), tense(past)]).
event(saw, [actor(_), object(_), tense(past)]).
event(forgot, [actor(_), object(_), tense(past)]).
event(scares, [actor(_), object(_), tense(present), number(singular)]).
event(scare, [actor(_), object(_), tense(present), number(plural)]).
event(hates, [actor(_), object(_), tense(present), number(singular)]).
event(hate, [actor(_), object(_), tense(present), number(plural)]).
event(gave, [actor(Person1), recipient(Person2), object(_), tense(past)]) :- Person1 \= Person2.

personal(he, [number(singular), gender(masculine)]).
personal(she, [number(singular), gender(feminine)]).
personal(it, [number(singular), gender(neutral)]).
personal(they, [ number(plural), gender(neutral)]).

possessive(his, [number(singular), gender(masculine)]).
possessive(her, [number(singular), gender(feminine)]).

% You have to write this:
% process(LogicalForm, Ref1, Ref2).

process([], Ref1, Ref1).

% Use actor and object instead of thing because of least knowledge theory
process(actor(thing(Name, _)), Ref1, Ref1):-
	thing(Name, Props),
	assert(history(thing(Name, Props))).

process(object(possessive(_, thing(Name, _))), Ref1, Ref1):-
	thing(Name, Props),
	assert(history(thing(Name, Props))).

process(object(thing(Name,_)), Ref1, Ref1):-
	thing(Name, Props),
	assert(history(thing(Name, Props))).


% John, a pairs.
process(event(Action, [actor(thing(Actor, _)), object(thing(Thing, _))]), Ref1, Ref3):-	
% call process for child
	process(actor(thing(Actor, _)), Ref1, Ref2),
	process(object(thing(Thing, _)), Ref2, Ref3),

% Add to history
	assert(history(event(Action, [actor(thing(Actor, _)), object(thing(Thing, _))]))).


% He, it pairs.
process(event(Action, [actor(personal(Actor)), object(personal(Pronoun))]), Ref1, [Name1, Name2|Ref1]):-
% If there exist a legal Pronoun or determiner
	personal(Actor, Props1),
	member(gender(Gender1), Props1),
	member(number(Number1), Props1),
	
	personal(Pronoun, Props3),
	member(gender(Gender2), Props3),
	member(number(Number2), Props3),

% And there is already a matching Actor
	history(thing(Name1, Props2)),
	member(gender(Gender1), Props2),
	member(number(Number1), Props2),

	history(thing(Name2, Props4)),
	member(gender(Gender2), Props4),
	member(number(Number2), Props4),

% Add to history
	assert(history(event(Action, [actor(personal(Actor)), object(personal(Pronoun))]))).


% He, his pairs.
process(event(Action, [actor(personal(Actor)), object(possessive(Pronoun, Thing))]), Ref1, [Name1, Name2|Ref2]):-
% call process for child
	process(object(possessive(Pronoun, Thing)), Ref1, Ref2),

% If there exist a legal Pronoun or determiner
	personal(Actor, Props1),
	member(gender(Gender), Props1),
	member(number(Number), Props1),

	possessive(Pronoun, Props3),
	member(gender(Gender2), Props3),
	member(number(Number2), Props3),

% And there is already a matching Actor
	history(thing(Name1, Props2)),
	member(gender(Gender), Props2),
	member(number(Number), Props2),

	history(thing(Name2, Props4)),
	member(gender(Gender2), Props4),
	member(number(Number2), Props4),

% Add to history
	assert(history(event(Action, [actor(personal(Actor)), object(possessive(Pronoun, Thing))]))).


% John, it pairs.
process(event(Action, [actor(thing(Actor, _)), object(personal(Pronoun))]), Ref1, [Name|Ref2]):-
% call process for child
	process(actor(thing(Actor, _)), Ref1, Ref2),

% If there exist a legal Pronoun or determiner
	personal(Pronoun, Props1),
	member(gender(Gender), Props1),
	member(number(Number), Props1),

% And there is already a matching Actor
	history(thing(Name, Props2)),
	member(gender(Gender), Props2),
	member(number(Number), Props2),

% Add to history
	assert(history(event(Action, [actor(thing(Actor, _)), object(personal(Pronoun))]))).


% John, his pairs.
process(event(Action, [actor(thing(Actor, _)), object(possessive(Pronoun, Thing))]), Ref1, [Name|Ref3]):-	
% call process for child
	process(actor(thing(Actor, _)), Ref1, Ref2),
	process(object(possessive(Pronoun, Thing)), Ref2, Ref3),

% If there exist a legal Pronoun or determiner
	possessive(Pronoun, Props1),
	member(gender(Gender), Props1),
	member(number(Number), Props1),

% And there is already a matching Actor
	history(thing(Name, Props2)),
	member(gender(Gender), Props2),
	member(number(Number), Props2),

% Add to history
	assert(history(event(Action, [actor(thing(Actor, _)), object(possessive(Pronoun, Thing))]))).

run(S, Refs) :-
	sentence(X, S, []), !,
	writeln(X),
	process(X, [], Refs),
	listing(history/1).