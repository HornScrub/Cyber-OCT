#!/bin/bash

# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.

# scalene - no sides are equal
# equilateral - all sides are equal
# isoceles - only 2 sides are equal

# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.

# Input Format
# Three integers, each on a new line.

# get three integers from the user, and store them in 3 seperate variables

# a, b, c
# a = b, b = c

echo "Enter length of side 1: "
read side1
echo "Enter length of side 2: "
read side2
echo "Enter length of side 3: "
read side3

# Hint &&(and) ||(or)

            # TRUE           #FALSE
if [ $side1 -eq $side2 ] && [ $side2 -eq $side3 ]; then
    echo "EQUALATERAL"
elif [ $side1 -eq $side2 ] || [ $side2 -eq $side] || [ $side1 -eq $side3 ]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi


# if side1 = side2, but side2 != side3 AND side1 != side3


    # blah blah
# else   #SCALENE
    # blah blah
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).
# Hint &&(and) ||(or)