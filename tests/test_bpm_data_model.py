from bact_device_models.devices.bpm_elem import BpmElem, BpmElemPlane, BpmElementList
import pytest
import time

def test_bpm_elems():
    """see if these can be instansiated"""
    a_bpm = BpmElem(
        x=BpmElemPlane(pos_raw=0, rms_raw=0),
        y=BpmElemPlane(pos_raw=0, rms_raw=0),
        intensity_s=0,
        intensity_z=0,
        stat=0,
        name="test",
        gain_raw="1",
    )

    bpms = BpmElementList()
    bpms.add_bpm_elem(a_bpm)

    # Support for ophyd describe
    d = bpms.describe_dict()
    # Check that entries are there
    d["source"]
    n_elm, = d["shape"]
    assert d["dtype"] == "array"
    assert n_elm > 0

    # Support for ophyd data export
    timestamp = time.time()
    d = bpms.to_dict(timestamp)
    print(d)
    assert d['timestamp'] == pytest.approx(timestamp, abs=0.1)
    val, =  d['value']
    assert val == a_bpm
