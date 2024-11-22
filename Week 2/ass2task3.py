import pandas as pd

a = {'t1': -1.66, 't2': 0.30, 't3': -0.08, 't4': 0.10, 't5': -1.17, 't6': -0.05, 't7': 0.84, 't8': -0.66, 't9': 0.42, 't10': -0.99}
b = {'t1': 0.29, 't2': 0.89, 't3': 0.82, 't4': 0.97, 't5': 0.53, 't6': 0.83, 't7': 1.06, 't8': 0.67, 't9': 0.86, 't10': 0.51}

sera = pd.Series(data=a, index=['t1','t2','t3','t4','t5','t6','t7','t8','t9','t10'])
serb = pd.Series(data=b, index=['t1','t2','t3','t4','t5','t6','t7','t8','t9','t10'])

indexlist=['t1','t2','t3','t4','t5','t6','t7','t8','t9','t10']

# function to calculate manhatten distances
def man_dist(series1, series2):
    if series1.size == series2.size:
        result = []
        series1list = series1.to_list()
        series2list = series2.to_list()
        for i in range(0,series1.size-1):
            result = result + [abs(series1list[i] - series2list[i])]
        return sum(result)
    else:
        print("series not the same size, aborting")

# function to calculate max distance
def inf_dist(series1, series2):
    if series1.size == series2.size:
        result = []
        series1list = series1.to_list()
        series2list = series2.to_list()
        for i in range(0,series1.size -1):
            result = result + [abs(series1list[i] - series2list[i])]
        return max(result)
    else:
        print('series not the same size, aborting')

# task 1:
print('Results for task 1, calculating the distances for raw data:')

print('Manhatten Distance:')
print(man_dist(sera, serb))

print('Inf Distance:')
print(inf_dist(sera, serb))

# offset translation

def offset_translation(series, mean):
    result = []
    serieslist = series.to_list()
    for i in range(0,series.size):
        result = result + [(serieslist[i] - mean)]
    return pd.Series(result, index = indexlist)

sera_offset = offset_translation(sera, sera.mean())
serb_offset = offset_translation(serb, serb.mean())

print('Series A with offset translation:')
print(sera_offset)
print('Series B with offset translation:')
print(serb_offset)

sera_offset.name = 'A'
serb_offset.name = 'B'

amp_df = pd.merge(sera_offset,serb_offset,left_index=True,right_index=True)
plot = amp_df.plot(grid=True,figsize=(10,4),title='A and B with offset translation')
plot.set_xticks(range(len(amp_df)))
plot.set_xticklabels(["%s" % item for item in indexlist])
fig = plot.get_figure()
fig.savefig('plots/offset_translation.png')

print('Recalculating distances:')
print('Manhatten Distance:')
print(man_dist(sera_offset, serb_offset))
print('Inf Distance:')
print(inf_dist(sera_offset,serb_offset))

# amplitude scaling:
def amp_scaling(series):
    mean = series.mean()    # mean
    s = series.std()        # standard deviation
    result = []
    serieslist = series.to_list()
    for i in range(0,series.size):
        result = result + [(serieslist[i] - mean)/s]
    return pd.Series(result, index=indexlist)

sera_amp = amp_scaling(sera)
serb_amp = amp_scaling(serb)

print('Series A with amplitude scaling:')
print(sera_amp)
print('Series B with amplitude scaling:')
print(serb_amp)
print('Recalculate distances:')
print('Manhatten Distance:')
print(man_dist(sera_amp,serb_amp))
print('Inf Distance:')
print(inf_dist(sera_amp,serb_amp))

sera_amp.name = 'A'
serb_amp.name = 'B'

amp_df = pd.merge(sera_amp,serb_amp,left_index=True,right_index=True)
plot = amp_df.plot(grid=True,figsize=(10,4),title='A and B with amplitude scaling')
plot.set_xticks(range(len(amp_df)))
plot.set_xticklabels(["%s" % item for item in indexlist])
fig = plot.get_figure()
fig.savefig('plots/amplitude_scaling.png')