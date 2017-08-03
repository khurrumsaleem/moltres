import yt
import numpy as np

field_label = {('all', 'group1'): r'$\phi_1\ moltres$',
               ('all', 'group2'): r'$\phi_2\ moltres$'}

ds = yt.load(
    '/home/lindsayad/projects/moltres/problems/'
    'constant_inlet_outlet_temp/2group.e', step=-1)

plt = yt.LinePlot(ds, [('all', 'group1'), ('all', 'group2')], [0, 81.28, 0], [
                  73, 81.28, 0], 1000, field_labels=field_label)
plt.annotate_legend(('all', 'group1'))
plt.set_x_unit('cm')
plt.set_x_unit('inch')
plt.set_xlabel('r (in)')
plt.set_ylabel(r'Fluxes ($\mathrm{10^{13}cm^{-2} s^{-1}}$)')
plt.save("moltres_radial_fluxes.eps")

msre_fast_radial_data = np.loadtxt(
    '/home/lindsayad/publications/figures/'
    'msre_fast_radial_flux.csv', skiprows=1, delimiter=',')
fast_x = msre_fast_radial_data[:, 0]
fast_flux = msre_fast_radial_data[:, 1]
msre_thermal_radial_data = np.loadtxt(
    '/home/lindsayad/publications/figures/'
    'msre_thermal_radial_flux.csv', skiprows=1, delimiter=',')
thermal_x = msre_thermal_radial_data[:, 0]
thermal_flux = msre_thermal_radial_data[:, 1]
plt.plots[('all', 'group1')].axes.plot(
    fast_x, fast_flux, label=r'$\phi_1\ msre$')
plt.plots[('all', 'group1')].axes.plot(
    thermal_x, thermal_flux, label=r'$\phi_2\ msre$')
plt.plots[('all', 'group1')].axes.legend()
plt._setup_plots()

plt.save('/home/lindsayad/publications/figures/'
         'combined_msre_moltres_radial.eps')
