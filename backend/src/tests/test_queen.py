import json

import pytest


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["queen", "d4", "d5"],
        ["queen", "d4", "c3"],
        ["queen", "a7", "b8"],
        ["queen", "h1", "a8"],
    ],
)
def test_queen_valid_move(test_app, chess_figure, curr_field, dest_field):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["figure"] == "queen"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "null"


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["queen", "d4", "a5"],
        ["queen", "d4", "d100"],
        ["queen", "h4", "g2"],
        ["queen", "h1", "f2"],
    ],
)
def test_queen_invalid_move(test_app, chess_figure, curr_field, dest_field):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["figure"] == "queen"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "Current move is not permitted."


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["queen", "d400", "e5"],
        ["queen", "d-10", "c5"],
        ["queen", "h9", "g5"],
        ["queen", "h10", "a8"],
    ],
)
def test_queen_invalid_field_validation_move(
    test_app,
    chess_figure,
    curr_field,
    dest_field,
):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 409
    assert data["figure"] == "queen"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "Field does not exist."


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["queeny", "d4", "d5"],
        ["queenggy", "d4", "c3"],
        ["queen_", "a7", "b8"],
        ["queentt", "h1", "a8"],
    ],
)
def test_queen_invalid_name_validation_move(
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
            "queen",
            "h1",
            [
                "g1",
                "f1",
                "e1",
                "d1",
                "c1",
                "b1",
                "a1",
                "g2",
                "f3",
                "e4",
                "d5",
                "c6",
                "b7",
                "a8",
                "h2",
                "h3",
                "h4",
                "h5",
                "h6",
                "h7",
                "h8",
            ],
        ],
        [
            "queen",
            "a7",
            [
                "b7",
                "c7",
                "d7",
                "e7",
                "f7",
                "g7",
                "h7",
                "b6",
                "c5",
                "d4",
                "e3",
                "f2",
                "g1",
                "a6",
                "a5",
                "a4",
                "a3",
                "a2",
                "a1",
                "a8",
                "b8",
            ],
        ],
    ],
)
def test_queen_available_moves(test_app, chess_figure, curr_field, available_moves):
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
        ["queen", "d40b0", []],
        ["queen", "a1o0", []],
        ["queen", "h-04", []],
        ["queen", "h9", []],
    ],
)
def test_queen_invalid_field_available_moves(
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
        ["queeny", "d4", []],
        ["queenggy", "d4", []],
        ["queen_", "h4", []],
        ["queentt", "h1", []],
    ],
)
def test_queen_invalid_name_available_moves(
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
