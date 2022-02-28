(declare-const p Bool)
(declare-const q Bool)
(define-fun conjecture () Bool
	(=> (or p q) p))
(assert (not conjecture))
(check-sat)

; result sat so true for some cases and false for some cases