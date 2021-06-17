from multiqc.modules.base_module import BaseMultiqcModule
import logging
from multiqc import config
from multiqc.plots import table, linegraph, bargraph
from copy import deepcopy
from collections import OrderedDict
import re
import os

log = logging.getLogger('multiqc')

class MultiqcModule(BaseMultiqcModule):
    def __init__(self):
        # Initialise the parent object
        super(MultiqcModule, self).__init__(name='Custom images', anchor='custom_images')

        # Parse logs
        for f in self.find_log_files("custom_images/images_tab", filehandles=True):
            for line in f['f']:
                line = line.split("\t")
                if len(line) < 3:
                    log.warning("Ignoring badly formatted line : "+" ".join(line))
                else:
                    image_file = line[0]
                    image_text = line[1]
                    image_description = line[2]

                    if os.path.isfile(image_file):
                        self.make_section(image_file,image_text,image_description)
                    else:
                        log.warning("Image "+image_file+" does not exist")

    def make_section(self,image_file,image_text,image_description):

        self.add_section(
            name = image_text,
            description = image_description,
            anchor = "custom_images_1",
            content = '<div class="mqc-custom-content-image"><img src="{}" /></div>'.format(image_file)
        )
