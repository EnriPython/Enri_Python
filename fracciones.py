#!/usr/bin/env python
# -*- coding: utf-8 -*-
     
from fractions import gcd
 
   
print"#### OPERACIONES CON FRACCIONES ####\n"     
class Fraccion(object):
    __slots__ = ['num', 'den']
     
    def __init__(self, num, den=1):
        self.num = num
        self.den = den
     
    def entrada(self):
        frac = raw_input('Introduce una fracción <numerador/denominador>:\n')
        if '/' not in frac:
            frac = frac + '/1'
        l1 = frac.rsplit('/')
        self.num = int(l1[0])
        self.den = int(l1[1])
        if self.num < 0 and self.den < 0:
            self.num = -self.num
            self.den = -self.den
        elif self.num > 0 and self.den < 0:
            self.num = -self.num
            self.den = -self.den
        l1 = []
     
    def __mul__(self, frac):
        mult = Fraccion(self.num, self.den)
        mult.num = self.num * frac.num
        mult.den = self.den * frac.den
        mult = mult.simplifica()
        return mult
     
    __rmul__ = __mul__
     
    def __div__(self, frac):
        divi = Fraccion(self.num, self.den)
        frac = ~frac
        divi = divi * frac
        divi = divi.simplifica()
        return divi
     
    __rdiv__ = __div__
     
    def __pow__(self, exp):
        pot = Fraccion(self.num, self.den)
        pot.num = self.num ** exp
        pot.den = self.den ** exp
        pot = pot.simplifica()
        return pot
     
    def __add__(self, frac):
        suma = Fraccion(self.num, self.den)
        if self.den == frac.den:
            suma.num = self.num + frac.num
            suma = suma.simplifica()
            return suma
        else:
            mcm1 = suma.mcm(self.den, frac.den)
            suma.num = (mcm1 / self.den) * self.num +\
            (mcm1 / frac.den) * frac.num
            suma.den = mcm1
            suma = suma.simplifica()
            return suma
     
    __radd__ = __add__
     
    def __sub__(self, frac):
        resta = Fraccion(self.num, self.den)
        frac = -frac
        resta = resta + frac
        resta = resta.simplifica()
        return resta
     
    __rsub__ = __sub__
     
    def __neg__(self):
        op = Fraccion(self.num, self.den)
        op.num = -self.num
        op.den = self.den
        return op
     
    def __invert__(self):
        inv = Fraccion(self.num, self.den)
        inv.num = self.den
        inv.den = self.num
        return inv
     
    def __abs__(self):
        absoluto = Fraccion(self.num, self.den)
        if self.num > 0 and self.den > 0:
            return absoluto
        elif self.num < 0:
            absoluto.num = -self.num
            return absoluto
        elif self.den < 0:
            absoluto.den = -self.den
            return absoluto
     
    def mcm(self, a, b):
        mincm = (a * b) / gcd(a, b)
        return mincm
     
    def __lt__(self, frac):
        c1 = self.num * frac.den
        c2 = self.den * frac.num
        if c1 < c2:
            return "VERDADERO"
        else:
            return "FALSO"
     
    def __le__(self, frac):
        c1 = self.num * frac.den
        c2 = self.den * frac.num
        if c1 <= c2:
            return "VERDADERO"
        else:
            return "FALSO"
     
    def __eq__(self, frac):
        c1 = self.num * frac.den
        c2 = self.den * frac.num
        if c1 == c2:
            return 'SON FACCIONES EQUIVALENTES'
        else:
            return 'NO SON FRACCIONES EQUIVALENTES'
     
    def __ne__(self, frac):
        c1 = self.num * frac.den
        c2 = self.den * frac.num
        if c1 != c2:
            return "VERDADERO"
        else:
            return "FALSO"
     
    def __gt__(self, frac):
        c1 = self.num * frac.den
        c2 = self.den * frac.num
        if c1 > c2:
            return "VERDADERO"
        else:
            return "FALSO"
     
    def __ge__(self, frac):
        c1 = self.num * frac.den
        c2 = self.den * frac.num
        if c1 >= c2:
            return "VERDADERO"
        else:
            return "FALSO"
     
    def simplifica(self):
        simp = Fraccion(self.num, self.den)
        mcd = gcd(self.num, self.den)
        simp.num = self.num / mcd
        simp.den = self.den / mcd
        return(simp)
     
    def __repr__(self):
        if self.num == self.den:
            return('1')
        elif self.den == 1:
            return('{}'.format(self.num))
########elif self.num &gt; 0 and self.den &lt; 0:
            return('{}/{}'.format(-self.num, -self.den))
        else:
            return('{}/{}'.format(self.num, self.den))
     
     
p = Fraccion(0, 0)
q = Fraccion(0, 0)
     
Fraccion.entrada(p)
Fraccion.entrada(q)
     
     
print('MULTIPLICACION = {}'.format(p * q))
print('DIVISION = {}'.format(p / q))
print('SUMA = {}'.format(p + q))
print('RESTA = {}'.format(p - q))
print ""
print('COMPARACIONES:\n')
print('{} < {} : {}'.format(p, q, p < q))
print('{} <= {} : {}'.format(p, q, p <= q))
print('{} y {} : {}'.format(p, q, p == q))
print('{} ES DISTINTA DE {} : {}'.format(p, q, p != q))
print('{} > {} : {}'.format(p, q, p > q))



