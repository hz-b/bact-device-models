from bact_device_models.filters.bpm_calibration import BPMCalibrationPlane
import pytest


def test010_bpm_filter_neutral_elements():
    """test that zeros and neutral elements work as expected"""
    calib = BPMCalibrationPlane(offset=0, scale=1)

    # check that default values are there
    assert calib.offset == 0
    assert calib.scale == 1
    # even if a bit BESSY II centred
    bit2val = 10 / (2 ** 15)
    assert calib.bit2val == pytest.approx(bit2val, rel=1e-12)

    assert calib.to_pos(1.0 / bit2val) == pytest.approx(1, 1e-12)
    assert calib.inverse(1.0 / bit2val) == pytest.approx(1, 1e-12)

    assert calib.to_pos(-1.0 / bit2val) == pytest.approx(-1, 1e-12)
    assert calib.inverse(-1.0 / bit2val) == pytest.approx(-1, 1e-12)

    assert calib.to_rms(1.0 / bit2val) == pytest.approx(1, 1e-12)
    assert calib.to_rms(-1.0 / bit2val) == pytest.approx(1, 1e-12)

    assert calib.forward(2.0) == pytest.approx(round(2 / bit2val), abs=1)


def test020_bpm_filter():

    bit2val = 1/100
    scale = 3
    offset = 2
    calib = BPMCalibrationPlane(offset=offset, scale=scale, bit2val=bit2val)

    assert calib.offset == offset
    assert calib.scale == scale
    assert calib.bit2val == bit2val

    # fmt: off
    assert calib.to_pos( 0) == pytest.approx(                    - offset, rel=1e-12)
    assert calib.to_pos( 1) == pytest.approx( 1 * bit2val * scale - offset, rel=1e-12)
    assert calib.to_pos( 2) == pytest.approx( 2 * bit2val * scale - offset, rel=1e-12)
    assert calib.to_pos( 3) == pytest.approx( 3 * bit2val * scale - offset, rel=1e-12)

    assert calib.to_pos(-1) == pytest.approx(-1 * bit2val * scale - offset, rel=1e-12)
    assert calib.to_pos(-2) == pytest.approx(-2 * bit2val * scale - offset, rel=1e-12)
    assert calib.to_pos(-3) == pytest.approx(-3 * bit2val * scale - offset, rel=1e-12)
    # fmot : on