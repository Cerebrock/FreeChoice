try:
    from Question import question_w_options
    r = question_w_options('TEMPS-A.txt', 2, '(.+)\s') 
    with open('Resultados TEMPS-A.txt', 'w+') as rs:
        rs.write('\n'.join(r))
except Exception as e:
    print(e)
    import time
    time.sleep(5)