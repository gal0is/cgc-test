import driller
import logging

logging.getLogger().setLevel('DEBUG')

d = driller.Driller("./CADET_00001",  # path to the target binary
                    b"racecar", # initial testcase
                    "\xff" * 65535, # AFL bitmap with no discovered transitions
                   )

new_inputs = d.drill()
