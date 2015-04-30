from os.path import join as opj

import pylab as pl
import numpy as np
from scipy.io import wavfile

genres = ['ambient', 'symphonic', 'country', 'rocknroll', 'metal']


def stimspecgram(fname):
    sr, wav = wavfile.read(fname)
    # specgram of mono sound (stereo avg)
    bins, freqs, Pxx, img = \
        pl.specgram(wav.mean(axis=1), Fs=sr, scale_by_freq=False,
                    vmin=0.0, vmax=100., cmap=pl.get_cmap('afmhot'),
                    aspect=1.333)
    pl.xlim((0.0, len(wav) / float(sr)))
    pl.ylim((0.0, 18000))
    ticks = np.arange(0, 20000, 5000)
    pl.yticks(ticks, ['%ik' % (a / 1000) if a else '0' for a in ticks])
    return img

fig = pl.figure(figsize=(10, 8))
count = 1
for i in range(5):
    for g, genre in enumerate(genres):
        pl.subplot(5, 5, count)
        count += 1
        p = stimspecgram(opj('stimuli', '%s_%.3i.wav' % (genre, i)))
        if not i:
            pl.title(genre.capitalize())
        if i < 4:
            p.get_axes().get_xaxis().set_visible(False)
        else:
            # last row
            pl.xlabel('Time in seconds')
            pass
        if g:
            p.get_axes().get_yaxis().set_visible(False)
        else:
            pl.ylabel('Stimulus %i' % i)
fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(p, cax=cbar_ax)
pl.savefig(opj('paper', 'pics', 'generated', 'stimulus_specgrams.svg'))
