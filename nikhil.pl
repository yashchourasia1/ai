male(mohan).
male(ulhas).
male(mangesh).
male(harshad).
male(akshay).
male(nikhil).
female(vijaya).
female(prathiba).
female(sabina).
female(aruna).
female(jasmeeta).
female(kamashi).
parent(mohan,mangesh).
parent(mohan,harshad).
parent(vijaya,mangesh).
parent(vijaya,harshad).
parent(ulhas,sabina).
parent(ulhas,aruna).
parent(prathiba,sabina).
parent(prathiba,aruna).
parent(harshad,akshay).
parent(aruna,kamashi).
parent(mangesh,nikhil).
parent(mangesh,jasmeeta).
parent(sabina,nikhil).
parent(sabina,jasmeeta).
mother(X,Y):- parent(X,Y), female(X), X\==Y.
father(X,Y):- parent(X,Y), male(X), X\==Y.
sibling(X,Y):- father(Z,X), father(Z,Y), X\==Y.
brother(X,Y):- father(Z, X), father(Z,Y), male(X), X\==Y.
sister(X,Y):- father(Z, X), father(Z,Y), female(X), X\==Y.
uncle(X,Y):- parent(Z,Y), sibling(X,Z), male(X), X\==Y.
aunt(X,Y):- parent(Z,Y), sibling(X,Z), female(X), X\==Y.
grandfather(X,Y):- parent(X,Z), parent(Z,Y), male(X), X\==Y.
grandmother(X,Y):- parent(X,Z), parent(Z,Y), female(X), X\==Y.