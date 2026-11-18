"""Rebuild Figs. 1, 4, 6 from attributed published images and reported data.

Dependencies: reportlab, Pillow, matplotlib. See figures/ATTRIBUTION.md.
No restoration model is run; no image detail or metric value is synthesized.
"""
from pathlib import Path
import csv

from PIL import Image, ImageFilter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'figures'
ASSETS = OUT / 'source_assets'
WIDTH = 516


def begin(name, height):
    c = canvas.Canvas(str(OUT / (name + '.pdf')),
                      pagesize=(WIDTH, height), pageCompression=1, invariant=1)
    c.setTitle(name.replace('_', ' ').title())
    c.setAuthor('Survey authors; source artwork credited in the caption')
    return c


def text(c, height, x, top, label, size=9, bold=False, center=False):
    c.setFillColorRGB(.10, .12, .14)
    c.setFont('Times-Bold' if bold else 'Times-Roman', size)
    draw = c.drawCentredString if center else c.drawString
    draw(x, height - top - size, label)


def picture(c, height, source, x, top, width):
    im = Image.open(ASSETS / source) if isinstance(source, str) else source
    ph = width * im.height / im.width
    c.drawImage(ImageReader(im), x, height - top - ph, width, ph, mask='auto')
    return ph


def temporal_profile_without_author_label():
    """Remove only the yellow '(ours)' annotation; retain the source unchanged.

    Interpolation is confined to the annotation glyphs and their JPEG edges.
    Pixels obscured by that label are cosmetic fill, not recovered measurements.
    """
    import numpy as np

    im = Image.open(ASSETS / 'stablevsr_S5_F6_0.jpg').convert('RGB')
    box = (908, 580, 1034, 628)
    patch = np.asarray(im.crop(box)).copy()
    r, g, b = patch.astype(float).transpose(2, 0, 1)
    yellow = (r > 140) & (g > 140) & (b < 150) & (r + g - 2 * b > 170)
    mask = np.asarray(Image.fromarray(yellow.astype('uint8') * 255)
                      .filter(ImageFilter.MaxFilter(5))) > 0
    values = patch.astype(float)
    known = ~mask
    # Seed each masked pixel from its nearest available local neighbors.
    while not known.all():
        p = np.pad(values * known[..., None], ((1, 1), (1, 1), (0, 0)))
        k = np.pad(known.astype(float), 1)
        count = k[:-2, 1:-1] + k[2:, 1:-1] + k[1:-1, :-2] + k[1:-1, 2:]
        total = p[:-2, 1:-1] + p[2:, 1:-1] + p[1:-1, :-2] + p[1:-1, 2:]
        frontier = ~known & (count > 0)
        values[frontier] = total[frontier] / count[frontier, None]
        known[frontier] = True
    for _ in range(300):
        p = np.pad(values, ((1, 1), (1, 1), (0, 0)), mode='edge')
        average = (p[:-2, 1:-1] + p[2:, 1:-1] + p[1:-1, :-2] + p[1:-1, 2:]) / 4
        values[mask] = average[mask]
    patch[mask] = np.clip(np.rint(values[mask]), 0, 255).astype('uint8')
    im.paste(Image.fromarray(patch), box)
    return im


def qualitative_examples():
    height = 427
    c = begin('tradeoff', height)
    text(c, height, 0, 0, '(a) Spatial reconstruction: a matched REDS30 example', 10, True)
    # Original PDF context, including its yellow ROI; exclude old caption only.
    context = Image.open(ASSETS / 'upscale_reds30_wall_labeled_group.png').crop((7, 8, 334, 193))
    picture(c, height, context, 0, 19, 110)
    text(c, height, 55, 85, 'Scene and detail region', 8.2, center=True)
    crops = [('bicubic', 'Bicubic'), ('stablesr', 'StableSR'),
             ('sdx4', 'SD x4 Upscaler'), ('realbasicvsr', 'RealBasicVSR'),
             ('upscale_a_video', 'Upscale-A-Video'), ('gt', 'Reference')]
    crop_width = 62
    for i, (suffix, label) in enumerate(crops):
        x = 120 + i * 66
        picture(c, height, 'upscale_reds30_wall_' + suffix + '.png', x, 19, crop_width)
        text(c, height, x + crop_width / 2, 85, label, 8.1, center=True)
    text(c, height, 0, 108, '(b) Temporal reconstruction: matched profiles from REDS4 sequence 000', 10, True)
    picture(c, height, temporal_profile_without_author_label(), 22, 124, 472)
    c.showPage()
    c.save()


def temporal_architectures():
    height = 460
    c = begin('temporal_mechanisms', height)
    text(c, height, 0, 0, '(a) StableVSR: motion-compensated temporal texture guidance', 10, True)
    picture(c, height, 'stablevsr_S4_F2_0.png', 0, 17, WIDTH)
    c.setStrokeColorRGB(.75, .78, .80)
    c.setLineWidth(.5)
    c.line(0, height - 214, WIDTH, height - 214)
    text(c, height, 0, 222, '(b) Upscale-A-Video: local temporal modules and global latent propagation', 10, True)
    picture(c, height, 'upscale_pipeline_github.png', 0, 240, WIDTH)
    # Height follows the source aspect ratio; no architecture blocks are redrawn.
    c.showPage()
    c.save()


def metric_correlations():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    from matplotlib.lines import Line2D

    times = Path('C:/Windows/Fonts/times.ttf')
    if times.exists():
        font_manager.fontManager.addfont(str(times))
    plt.rcParams.update({'font.family': 'serif',
                         'font.serif': ['Times New Roman', 'DejaVu Serif'],
                         'font.size': 8.3, 'pdf.fonttype': 42, 'ps.fonttype': 42})
    with (ROOT / 'research/metric_study_table1.csv').open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 30
    fig = plt.figure(figsize=(WIDTH / 72, 345 / 72), facecolor='white')
    axes = [fig.add_axes([.145, .12, .325, .76]),
            fig.add_axes([.64, .12, .325, .76])]
    blue, orange = '#27679D', '#C06B29'
    aliases = {'Dover': 'DOVER', 'Cover': 'COVER', 'PIEAPP': 'PieAPP'}
    for ax, group, title in zip(axes, (rows[:15], rows[15:]),
                               ('(a) Full-reference metrics', '(b) No-reference metrics')):
        ys = list(range(len(group)))
        within = [float(r['within_sequence_srcc']) for r in group]
        overall = [float(r['overall_srcc']) for r in group]
        for y, w, o in zip(ys, within, overall):
            if y % 2 == 0:
                ax.axhspan(y - .5, y + .5, color='#F2F4F6', linewidth=0, zorder=0)
            ax.plot([w, o], [y, y], color='#969DA3', lw=1, zorder=2)
        ax.scatter(within, ys, s=23, marker='o', color=blue, zorder=4,
                   edgecolor='white', linewidth=.35)
        ax.scatter(overall, ys, s=23, marker='D', color=orange, zorder=5,
                   edgecolor='white', linewidth=.35)
        ax.set_yticks(ys, [aliases.get(r['metric'], r['metric']) for r in group])
        ax.set_ylim(14.6, -.6)
        ax.set_xlim(0, 1)
        ax.set_xticks([0, .2, .4, .6, .8, 1])
        ax.set_xlabel('Reported SRCC', labelpad=5)
        ax.set_title(title, fontsize=10, fontweight='bold', loc='left', pad=25)
        ax.grid(axis='x', color='#D7DBDE', linewidth=.45, zorder=1)
        ax.tick_params(axis='y', length=0, pad=4)
        ax.tick_params(axis='x', length=3, color='#879198')
        for side in ('left', 'right', 'top'):
            ax.spines[side].set_visible(False)
        ax.spines['bottom'].set_color('#879198')
    handles = [Line2D([], [], marker='o', color=blue, ls='', markersize=5,
                      label='Within-source (Fisher aggregation)'),
               Line2D([], [], marker='D', color=orange, ls='', markersize=5,
                      label='Overall (across sources)')]
    fig.legend(handles=handles, loc='upper center', bbox_to_anchor=(.52, .945),
               ncol=2, frameon=False, fontsize=8.5, handletextpad=.4, columnspacing=2)
    fig.savefig(OUT / 'benchmark.pdf', metadata={'Title': 'Reported quality-metric correlations',
                'Author': 'Survey authors; data from Herb et al., Table I',
                'CreationDate': None, 'ModDate': None})
    fig.savefig(OUT / 'benchmark.png', dpi=180)
    plt.close(fig)


def main():
    qualitative_examples()
    temporal_architectures()
    metric_correlations()
    print('Generated attributed Figs. 1 and 4 and data-based Fig. 6.')


if __name__ == '__main__':
    main()
