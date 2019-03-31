% Write the following statements in FOPL form and by converting them into prolog program test
% the given goal.
% 1. Every American who sells weapons to hostile nations is a criminal.
% 2. Every enemy of America is a hostile.
% 3. Iraque has some missiles.
% 4. All missiles of Iraque were sold by George.
% 5. George is an American.
% 6. Iraque is a country.
% 7. Iraque is the enemy of America.
% 8. Missiles are weapens.
criminal(X):-
    american(X),sells_missiles(X,Y),hostile(Y).
enemy_of_america(X) :-
    hostile(X).
enemy_of_america(iraq).
hostile(X):-
    country(X).
has_missile(iraq).
sells_missiles(george,iraq).
american(george).
country(iraq).

% Goal criminal(george).