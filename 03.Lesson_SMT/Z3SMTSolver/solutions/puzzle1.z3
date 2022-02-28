
(declare-const a Real)
(declare-const b Real)
(declare-const c Real)
(assert (= (+ a a) 10))
(assert (= (+ (* a b) b) 12))
(assert (= (- (* a b) (* c a)) a))
(check-sat)

; result a=5.0, b=2.0, c=1.0