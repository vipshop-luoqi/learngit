#!/usr/bin/env python3
# -*- coding: utf-8 -*-
students = {'Alian':76,'Bob':88,'Cathy':90,'Danieal':95,'Ella':100}
for key in students:
    print(key)
for value in students.values():
    print(value)
for k,v in students.items():
    print(k,v)
    
    
#sample2
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)


