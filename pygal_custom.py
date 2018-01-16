# Adapted from : https://stackoverflow.com/questions/36322683/pygal-charts-not-displaying-tooltips-in-jupyter-ipython-notebook
from IPython.display import display, HTML
import pygal
import palettable

# Define raw HTML template for the notebook
base_html = """
<!DOCTYPE html>
<html>
  <head>
  <meta charset="UTF-8">
  <script type="text/javascript" src="http://kozea.github.com/pygal.js/javascripts/svg.jquery.js"></script>
  <script type="text/javascript" src="https://kozea.github.io/pygal.js/2.0.x/pygal-tooltips.min.js""></script>
  </head>
  <body>
    <figure>
      {rendered_chart}
    </figure>
  </body>
</html>
"""


def galplot(chart):
    rendered_chart = chart.render()
    plot_html = base_html.format(rendered_chart=rendered_chart)
    display(HTML(plot_html))

# Custom CSS for pygal
custom_css = '''
  {{ id }}.axis .line{
    stroke: none;
  }
  {{ id }}.tooltip .value{
    font-size: 10pt;
  }
  {{ id }}.tooltip .legend{
    font-size: 10pt;
  }
  {{ id }}.tooltip .x_label{
    font-size: 10pt;
  }
'''

custom_css_file = '/tmp/pygal_custom_style.css'
with open(custom_css_file, 'w') as f:
  f.write(custom_css)
config = pygal.Config(fill=True, interpolate='cubic')
config.css.append('file://' + custom_css_file)


# Custom style for pygal
custom_style = pygal.style.Style(background='transparent',
                                 plot_background='white',
                                 font_family='Lato, Arial',
                                 opacity='.6',
                                 opacity_hover='.9',
                                 transition='400ms ease-in',
                                 guide_stroke_dasharray='4,0',
                                 major_guide_stroke_dasharray='4,0',
                                 label_font_size=15,
                                 major_label_font_size=15,
                                 value_font_size=10,
                                 value_label_font_size=10,
                                 tooltip_font_size=10,
                                 title_font_size=20,
                                 legend_font_size=15,
                                 no_data_font_size=64,
                                 colors=palettable.cartocolors.qualitative.Bold_10.hex_colors,
                                 guide_stroke_color='#D3D3D3',
                                 major_guide_stroke_color='#D3D3D3')
