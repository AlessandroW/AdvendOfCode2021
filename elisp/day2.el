;;; day2.el --- AoC Day 2 -*- lexical-binding: t; -*-
;;
;; Copyright (C) 2021 Alessandro Wollek
;;
;; Author: Alessandro Wollek <https://github.com/wollek>
;; Maintainer: Alessandro Wollek <alessandro.wollek@tum.de>
;; Created: Dezember 03, 2021
;; Modified: Dezember 03, 2021
;; Version: 0.0.1
;; Keywords: abbrev bib c calendar comm convenience data docs emulations extensions faces files frames games hardware help hypermedia i18n internal languages lisp local maint mail matching mouse multimedia news outlines processes terminals tex tools unix vc wp
;; Homepage: https://github.com/wollek/day2
;; Package-Requires: ((emacs "24.3"))
;;
;; This file is not part of GNU Emacs.
;;
;;; Commentary:
;;
;;
;;
;;; Code:

(defun day2 ()
  "Solution for the second day of the advent of code 2021."
  (let ((horizontal 0) (depth 0) (aim 0) (input (s-split "\n" (f-read-text "~/repositories/AdventOfCode2021/day2.txt") 'omit-nulls)))
    (dolist (line input)
      (setq line (s-split " " line))
      (let ((command (car line)) (value (car (cdr line))))
        (setq value (string-to-number value))
        (cond ((string= command "forward") (progn (incf horizontal value)
                                                  (incf depth (* aim value))))
              ((string= command "down") (incf aim value))
              ((string= command "up") (decf aim value)))))
    (print (format "Part 1: %d" (* horizontal aim)))
    (print (format "Part 2: %d" (* horizontal depth)))
    (list (* horizontal aim) (* horizontal depth))))
(day2)
(provide 'day2)
;;; day2.el ends here
