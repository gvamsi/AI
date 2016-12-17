"""

Question 1: In test cases where is Pacman boxed in (which is to say, he is unable to change his observation point),
why does Pacman sometimes have trouble finding the exact location of the ghost?

Solution: From the current location (boxed) pacman cannot get enough inofrmation to converge on the ghost's location.
There are 4 possible location but we cannot decide on the direction and hence there is trouble finding the exact location of
ghost.

Question 2: For which of the test cases do you notice differences emerging in the shading of the squares?
Can you explain why some squares get lighter and some squares get darker?

Solution: In this scenario pacman knows how the ghosts move. Since the ghost moves to the south, after certain iterations
the ghost is in the southern part of the board.
The differnece in colors is noticed in test cases
2-ExactElapse.test and 3-ExactElapse.test

As the belief increases the probability increase and higher probability means lighter color and lower probabiltiy means
darker color.

Question 3: Notice the difference between test 1 and test 3. In both tests, pacman knows that the ghosts will move to the
sides of the gameboard. What is different between the tests, and why?

Solution: In test case 1 Pacman has to converge based on the movements of the ghost (the elapse alone). The distance
measures are not known.

In test case 3 Pacman has knowledge of both the movements and distance (elapse and observe)
"""
