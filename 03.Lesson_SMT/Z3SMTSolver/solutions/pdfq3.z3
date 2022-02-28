(declare-const p Bool)
(declare-const q Bool)
(define-fun conjecture () Bool
	(and (and p (or q (not p))) (not q)))
(assert (not conjecture))
(check-sat)

; result sat so true for some cases and false for some cases