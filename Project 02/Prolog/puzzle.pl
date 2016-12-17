exists(H, list(H, _, _, _, _)).
exists(H, list(_, H, _, _, _)).
exists(H, list(_, _, H, _, _)).
exists(H, list(_, _, _, H, _)).
exists(H, list(_, _, _, _, H)).

left(R, L, list(L, R, _, _, _)).
left(R, L, list(_, L, R, _, _)).
left(R, L, list(_, _, L, R, _)).
left(R, L, list(_, _, _, L, R)).

centre(H, list(_, _, H, _, _)).
first(H, list(H, _, _, _, _)).

neighbor(H1, H2, list(H1, H2, _, _, _)).
neighbor(H1, H2, list(_, H1, H2, _, _)).
neighbor(H1, H2, list(_, _, H1, H2, _)).
neighbor(H1, H2, list(_, _, _, H1, H2)).
neighbor(H1, H2, list(H2, H1, _, _, _)).
neighbor(H1, H2, list(_, H2, H1, _, _)).
neighbor(H1, H2, list(_, _, H2, H1, _)).
neighbor(H1, H2, list(_, _, _, H2, H1)).

puzzle(Houses) :-
    exists(house(red, english, _, _, _), Houses),
    exists(house(_, swede, _, _, dog), Houses),
    exists(house(_, dane, tea, _, _), Houses),
    left(house(white, _, _, _, _),house(green, _, coffee, _, _), Houses),
    exists(house(_,_,_,pallsmoker,birds),Houses),
    centre(house(_, _, milk, _, _), Houses),
    first(house(_, norwegian, _, _, _), Houses),
    neighbor(house(_, _, _, blendsmoker, _), house(_, _, _, _, cats), Houses),
    exists(house(_, _, bier, bluemaster, _), Houses),
    neighbor(house(yellow, _, _, dunhill, _),house(_, _, _, _, horse), Houses),
    exists(house(_, german, _, prince, _), Houses),
    neighbor(house(_, norwegian, _, _, _), house(blue, _, _, _, _), Houses),
    neighbor(house(_, _, _, blendsmoker, _), house(_, _, water, _, _), Houses),
	exists(house(_, _, _, _, fish), Houses).