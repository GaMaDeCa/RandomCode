(define (random-polka dots rRadius minRadius maxRadius style width height)
           (if (= dots 0)
                (empty-scene width height)
           (place-image
                 (circle rRadius style (make-color (random 255) (random 255) (random 255)))
            (+ rRadius (random (- width (* rRadius 2)))) (+ rRadius (random (- height (* rRadius 2))))
           (random-polka (- dots 1)  (+ minRadius (random (- maxRadius minRadius))) minRadius maxRadius style width height))
))

;; SETTINGS
(define dots (+ 42 (random 99)))
(define minRadius 33)
(define maxRadius 99)
(define style (if (= (random 2) 0) "solid" "outline"))
(define width 900)
(define height 1200)

(show-image (random-polka dots (+ minRadius (random (- maxRadius minRadius))) minRadius maxRadius style width height))