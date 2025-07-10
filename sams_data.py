import demod
import datetime

from demod.simulators.load_simulators import LoadSimulator
from demod.datasets.CREST.loader import Crest
from demod.simulators.base_simulators import SimLogger

sim = LoadSimulator(
  n_households=1,
  data=Crest(),
  logger=SimLogger(
    'current_time',
    'get_power_demand'
  ),
  step_size=datetime.timedelta(minutes=60)
)

for i in range(24 * 7):
    sim.step()

sim.logger.plot()
sim.logger.plot_column()
elec_cons = sim.logger.get('get_power_demand', aggregated=False)