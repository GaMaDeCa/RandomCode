;; Random coin flip(github.com/GaMaDeCa), shows "Head" if flipResult = 1, else "Tail"

; Tested using "Simple Scheme" by Bryan Chadwick
; Version 1.24
; Size 778.416 Bytes
; Hash SHA512 451fef7197bcfacdb6179f8d4268c1381530c4700fb676ccff132b1033c85ca4d3a40db04f2bcd32e29e0b47aa728971ee55a0e16c4169047bf2ea9f364b9363
; Download https://apkpure.com/br/simple-scheme/chadwick.apps.simplescheme

(define flipResult (random 2))

(show-image
	(place-image
		(if (= flipResult 1)
			(text "Head" 80 "solid" "#00FF00")
			(text "Tail" 80 "solid" "yellow")     
		)
		300 300
	(place-image
		(if (= flipResult 1)
			(circle 300 "solid" "#F00")
			(circle 300 "solid" "#00F")
		)
		300 300
	(empty-scene))
	)
)