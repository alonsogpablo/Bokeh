__author__ = 'palonso0'
import pandas as pd
import json
from collections import defaultdict
from bokeh.plotting import figure, output_file, show,ColumnDataSource
from bokeh.models import HoverTool


cell = pd.read_csv('C:\\Desarrollo_Pablo\\Estad\\RSSI_HUA_Z6.csv',sep=',',decimal='.')


celda=cell['celda'].tolist()
rssi_media=cell['RSSI_media'].tolist()
persistencia=cell['persistencia'].tolist()

source = ColumnDataSource(
        data=dict(
            x=persistencia,
            y=rssi_media,
            desc=celda,
        )
    )

# output to static HTML file
output_file("C:\\Desarrollo_Pablo\\Estad\\rssi_hua3g.html")

TOOLS = [HoverTool()]

hover = HoverTool(
        tooltips=[
            ("PERSISTENCIA (DIAS):", "@x"),
            ("RSSI MEDIA", "@y"),
            ("CELDA", "@desc"),
            ])

p = figure(plot_width=800, plot_height=800, title='Persistencia RSSI', tools=[hover])

p.xaxis.axis_label = 'PERSISTENCIA (DIAS)'
p.yaxis.axis_label = 'RSSI MEDIA'

# add a circle renderer with a size, color, and alpha
p.circle('x', 'y', size=20, color="navy", alpha=0.5,source=source)

# show the results
show(p)


