import json

import pytest


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["rook", "d4", "d5"],
        ["rook", "d4", "c4"],
        ["rook", "a7", "a5"],
        ["rook", "h1", "a1"],
    ],
)
def test_rook_valid_move(test_app, chess_figure, curr_field, dest_field):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["figure"] == "rook"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "null"


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["rook", "d4", "a5"],
        ["rook", "d4", "d100"],
        ["rook", "h4", "g2"],
        ["rook", "h1", "f2"],
    ],
)
def test_rook_invalid_move(test_app, chess_figure, curr_field, dest_field):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["figure"] == "rook"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "Current move is not permitted."


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["rook", "d400", "e5"],
        ["rook", "d-10", "c5"],
        ["rook", "h9", "g5"],
        ["rook", "h10", "a8"],
    ],
)
def test_rook_invalid_field_validation_move(
    test_app,
    chess_figure,
    curr_field,
    dest_field,
):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 409
    assert data["figure"] == "rook"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "Field does not exist."


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["rooky", "d4", "d5"],
        ["rookggy", "d4", "a4"],
        ["rook_", "a7", "a1"],
        ["rooktt", "h1", "h8"],
    ],
)
def test_rook_invalid_name_validation_move(
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
            "rook",
            "h4",
            [
                "h3",
                "h2",
                "h1",
                "g4",
                "f4",
                "e4",
                "d4",
                "c4",
                "b4",
                "a4",
                "h5",
                "h6",
                "h7",
                "h8",
            ],
        ],
        [
            "rook",
            "d4",
            [
                "e4",
                "f4",
                "g4",
                "h4",
                "d3",
                "d2",
                "d1",
                "c4",
                "b4",
                "a4",
                "d5",
                "d6",
                "d7",
                "d8",
            ],
        ],
    ],
)
def test_rook_available_moves(test_app, chess_figure, curr_field, available_moves):
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
        ["rook", "d40b0", []],
        ["rook", "a1o0", []],
        ["rook", "h-04", []],
        ["rook", "h9", []],
    ],
)
def test_rook_invalid_field_available_moves(
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
        ["rooky", "d4", []],
        ["r__k", "d4", []],
        ["rook_ie", "h4", []],
        ["rookie", "h1", []],
    ],
)
def test_rook_invalid_name_available_moves(
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
