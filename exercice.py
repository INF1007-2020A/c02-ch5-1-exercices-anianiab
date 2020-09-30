#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	TAX_RATE = 0,15

	#Calculez sous total
	somme = 0
	for item in data:
    		somme += item[INDEX_PRICE] * item[INDEX_QUANTITY]
			
	#Calcultez taxes et total
	taxes = 0,15 * somme
	total = somme + taxes
	

	# retournez la facture formatée
	result = name
	result += "\n" + "SOUS-TOTAL {SOMME : > 10.2f} $"
	result += "\n" + " TAXES {taxes : > 10.2f} $"
	result += "\n" + " TOTAL {total : > 10.2f} $"

	return ""


def format_number(number, num_decimal_digits):
    	#separer les parties entiere et decimale
	decimal_part = abs(number) % 1.0
	whole_part = int(abs(number))

		# formater la partie decimale
	decimal_str = f"(decimal_part :.(num_decimal_digits)f)"[1:]
	# 0,12345 = 1.123 => arrondir
	decimal_part = "." + str(int(round(decimal_part * 10**num_decimal_digits)))



		# formater la partie entiere
	whole_part = ""
	while whole_part >= 1000:
    		digits = whole_part % 1000
			digits_str = f" {digits :0>3}"
			whole_part_str = digits_str + whole_part_str
			whole_part //= 1000
		whole_part_str = str(whole_part) + whole_part_str


		# concatener les deux parties)
    	
	return ("-" if number < 0) + whole_part_str

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
