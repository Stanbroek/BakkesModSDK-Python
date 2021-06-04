import os
import time

import pybind11_stubgen


def onLoad():
    print("Generating pybind11 stub")
    start = time.time()
    output_dir = os.path.dirname(__file__)
    print(output_dir)
    pybind11_stubgen.main(['bakkesmod', '-o', output_dir, '--root-module-suffix=', '--ignore-invalid=signature', '--skip-signature-downgrade', '--log-level=ERROR'])
    end = time.time()
    print("Generated pybind11 stub in %.2fs" % (end - start))
