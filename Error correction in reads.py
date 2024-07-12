# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:39:43 2024

@author: gbulb
"""
dict_of_strings={'Rosalind_52':'TCATC','Rosalind_44':'TTCAT','Rosalind_68':'TCATC','Rosalind_28':'GATGA','Rosalind_95':'GAGGA','Rosalind_66':'TTTCA','Rosalind_33':'ATCAA','Rosalind_21':'TTGAT','Rosalind_18':'TTTCC'}

class finding_pairs:
     def point_mutations(dict_of_strings):
         dict_for_differences={}
         for key1 in dict_of_strings.keys():
             for key2 in dict_of_strings.keys():
                 if key1!=key2:
                     j=0
                     for i in range(len(dict_of_strings[key1])):
                         if dict_of_strings[key1][i]!=dict_of_strings[key2][i]:
                            j+=1
                     if (key2,key1) not in dict_for_differences.keys():
                        dict_for_differences[((key1,key2))]=j
         return dict_for_differences
     def point_mutations_equal_to_1(dict_for_differences):
         for key in dict_for_differences.keys():
             if dict_for_differences[key]==1:
                print(f'{dict_of_strings[key[0]]}-->{dict_of_strings[key[1]]}')

                      
if __name__=="__main__":
   dict_for_differences=finding_pairs.point_mutations(dict_of_strings)
   finding_pairs.point_mutations_equal_to_1(dict_for_differences)
   
               
                       
    
    