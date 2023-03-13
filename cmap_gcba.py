from matplotlib.colors import LinearSegmentedColormap

cmap_gcba =  LinearSegmentedColormap.from_list('gcba', (
    # Edit this gradient at https://eltos.github.io/gradient/#gcba=EC607E-F08372-FFD500-EEEDA6-29BDEF
    (0.000, (0.925, 0.376, 0.494)),
    (0.250, (0.941, 0.514, 0.447)),
    (0.500, (1.000, 0.835, 0.000)),
    (0.750, (0.933, 0.929, 0.651)),
    (1.000, (0.161, 0.741, 0.937))))

cmap_gcba_2 = LinearSegmentedColormap.from_list('gcba', (
    # Edit this gradient at https://eltos.github.io/gradient/#gcba=EC607E-F08372-FFD500
    (0.000, (0.925, 0.376, 0.494)),
    (0.500, (0.941, 0.514, 0.447)),
    (1.000, (1.000, 0.835, 0.000))))

cmap_gcba_2_r = LinearSegmentedColormap.from_list('gcba', (
        # Edit this gradient at https://eltos.github.io/gradient/#gcba_2=FFD500-F08372-EC607E
        (0.000, (1.000, 0.835, 0.000)),
        (0.500, (0.941, 0.514, 0.447)),
        (1.000, (0.925, 0.376, 0.494))))

cmap_gcba_1 = LinearSegmentedColormap.from_list('gcba_1', (
    # Edit this gradient at https://eltos.github.io/gradient/#gcba_1=FFD500-EEEDA6-29BDEF
    (0.000, (1.000, 0.835, 0.000)),
    (0.500, (0.933, 0.929, 0.651)),
    (1.000, (0.161, 0.741, 0.937))))

cmap_gcba_1_r =LinearSegmentedColormap.from_list('gcba_', (
    # Edit this gradient at https://eltos.github.io/gradient/#gcba_=29BDEF-FFD500
    (0.000, (0.161, 0.741, 0.937)),
    (1.000, (1.000, 0.835, 0.000))))