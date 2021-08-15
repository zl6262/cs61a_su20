(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond 
      ((< num 0) -1)
      ((= num 0) 0)
      ((> num 0) 1)
  )
)


(define (square x) (* x x))

(define (pow x y)
  (cond
    ((zero? y) 1)
    ((even? y) (square (pow x (/ y 2))))
    ((odd? y) (* x (pow x (- y 1))))
  )
)


(define (unique s)
  (cond
      ((null? s) ())
      ((null? (filter (lambda (x) (eq? x (car s))) (cdr s)))
          (cons (car s) (unique (cdr s))))
      (else (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s)))))
  )
)


(define (replicate x n)
    (define (helper n result)
      (if (= n 0)
          result
          (helper (- n 1) (cons x result))
      )
    )
    (helper n nil)
  )


(define (accumulate combiner start n term)
  (define (helper i result)
    (if (= i n)
        (combiner result (term n))
    (helper (+ i 1) (combiner result (term i)))
  )
  )
  (helper 1 start)
)


(define (accumulate-tail combiner start n term)
   (define (helper i result)
    (if (= i n)
        (combiner result (term n))
    (helper (+ i 1) (combiner result (term i)))
  )
  )
  (helper 1 start)
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)

