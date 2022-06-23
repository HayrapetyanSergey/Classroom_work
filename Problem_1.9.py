def bank(a):
    frs_year = a + ((a * 4) / 100 )
    sec_year = frs_year + ((frs_year * 4) / 100)
    thr_year = sec_year + ((sec_year * 4) / 100)
    return  (f'1st year is ${frs_year}' ,f'2nd year is ${sec_year}', f'3th year is ${thr_year}')


money = float(input("The amount you invested is $"))
print(bank(money))