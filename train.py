#!/usr/bin/env python
import pickle
def main():
        with open('cleaned_data.txt') as f:
                doc = f.readlines()
        reviewcount=len(doc)
        pos=neg=0
        for line in doc:
                if line[0]=='+':
                        pos=pos+1
                elif line[0]=='-':
                        neg=neg+1

        priorp=float(pos)/reviewcount
        priorn=float(neg)/reviewcount

        print (priorp,priorn)

        pickle.dump(doc,open( "model.pkl", "wb" ) )

main()
