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
	return ""

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
