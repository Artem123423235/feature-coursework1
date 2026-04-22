import os
from src.models.aeroplane import Aeroplane
from src.storage.json_saver import JSONSaver


def test_add_and_get_aeroplane(tmp_path):
    file_path = tmp_path / "test.json"
    saver = JSONSaver(str(file_path))
    plane = Aeroplane("UAL1621", "United States", 268.79, 10203.18)

    saver.add_aeroplane(plane)
    result = saver.get_aeroplanes(callsign="UAL1621")

    assert len(result) == 1
    assert result[0]["callsign"] == "UAL1621"


def test_delete_aeroplane(tmp_path):
    file_path = tmp_path / "test.json"
    saver = JSONSaver(str(file_path))
    plane = Aeroplane("UAL1621", "United States", 268.79, 10203.18)

    saver.add_aeroplane(plane)
    saver.delete_aeroplane(plane)

    result = saver.get_aeroplanes(callsign="UAL1621")
    assert len(result) == 0
