import matplotlib.pyplot as plt
import requests


def plot_palette(model):
    """_summary_

    Args:
        model (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if model not in {"default", "ui"}:
        raise ValueError(f"{model} is not supported.")

    data = f'{{"model": "{model}"}}'

    response = requests.post("http://colormind.io/api/", data=data)
    palette = response.json()

    fig, axs = plt.subplots(figsize=(10, 2), nrows=1, ncols=5)

    for idx, color in enumerate(palette["result"]):
        color_decimal = [val / 256 for val in color]
        axs[idx].set_facecolor(color_decimal)

        axs[idx].set_title(color)
        axs[idx].set_xticks([])
        axs[idx].set_yticks([])

    return fig
