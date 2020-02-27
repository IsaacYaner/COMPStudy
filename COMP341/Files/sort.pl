insert(Num, [], [Num]).

insert(Num, [A | B], [Num, A | B]) :-
    Num =< A.

insert(Num, [A | B], [A | C]) :- 
    Num > A,
    insert(Num, B, C).

isort([], []).

isort([Head | Tail], Result) :-
    isort(Tail, SortedTail),
    insert(Head, SortedTail, Result).

split([], [], []).

split([A], [A], []).

split([A | B], [A | SubB], SubA) :-
    split(B, SubA, SubB).

merge([], [], []).

merge(A, [], A).

merge([], B, B).

merge([A|B], [C|D], [A|Sub]) :-
    A =< C,
    merge(B, [C|D], Sub).

merge([A|B], [C|D], [C|Sub]) :-
    A > C,
    merge([A|B], D, Sub).