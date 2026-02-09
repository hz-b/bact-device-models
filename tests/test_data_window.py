from dataclasses import asdict

import jsons

from bact_device_models.devices.data_window import DataWindow


def test_data_window_init():
    dw = DataWindow.from_slice(slice(None))
    assert dw.start is None
    assert dw.stop is None
    assert dw.step is None


    dw = DataWindow.from_slice(slice(None, 2000))
    assert dw.start is None
    assert dw.stop == 2000
    assert dw.step == None

    dw = DataWindow.from_slice(slice(0, 2000))
    assert dw.start == 0
    assert dw.stop == 2000
    assert dw.step == None


def test_data_window_export_with_jsons():
    dw = DataWindow.from_slice(slice(None, 2000))
    d = jsons.dump(dw)
    d["start"] == None
    d["step"] == None
    d["stop"] == 2000


def test_data_window_export_as_dict():
    dw = DataWindow.from_slice(slice(None))
    d = asdict(dw)
    d["start"] == None
    d["step"] == None
    d["stop"] == None

    dw2 = jsons.load(d, DataWindow)
    assert dw == dw2

    dw = DataWindow.from_slice(slice(0, 2000))
    d = asdict(dw)
    d["start"] == 0
    d["step"] == 2000
    d["stop"] == None

    dw2 = jsons.load(d, DataWindow)
    assert dw == dw2

