(define (triangle x1 y1 x2 y2 x3 y3 color)
  (place-image
   (line (- x2 x1) (- y2 y1) color)
   (/ (+ x1 x2) 2) (/ (+ y1 y2) 2)
   (place-image
    (line (- x3 x2) (- y3 y2) color)
    (/ (+ x2 x3) 2) (/ (+ y2 y3) 2)
    (place-image
     (line (- x1 x3) (- y1 y3) color)
     (/ (+ x3 x1) 2) (/ (+ y3 y1) 2)
     (empty-scene)))))

(show-image (triangle 180 180 450 330 180 600 "blue"))
