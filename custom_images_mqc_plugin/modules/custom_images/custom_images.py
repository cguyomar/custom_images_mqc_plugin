from multiqc.modules.base_module import BaseMultiqcModule
import logging
from multiqc import config
from multiqc.plots import table, linegraph, bargraph
from copy import deepcopy
from collections import OrderedDict
import re
import os
import base64

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
                    image_file = os.path.expanduser(image_file)
                    image_text = line[1]
                    image_description = line[2]

                    if os.path.isabs(image_file):
                        image_path = image_file

                    else:
                        image_path = os.path.join(f["root"], image_file)

                    if os.path.isfile(image_path):
                        self.make_section(image_path,image_text,image_description)
                    else:
                        log.warning("Image "+image_path+" does not exist")

    def make_section(self,image_path,image_text,image_description):

        extension = os.path.splitext(image_path)[1]
        print(extension)
        assert (extension == ".png") | (extension == ".jpeg") | (extension == ".jpg")
        image_in = open(image_path,"rb")
        image_string = base64.b64encode(image_in.read()).decode("utf-8")
        image_html = '<div class="mqc-custom-content-image"><img src="data:image/{};base64,{}" /></div>'.format(
                            extension, image_string)

        self.add_section(
            name = image_text,
            description = image_description,
            anchor = "custom_images_1",
            content = image_html
        )
