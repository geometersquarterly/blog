#!/usr/bin/env python
# coding: utf-8

# # Testing Interactive Plotting

# Let's render some maths:
# $
# \mathcal{L}_X \omega = \textbf{i}_X \textbf{d} \omega + \textbf{d} \textbf{i}_X \omega
# $

# In[1]:


import numpy as np
import plotly as ply
import plotly.graph_objects as go
from IPython.display import HTML, IFrame
from plotly.offline import init_notebook_mode, plot
init_notebook_mode(connected=True)


# In[2]:


def show(figure, local=False):
    ply.offline.plot(figure, filename="figure.html", auto_open=False)
    if local==True:
        display(IFrame("figure.html", width=800, height=800))
    else:
        display(HTML("figure.html"))


# In[3]:


## plotting torus

R = 2
r = 1

u, v = np.mgrid[0:2*np.pi:200j, 0:2*np.pi:200j]
x = (R+r*np.cos(v)) * np.cos(u)
y = (R+r*np.cos(v)) * np.sin(u)
z = r*np.sin(v)
torus = go.Surface(x=x, y=y, z=z)


# In[4]:


fig = go.Figure()
fig.add_trace(torus)
fig.update_traces(showscale=False)
fig.update_layout(
    scene = dict(
        xaxis = dict(
            color="rgb(255, 255, 255)",
            showbackground=False,
            showgrid = False,
            showspikes = False
        ),
        yaxis = dict(
            color="rgb(255, 255, 255)",
            showbackground=False,
            showgrid = False,
            showspikes = False
        ),
        zaxis = dict(
            color="rgb(255, 255, 255)",
            showbackground=False,
            showgrid = False,
            showspikes = False
        ))
    )


# In[5]:


show(fig)#local=True)

