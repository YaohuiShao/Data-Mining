# Task 6
Using the three-word sequence counts you found in task 4, find the entropy of words for each two-word context. For a given two-word context, the entropy of the next word is given as
H(c) = ? p(w | c) · log2 (p(w | c))
  w?followers(c)

where H(c) is the entropy of context c, followers(c) are the words which were seen to follow context c and p(w | c) is the probability that the word w follows context c and is defined as
p(w | c) = count(c w)/?w??followers(c) count(c w' )

For example, consider the following three-word sequences with their respective counts:
Sequence                            Count
big green apple				7
big green pear 				4
big green watermelon   		3
small red apple 			1
small red car 				2
tiny grey mouse			5

There are three contexts: big green, small red and tiny grey. The context big green can be followed by apple, pear or watermelon. The context small red can be followed by apple or car and the context tiny grey can be only followed by mouse. The probability of a word depends on the context. For example, the probability of apple in the context big green is:

p(apple | big green) = 7 /(7+4+3)= 1/2
whilst in the context of small red it is:p(apple | small red) = 1/(1+2) = 1/3
The entropy of words for the context big green would be:
H(big green) = -(1/2)	·log2(1/2) - (2/7)·log2(2/7) - (3/14)·log2(3/14)

Finally, the output for the given example counts would be:
big green   1.4926small red    0.9183tiny grey     0

In your output, you are not required to round your entropy values to a specific number of decimal digits.