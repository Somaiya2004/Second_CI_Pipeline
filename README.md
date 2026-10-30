# Second CI/CD Pipeline (Programs 31–40)

This repository contains Python programming assignments (Programs 31 through 40) developed under a strict **branch-per-program workflow** and validated via an automated **GitHub Actions CI/CD pipeline**.

---

## 🚀 Repository Structure

\\\	ext
Second_CI_Pipeline/
|-- __init__.py
|-- requirements.txt
|-- .github/
|   \-- workflows/
|       \-- ci.yml
|-- 31_pangram.py & test_31_pangram.py
|-- 32_count_words.py & test_32_count_words.py
|-- 33_first_non_repeating.py & test_33_first_non_repeating.py
|-- 34_check_sorted.py & test_34_check_sorted.py
|-- 35_move_zeros.py & test_35_move_zeros.py
|-- 36_most_frequent.py & test_36_most_frequent.py
|-- 37_rotate_string.py & test_37_rotate_string.py
|-- 38_missing_number_xor.py & test_38_missing_number_xor.py
|-- 39_transpose_matrix.py & test_39_transpose_matrix.py
\-- 40_gcd.py & test_40_gcd.py
\\\

---

## 📋 Program List & Branch Mapping

| No. | Program Title | Program File | Test File | Branch Name |
| :--- | :--- | :--- | :--- | :--- |
| **31** | Check Pangram String | \31_pangram.py\ | \	est_31_pangram.py\ | \31-pangram\ |
| **32** | Count Words in a Sentence | \32_count_words.py\ | \	est_32_count_words.py\ | \32-count-words\ |
| **33** | First Non-Repeating Character | \33_first_non_repeating.py\ | \	est_33_first_non_repeating.py\ | \33-first-non-repeating\ |
| **34** | Check Whether a List Is Sorted | \34_check_sorted.py\ | \	est_34_check_sorted.py\ | \34-check-sorted\ |
| **35** | Move All Zeros to the End | \35_move_zeros.py\ | \	est_35_move_zeros.py\ | \35-move-zeros\ |
| **36** | Most Frequent Element | \36_most_frequent.py\ | \	est_36_most_frequent.py\ | \36-most-frequent\ |
| **37** | Rotate a String by K Positions | \37_rotate_string.py\ | \	est_37_rotate_string.py\ | \37-rotate-string\ |
| **38** | Missing Number Using XOR | \38_missing_number_xor.py\ | \	est_38_missing_number_xor.py\ | \38-missing-number-xor\ |
| **39** | Transpose a Matrix | \39_transpose_matrix.py\ | \	est_39_transpose_matrix.py\ | \39-transpose-matrix\ |
| **40** | Greatest Common Divisor (GCD) | \40_gcd.py\ | \	est_40_gcd.py\ | \40-gcd\ |

---

## 🛠️ Workflow Guidelines

1. **Feature Branches**: Every program has its own isolated feature branch following the naming convention above.
2. **Dynamic Imports**: Because script filenames start with digits, test files use Python's importlib module to import program functions safely.
3. **Automated CI**: Pull Requests targeting main automatically run syntax checking via compileall and execute test suites using pytest.
