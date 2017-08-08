/* [+,-] */
insertionsort(LIST, SORTED) :- insertsort(LIST, [], SORTED).

/* [+,+,-] */
insertsort([], ACCUMULATOR, ACCUMULATOR).
insertsort([HEAD | TAIL], ACCUMULATOR, SORTED) :- insert(HEAD, ACCUMULATOR, NEWACCUMULATOR),
                                                  insertsort(TAIL, NEWACCUMULATOR, SORTED).

/* [+,+,-] */
insert(ELEM, [HEAD | TAIL], [HEAD | NEWTAIL]) :- ELEM @> HEAD, insert(ELEM, TAIL, NEWTAIL).
insert(ELEM, [HEAD | TAIL], [ELEM, HEAD | TAIL]) :- ELEM @=< HEAD.
insert(ELEM, [] , [ELEM]).



 insertionsort([2,3,1,4],L).
L = [1, 2, 3, 4] .
