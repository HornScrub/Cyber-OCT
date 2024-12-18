#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated
# https://linuxize.com/post/bash-case-statement/

read -p "How was your day? " ANSWER


while [ true ];do
    case $ANSWER in

    good | Good)
        echo -n "I'm glad you're having a good day!"
        break
        ;;

    bad | Bad)
        echo -n "I hope your day gets better!"
        break
        ;;

    okay)
        echo -n "That's fine!"
        break
        ;;
    *)
        echo  "I'm sorry, I don't understand!"
        read -p "How was your day? " ANSWER
        ;;
    esac
done
