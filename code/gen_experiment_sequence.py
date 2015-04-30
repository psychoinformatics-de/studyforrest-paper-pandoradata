# -*- coding: utf-8 -*-

import random
import copy

# genre association per run
stimuli = {
    'ambient': [4, 5, 7, 16, 25],
    'rocknroll': [3, 12, 17, 18, 20],
    'metal': [6, 10, 11, 13, 22],
    'symphonic': [2, 8, 14, 15, 21],
    'country': [1, 9, 19, 23, 24]
}

# genre order (code mapping) per run
genre_seq = [
    ['ambient', 'rocknroll', 'metal', 'symphonic', 'country'],
    ['symphonic', 'rocknroll', 'metal', 'country', 'ambient'],
    ['country', 'metal', 'symphonic', 'rocknroll', 'ambient'],
    ['rocknroll', 'ambient', 'country', 'metal', 'symphonic'],
    ['country', 'ambient', 'rocknroll', 'metal', 'symphonic'],
    ['country', 'ambient', 'symphonic', 'rocknroll', 'metal'],
    ['rocknroll', 'metal', 'country', 'ambient', 'symphonic'],
    ['rocknroll', 'country', 'symphonic', 'ambient', 'metal']
]

# debruijn sequences per run (level2-counterbalanced)
category_seq = [
    [0,4,2,4,1,3,3,2,2,3,4,4,3,1,2,0,3,0,1,4,0,2,1,1,0],
    [0,4,0,1,0,2,3,1,3,0,3,4,4,3,3,2,4,2,1,4,1,1,2,2,0],
    [0,4,3,4,4,0,2,4,2,3,0,3,2,1,2,2,0,1,3,3,1,1,4,1,0],
    [0,4,4,0,3,4,2,0,2,1,0,1,4,3,3,1,2,3,2,2,4,1,1,3,0],
    [0,4,3,0,1,3,4,1,4,4,0,3,1,1,0,2,3,3,2,2,1,2,4,2,0],
    [0,4,1,2,0,3,2,2,3,4,3,3,1,1,4,0,2,4,4,2,1,3,0,1,0],
    [0,4,0,1,4,2,2,3,3,2,4,4,3,1,1,3,0,2,0,3,4,1,2,1,0],
    [0,4,2,1,1,3,0,1,2,4,4,0,2,0,3,1,4,3,3,2,2,3,4,1,0],
]

question_objects = [
    "Gitarren?",
    "schnelles Tempo?",
    "Pianos?",
    "Gesang?",
    "mehr als ein Instrument?",
    "Violinen?",
    "Schlaginstrumente?",
    "eine fröhliche Melodie?",
    "menschliche Stimmen?",
    "eine Sängerin?",
    "eine Trompete?",
    "eine sanfte Melodie?",
    "einen schnellen Rythmus?",
    "hohe Töne?"
]

delay_steps = [4,6,6,6,8]

def gen_run(nmbr):
    seq = category_seq[nmbr]
    genre_codes = genre_seq[nmbr]
    genre_delay = {}
    run_stim = {}
    questions = copy.deepcopy(question_objects)
    random.shuffle(questions)
    ofile = open('run%i.csv' % nmbr, 'w')
    ofile.write('run,genre,stim,delay,catch,question\n')
    # for all genres
    for g in stimuli:
        # create random delay order per genre
        gd = copy.deepcopy(delay_steps)
        random.shuffle(gd)
        genre_delay[g] = gd
        # create random stim order per genre
        so = copy.deepcopy(stimuli[g])
        random.shuffle(so)
        run_stim[g] = so
    # generate trials
    for s in seq:
        g = genre_codes[s]
        stim = run_stim[g].pop()
        delay = genre_delay[g].pop()
        if delay == 8:
            catch = 1
            catch_question = questions.pop()
        else:
            catch = 0
            catch_question = ''
        ofile.write('%s,"%s","%.3i.wav",%i,%i,"%s"\n' \
                    % (nmbr, g, stim, delay, catch, catch_question))
    ofile.close()

for i in range(8):
    gen_run(i)
