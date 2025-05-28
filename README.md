# Python Practice Playground ✨

Welcome! This repository is my personal collection of Python code, focusing on algorithms, data structures, Object-Oriented Programming (OOP), Low-Level Design (LLD), and solutions to various coding challenges (primarily LeetCode). It serves as a space for learning, practice, and demonstrating problem-solving approaches.

**Navigation:** Use the Table of Contents below or expand the collapsible sections to explore different categories.

## Table of Contents

*   [Low-Level Design (LLD)](#low-level-design-lld-)
*   [Maths](#maths-)
*   [Patterns](#patterns-)
*   [Sorting](#sorting-)
*   [Array](#array-)
*   [Binary Search](#binary-search-)
*   [Graph](#graph-)
*   [Hashing](#hashing-)
*   [Set](#set-)
*   [String](#string-)
*   [Tree](#tree-)
*   [Other Concepts](#other-concepts-)
*   [How to Use](#how-to-use)
*   [Contributing](#contributing)

---

## Project Index

Click the **`<summary>`** tags to expand/collapse the detailed file lists for each category.

<details>
<summary><strong>Low-Level Design (LLD) 🎨</strong> (6 items)</summary>

| Program Name                                  | Location                                                                      | Status | Notes                               |
| :-------------------------------------------- | :---------------------------------------------------------------------------- | :----- | :---------------------------------- |
| Design Stack Overflow (Conceptual)            | [LLD/Design Stackoverflow/](LLD/Design%20Stackoverflow/)                       | Done   | Basic structure files             |
| Basic Class Example                           | [LLD/Oops/class.py](LLD/Oops/class.py)                                        | Done   |                                     |
| Payment Interface Example (Interface/ABC)     | [LLD/Oops/interface_and_abc/payments_example/](LLD/Oops/interface_and_abc/payments_example/) | Done   | Demonstrates interface concept    |
| Vehicle Interface Example (Interface/ABC)     | [LLD/Oops/interface_and_abc/vehicles_example/](LLD/Oops/interface_and_abc/vehicles_example/) | Done   | Demonstrates interface concept    |
| Tic Tac Toe (Requirement Gathering Conceptual)| [LLD/Tic Tac Toe/Requirement Gathering](LLD/Tic%20Tac%20Toe/Requirement%20Gathering) | Done   | Text description                    |
| Tic Tac Toe Implementation                    | [LLD/Tic Tac Toe/tic_tac_toe.py](LLD/Tic%20Tac%20Toe/tic_tac_toe.py)             | Done   |                                     |

</details>

<details>
<summary><strong>Maths 📐</strong> (47 items)</summary>

| Program Name                                                       | Location                                                                                         | Status | Notes (LeetCode #)                 |
| :----------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- | :----- | :--------------------------------- |
| Is Palindrome (Integer Overflow Avoidance)                         | [is_a_no_palindrome_bruteforce_to_avoid_integer_overflow.py](Maths/IsPalindrome/is_a_no_palindrome_bruteforce_to_avoid_integer_overflow.py)                  | Done   | [9](https://leetcode.com/problems/palindrome-number/) - Variation |
| Is Palindrome (Compare MSB/LSB)                                    | [is_a_no_palindrome_by_comparing_lsb_and_msb_and_chopping_them_both.py](Maths/IsPalindrome/is_a_no_palindrome_by_comparing_lsb_and_msb_and_chopping_them_both.py)         | Done   | [9](https://leetcode.com/problems/palindrome-number/) - Variation |
| Is Palindrome (Optimized Integer)                                  | [is_a_no_palindrome_optimized.py](Maths/IsPalindrome/is_a_no_palindrome_optimized.py)                                             | Done   | [9](https://leetcode.com/problems/palindrome-number/)             |
| Is Palindrome (Integer Overflow Prone)                             | [is_a_no_palindrome_prone_to_integer_overflow.py](Maths/IsPalindrome/is_a_no_palindrome_prone_to_integer_overflow.py)                             | Done   | [9](https://leetcode.com/problems/palindrome-number/) - Variation |
| Is Palindrome (String Reverse)                                     | [is_a_no_palindrome_using_string_and_reversing_complete_string.py](Maths/IsPalindrome/is_a_no_palindrome_using_string_and_reversing_complete_string.py)            | Done   | [9](https://leetcode.com/problems/palindrome-number/) - Variation |
| Is Palindrome (String Two Pointer)                                 | [is_a_no_palindrome_using_string_and_using_two_pointer.py](Maths/IsPalindrome/is_a_no_palindrome_using_string_and_using_two_pointer.py)                    | Done   | [9](https://leetcode.com/problems/palindrome-number/) - Variation |
| Arithmetic Subarrays (Bruteforce)                                  | [arithmetic_subarrays_1630_bruteforce.py](Maths/arithmetic_subarrays_1630_bruteforce.py)                                                  | Done   | [1630](https://leetcode.com/problems/arithmetic-subarrays/)        |
| Arithmetic Subarrays (Optimized)                                   | [arithmetic_subarrays_1630_optimized_without_sorting.py](Maths/arithmetic_subarrays_1630_optimized_without_sorting.py)                                   | Done   | [1630](https://leetcode.com/problems/arithmetic-subarrays/)        |
| Avg Values of Even Nos Divisible by Three                          | [avg_values_of_even_nos_that_are_divisible_by_three_2455.py](Maths/avg_values_of_even_nos_that_are_divisible_by_three_2455.py)                               | Done   | [2455](https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/) |
| Base 7                                                             | [base_7_504.py](Maths/base_7_504.py)                                                                            | Done   | [504](https://leetcode.com/problems/base-7/)                       |
| Check If No is Sum of Power of Three                               | [check_if_no_is_sum_of_power_of_three_1780.py](Maths/check_if_no_is_sum_of_power_of_three_1780.py)                                             | Done   | [1780](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/) |
| Check If the No is Fascinating                                     | [check_if_the_no_is_fascinating_2729.py](Maths/check_if_the_no_is_fascinating_2729.py)                                                   | Done   | [2729](https://leetcode.com/problems/check-if-the-number-is-fascinating/) |
| Closest Prime Numbers in Range (TLE Likely)                        | [closest_prime_no_in_ranges_2523.py](Maths/closest_prime_no_in_ranges_2523.py)                                                       | Done   | [2523](https://leetcode.com/problems/closest-prime-numbers-in-range/) |
| Closest Prime Numbers in Range (Optimized Sieve)                   | [closest_prime_no_in_ranges_2523_n*sqrt(n).py](Maths/closest_prime_no_in_ranges_2523_n*sqrt%28n%29.py)                                       | Done   | [2523](https://leetcode.com/problems/closest-prime-numbers-in-range/) |
| Color of Chessboard Square                                         | [color_of_chessboard_1812.py](Maths/color_of_chessboard_1812.py)                                                              | Done   | [1812](https://leetcode.com/problems/determine-color-of-a-chessboard-square/) |
| Complex Number Multiplication                                      | [complex_no_multiplication_537.py](Maths/complex_no_multiplication_537.py)                                                         | Done   | [537](https://leetcode.com/problems/complex-number-multiplication/) |
| Count Digits                                                       | [count_no_of_digits.py](Maths/count_no_of_digits.py)                                                                    | Done   |                                    |
| Count Digits (Optimized Log)                                       | [count_no_of_digits_optimized.py](Maths/count_no_of_digits_optimized.py)                                                          | Done   |                                    |
| Count Primes (Bruteforce)                                          | [count_primes_204_bruteforce_n_*_sqrt(n).py](Maths/count_primes_204_bruteforce_n_%2A_sqrt%28n%29.py)                                               | Done   | [204](https://leetcode.com/problems/count-primes/)               |
| Count Primes (Sieve of Eratosthenes)                               | [count_primes_204_sieve_of_eratosthenes..py](Maths/count_primes_204_sieve_of_eratosthenes..py)                                               | Done   | [204](https://leetcode.com/problems/count-primes/)               |
| Count Symmetrical Integers                                         | [count_symmetrical_integers_2843.py](Maths/angle_between_hands_of_a_clock_1344.py)                                                       | Done   | [2843](https://leetcode.com/problems/count-symmetric-integers/) |
| Difference Between Element Sum and Digit Sum                       | [difference_betwen_element_sum_and_digit_sum_2535.py](Maths/difference_betwen_element_sum_and_digit_sum_2535.py)                                      | Done   | [2535](https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/) |
| Fibonacci Number                                                   | [fibonacii_number_509.py](Maths/fibonacii_number_509.py)                                                                  | Done   | [509](https://leetcode.com/problems/fibonacci-number/)           |
| Find GCD of Array                                                  | [find_gcd_of_array_1979.py](Maths/find_gcd_of_array_1979.py)                                                                | Done   | [1979](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) |
| Find if Digits Can be Won (Typo?)                                  | [find_if_digits_can_be_won_3232.py](Maths/find_if_digits_can_be_won_3232.py)                                                        | Done   | (Typo? Needs check)               |
| Find the Difference (XOR)                                          | [find_the_difference_using_xor_389.py](Maths/find_the_difference_using_xor_389.py)                                                     | Done   | [389](https://leetcode.com/problems/find-the-difference/)        |
| Find the Pivot Integer                                             | [find_the_pivot_integer_2485.py](Maths/find_the_pivot_integer_2485.py)                                                           | Done   | [2485](https://leetcode.com/problems/find-the-pivot-integer/)    |
| GCD Implementation                                                 | [gcd.py](Maths/gcd.py)                                                                                   | Done   |                                    |
| Harshad Number                                                     | [harshad_no_3099.py](Maths/harshad_no_3099.py)                                                                       | Done   | [3099](https://leetcode.com/problems/harshad-number/)            |
| Is Armstrong Number                                                | [is_armstrong_no.py](Maths/is_armstrong_no.py)                                                                       | Done   |                                    |
| Is Prime (Optimized)                                               | [is_prime_optimized.py](Maths/is_prime_optimized.py)                                                                    | Done   |                                    |
| Is Ugly                                                            | [is_ugly_263.py](Maths/is_ugly_263.py)                                                                           | Done   | [263](https://leetcode.com/problems/ugly-number/)                |
| Max Sum of Pair with Equal Digit Sum (Bruteforce)                  | [max_sum_of_a_pair_with_equal_sum_of_digits_2342_bruteforce_quadratic.py](Maths/max_sum_of_a_pair_with_equal_sum_of_digits_2342_bruteforce_quadratic.py)                  | Done   | [2342](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/) |
| Max Sum of Pair with Equal Digit Sum (Hashing)                     | [max_sum_of_a_pair_with_equal_sum_of_digits_2342_linear_time_hashing.py](Maths/max_sum_of_a_pair_with_equal_sum_of_digits_2342_linear_time_hashing.py)                   | Done   | [2342](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/) |
| Number After Double Reversal (Modulo)                              | [no_after_double_reversal_2119_modulous.py](Maths/no_after_double_reversal_2119_modulous.py)                                                | Done   | [2119](https://leetcode.com/problems/a-number-after-a-double-reversal/) |
| Number of 1 Bits (Hamming Weight)                                  | [no_of_1_bits_191_logn.py](Maths/no_of_1_bits_191_logn.py)                                                                 | Done   | [191](https://leetcode.com/problems/number-of-1-bits/)           |
| Number of Common Factors                                           | [no_of_common_factors_2427.py](Maths/no_of_common_factors_2427.py)                                                             | Done   | [2427](https://leetcode.com/problems/number-of-common-factors/)  |
| Number of Steps to Reduce a Number to Zero                         | [no_of_steps_to_reduce_a_no_to_zero.py](Maths/no_of_steps_to_reduce_a_no_to_zero.py)                                                    | Done   | [1342](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) |
| Print All Divisors                                                 | [print_all_divisors.py](Maths/print_all_divisors.py)                                                                    | Done   |                                    |
| Reverse a Number                                                   | [reverse_a_no.py](Maths/reverse_a_no.py)                                                                          | Done   | [7](https://leetcode.com/problems/reverse-integer/)              |
| Set Mismatch (Using Math)                                          | [set_mismatch_645_using_math.py](Maths/set_mismatch_645_using_math.py)                                                           | Done   | [645](https://leetcode.com/problems/set-mismatch/)               |
| Sieve of Eratosthenes Implementation                               | [sieve_of_eratosthenes.py](Maths/sieve_of_eratosthenes.py)                                                                 | Done   |                                    |
| Single Element in a Sorted Array (Bruteforce)                      | [singleNonDuplicate540.py](Maths/singleNonDuplicate540.py)                                                                 | Done   | [540](https://leetcode.com/problems/single-element-in-a-sorted-array/) |
| Single Element in a Sorted Array (Binary Search)                   | [singleNonDuplicate540_binary_search.py](Maths/singleNonDuplicate540_binary_search.py)                                                   | Done   | [540](https://leetcode.com/problems/single-element-in-a-sorted-array/) |
| Square Root (Bruteforce)                                           | [square_root_of_a_no_69_bruteforce_sqrt_time_complexity.py](Maths/square_root_of_a_no_69_bruteforce_sqrt_time_complexity.py)                                | Done   | [69](https://leetcode.com/problems/sqrtx/)                       |
| Subtract Product and Sum of Digits                                 | [subtact_prod_and_sum_of_digits_of_a_no_1281.py](Maths/subtact_prod_and_sum_of_digits_of_a_no_1281.py)                                           | Done   | [1281](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/) |
| Sum Multiples                                                      | [sum_multiples_2652.py](Maths/sum_multiples_2652.py)                                                                    | Done   | [2652](https://leetcode.com/problems/sum-multiples/)             |
| Sum Multiples (Optimized O(1))                                     | [sum_multiples_2652_optimized.py](Maths/sum_multiples_2652_optimized.py)                                                          | Done   | [2652](https://leetcode.com/problems/sum-multiples/)             |
| The Kth Factor of N                                                | [the_kth_factor_of_n_1492.py](Maths/the_kth_factor_of_n_1492.py)                                                              | Done   | [1492](https://leetcode.com/problems/the-kth-factor-of-n/)       |
| Three Divisors (Linear Time)                                       | [three_divisors_linear_time_1952.py](Maths/three_divisors_linear_time_1952.py)                                                       | Done   | [1952](https://leetcode.com/problems/three-divisors/)            |
| Three Divisors (Optimized Prime Check)                             | [three_divisors_optimized_using_prime_no_1952.py](Maths/three_divisors_optimized_using_prime_no_1952.py)                                          | Done   | [1952](https://leetcode.com/problems/three-divisors/)            |
| Water Bottles                                                      | [water_bodies_1518.py](Maths/water_bodies_1518.py)                                                                       | Done   | [1518](https://leetcode.com/problems/water-bottles/)             |
| XOR Operation in an Array                                          | [xor_operation_in_array_1486.py](Maths/xor_operation_in_array_1486.py)                                                           | Done   | [1486](https://leetcode.com/problems/xor-operation-in-an-array/) |

</details>

<details>
<summary><strong>Patterns 🖼️</strong> (11 items)</summary>

| Program Name                       | Location                                                                | Status |
| :--------------------------------- | :---------------------------------------------------------------------- | :----- |
| Decreasing Stars Pyramid           | [decreasing_stars_top_to_bottom_pyramid.py](Patterns/decreasing_stars_top_to_bottom_pyramid.py)    | Done   |
| Diamond Pattern                    | [diamond.py](Patterns/diamond.py)                                       | Done   |
| Half Diamond Pattern               | [halfdiamond.py](Patterns/halfdiamond.py)                               | Done   |
| Numbers Pyramid                    | [numbers_top_to_bottom_pyramid.py](Patterns/numbers_top_to_bottom_pyramid.py)             | Done   |
| Numbers Pyramid (Alternative)      | [numbers_top_to_bottom_pyramid_alternative_solution.py](Patterns/numbers_top_to_bottom_pyramid_alternative_solution.py) | Done |
| Numbers Pyramid (Row No Repeat)    | [numbers_top_to_bottom_pyramid_row_no_repeat.py](Patterns/numbers_top_to_bottom_pyramid_row_no_repeat.py) | Done |
| Stars Square Pattern               | [stars_square_pattern.py](Patterns/stars_square_pattern.py)                      | Done   |
| Stars Pyramid                      | [stars_top_to_bottom_pyramid.py](Patterns/stars_top_to_bottom_pyramid.py)               | Done   |
| Christmas Tree                     | [xmastree.py](Patterns/xmastree.py)                                     | Done   |
| Inverted Christmas Tree            | [xmastree_inverted.py](Patterns/xmastree_inverted.py)                         | Done   |

</details>

<details>
<summary><strong>Sorting ⇅</strong> (28 items)</summary>

| Program Name                                        | Location                                                                                          | Status | Notes (LC #)     |
| :-------------------------------------------------- | :------------------------------------------------------------------------------------------------ | :----- | :--------------- |
| Bubble Sort                                         | [bubble_sort.py](Sorting/bubble_sort.py)                                                            | Done   |                  |
| Count Smaller Numbers (Bruteforce)                  | [count_no_smaller_than_current_no_bruteforce_1365.py](Sorting/count_no_smaller_than_current_no_bruteforce_1365.py)                       | Done   | [1365](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) |
| Count Smaller Numbers (Optimized/Sorting)           | [count_no_smaller_than_current_no_optimized_1365.py](Sorting/count_no_smaller_than_current_no_optimized_1365.py)                        | Done   | [1365](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) |
| Find Target Indices After Sorting                   | [find_target_indices_after_sorting_2089.py](Sorting/find_target_indices_after_sorting_2089.py)                                 | Done   | [2089](https://leetcode.com/problems/find-target-indices-after-sorting-array/) |
| Find the Difference (Sorting)                       | [find_the_difference_using_sorting_389.py](Sorting/find_the_difference_using_sorting_389.py)                                  | Done   | [389](https://leetcode.com/problems/find-the-difference/)        |
| Find Integer Added to Array I                       | [find_the_integer_added_to_array_I_3131_sorting.py](Sorting/find_the_integer_added_to_array_I_3131_sorting.py)                         | Done   | [3131](https://leetcode.com/problems/find-the-integer-added-to-array-i/) |
| Height Checker                                      | [height_checker_1051.py](Sorting/height_checker_1051.py)                                                    | Done   | [1051](https://leetcode.com/problems/height-checker/)            |
| Insertion Sort                                      | [insert_sort.py](Sorting/insert_sort.py)                                                            | Done   |                  |
| Maximum Number of Coins You Can Get                 | [maximum_no_of_coins_you_can_get_1561.py](Sorting/maximum_no_of_coins_you_can_get_1561.py)                                   | Done   | [1561](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/) |
| Max Prod Diff (Find Max/Min)                        | [maximum_product_difference_between_two_pairs_by_finding_two_max_and_two_mins_1913.py](Sorting/maximum_product_difference_between_two_pairs_by_finding_two_max_and_two_mins_1913.py) | Done | [1913](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/) |
| Max Prod Diff (Sorting)                             | [maximum_product_difference_between_two_pairs_using_sorting_1913.py](Sorting/maximum_product_difference_between_two_pairs_using_sorting_1913.py)        | Done   | [1913](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/) |
| Max Prod of Two Elements (Linear)                   | [maximum_product_of_two_elements_in_an_array_1464_optimized_linear_traversal.py](Sorting/maximum_product_of_two_elements_in_an_array_1464_optimized_linear_traversal.py) | Done | [1464](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) |
| Max Prod of Two Elements (Sorting)                  | [maximum_product_of_two_elements_in_an_array_1464_sorting.py](Sorting/maximum_product_of_two_elements_in_an_array_1464_sorting.py)               | Done   | [1464](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) |
| Merge Two 2D Arrays (Hashing + Sorting)             | [merge_two_2D_arrays_by_summing_values_2570_linear_space_hashing_and_sorting.py](Sorting/merge_two_2D_arrays_by_summing_values_2570_linear_space_hashing_and_sorting.py) | Done | [2570](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/) |
| Minimum Average of Smallest and Largest             | [minimum_average_of_smallest_and_largest_elements_3194.py](Sorting/minimum_average_of_smallest_and_largest_elements_3194.py)                  | Done   | [3194](https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/) |
| Minimum Number Game                                 | [minimum_number_game_2974.py](Sorting/minimum_number_game_2974.py)                                               | Done   | [2974](https://leetcode.com/problems/minimum-number-game/)       |
| Minimum Sum of Four Digit No After Splitting        | [mininum_sum_of_four_digit_no_after_splitting_digits_2160.py](Sorting/mininum_sum_of_four_digit_no_after_splitting_digits_2160.py)               | Done   | [2160](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/) |
| Selection Sort                                      | [selection_sort.py](Sorting/selection_sort.py)                                                        | Done   |                  |
| Sort Array By Parity (Extra Space)                  | [sort_array_by_parity_905_extra_space.py](Sorting/sort_array_by_parity_905_extra_space.py)                                   | Done   | [905](https://leetcode.com/problems/sort-array-by-parity/)       |
| Sort Array By Parity (In-place)                     | [sort_array_by_parity_905_no_extra_space.py](Sorting/sort_array_by_parity_905_no_extra_space.py)                                | Done   | [905](https://leetcode.com/problems/sort-array-by-parity/)       |
| Sort Binary Array                                   | [sort_binary_array.py](Sorting/sort_binary_array.py)                                                      | Done   | (Similar to 75)  |
| Sort Colors (Counting Sort)                         | [sort_colors_counting_sort_75.py](Sorting/sort_colors_counting_sort_75.py)                                           | Done   | [75](https://leetcode.com/problems/sort-colors/)                 |
| Sorting the Sentence (Bruteforce)                   | [sorting_the_sentence_1859_bruteforce.py](Sorting/sorting_the_sentence_1859_bruteforce.py)                                   | Done   | [1859](https://leetcode.com/problems/sorting-the-sentence/)      |
| Sorting the Sentence (Hashing)                      | [sorting_the_sentence_1859_optimized_hashing.py](Sorting/sorting_the_sentence_1859_optimized_hashing.py)                            | Done   | [1859](https://leetcode.com/problems/sorting-the-sentence/)      |
| Sorting the Sentence (Sorting)                      | [sorting_the_sentence_1859_optimized_sorting.py](Sorting/sorting_the_sentence_1859_optimized_sorting.py)                            | Done   | [1859](https://leetcode.com/problems/sorting-the-sentence/)      |
| Third Maximum Number                                | [third_maximum_no_414.py](Sorting/third_maximum_no_414.py)                                                   | Done   | [414](https://leetcode.com/problems/third-maximum-number/)       |
| Widest Vertical Area Between Two Points             | [widest_vertical_area_in_graph_1637.py](Sorting/widest_vertical_area_in_graph_1637.py)                                     | Done   | [1637](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/) |

</details>

<details>
<summary><strong>Array 🔢</strong> (60 items)</summary>

| Program Name                                        | Location                                                                       | Status | Notes (LC #)        |
| :-------------------------------------------------- | :----------------------------------------------------------------------------- | :----- | :------------------ |
| Apply Operations on an Array (Extra Space)          | [apply_operations_on_an_array_2460_extra_space.py](array/apply_operations_on_an_array_2460_extra_space.py)               | Done   | [2460](https://leetcode.com/problems/apply-operations-to-an-array/) |
| Apply Operations on an Array (Constant Space)       | [apply_operations_on_an_array_2460_optimized_constant_space.py](array/apply_operations_on_an_array_2460_optimized_constant_space.py)  | Done   | [2460](https://leetcode.com/problems/apply-operations-to-an-array/) |
| Build Array from Permutation                        | [build_array_from_permutation_1920.py](array/build_array_from_permutation_1920.py)                           | Done   | [1920](https://leetcode.com/problems/build-array-from-permutation/) |
| Capacity To Ship Packages (Bruteforce)              | [capacity_to_ship_packages_within_d_days_1011_bruteforce_quadratic_time.py](array/capacity_to_ship_packages_within_d_days_1011_bruteforce_quadratic_time.py) | Done | [1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) |
| Categorize Box                                      | [categorize_box_2525.py](array/categorize_box_2525.py)                                         | Done   | [2525](https://leetcode.com/problems/categorize-box-according-to-criteria/) |
| Check If Array Is Sorted and Rotated (Bruteforce)   | [check_if_array_is_sorted_and_rotated_1752_bruteforce_quadratic_time.py](array/check_if_array_is_sorted_and_rotated_1752_bruteforce_quadratic_time.py) | Done | [1752](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) |
| Check If Array Is Sorted and Rotated (Optimized)    | [check_if_array_is_sorted_and_rotated_1752_optimized_linear_time.py](array/check_if_array_is_sorted_and_rotated_1752_optimized_linear_time.py) | Done | [1752](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) |
| Check If N and Its Double Exist                     | [check_if_n_and_its_double_exist_1346.py](array/check_if_n_and_its_double_exist_1346.py)                        | Done   | [1346](https://leetcode.com/problems/check-if-n-and-its-double-exist/) |
| Count Items Matching a Rule                         | [count_items_matching_a_rule_1773.py](array/count_items_matching_a_rule_1773.py)                            | Done   | [1773](https://leetcode.com/problems/count-items-matching-a-rule/) |
| Count Negative Numbers in Sorted Matrix (Bruteforce)| [count_negative_no_in_a_sorted_array_1351_bruteforce.py](array/count_negative_no_in_a_sorted_array_1351_bruteforce.py)         | Done   | [1351](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) |
| Count Number of Bad Pairs (Bruteforce)              | [count_no_of_bad_pairs_bruteforce_2364_quadratic_time.py](array/count_no_of_bad_pairs_bruteforce_2364_quadratic_time.py)        | Done   | [2364](https://leetcode.com/problems/count-number-of-bad-pairs/) |
| Count Pairs That Form a Complete Day I (Bruteforce) | [count_pairs_that_form_a_complete_day_1_3184_bruteforce.py](array/count_pairs_that_form_a_complete_day_1_3184_bruteforce.py)      | Done   | [3184](https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/) |
| Count Pairs With Sum Less Than Target               | [count_pairs_with_sum_less_than_target.py](array/count_pairs_with_sum_less_than_target.py)                       | Done   | [2824](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/) |
| Count Subarrays of Length Three (Placeholder)       | [count_subarrays_of_length_three_with_condition.py](array/count_subarrays_of_length_three_with_condition.py)              | Done   | (Needs LC #?)     |
| Decompress Run-Length Encoded List                  | [decompress_run_length_encoded_list_1313.py](array/decompress_run_length_encoded_list_1313.py)                     | Done   | [1313](https://leetcode.com/problems/decompress-run-length-encoded-list/) |
| Find the Difference Between Two Arrays              | [difference_between_two_arrays_2215.py](array/difference_between_two_arrays_2215.py)                          | Done   | [2215](https://leetcode.com/problems/find-the-difference-of-two-arrays/) |
| Divide Array Into Equal Pairs (Using Array Counts)  | [divide_array_into_equal_parts_2206_using_array.py](array/divide_array_into_equal_parts_2206_using_array.py)              | Done   | [2206](https://leetcode.com/problems/divide-array-into-equal-pairs/) |
| Final Prices With Discount                          | [final_price_with_discount_1475.py](array/final_price_with_discount_1475.py)                              | Done   | [1475](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) - Stack      |
| Final Value After Performing Operations             | [final_value_after_performing_operations_2011.py](array/final_value_after_performing_operations_2011.py)                | Done   | [2011](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/) |
| Find Lucky Integer in an Array                      | [find_lucky_integer_in_an_array_1394.py](array/find_lucky_integer_in_an_array_1394.py)                         | Done   | [1394](https://leetcode.com/problems/find-lucky-integer-in-an-array/) |
| Find Minimum in Rotated Sorted Array (Linear)       | [find_minimum_in_rotated_sorted_array_153_bruteforce_linear_time.py](array/find_minimum_in_rotated_sorted_array_153_bruteforce_linear_time.py) | Done | [153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) |
| Find Missing and Repeating No (Bruteforce)          | [find_missing_and_repeating_no_2965_bruteforce_quadratic.py](array/find_missing_and_repeating_no_2965_bruteforce_quadratic.py)    | Done   | (GFG/Similar [645](https://leetcode.com/problems/set-mismatch/)) |
| Find Peak Element (Linear)                          | [find_peak_element_162_bruteforce_linear_time_complexity.py](array/find_peak_element_162_bruteforce_linear_time_complexity.py)     | Done   | [162](https://leetcode.com/problems/find-peak-element/) |
| Find the Highest Altitude                           | [find_the_highest_altitude_1732.py](array/find_the_highest_altitude_1732.py)                              | Done   | [1732](https://leetcode.com/problems/find-the-highest-altitude/) |
| Find Smallest Divisor Given Threshold (Bruteforce)  | [find_the_smallest_divisor_given_a_threshold_1283_using_bruteforce.py](array/find_the_smallest_divisor_given_a_threshold_1283_using_bruteforce.py) | Done | [1283](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) |
| Fizz Buzz                                           | [fizz_buzz_412.py](array/fizz_buzz_412.py)                                               | Done   | [412](https://leetcode.com/problems/fizz-buzz/) |
| Flipping an Image                                   | [flipping_an_image_832.py](array/flipping_an_image_832.py)                                       | Done   | [832](https://leetcode.com/problems/flipping-an-image/) |
| Intersection of Two Arrays                          | [intersection_of_two_arrays_349.py](array/intersection_of_two_arrays_349.py)                              | Done   | [349](https://leetcode.com/problems/intersection-of-two-arrays/) - Set       |
| Koko Eating Bananas (Bruteforce)                    | [koko_eating_bananas_875_bruteforce_quadratic_time.py](array/koko_eating_bananas_875_bruteforce_quadratic_time.py)           | Done   | [875](https://leetcode.com/problems/koko-eating-bananas/) |
| Kth Missing Positive Number (Linear)                | [kth_missing_positive_no_from_sorted_array_1539.py](array/kth_missing_positive_no_from_sorted_array_1539.py)              | Done   | [1539](https://leetcode.com/problems/kth-missing-positive-number/) |
| Longest Inc/Dec Subarray (Bruteforce)               | [longest_strictly_increasing_or_decreasing_array_3015_bruteforce_quadratic_time.py](array/longest_strictly_increasing_or_decreasing_array_3015_bruteforce_quadratic_time.py) | Done | (Typo 3105?)    |
| Matrix Diagonal Sum (Bruteforce)                    | [matrix_diagonal_sum_bruteforce_1572.py](array/matrix_diagonal_sum_bruteforce_1572.py)                         | Done   | [1572](https://leetcode.com/problems/matrix-diagonal-sum/) |
| Matrix Diagonal Sum (Optimized)                     | [matrix_diagonal_sum_optimized_1572.py](array/matrix_diagonal_sum_optimized_1572.py)                          | Done   | [1572](https://leetcode.com/problems/matrix-diagonal-sum/) |
| Max Number of Words Found in Sentences              | [max_no_of_words_in_sentence_114.py](array/max_no_of_words_in_sentence_114.py)                               | Done   | [2114](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/) |
| Maximum Ascending Subarray Sum (Bruteforce)         | [maximum_ascending_subarray_sum_1800_bruteforce_quadratic_time.py](array/maximum_ascending_subarray_sum_1800_bruteforce_quadratic_time.py) | Done | [1800](https://leetcode.com/problems/maximum-ascending-subarray-sum/) |
| Maximum Ascending Subarray Sum (Optimized)          | [maximum_ascending_subarray_sum_1800_optimized_linear_time.py](array/maximum_ascending_subarray_sum_1800_optimized_linear_time.py)   | Done   | [1800](https://leetcode.com/problems/maximum-ascending-subarray-sum/) |
| Max Count of Positive and Negative (Linear)         | [maximum_count_of_positive_and_negative_integers_2529_bruteforce_linear.py](array/maximum_count_of_positive_and_negative_integers_2529_bruteforce_linear.py) | Done | [2529](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/) |
| Merge Strings Alternately                           | [merge_strings_alternatively_1768.py](array/merge_strings_alternatively_1768.py)                            | Done   | [1768](https://leetcode.com/problems/merge-strings-alternately/) |
| Minimum Absolute Difference                         | [min_absolute_difference_1200.py](array/min_absolute_difference_1200.py)                                | Done   | [1200](https://leetcode.com/problems/minimum-absolute-difference/) - Sorting  |
| Minimum Index Sum of Two Lists                      | [min_index_sum_of_two_lists_599.py](array/min_index_sum_of_two_lists_599.py)                              | Done   | [599](https://leetcode.com/problems/minimum-index-sum-of-two-lists/) - Hashing   |
| Min No of Days to Make M Bouquets (Bruteforce)      | [min_no_of_days_to_make_m_bouquets_1482_bruteforce_quadratic_time.py](array/min_no_of_days_to_make_m_bouquets_1482_bruteforce_quadratic_time.py) | Done | [1482](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) |
| Minimum Operations Make Columns Increasing          | [minimum_operations_to_make_columns_strictly_increasing_3402.py](array/minimum_operations_to_make_columns_strictly_increasing_3402.py) | Done   | (Typo?)           |
| Minimum Cuts to Divide a Circle                     | [mininum_cuts_to_divide_a_circle_2481.py](array/mininum_cuts_to_divide_a_circle_2481.py)                        | Done   | [2481](https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/) |
| Neither Minimum nor Maximum (Linear Space)          | [neither_minimum_nor_maximum_2733_linear_space.py](array/neither_minimum_nor_maximum_2733_linear_space.py)               | Done   | [2733](https://leetcode.com/problems/neither-minimum-nor-maximum/) |
| Neither Minimum nor Maximum (Constant Space)        | [neither_minimum_nor_maximum_2733_optimized_constant_space.py](array/neither_minimum_nor_maximum_2733_optimized_constant_space.py)   | Done   | [2733](https://leetcode.com/problems/neither-minimum-nor-maximum/) |
| Number of Employees Who Met the Target              | [no_of_employees_who_meet_the_target_2798.py](array/no_of_employees_who_meet_the_target_2798.py)                    | Done   | [2798](https://leetcode.com/problems/number-of-employees-who-met-the-target/) |
| Number of Pairs with Absolute Difference K          | [no_of_pair_with_absolute_difference_k.py](array/no_of_pair_with_absolute_difference_k.py)                       | Done   | [2006](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/) |
| Number of Pairs with Sum K                          | [no_of_pair_with_sum_k.py](array/no_of_pair_with_sum_k.py)                                       | Done   | (Similar [1](https://leetcode.com/problems/two-sum/), [167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/))  |
| Partition Array According to Pivot                  | [partition_array_according_to_given_plot_2161_linear_space.py](array/partition_array_according_to_given_plot_2161_linear_space.py)   | Done   | [2161](https://leetcode.com/problems/partition-array-according-to-given-pivot/) |
| Peak Index in a Mountain Array (Linear)             | [peak_index_in_a_mountain_array_852_bruteforce_linear.py](array/peak_index_in_a_mountain_array_852_bruteforce_linear.py)        | Done   | [852](https://leetcode.com/problems/peak-index-in-a-mountain-array/) |
| Product of the Last K Numbers (Bruteforce)          | [product_of_last_k_numbers_1352_bruteforce.py](array/product_of_last_k_numbers_1352_bruteforce.py)                   | Done   | [1352](https://leetcode.com/problems/product-of-the-last-k-numbers/) |
| Product of the Last K Numbers (Bruteforce 2)        | [product_of_last_k_numbers_1352_bruteforce_solution_2.py](array/product_of_last_k_numbers_1352_bruteforce_solution_2.py)        | Done   | [1352](https://leetcode.com/problems/product-of-the-last-k-numbers/) |
| Product of the Last K Numbers (Prefix Product)      | [product_of_last_k_numbers_1352_optmized_prefix_product.py](array/product_of_last_k_numbers_1352_optmized_prefix_product.py)      | Done   | [1352](https://leetcode.com/problems/product-of-the-last-k-numbers/) |
| Replace Elements with Greatest on Right             | [replace_elements_with_greatest_element_on_right_side_1299.py](array/replace_elements_with_greatest_element_on_right_side_1299.py)   | Done   | [1299](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) |
| Richest Customer Wealth                             | [richest_customer_wealth_1672.py](array/richest_customer_wealth_1672.py)                                | Done   | [1672](https://leetcode.com/problems/richest-customer-wealth/) |
| Row With Maximum Ones (Bruteforce)                  | [row_with_maximum_ones_2643_bruteforce.py](array/row_with_maximum_ones_2643_bruteforce.py)                       | Done   | [2643](https://leetcode.com/problems/row-with-maximum-ones/) |
| Row With Maximum Ones (Optimized)                   | [row_with_maximum_ones_2643_optimized.py](array/row_with_maximum_ones_2643_optimized.py)                        | Done   | [2643](https://leetcode.com/problems/row-with-maximum-ones/) |
| Running Sum of 1d Array                             | [running_sum_of_1d_array_or_cummulative_sum_1480.py](array/running_sum_of_1d_array_or_cummulative_sum_1480.py)             | Done   | [1480](https://leetcode.com/problems/running-sum-of-1d-array/) |
| Search a 2D Matrix (Bruteforce)                     | [search_a_2d_matrix_74_bruteforce_quadratic.py](array/search_a_2d_matrix_74_bruteforce_quadratic.py)                  | Done   | [74](https://leetcode.com/problems/search-a-2d-matrix/) |
| Search in Rotated Sorted Array (Linear)             | [search_in_rotated_sorted_array_33_bruteforce_linear_time.py](array/search_in_rotated_sorted_array_33_bruteforce_linear_time.py)    | Done   | [33](https://leetcode.com/problems/search-in-rotated-sorted-array/) |
| Separate the Digits in an Array                     | [separate_the_digits_in_an_array_2553.py](array/separate_the_digits_in_an_array_2553.py)                        | Done   | [2553](https://leetcode.com/problems/separate-the-digits-in-an-array/) |
| Set Mismatch (Using Array/Hashing)                  | [set_mismatch_645_using_array.py](array/set_mismatch_645_using_array.py)                                | Done   | [645](https://leetcode.com/problems/set-mismatch/) |
| Shuffle the Array                                   | [shuffle_the_array_1470.py](array/shuffle_the_array_1470.py)                                      | Done   | [1470](https://leetcode.com/problems/shuffle-the-array/) |
| Special Array I                                     | [special_array_3151.py](array/special_array_3151.py)                                          | Done   | [3151](https://leetcode.com/problems/special-array-i/) |
| String Matching in an Array (Bruteforce)            | [string_matching_in_array_by_1408.py](array/string_matching_in_array_by_1408.py)                            | Done   | [1408](https://leetcode.com/problems/string-matching-in-an-array/) |
| String Matching in an Array (Sorting)               | [string_matching_in_array_by_sorting_1408.py](array/string_matching_in_array_by_sorting_1408.py)                    | Done   | [1408](https://leetcode.com/problems/string-matching-in-an-array/) |
| Subrectangle Queries                                | [subrectangle_queries_1476.py](array/subrectangle_queries_1476.py)                                   | Done   | [1476](https://leetcode.com/problems/subrectangle-queries/) |
| Sum of Squares of Special Elements                  | [sum_of_squares_of_special_elements_2778.py](array/sum_of_squares_of_special_elements_2778.py)                     | Done   | [2778](https://leetcode.com/problems/sum-of-squares-of-special-elements/) |
| Sort Array By Parity II (In-Place - Misnamed)       | [transform_array_by_parity_3467.py](array/transform_array_by_parity_3467.py)                              | Done   | (Typo? Rel [905](https://leetcode.com/problems/sort-array-by-parity/)/[922](https://leetcode.com/problems/sort-array-by-parity-ii/)) |
| Two Sum II - Input Array Is Sorted                  | [two_sum_for_given_sorted_array_167.py](array/two_sum_for_given_sorted_array_167.py)                          | Done   | [167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |
| Valid Sudoku                                        | [valid_sudoku_36.py](array/valid_sudoku_36.py)                                             | Done   | [36](https://leetcode.com/problems/valid-sudoku/) |
| Find XOR Sum of Numbers Appearing Twice             | [xor_of_no_which_exist_twice_3158.py](array/xor_of_no_which_exist_twice_3158.py)                            | Done   | [3158](https://leetcode.com/problems/find-the-xor-sum-of-all-pairs-bitwise-and/) |

</details>

<details>
<summary><strong>Binary Search 🔍</strong> (23 items)</summary>

| Program Name                                        | Location                                                                                     | Status | Notes (LC #) |
| :-------------------------------------------------- | :------------------------------------------------------------------------------------------- | :----- | :----------- |
| Binary Search (Iterative Template)                  | [binary_search_704.py](binarysearch/binary_search_704.py)                                          | Done   | [704](https://leetcode.com/problems/binary-search/)        |
| Binary Search (Iterative)                           | [binary_search_iterative.py](binarysearch/binary_search_iterative.py)                                | Done   |              |
| Binary Search (Recursive)                           | [binary_search_recursive.py](binarysearch/binary_search_recursive.py)                                | Done   |              |
| Book Allocation Problem                             | [book_allocation.py](binarysearch/book_allocation.py)                                            | Done   | (GFG/Famous) |
| Capacity To Ship Packages (Binary Search)           | [capacity_to_ship_packages_within_d_days_1011_using_binary_search.py](binarysearch/capacity_to_ship_packages_within_d_days_1011_using_binary_search.py) | Done | [1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) |
| Find First and Last Position of Element             | [find_first_and_last_occurence_of_element_34.py](binarysearch/find_first_and_last_occurence_of_element_34.py)            | Done   | [34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |
| Find Minimum in Rotated Sorted Array (Binary Search)| [find_minimum_in_rotated_sorted_array_153_binary_search.py](binarysearch/find_minimum_in_rotated_sorted_array_153_binary_search.py) | Done   | [153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) |
| Find Peak Element (Binary Search)                   | [find_peak_element_162_optimized_binary_search.py](binarysearch/find_peak_element_162_optimized_binary_search.py)          | Done   | [162](https://leetcode.com/problems/find-peak-element/) |
| Find Smallest Divisor Given Threshold (Binary Search)|[find_the_smallest_divisor_given_a_threshold_1283_using_binary_search.py](binarysearch/find_the_smallest_divisor_given_a_threshold_1283_using_binary_search.py) | Done | [1283](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) |
| Find Upper Bound                                    | [find_upper_bound_in_a_sorted_array.py](binarysearch/find_upper_bound_in_a_sorted_array.py)                     | Done   |              |
| Find Lower Bound                                    | [first_lower_bound_in_a_sorted_array.py](binarysearch/first_lower_bound_in_a_sorted_array.py)                    | Done   |              |
| Floor and Ceiling                                   | [floor_and_ceiling_of_a_sorted_array.py](binarysearch/floor_and_ceiling_of_a_sorted_array.py)                    | Done   |              |
| Floor in Sorted Array                               | [floor_in_a_sorted_array.py](binarysearch/floor_in_a_sorted_array.py)                                | Done   |              |
| Koko Eating Bananas (Binary Search)                 | [koko_eating_bananas_875_binary_search.py](binarysearch/koko_eating_bananas_875_binary_search.py)                  | Done   | [875](https://leetcode.com/problems/koko-eating-bananas/) |
| Kth Missing Positive Number (Binary Search)         | [kth_missing_positive_no_from_sorted_array_1539_binary_search.py](binarysearch/kth_missing_positive_no_from_sorted_array_1539_binary_search.py) | Done | [1539](https://leetcode.com/problems/kth-missing-positive-number/) |
| Max Count of Positive and Negative (Binary Search)  | [maximum_count_of_positive_and_negative_integers_2529_binary_search.py](binarysearch/maximum_count_of_positive_and_negative_integers_2529_binary_search.py) | Done | [2529](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/) |
| Min No of Days to Make M Bouquets (Binary Search)   | [min_no_of_days_to_make_m_bouquets_1482_using_binary_search.py](binarysearch/min_no_of_days_to_make_m_bouquets_1482_using_binary_search.py) | Done | [1482](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) |
| Peak Index in a Mountain Array (Binary Search)      | [peak_index_in_a_mountain_array_852_binary_search.py](binarysearch/peak_index_in_a_mountain_array_852_binary_search.py)       | Done   | [852](https://leetcode.com/problems/peak-index-in-a-mountain-array/) |
| Row with Maximum Ones (Binary Search)               | [row_with_maximum_ones_row_wise_sorted_binary_search_gfg.py](binarysearch/row_with_maximum_ones_row_wise_sorted_binary_search_gfg.py)| Done   | (GFG/Rel [2643](https://leetcode.com/problems/row-with-maximum-ones/)) |
| Search a 2D Matrix (Binary Search mlogn)          | [search_a_2d_matrix_74_bruteforce_binary_search_mlogn.py](binarysearch/search_a_2d_matrix_74_bruteforce_binary_search_mlogn.py)   | Done   | [74](https://leetcode.com/problems/search-a-2d-matrix/) |
| Search a 2D Matrix (Binary Search log(m*n))       | [search_a_2d_matrix_74_optimized_binary_search_logm+n.py](binarysearch/search_a_2d_matrix_74_optimized_binary_search_logm%2Bn.py)   | Done   | [74](https://leetcode.com/problems/search-a-2d-matrix/) |
| Search in Infinite Sorted Array                     | [search_in_infinite_sorted_array.py](binarysearch/search_in_infinite_sorted_array.py)                        | Done   | (Common Prob) |
| Search in Rotated Sorted Array (Binary Search)      | [search_in_rotated_sorted_array_33_binary_search.py](binarysearch/search_in_rotated_sorted_array_33_binary_search.py)        | Done   | [33](https://leetcode.com/problems/search-in-rotated-sorted-array/) |
| Search in Rotated Sorted Array II (Duplicates)      | [search_in_rotated_sorted_array_having_duplicates_81_binary_search.py](binarysearch/search_in_rotated_sorted_array_having_duplicates_81_binary_search.py) | Done | [81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) |
| Search Insert Position                              | [search_insert_position_35.py](binarysearch/search_insert_position_35.py)                              | Done   | [35](https://leetcode.com/problems/search-insert-position/) |
| Square Root (Binary Search)                         | [square_root_of_a_no_69_optimized_binary_search.py](binarysearch/square_root_of_a_no_69_optimized_binary_search.py)         | Done   | [69](https://leetcode.com/problems/sqrtx/) |
| Square Root (Binary Search Alt)                     | [square_root_of_a_no_69_optimized_binary_search_using_ans.py](binarysearch/square_root_of_a_no_69_optimized_binary_search_using_ans.py) | Done | [69](https://leetcode.com/problems/sqrtx/) |
| Valid Perfect Square                                | [valid_perfect_square_367.py](binarysearch/valid_perfect_square_367.py)                               | Done   | [367](https://leetcode.com/problems/valid-perfect-square/) |

</details>

<details>
<summary><strong>Graph 🕸️</strong> (3 items)</summary>

| Program Name                       | Location                                                              | Status | Notes (LC #) |
| :--------------------------------- | :-------------------------------------------------------------------- | :----- | :----------- |
| Find Center of Star Graph (Optim.) | [find_center_of_star_graph_optimized_1791.py](graph/find_center_of_star_graph_optimized_1791.py)   | Done   | [1791](https://leetcode.com/problems/find-center-of-star-graph/) |
| Find Center of Star Graph (Hash)   | [find_center_of_star_graph_using_hashing1791.py](graph/find_center_of_star_graph_using_hashing1791.py)| Done   | [1791](https://leetcode.com/problems/find-center-of-star-graph/) |
| Number of Islands                  | [no_of_islands_200.py](graph/no_of_islands_200.py)                          | Done   | [200](https://leetcode.com/problems/number-of-islands/) - DFS/BFS |

</details>

<details>
<summary><strong>Hashing 🔑</strong> (25 items)</summary>

| Program Name                                | Location                                                                             | Status | Notes (LC #) |
| :------------------------------------------ | :----------------------------------------------------------------------------------- | :----- | :----------- |
| Common Elements Between Two Arrays          | [common_elements_between_two_arrays_2956.py](hashing/common_elements_between_two_arrays_2956.py)                     | Done   | [2956](https://leetcode.com/problems/find-common-elements-between-two-arrays/) |
| Contains Duplicate                          | [contains_dupilcate_217.py](hashing/contains_dupilcate_217.py)                                      | Done   | [217](https://leetcode.com/problems/contains-duplicate/) |
| Count Frequency                             | [count_frequency.php.py](hashing/count_frequency.php.py)                                           | Done   | (Filename typo) |
| Determine if String Halves Are Alike        | [determine_if_string_halves_are_alike_1704.py](hashing/determine_if_string_halves_are_alike_1704.py)                   | Done   | [1704](https://leetcode.com/problems/determine-if-string-halves-are-alike/) |
| Divide Array Into Equal Pairs               | [divide_array_into_equal_parts_2206.py](hashing/divide_array_into_equal_parts_2206.py)                          | Done   | [2206](https://leetcode.com/problems/divide-array-into-equal-pairs/) |
| Find the Difference (Hashing)               | [find_the_difference_389.py](hashing/find_the_difference_389.py)                                     | Done   | [389](https://leetcode.com/problems/find-the-difference/) |
| Find Words That Can Be Formed by Characters | [find_words_219.py](hashing/find_words_219.py)                                                     | Done   | [1160](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/) |
| Basic Hashing Function Example              | [hashing_function.py](hashing/hashing_function.py)                                                | Done   |              |
| HashMap Chaining Example                    | [hashmap_chaining_to_avoid_collision.py](hashing/hashmap_chaining_to_avoid_collision.py)                         | Done   |              |
| HashMap Class Example                       | [hashmap_class.py](hashing/hashmap_class.py)                                                   | Done   |              |
| Intersection of Two Arrays II               | [intersection_of_two_arrays_II_350.py](hashing/intersection_of_two_arrays_II_350.py)                           | Done   | [350](https://leetcode.com/problems/intersection-of-two-arrays-ii/) |
| Isomorphic Strings                          | [isomorphic_strings_205.py](hashing/isomorphic_strings_205.py)                                      | Done   | [205](https://leetcode.com/problems/isomorphic-strings/) |
| Jewels and Stones (Dict)                    | [jewels_and_stones_dictionary_way_771.py](hashing/jewels_and_stones_dictionary_way_771.py)                        | Done   | [771](https://leetcode.com/problems/jewels-and-stones/) |
| Jewels and Stones (Loops)                   | [jewels_and_stones_long_way_771.py](hashing/jewels_and_stones_long_way_771.py)                              | Done   | [771](https://leetcode.com/problems/jewels-and-stones/) |
| Jewels and Stones (Set)                     | [jewels_and_stones_using_set_771.py](hashing/jewels_and_stones_using_set_771.py)                             | Done   | [771](https://leetcode.com/problems/jewels-and-stones/) |
| Kth Distinct String in an Array             | [kth_distinct_string_in_an_array_2053.py](hashing/kth_distinct_string_in_an_array_2053.py)                        | Done   | [2053](https://leetcode.com/problems/kth-distinct-string-in-an-array/) |
| Majority Element                            | [majority_element_169.py](hashing/majority_element_169.py)                                        | Done   | [169](https://leetcode.com/problems/majority-element/) |
| Merge Two 2D Arrays (Hashing)               | [merge_two_2D_arrays_by_summing_values_2570_linear_space_hashing.py](hashing/merge_two_2D_arrays_by_summing_values_2570_linear_space_hashing.py) | Done | [2570](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/) |
| Min Pushes to Type Word II                  | [min_no_of_pushes_to_type_word_II_3016_hashing.py](hashing/min_no_of_pushes_to_type_word_II_3016_hashing.py)               | Done   | [3016](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/) |
| Minimum Steps to Make Two Strings Anagram   | [minimum_no_of_steps_to_make_two_strings_anagram_1347.py](hashing/minimum_no_of_steps_to_make_two_strings_anagram_1347.py)        | Done   | [1347](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/) |
| Missing Number                              | [missing_number_268.py](hashing/missing_number_268.py)                                          | Done   | [268](https://leetcode.com/problems/missing-number/) |
| Most Frequent/Least Frequent Element        | [most_frequent_least_frequent_element.py](hashing/most_frequent_least_frequent_element.py)                        | Done   | (Custom)     |
| Ransom Note                                 | [ransom_note_383.py](hashing/ransom_note_383.py)                                             | Done   | [383](https://leetcode.com/problems/ransom-note/) |
| Single Number                               | [single_number_136.py](hashing/single_number_136.py)                                          | Done   | [136](https://leetcode.com/problems/single-number/) - XOR better |
| Sum of Unique Elements                      | [sum_of_unique_elements_1748.py](hashing/sum_of_unique_elements_1748.py)                          | Done   | [1748](https://leetcode.com/problems/sum-of-unique-elements/) |
| Two Sum                                     | [two_sum_1.py](hashing/two_sum_1.py)                                                   | Done   | [1](https://leetcode.com/problems/two-sum/)          |
| Valid Anagram                               | [valid_anagram_242.py](hashing/valid_anagram_242.py)                                           | Done   | [242](https://leetcode.com/problems/valid-anagram/) |
| Word Pattern                                | [word_pattern_290.py](hashing/word_pattern_290.py)                                           | Done   | [290](https://leetcode.com/problems/word-pattern/) |

</details>

<details>
<summary><strong>Set 🧊</strong> (2 items)</summary>

| Program Name                                        | Location                                                                                       | Status | Notes (LC #) |
| :-------------------------------------------------- | :--------------------------------------------------------------------------------------------- | :----- | :----------- |
| Greatest English Letter (Set)                       | [greatest_english_letter_in_upper_case_and_lower_case_2309_optimized_set.py](Set/greatest_english_letter_in_upper_case_and_lower_case_2309_optimized_set.py) | Done | [2309](https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/) |
| Unique Email Addresses                              | [unique_email_address_929.py](Set/unique_email_address_929.py)                                       | Done   | [929](https://leetcode.com/problems/unique-email-addresses/) |

</details>

<details>
<summary><strong>String 📜</strong> (49 items)</summary>

| Program Name                                      | Location                                                                                               | Status | Notes (LC #)     |
| :------------------------------------------------ | :----------------------------------------------------------------------------------------------------- | :----- | :--------------- |
| Capitalize the Title                              | [capitalize_the_title_2129.py](string/capitalize_the_title_2129.py)                                                  | Done   | [2129](https://leetcode.com/problems/capitalize-the-title/) |
| Cells in Range on Excel Sheet                     | [cells_in_the_range_of_an_excel_sheet_2194.py](string/cells_in_the_range_of_an_excel_sheet_2194.py)                                  | Done   | [2194](https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/) |
| Check if String Is Good (Likely Misnamed)         | [check_balanced_string_3340.py](string/check_balanced_string_3340.py)                                                 | Done   | (Typo? Needs check)|
| Check if All A's Appear Before All B's            | [check_if_all_a's_appear_before_all_b's_2124.py](string/check_if_all_a's_appear_before_all_b's_2124.py)                                | Done   | [2124](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/) |
| Check if All A's Appear Before All B's (Optimized)| [check_if_all_a's_appear_before_all_b's_2124_optimized.py](string/check_if_all_a's_appear_before_all_b's_2124_optimized.py)                      | Done   | [2124](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/) |
| Check if All Characters Have Equal Occurrences    | [check_if_all_characters_have_equal_no_of_occurences_1942.py](string/check_if_all_characters_have_equal_no_of_occurences_1942.py)                   | Done   | [1941](https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/) |
| Check if Numbers Are Ascending in Sentence        | [check_if_no_are_in_ascending_order_in_a_sentence_2042.py](string/check_if_no_are_in_ascending_order_in_a_sentence_2042.py)                      | Done   | [2042](https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/) |
| Check if One Swap Makes Strings Equal (Extra Space)|[check_if_one_character_swap_can_make_two_strings_equal_1790_extra_space.py](string/check_if_one_character_swap_can_make_two_strings_equal_1790_extra_space.py)    | Done   | [1790](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/) |
| Check if One Swap Makes Strings Equal (No Extra)  |[check_if_one_character_swap_can_make_two_strings_equal_1790_no_extra_space.py](string/check_if_one_character_swap_can_make_two_strings_equal_1790_no_extra_space.py) | Done   | [1790](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/) |
| Check if Sentence Is Pangram                    | [check_if_sentence_is_pangram_1832.py](string/check_if_sentence_is_pangram_1832.py)                                          | Done   | [1832](https://leetcode.com/problems/check-if-the-sentence-is-pangram/) |
| Check If String Is Acronym of Words             | [check_if_string_is_acronym_of_words_2828.py](string/check_if_string_is_acronym_of_words_2828.py)                                   | Done   | [2828](https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/) |
| Check If Two String Arrays are Equivalent (BF)    | [check_if_two_string_arrays_are_equivalent_1662_bruteforce_quadratic_because_of_list_are_immutable.py](string/check_if_two_string_arrays_are_equivalent_1662_bruteforce_quadratic_because_of_list_are_immutable.py) | Done | [1662](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/) |
| Check If Two String Arrays are Equivalent (Opt)   | [check_if_two_string_arrays_are_equivalent_1662_optimized.py](string/check_if_two_string_arrays_are_equivalent_1662_optimized.py)                   | Done   | [1662](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/) |
| Convert Date Format (Likely Misnamed)             | [convert_date_to_binary_3280.py](string/convert_date_to_binary_3280.py)                                                | Done   | (Typo? Needs check)|
| Count Prefix and Suffix Pairs I (BF)              | [count_prefix_and_suffix_pairs_3042_bruteforce.py](string/count_prefix_and_suffix_pairs_3042_bruteforce.py)                              | Done   | [3042](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/) |
| Count Vowel Strings in Ranges                     | [count_vowel_string_in_ranges_2559.py](string/count_vowel_string_in_ranges_2559.py)                                          | Done   | [2559](https://leetcode.com/problems/count-vowel-strings-in-ranges/) - Prefix Sum |
| Count Words With Given Prefix                     | [count_words_with_given_prefix_2185.py](string/count_words_with_given_prefix_2185.py)                                         | Done   | [2185](https://leetcode.com/problems/counting-words-with-a-given-prefix/) |
| Decode the Message                                | [decode_the_message_2325.py](string/decode_the_message_2325.py)                                                    | Done   | [2325](https://leetcode.com/problems/decode-the-message/) |
| Decrypt String from Alphabet to Integer Mapping   | [decrypt_string_from_alphabet_to_integer_mapping_1309.py](string/decrypt_string_from_alphabet_to_integer_mapping_1309.py)                       | Done   | [1309](https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/) |
| Defanging an IP Address                           | [defanging_an_ip_address_1108.py](string/defanging_an_ip_address_1108.py)                                               | Done   | [1108](https://leetcode.com/problems/defanging-an-ip-address/) |
| Faulty Keyboard                                   | [faulty_keyboard_2810.py](string/faulty_keyboard_2810.py)                                                       | Done   | [2810](https://leetcode.com/problems/faulty-keyboard/) |
| Find First Palindromic String in Array            | [find_first_palindromic_string_in_array_2108.py](string/find_first_palindromic_string_in_array_2108.py)                                | Done   | [2108](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/) |
| Find Indices of Subarrays w/ Boundary Condition   | [find_indices_of_stable_mountains_3285.py](string/find_indices_of_stable_mountains_3285.py)                                      | Done   | (Typo?)          |
| Find Unique Binary String (Optimized Cantor)      | [find_unique_binary_string_1980_optimized_cantors_diagonalization.py](string/find_unique_binary_string_1980_optimized_cantors_diagonalization.py)           | Done   | [1980](https://leetcode.com/problems/find-unique-binary-string/) |
| Find Unique Binary String (BF Set)                | [find_unique_binary_string_1980_quadratic_time.py](string/find_unique_binary_string_1980_quadratic_time.py)                              | Done   | [1980](https://leetcode.com/problems/find-unique-binary-string/) |
| First Letter to Appear Twice                      | [first_letter_to_appear_twice_2351.py](string/first_letter_to_appear_twice_2351.py)                                          | Done   | [2351](https://leetcode.com/problems/first-letter-to-appear-twice/) - Set       |
| Goal Parser Interpretation                        | [goal_parser_interpretation_1678.py](string/goal_parser_interpretation_1678.py)                                            | Done   | [1678](https://leetcode.com/problems/goal-parser-interpretation/) |
| Greatest English Letter (Array/Hashing)           | [greatest_english_letter_in_upper_case_and_lower_case_2309.py](string/greatest_english_letter_in_upper_case_and_lower_case_2309.py)                  | Done   | [2309](https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/) |
| Calculate Digit Sum of a String (Likely Misnamed) | [hash_divided_string_3271.py](string/hash_divided_string_3271.py)                                                   | Done   | (Typo? Rel [1945](https://leetcode.com/problems/sum-of-digits-of-string-after-convert/)) |
| Largest Odd Number in String                      | [largest_odd_no_in_string_1903.py](string/largest_odd_no_in_string_1903.py)                                              | Done   | [1903](https://leetcode.com/problems/largest-odd-number-in-string/) |
| Max Nesting Depth of Parentheses                  | [max_nesting_depth_of_parantheses_1614.py](string/max_nesting_depth_of_parantheses_1614.py)                                      | Done   | [1614](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/) |
| Max Number of String Pairs (Optimized Set)        | [max_no_of_string_pairs_2744_optimized_linear_time.py](string/max_no_of_string_pairs_2744_optimized_linear_time.py)                          | Done   | [2744](https://leetcode.com/problems/find-maximum-number-of-string-pairs/) |
| Max Number of String Pairs (BF)                   | [max_no_of_string_pairs_2744_quadratic_time.py](string/max_no_of_string_pairs_2744_quadratic_time.py)                                 | Done   | [2744](https://leetcode.com/problems/find-maximum-number-of-string-pairs/) |
| Maximum Odd Binary Number                         | [max_odd_binary_no_2864.py](string/max_odd_binary_no_2864.py)                                                     | Done   | [2864](https://leetcode.com/problems/maximum-odd-binary-number/) |
| Min Pushes to Type Word I (BF - Misnamed file)    | [min_no_of_pushes_to_type_word_II_3016_bruteforce.py](string/min_no_of_pushes_to_type_word_II_3016_bruteforce.py)                           | Done   | [3015](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/) |
| Number After Double Reversal (String)             | [no_after_double_reversal_2119_string.py](string/no_after_double_reversal_2119_string.py)                                       | Done   | [2119](https://leetcode.com/problems/a-number-after-a-double-reversal/) |
| Number of Changing Keys                           | [no_of_changing_keys_3019.py](string/no_of_changing_keys_3019.py)                                                       | Done   | [3019](https://leetcode.com/problems/number-of-changing-keys/) |
| Number of Consistent Strings                      | [no_of_consistent_string_1684.py](string/no_of_consistent_string_1684.py)                                               | Done   | [1684](https://leetcode.com/problems/count-the-number-of-consistent-strings/) - Set       |
| Number of Pairs Concatenation Equal Target (BF)   | [no_of_pairs_with_concatenation_equal_to_target_2023_quadratic_time.py](string/no_of_pairs_with_concatenation_equal_to_target_2023_quadratic_time.py)         | Done   | [2023](https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/) |
| Number of Senior Citizens                         | [no_of_senior_citizens_2678.py](string/no_of_senior_citizens_2678.py)                                                 | Done   | [2678](https://leetcode.com/problems/number-of-senior-citizens/) |
| Percentage of Letter in String                    | [percentage_of_letter_in_string_2278.py](string/percentage_of_letter_in_string_2278.py)                                        | Done   | [2278](https://leetcode.com/problems/percentage-of-letter-in-string/) |
| Removing Trailing Zeros From a String             | [removing_trailing_zero_from_a_string_2710.py](string/removing_trailing_zero_from_a_string_2710.py)                                  | Done   | [2710](https://leetcode.com/problems/removing-trailing-zeros-from-a-string/) |
| String Score (Likely Misnamed)                    | [reverse_degree_of_a_string_3498.py](string/reverse_degree_of_a_string_3498.py)                                            | Done   | (Typo? Rel [3110](https://leetcode.com/problems/score-of-a-string/)) |
| Reverse Prefix of Word                            | [reverse_prefix_of_word_2000.py](string/reverse_prefix_of_word_2000.py)                                                | Done   | [2000](https://leetcode.com/problems/reverse-prefix-of-word/) |
| Robot Return to Origin                            | [robot_return_to_origin_657.py](string/robot_return_to_origin_657.py)                                                 | Done   | [657](https://leetcode.com/problems/robot-return-to-origin/) |
| Score of a String                                 | [score_of_a_string_3110.py](string/score_of_a_string_3110.py)                                                     | Done   | [3110](https://leetcode.com/problems/score-of-a-string/) |
| Shuffle String (BF)                               | [shuffle_string_1528_bruteforce.py](string/shuffle_string_1528_bruteforce.py)                                             | Done   | [1528](https://leetcode.com/problems/shuffle-string/) |
| Shuffle String (Linear Extra Space)               | [shuffle_string_1528_linear_line_extra_time_complexity.py](string/shuffle_string_1528_linear_line_extra_time_complexity.py)                      | Done   | [1528](https://leetcode.com/problems/shuffle-string/) |
| Shuffle String (In-place Cycle Sort - Misnamed)   | [shuffle_string_1528_linear_line_optimized.py](string/shuffle_string_1528_linear_line_optimized.py)                                  | Done   | [1528](https://leetcode.com/problems/shuffle-string/) |
| Snake in Matrix (Likely Misnamed)                 | [snake_in_matrix_3248.py](string/snake_in_matrix_3248.py)                                                       | Done   | (Typo?)          |
| Split Strings by Separator                        | [split_strings_by_separator_2788.py](string/split_strings_by_separator_2788.py)                                       | Done   | [2788](https://leetcode.com/problems/split-strings-by-separator/) |
| Strictly Palindromic Number                       | [strictly_palindromic_no_2396.py](string/strictly_palindromic_no_2396.py)                                             | Done   | [2396](https://leetcode.com/problems/strictly-palindromic-number/) |
| Sum of Digits of String After Convert             | [sum_of_digit_of_string_after_convert_1945.py](string/sum_of_digit_of_string_after_convert_1945.py)                                | Done   | [1945](https://leetcode.com/problems/sum-of-digits-of-string-after-convert/) |
| To Lower Case                                     | [to_lower_case_709.py](string/to_lower_case_709.py)                                                     | Done   | [709](https://leetcode.com/problems/to-lower-case/) |
| Truncate Sentence                                 | [truncate_sentence_1816.py](string/truncate_sentence_1816.py)                                               | Done   | [1816](https://leetcode.com/problems/truncate-sentence/) |
| Uncommon Words from Two Sentences                 | [uncommon_words_from_two_sentences_884.py](string/uncommon_words_from_two_sentences_884.py)                                | Done   | [884](https://leetcode.com/problems/uncommon-words-from-two-sentences/) - Hashing  |
| Unique Morse Code Words                           | [unique_morse_code_words_804.py](string/unique_morse_code_words_804.py)                                                | Done   | [804](https://leetcode.com/problems/unique-morse-code-words/) - Set        |

</details>

<details>
<summary><strong>Tree 🌳</strong> (4 items)</summary>

| Program Name                      | Location                                                   | Status | Notes (LC #) |
| :-------------------------------- | :--------------------------------------------------------- | :----- | :----------- |
| Binary Tree Inorder Traversal     | [binary_tree_inorder_traversal_94.py](tree/binary_tree_inorder_traversal_94.py) | Done   | [94](https://leetcode.com/problems/binary-tree-inorder-traversal/) |
| Binary Tree Level Order Traversal | [binary_tree_level_order_traversal_102.py](tree/binary_tree_level_order_traversal_102.py)| Done | [102](https://leetcode.com/problems/binary-tree-level-order-traversal/) |
| Binary Tree Postorder Traversal   | [binary_tree_postorder_traversal_94.py](tree/binary_tree_postorder_traversal_94.py) | Done | [145](https://leetcode.com/problems/binary-tree-postorder-traversal/) |
| Binary Tree Preorder Traversal    | [binary_tree_preorder_traversal_144.py](tree/binary_tree_preorder_traversal_144.py)| Done | [144](https://leetcode.com/problems/binary-tree-preorder-traversal/) |

</details>

<details>
<summary><strong>Other Concepts 💡</strong> (10 items)</summary>

| Program Name                    | Location                                                       | Status | Notes         |
| :------------------------------ | :------------------------------------------------------------- | :----- | :------------ |
| Basic Loops Example             | [Loops/loops.py](Loops/loops.py)                               | Done   |               |
| Factorial                       | [recursion/factorial.py](recursion/factorial.py)               | Done   |               |
| Fibonacci                       | [recursion/fibonacci.py](recursion/fibonacci.py)               | Done   |               |
| Max in Array (Recursion)        | [recursion/max_in_an_array.py](recursion/max_in_an_array.py)         | Done   |               |
| Min in Array (Recursion)        | [recursion/min_in_an_array.py](recursion/min_in_an_array.py)         | Done   |               |
| Print Reverse String (Recursion)| [recursion/printReverseString.py](recursion/printReverseString.py)      | Done   |               |
| Print Array (Recursion)         | [recursion/print_elements_of_array.py](recursion/print_elements_of_array.py) | Done  |               |
| Print Array Reverse (Recursion) | [recursion/print_elements_of_array_reverse_order.py](recursion/print_elements_of_array_reverse_order.py) | Done |           |
| Python Profiling - Bottleneck   | [pythonprofiling/bottleneck_checking.py](Python Concepts/Python Profiling/bottleneck_checking.py) | Done | Example       |
| Python Profiling - Frequencies| [pythonprofiling/call_frequencies.py](Python Concepts/Python Profiling/call_frequencies.py)  | Done | Example       |
| Python Profiling - Time Check   | [pythonprofiling/optimization_time_check.py](Python Concepts/Python Profiling/optimization_time_check.py) | Done | Example       |

</details>

---

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    ```
2.  **Navigate:** Browse the directories based on the category you're interested in (e.g., `cd array`).
3.  **Run:** Execute the Python files directly using `python <filename>.py`. Check individual files for any specific usage notes or required inputs.

## Contributing

This repository is primarily for my personal learning and practice. However, constructive feedback, suggestions for optimizations, or bug reports are welcome! Please feel free to open an issue.

---
