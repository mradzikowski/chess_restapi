import json

import pytest


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["knight", "d4", "f5"],
        ["knight", "d4", "c2"],
        ["knight", "a7", "c6"],
        ["knight", "h1", "f2"],
    ],
)
def test_knight_valid_move(test_app, chess_figure, curr_field, dest_field):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["figure"] == "knight"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "null"


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["knight", "d4", "d5"],
        ["knight", "d4", "d100"],
        ["knight", "h4", "g8"],
        ["knight", "h1", "a8"],
    ],
)
def test_knight_invalid_move(test_app, chess_figure, curr_field, dest_field):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["figure"] == "knight"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "Current move is not permitted."


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["knight", "d400", "e5"],
        ["knight", "d-10", "c5"],
        ["knight", "h9", "g5"],
        ["knight", "h10", "a8"],
    ],
)
def test_knight_invalid_field_validation_move(
    test_app,
    chess_figure,
    curr_field,
    dest_field,
):
    client = test_app.test_client()
    resp = client.get(f"/api/v1/{chess_figure}/{curr_field}/{dest_field}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 409
    assert data["figure"] == "knight"
    assert data["currentField"] == curr_field
    assert data["destField"] == dest_field
    assert data["error"] == "Field does not exist."


@pytest.mark.parametrize(
    "chess_figure, curr_field, dest_field",
    [
        ["knighty", "d4", "e5"],
        ["knightggy", "d4", "c5"],
        ["knight_", "h4", "g4"],
        ["knighttt", "h1", "h2"],
    ],
)
def test_knight_invalid_name_validation_move(
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
        ["knight", "h1", ["f2", "g3"]],
        ["knight", "a7", ["c6", "b5", "c8"]],
    ],
)
def test_knight_available_moves(test_app, chess_figure, curr_field, available_moves):
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
        ["knight", "d40b0", []],
        ["knight", "a1o0", []],
        ["knight", "h-04", []],
        ["knight", "h9", []],
    ],
)
def test_knight_invalid_field_available_moves(
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
        ["knighty", "d4", []],
        ["knightggy", "d4", []],
        ["knight_", "h4", []],
        ["knighttt", "h1", []],
    ],
)
def test_knight_invalid_name_available_moves(
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
