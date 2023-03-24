
# 여기서는 미리 주어진 시계열 데이터를 기반으로 time series chart를 그리는 방법을 설명한다.
# http://ymkimit.blogspot.com/2014/07/matplotlib-time-series.html

import datetime as dt
import matplotlib.pyplot as plt

# 차트를 그릴 canvas를 준비한다
# Preparation
fig = plt.figure(figsize=(16,3))

# 시간과 값으로 구성된 데이터를 준비하고 x, y축에 해당하는 리스트를 생성한다.
plot_data = [
    ["2013-03-18 15:31:36.617",0],
    ["2013-03-18 15:31:38.511",15],
    ["2013-03-18 15:31:40.324",30],
    ["2013-03-18 15:31:42.144",35],
    ["2013-03-18 15:31:43.961",60]
]

# plot data
x,y = [],[]

# 두번째 줄에서는 strptime를 이용하여 문자열을 컴퓨터가 인식할 수 있는 시간 포맷으로 변경한다.
# 이후 두 줄에서 x,y축에 데이터를 입력한다.
for line in plot_data:
    times = dt.datetime.strptime(line[0],'%Y-%m-%d %H:%M:%S.%f')
    x.append(times)
    y.append(line[1])

# 차트에 x,y 데이터를 내부적으로 표시한다
#plt.plot(x,y,'o-', label="value")
plt.plot(x,y,linestyle='-', marker='o', label="value")

plt.xlabel('time')
plt.legend(loc=2)
plt.show()