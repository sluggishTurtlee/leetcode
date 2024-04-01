class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        I=1, II=2, III=3, IV=4, V=5, VI=6, VII=, VIII=8, VIIII=9, X=10
        '''
        four=s.count('IV')  #4
        nine=s.count('IX')  #9
        xl=s.count('XL')    #40
        xc=s.count('XC')    #90
        cd=s.count('CD')    #400
        cm=s.count('CM')    #900
        i=s.count('I')
        v=s.count('V')
        x=s.count('X')
        l=s.count('L')
        c=s.count('C')
        d=s.count('D')
        m=s.count('M')

        value=(four*4 + nine*9 + xl*40 + xc*90 + cd*400 + cm*900
         + i*1 + v*5 + x*10 + l*50 + c*100 + d*500 + m*1000
         - four*6 - nine*11 - xl*60 - xc*110 - cd*600 - cm*1100)

        return value
