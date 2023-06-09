from materialyoucolor.hct.hct import Hct
from materialyoucolor.palettes.tonal_palette import TonalPalette


class CorePalette:
    def __init__(self, argb):
        hct = Hct.fromInt(argb)
        hue = hct.hue
        self.a1 = TonalPalette.fromHueAndChroma(hue, max(48, hct.chroma))
        self.a2 = TonalPalette.fromHueAndChroma(hue, 16)
        self.a3 = TonalPalette.fromHueAndChroma(hue + 60, 24)
        self.n1 = TonalPalette.fromHueAndChroma(hue, 6)
        self.n2 = TonalPalette.fromHueAndChroma(hue, 8)
        self.error = TonalPalette.fromHueAndChroma(25, 84)

    @staticmethod
    def of(argb):
        return CorePalette(argb)
