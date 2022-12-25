"""Helper to make image boilerplate """

import os

filez = os.listdir("images/2022_08_26_UTMB")

for file in filez:
    stem = os.path.splitext(file)[0]
    print(f"""
.. |{stem}| image:: images/2022_08_26_UTMB/small/{file}
   :width: 300px
   :target: images/2022_08_26_UTMB/{file}
""")

