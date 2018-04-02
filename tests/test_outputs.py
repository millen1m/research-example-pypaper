import matplotlib
matplotlib.use('agg')
from matplotlib.testing.decorators import image_comparison


# On first run copy the file from /Applications/PyCharm.app/Contents/bin/result_images/test_outputs/

@image_comparison(baseline_images=['comparison_of_footing_capacities'], extensions=['png'])
def test_figure_comparison_of_footing_capacities():
    from ep_scripts.outputs.figure_comparison_of_footing_capacities import create
    create()


if __name__ == '__main__':
    test_figure_comparison_of_footing_capacities()