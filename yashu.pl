male(ramesh).
male(ashok).
male(rupesh).
male(ankesh).
male(arjun).
male(yash).
female(shanti).
female(malti).
female(dimple).
female(neha).
female(shranya).
female(shree).
parent(ramesh,rupesh).
parent(ramesh,ankesh).
parent(shanti,rupesh).
parent(shanti,ankesh).
parent(ashok,dimple).
parent(ashok,neha).
parent(malti,dimple).
parent(malti,neha).
parent(ankesh,arjun).
parent(neha,shree).
parent(rupesh,yash).
parent(rupesh,shranya).
parent(dimple,yash).
parent(dimple,shranya).
mother(X,Y):- parent(X,Y), female(X), X\==Y.
father(X,Y):- parent(X,Y), male(X), X\==Y.
sibling(X,Y):- father(Z,X), father(Z,Y), X\==Y.
brother(X,Y):- father(Z, X), father(Z,Y), male(X), X\==Y.
sister(X,Y):- father(Z, X), father(Z,Y), female(X), X\==Y.
uncle(X,Y):- parent(Z,Y), sibling(X,Z), male(X), X\==Y.
aunt(X,Y):- parent(Z,Y), sibling(X,Z), female(X), X\==Y.
grandfather(X,Y):- parent(X,Z), parent(Z,Y), male(X), X\==Y.
grandmother(X,Y):- parent(X,Z), parent(Z,Y), female(X), X\==Y.