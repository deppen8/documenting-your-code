import matplotlib.pyplot as plt
import requests
from matplotlib.figure import Figure


def plot_palette(model: str) -> Figure:
    """Display five color swatches side-by-side.

    Parameters
    ----------
    model : {"default", "ui"}
        Color set to use. ``"default"`` and ``"ui"`` are always available. Other color sets rotate.
        See `colormind.io/list <http://colormind.io/list/>`_ for current options.

    Returns
    -------
    Figure
        A plot of the complete 1 x 5 sequence of color patches.

    Raises
    ------
    ValueError
        When ``model`` is not one of ``{"default", "ui"}``.
    """
    # Validate model input values
    if model not in {"default", "ui"}:
        raise ValueError(f"{model} is not supported.")

    # Make query and turn response into dict or plain tezt.
    data = f'{{"model": "{model}"}}'
    response = requests.post("http://colormind.io/api/", data=data)
    palette = response.json()

    # Initialize matplotlib Figure object with 5 axes
    fig, axs = plt.subplots(figsize=(10, 2), nrows=1, ncols=5)

    # Plot each color from the palette on its own Axes object
    for idx, color in enumerate(palette["result"]):
        # Convert to correct color range for plotting
        color_decimal = [val / 256 for val in color]
        axs[idx].set_facecolor(color_decimal)

        # Add title and remove x and y ticks
        axs[idx].set_title(color)
        axs[idx].set_xticks([])
        axs[idx].set_yticks([])

    return fig
