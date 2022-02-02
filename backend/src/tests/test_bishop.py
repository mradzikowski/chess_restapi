import json

import pytest


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["bishop", "d4", "e5"],
        ["bishop", "d4", "c5"],
        ["bishop", "h4", "g5"],
        ["bishop", "h1", "a8"],
    ],
)
def test_bishop_valid_move(test_app, chess_figure, curr_field, dest_field):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["figure"] == "bishop"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "null"


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["bishop", "d4", "d5"],
        ["bishop", "d4", "e4"],
        ["bishop", "h4", "g4"],
        ["bishop", "h1", "h8"],
    ],
)
def test_bishop_invalid_move(test_app, chess_figure, curr_field, dest_field):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["figure"] == "bishop"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "Current move is not permitted."


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["bishop", "d40", "e5"],
        ["bishop", "d-1", "c5"],
        ["bishop", "h9", "g5"],
        ["bishop", "h10", "a8"],
    ],
)
def test_bishop_invalid_field_validation_move(
    test_app,
    chess_figure,
    curr_field,
    dest_field,
):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 409
    assert data["figure"] == "bishop"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "Field does not exist."


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["bishopy", "d4", "e5"],
        ["bishkopt", "d4", "c5"],
        ["bishooop", "h4", "g5"],
        ["bisop", "h1", "a8"],
    ],
)
def test_bishop_invalid_name_validation_move(
    test_app,
    chess_figure,
    curr_field,
    dest_field,
):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert data["figure"] == chess_figure
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == f"Chess figure - {chess_figure} - does not exist."


@pytest.mark.parametrize(
    "chess_figure, curr_field, available_moves",
    [
        [
            "bishop",
            "d4",
            [
                "e3",
                "f2",
                "g1",
                "c3",
                "b2",
                "a1",
                "c5",
                "b6",
                "a7",
                "e5",
                "f6",
                "g7",
                "h8",
            ],
        ],
        ["bishop", "a1", ["b2", "c3", "d4", "e5", "f6", "g7", "h8"]],
        ["bishop", "h4", ["g3", "f2", "e1", "g5", "f6", "e7", "d8"]],
        ["bishop", "h1", ["g2", "f3", "e4", "d5", "c6", "b7", "a8"]],
    ],
)
def test_bishop_available_moves(test_app, chess_figure, curr_field, available_moves):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["figure"] == chess_figure
    assert data["currentField"] == curr_field
    assert data["availableMoves"].sort() == available_moves.sort()
    assert data["error"] == "null"


@pytest.mark.parametrize(
    "chess_figure, curr_field, available_moves",
    [
        ["bishop", "d400", []],
        ["bishop", "a10", []],
        ["bishop", "h04", []],
        ["bishop", "h9", []],
    ],
)
def test_bishop_invalid_field_available_moves(
    test_app,
    chess_figure,
    curr_field,
    available_moves,
):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 409
    assert data["figure"] == chess_figure
    assert data["currentField"] == curr_field
    assert data["availableMoves"] == []
    assert data["error"] == "Field does not exist."


@pytest.mark.parametrize(
    "chess_figure, curr_field, available_moves",
    [
        ["bishopy", "d4", []],
        ["bishkopt", "d4", []],
        ["bishooop", "h4", []],
        ["bisop", "h1", []],
    ],
)
def test_bishop_invalid_name_available_moves(
    test_app,
    chess_figure,
    curr_field,
    available_moves,
):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert data["figure"] == chess_figure
    assert data["currentField"] == curr_field
    assert data["availableMoves"] == []
    assert data["error"] == f"Chess figure - {chess_figure} - does not exist."
