bigger(X,Y,Z):-
    X>Y,Z=X.
bigger(X,Y,Z):-
    X<Y,Z=Y.
bigger(X,Y,Z):-
    X=Y,Z=Y.
