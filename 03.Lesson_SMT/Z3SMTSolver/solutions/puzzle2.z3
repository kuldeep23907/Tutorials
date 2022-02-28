(declare-const p Bool)
(declare-const q Bool)
(define-fun conjecture () Bool
	(= (= (and p q) p)
		(=> p q)))
(assert (not conjecture))
(check-sat)


; result unsat