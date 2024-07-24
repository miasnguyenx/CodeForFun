
def garage(initial, final):
    seq = []
    steps = 0
    while initial != final:
        zero_initial_pos = initial.index(0) #3
        if zero_initial_pos != final.index(0): # 3 != 0
            car_to_move = final[zero_initial_pos] # move 2
            pos_to_move = initial.index(car_to_move)
            initial[zero_initial_pos], initial[pos_to_move] = initial[pos_to_move], initial[zero_initial_pos]
        else:
            for i in range(len(initial)):
                if initial[i] != final[i]:
                    initial[zero_initial_pos], initial[i] = initial[i], initial[zero_initial_pos]
                    break
        seq.append(initial)
        steps += 1
    return steps, seq

initial = [1,2,3,0,4]
final = [0,1,2,3,4]

print(garage(initial, final))
