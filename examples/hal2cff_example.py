# +
from hal2cff import hal2cff

import ipywidgets as widgets
from IPython.display import display, display_html
# -

# # hal2cff example


# +
button = widgets.Button(description="Convert")
url = widgets.Textarea(value = "https://hal.archives-ouvertes.fr/hal-01361430v1")
Box = widgets.HBox([url,button])
display(Box)

output = widgets.Output()
display(output)


# -

def run_and_display_query(_):
    result = hal2cff(url.value)
    with output:
        output.clear_output()
        display_html("<pre>" + result + "<\pre>", raw = True)


button.on_click(run_and_display_query)
