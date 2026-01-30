import pytest

from bact_device_models.devices.orbit import Orbit, BPMPosition, BPMButtons, BPMReading


def test_bpm_to_orbit():
    orb = Orbit(
        orbit=[
            BPMReading(
                name="dev_1",
                pos=BPMPosition(x=355, y=113),
                btns=BPMButtons(a=1, b=2, c=3, d=4),
            ),
            BPMReading(
                name="dev_2",
                pos=BPMPosition(x=42, y=1024),
                btns=BPMButtons(a=3, b=5, c=7, d=11),
            ),
        ]
    )

    orb.identifiers()
    r1 = orb.get_element("dev_1")
    assert r1.pos.x == 355
    assert r1.pos.y == 113
    assert r1.name == "dev_1"
    assert r1.btns.a == 1
    assert r1.btns.b == 2
    assert r1.btns.c == 3
    assert r1.btns.d == 4
    del r1

    r2 = orb.get_element("dev_2")
    assert r2.pos.x == 42
    assert r2.pos.y == 1024

    with pytest.raises(KeyError):
        orb.get_element("dev_3")
