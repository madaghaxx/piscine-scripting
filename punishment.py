def do_punishment(first_part, second_part, nb_lines):
    res = ""
    for _ in range(nb_lines):
        res += first_part.strip() + " " + second_part.strip() + ".\n"
    return res.rstrip('\n')