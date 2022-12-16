% test file for adventure in prolog

mortal(X) :- person(X).

person(socrates).
person(plato).
person(zeno).
person(bob).
person(aristotle).

mortal_report :-
	write('Known mortals are:'),nl,
	mortal(X),
	write(X),nl.
