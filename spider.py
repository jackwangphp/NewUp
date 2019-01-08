from pyquery import PyQuery as pq


Comic = pq(url='https://www.tohomh.com/quanzhifashi/')
print(Comic('#detail-list-select-1 > li:nth-child(1) > a'))
