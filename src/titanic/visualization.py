import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def plot_age_distribution(data: pd.DataFrame):
    fig = plt.figure(figsize=(12, 8))
    gs = fig.add_gridspec(3, 1)
    gs.update(hspace=-0.55)

    axes = list()
    colors = ["#022133", "#5c693b", "#51371c"]

    for idx, cls, c in zip(range(3), sorted(data["Class"].unique()), colors):
        axes.append(fig.add_subplot(gs[idx, 0]))

        # you can also draw density plot with matplotlib + scipy.
        sns.kdeplot(
            x="Age",
            data=data[data["Class"] == cls],
            fill=True,
            ax=axes[idx],
            cut=0,
            bw_method=0.25,
            lw=1.4,
            edgecolor="lightgray",
            hue="Survived",
            multiple="stack",
            palette="PuBu",
            alpha=0.7,
        )

        axes[idx].set_ylim(0, 0.04)
        axes[idx].set_xlim(0, 85)

        axes[idx].set_yticks([])
        if idx != 2:
            axes[idx].set_xticks([])
        axes[idx].set_ylabel("")
        axes[idx].set_xlabel("")

        spines = ["top", "right", "left", "bottom"]
        for s in spines:
            axes[idx].spines[s].set_visible(False)

        axes[idx].patch.set_alpha(0)
        axes[idx].text(
            -0.2,
            0,
            f"Class {cls}",
            fontweight="light",
            fontfamily="serif",
            fontsize=11,
            ha="right",
        )
        if idx != 1:
            axes[idx].get_legend().remove()

    fig.text(
        0.13,
        0.81,
        "Age distribution by Class in Titanic",
        fontweight="bold",
        fontfamily="serif",
        fontsize=16,
    )

    plt.show()


def plot_correlation_matrix(data: pd.DataFrame) -> pd.DataFrame:
    corr = data.corr(numeric_only=True)
    _, ax = plt.subplots(1, 1, figsize=(7, 7))

    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    sns.heatmap(
        corr,
        square=True,
        mask=mask,
        linewidth=2.5,
        vmax=0.4,
        vmin=-0.4,
        cmap=cmap,
        cbar=False,
        ax=ax,
    )

    ax.set_yticklabels(
        ax.get_xticklabels(), fontfamily="serif", rotation=0, fontsize=11
    )
    ax.set_xticklabels(
        ax.get_xticklabels(), fontfamily="serif", rotation=90, fontsize=11
    )

    plt.tight_layout()
    plt.show()
