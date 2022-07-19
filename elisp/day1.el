;;; day1.el --- Day 1 of the Advent of Code 2021 -*- lexical-binding: t; -*-
;;
;; Copyright (C) 2021 Alessandro Wollek
;;
;; Author: Alessandro Wollek <https://github.com/wollek>
;; Maintainer: Alessandro Wollek <alessandro.wollek@tum.de>
;; Created: Dezember 02, 2021
;; Modified: Dezember 02, 2021
;; Version: 0.0.1
;; Keywords: abbrev bib c calendar comm convenience data docs emulations extensions faces files frames games hardware help hypermedia i18n internal languages lisp local maint mail matching mouse multimedia news outlines processes terminals tex tools unix vc wp
;; Homepage: https://github.com/AlessandroW/AdventOfCode2021
;; Package-Requires: ((emacs "24.3"))
;;
;; This file is not part of GNU Emacs.
;;
;;; Commentary:
;;
;;  Description
;;
;;; Code:
(defun day1-part1()
  "Count the number of increasing values."
  (let ((result 0)
        (index 0)
        (input (-map #'string-to-number (s-split "\n" (f-read-text "~/repositories/AdventOfCode2021/day1.txt") 'omit-nulls))))
    (while (< index (length input))
      (if (and (> index 0) (> (nth index input)
                              (nth (1- index) input)))
          (setq result (1+ result)))
      (setq index (1+ index)))
    result))

(defun day1-part2()
  "Count the number of increasing 3-windows."
  (let ((result 0)
        (index 0)
        (input (-map #'string-to-number (s-split "\n" (f-read-text "~/repositories/AdventOfCode2021/day1.txt") 'omit-nulls))))
    (while (< index (length input))
      (if (and (> index 2) (> (nth index input)
                              (nth (- index 3) input)))
          (setq result (1+ result)))
      (setq index (1+ index)))
    result))

(print "Part 1")
(print (day1-part1))
(print "Part 2")
(print (day1-part2))

(provide 'day1)
;;; day1.el ends here
