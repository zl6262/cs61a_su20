(define (rle s)
    (define (helper num, count s) 
        (if (= num (car s))
            (helper num, (+ count 1) (cdr s))
            (
                (cons-stream (list num count) (helper (car s) 1 (cdr s)))
            )
        )
    )
)



(define (group-by-nondecreasing s)
    'YOUR-CODE-HERE)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

