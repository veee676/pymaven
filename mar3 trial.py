# %%
import load_data as ld
import plot_instrument as pltins
# %%
# loading data
date_str = '2015-05-05'
mag = ld.load_mag([date_str])
static = ld.load_static([date_str])
# %%
pltins.plot_mag(mag, '2015-05-05T00:00:00','2015-05-05T23:59:59')
# %%
pltins.plot_static(static, '2015-05-05T17:20:00','2015-05-05T18:20:00')
# %%
swia = ld.load_swia_flux(['2015-05-05'])
pltins.plot_swia_flux(swia, '2015-05-05T17:20:00','2015-05-05T18:20:00')
# %%
# trying to create one figure that plots heavy ions together and not separately
pltins.plot_heavy_ions_only(static, '2015-05-05T17:20:00','2015-05-05T18:20:00')
# %%
