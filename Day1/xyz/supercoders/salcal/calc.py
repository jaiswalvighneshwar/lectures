from abc import ABCMeta,abstractmethod
from invalid_day_error import InvalidDaysError

class SalariedIndividual(object):

    __metaclass__ = ABCMeta      #ths is done to set the class as abstract class
    @abstractmethod             #this makes the method\function abstract
    def get_days(self):
        pass
    @abstractmethod
    def get_cost(self):
        pass

class SalCal(object):
        @staticmethod
        def calc(salaried_individual):
            if isinstance(salaried_individual,SalariedIndividual):
	      try:
		print 'Sal cal Begins'
	    	days = salaried_individual.get_days()
	
   		if days < 0:
		  raise ValueError()
		if days > 25:
		  raise InvalidDaysError('No more working')	

                cost = salaried_individual.get_cost()

                PROFESSIONAL_TAX = 200
                taxable_income = days * cost
                income_on_hand = taxable_income - 0.1 * taxable_income
		print 'Salcal returns'
                return income_on_hand - PROFESSIONAL_TAX
	      finally: 
		print 'sal call end' 

            else:
                #print "Not Eligible!! Check object passed"
		raise TypeError('Pass in Salaried Individual')
