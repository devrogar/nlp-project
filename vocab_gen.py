#!/usr/bin/env python
import sys
def main():
        with open('cleaned_data.txt') as f:
                lines = f.readlines()
        one=[]
        two=[]
        
        target=open("vocabulary.txt", 'w')

        for line in lines:
                line = line.strip().split(" ")
                for word in line:
                        if word.isalpha():
                                if word not in one:
                                        one.append(word)
                                elif word not in two:
                                        two.append(word)
        two.sort()
        for word in two:
                target.write(word+'\n')
        target.close()
main()
