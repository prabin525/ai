mother(kaushalya,ram).
mother(kaikai,bharat).
mother(sumitra,laxman).
mother(sumitra,satrughan).
husband(dasarath,kaushalya).
husband(dasarath,kaikai).
husband(dasarath,sumitra).
son(A,C):-
    mother(C,A).
son(A,C):-
    husband(C,B),mother(B,A).
father(A,B):-
    husband(A,C),mother(C,B).
% GOAL son(X,kaikai).
% son( “Ram”,X).
% father(X,”Ram”).
% gplc filename.pl