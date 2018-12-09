from stringshifter.utils import check_divisibility,check_string_validity,check_num,shift_string,map_case,convert_to_input_case,join_string
from stringshifter.patterns import *
import sys
class StringShifter:
    #class level attribute could be changed to user input but not mentioned
    divisibility=3
    RC="CONTIGUOUS PATTERN RUN RECURSIVELY"
    RNC="CONTIGUOUS PATTERN RUN NON RECURSIVELY"
    NRNC="NON CONTIGUOUS PATTERN RUN NON RECURSIVELY"
    NRC="NON CONTIGUOUS PATTERN RUN RECURSIVELY"
    def __init__(self,S,C,N):
        self.S=S
        self.C=C
        self.N=N
        self.check_preconditions()
        self.Cshift = self.get_shift()
        self.divide_S()


    def get_shift(self):
        c = map_case(self.C)
        return  convert_to_input_case(shift_string(self.C,self.N),c)
    def divide_S(self):
        len_S = get_len(self.S)
        one_three= int(len_S/3)
        self.S_first = self.S[0:one_three]
        self.S_second= self.S[one_three:]

    def check_preconditions(self):
        check_num(self.N)
        check_divisibility(self.S,StringShifter.divisibility)
        check_string_validity(self.S)
        check_string_validity(self.C)

    def run_non_recursive_contiguous(self):

        self.S_replaced= pattern_replace_non_recursive(self.S_first,self.S_second,self.C,self.Cshift)
        self.print_out(StringShifter.RNC)

    def run_recursive_contiguous(self):
        self.S_replaced = pattern_replace_recursive(self.S_first, self.S_second, self.C, self.Cshift)
        self.print_out(StringShifter.RC)
    def run_non_recursive_non_contiguous(self):
        self.S_replaced= non_contigious_right_replace_non_recursive(self.S_first,self.S_second,self.C,self.Cshift)
        self.print_out(StringShifter.NRNC)

    def print_out(self,algo):
        print(algo)
        print("----------------------------------------")
        print("C:      {}".format(self.C))
        print("CShift: {}".format(self.Cshift))
        print("S:      {}".format(self.S))
        print("SShift: {}".format(self.S_replaced))
        print("----------------------------------------")

def run_shifter(S,C,N,noncont):
    try:
        s = StringShifter(S,C,N)
        if noncont:
            s.run_non_recursive_non_contiguous()
        else:
            s.run_non_recursive_contiguous()
            s.run_recursive_contiguous()
    except Exception as e:
        print("Error: {}".format(str(e)))
        print("\n")
        #print(str(e))

def main(**kwargs):
    try:
        if not kwargs:
            print("String Shifter")
            print("---------------")
            while True:

                S=input("Enter S: ").strip()
                C=input("Enter C: ").strip()
                N= int(input("Enter N: "))
                R= True if input("Non Contigious Pattern (y|n)?: ").lower()=="y" else False
                run_shifter(S,C,N,R)

        else:
            S= kwargs['S']
            C= kwargs['C']
            N= int(kwargs['N'])
            R= True if (kwargs['R']).lower()=="y" else False
            run_shifter(S, C, N, R)
    except KeyboardInterrupt:
        print("\n")
        print("Exiting")
        return 0
    except Exception as e:
        print("\n")
        print('Unrecoverable Error')
        print(str(e))
        return 1



if __name__=="__main__":
    if sys.argv:
        main(**dict(arg.split('=') for arg in sys.argv[1:]))
    else:
        main()