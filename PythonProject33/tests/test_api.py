from unittest.mock import Mock, patch
from src.api.aeroplanes_api import AeroplanesAPI


@patch("src.api.aeroplanes_api.requests.get")
def test_get_country_coordinates(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = [
        {
            "boundingbox": ["10", "20", "30", "40"]
        }
    ]
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    api = AeroplanesAPI()
    coords = api.get_country_coordinates("Spain")

    assert coords == {"south": 10.0, "north": 20.0, "west": 30.0, "east": 40.0}
