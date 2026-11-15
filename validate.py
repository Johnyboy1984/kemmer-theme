from pathlib import Path
import yaml

def luminance(h):
    rgb = [int(h[i:i+2], 16)/255 for i in (1,3,5)]
    rgb = [v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in rgb]
    return sum(v*w for v,w in zip(rgb, (.2126,.7152,.0722)))

theme = yaml.safe_load(Path(__file__).with_name('themes').joinpath('kemmer_theme.yaml').read_text(encoding='utf-8'))['Kemmer Theme']
assert set(theme['modes']) == {'light', 'dark'}
for mode, values in theme['modes'].items():
    for key in ('primary-text-color','secondary-text-color'):
        a,b = sorted((luminance(values[key]), luminance(values['card-background-color'])))
        ratio = (b+.05)/(a+.05)
        assert ratio >= 4.5, (mode,key,ratio)
        print(f'{mode}: {key}: {ratio:.2f}:1')
print('YAML and text contrast checks passed.')
